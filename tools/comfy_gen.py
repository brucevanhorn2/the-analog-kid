#!/usr/bin/env python
"""The Analog Kid — ComfyUI background generator.

Drives a local ComfyUI server (HTTP API) to render period-accurate 1955
backgrounds in the established photoreal/cinematic style, then writes the
finished PNG to a target path inside the game.

Stdlib only (urllib/json) so it runs under any Python 3 — intended to be
invoked with the ComfyUI venv interpreter.

Usage:
    python comfy_gen.py --prompt "<scene>" --out "<path.png>" [--seed N]
    python comfy_gen.py --jobs jobs.json      # batch: list of {prompt,out,seed?}
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
import uuid

COMFY = os.environ.get("COMFY_HOST", "http://127.0.0.1:8000")
CKPT = os.environ.get("COMFY_CKPT", "juggernautXL_ragnarokBy.safetensors")

# Shared look so every location reads as one cohesive set.
ERA = os.environ.get("COMFY_ERA", "1955 small-town America")
STYLE = (
    "photorealistic cinematic film still, " + ERA + ", "
    "warm natural lighting, 35mm Kodachrome color, soft atmospheric haze, "
    "highly detailed, wide shot, "
    "no people, empty scene, period accurate"
)
NEGATIVE = (
    "people, person, crowd, pedestrians, modern cars, modern signage, "
    "smartphone, text, watermark, signature, logo, cartoon, anime, "
    "illustration, painting, drawing, sketch, lowres, blurry, out of focus, "
    "deformed, distorted, oversaturated, cgi, 3d render, video game, fisheye, "
    "frame, border"
)

GEN_W, GEN_H = 1344, 768       # SDXL-friendly 16:9-ish generation size
OUT_W, OUT_H = 2560, 1440      # match existing finished backgrounds


def build_workflow(prompt, seed):
    pos = f"{prompt}, {STYLE}"
    prefix = "analogkid_" + uuid.uuid4().hex[:8]
    return prefix, {
        "1": {"class_type": "CheckpointLoaderSimple",
              "inputs": {"ckpt_name": CKPT}},
        "2": {"class_type": "CLIPTextEncode",
              "inputs": {"text": pos, "clip": ["1", 1]}},
        "3": {"class_type": "CLIPTextEncode",
              "inputs": {"text": NEGATIVE, "clip": ["1", 1]}},
        "4": {"class_type": "EmptyLatentImage",
              "inputs": {"width": GEN_W, "height": GEN_H, "batch_size": 1}},
        "5": {"class_type": "KSampler",
              "inputs": {"seed": seed, "steps": 30, "cfg": 6.0,
                         "sampler_name": "dpmpp_2m_sde", "scheduler": "karras",
                         "denoise": 1.0, "model": ["1", 0],
                         "positive": ["2", 0], "negative": ["3", 0],
                         "latent_image": ["4", 0]}},
        "6": {"class_type": "VAEDecode",
              "inputs": {"samples": ["5", 0], "vae": ["1", 2]}},
        "7": {"class_type": "ImageScale",
              "inputs": {"image": ["6", 0], "upscale_method": "lanczos",
                         "width": OUT_W, "height": OUT_H, "crop": "center"}},
        "8": {"class_type": "SaveImage",
              "inputs": {"images": ["7", 0], "filename_prefix": prefix}},
    }, prefix


def _post(path, payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(COMFY + path, data=data,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def _get(path):
    with urllib.request.urlopen(COMFY + path, timeout=30) as r:
        return r.read()


def generate(prompt, out_path, seed):
    client_id = uuid.uuid4().hex
    _, workflow, _ = build_workflow(prompt, seed)
    resp = _post("/prompt", {"prompt": workflow, "client_id": client_id})
    pid = resp["prompt_id"]
    print(f"  queued {pid} -> {os.path.basename(out_path)}", flush=True)

    # Poll history until this prompt completes.
    deadline = time.time() + 600
    while time.time() < deadline:
        time.sleep(2)
        try:
            hist = json.loads(_get(f"/history/{pid}"))
        except urllib.error.URLError:
            continue
        if pid in hist:
            outputs = hist[pid].get("outputs", {})
            imgs = outputs.get("8", {}).get("images", [])
            if imgs:
                img = imgs[0]
                q = urllib.parse.urlencode({
                    "filename": img["filename"],
                    "subfolder": img.get("subfolder", ""),
                    "type": img.get("type", "output")})
                blob = _get("/view?" + q)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                with open(out_path, "wb") as f:
                    f.write(blob)
                print(f"  saved {out_path} ({len(blob)} bytes)", flush=True)
                return True
            status = hist[pid].get("status", {})
            if status.get("status_str") == "error":
                print(f"  ERROR: {json.dumps(status)[:400]}", flush=True)
                return False
    print("  TIMEOUT", flush=True)
    return False


import urllib.parse  # noqa: E402  (after stdlib block for clarity)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt")
    ap.add_argument("--out")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--jobs")
    args = ap.parse_args()

    if args.jobs:
        with open(args.jobs, encoding="utf-8") as f:
            jobs = json.load(f)
        ok = 0
        for i, j in enumerate(jobs):
            seed = j.get("seed", 1000 + i)
            print(f"[{i+1}/{len(jobs)}] {j['out']}", flush=True)
            if generate(j["prompt"], j["out"], seed):
                ok += 1
        print(f"DONE: {ok}/{len(jobs)} succeeded", flush=True)
        sys.exit(0 if ok == len(jobs) else 1)

    if not args.prompt or not args.out:
        ap.error("need --prompt and --out (or --jobs)")
    sys.exit(0 if generate(args.prompt, args.out, args.seed or 1234) else 1)


if __name__ == "__main__":
    main()
