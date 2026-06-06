#!/usr/bin/env python
"""The Analog Kid — ComfyUI character portrait generator.

Person-focused companion to comfy_gen.py: renders dignified 1955 portrait
photographs of the protagonists for the character-select screen. Stdlib only.

Usage:
    python comfy_portrait.py --jobs portraits.json   # [{prompt,out,seed?}]
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
import uuid

COMFY = os.environ.get("COMFY_HOST", "http://127.0.0.1:8000")
CKPT = os.environ.get("COMFY_CKPT", "juggernautXL_ragnarokBy.safetensors")

STYLE = (
    "1955 color portrait photograph, head and shoulders, dignified, "
    "warm studio lighting, Kodachrome, 35mm film, shallow depth of field, "
    "sharp focus on the face, period-accurate clothing, neutral backdrop, "
    "highly detailed, photorealistic"
)
NEGATIVE = (
    "deformed face, asymmetric eyes, extra fingers, bad anatomy, "
    "modern clothing, modern hairstyle, text, watermark, signature, logo, "
    "cartoon, anime, illustration, painting, 3d render, cgi, lowres, "
    "blurry, out of focus, jpeg artifacts, ugly, disfigured"
)

GEN_W, GEN_H = 832, 1216
OUT_W, OUT_H = 1024, 1536


def build_workflow(prompt, seed):
    pos = f"{prompt}, {STYLE}"
    prefix = "akid_port_" + uuid.uuid4().hex[:8]
    return {
        "1": {"class_type": "CheckpointLoaderSimple",
              "inputs": {"ckpt_name": CKPT}},
        "2": {"class_type": "CLIPTextEncode",
              "inputs": {"text": pos, "clip": ["1", 1]}},
        "3": {"class_type": "CLIPTextEncode",
              "inputs": {"text": NEGATIVE, "clip": ["1", 1]}},
        "4": {"class_type": "EmptyLatentImage",
              "inputs": {"width": GEN_W, "height": GEN_H, "batch_size": 1}},
        "5": {"class_type": "KSampler",
              "inputs": {"seed": seed, "steps": 32, "cfg": 6.0,
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
    }


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
    workflow = build_workflow(prompt, seed)
    resp = _post("/prompt", {"prompt": workflow, "client_id": client_id})
    pid = resp["prompt_id"]
    print(f"  queued {pid} -> {os.path.basename(out_path)}", flush=True)
    deadline = time.time() + 600
    while time.time() < deadline:
        time.sleep(2)
        try:
            hist = json.loads(_get(f"/history/{pid}"))
        except urllib.error.URLError:
            continue
        if pid in hist:
            imgs = hist[pid].get("outputs", {}).get("8", {}).get("images", [])
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
            if hist[pid].get("status", {}).get("status_str") == "error":
                print(f"  ERROR: {json.dumps(hist[pid]['status'])[:400]}", flush=True)
                return False
    print("  TIMEOUT", flush=True)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", required=True)
    args = ap.parse_args()
    with open(args.jobs, encoding="utf-8") as f:
        jobs = json.load(f)
    ok = 0
    for i, j in enumerate(jobs):
        print(f"[{i+1}/{len(jobs)}] {j['out']}", flush=True)
        if generate(j["prompt"], j["out"], j.get("seed", 3000 + i)):
            ok += 1
    print(f"DONE: {ok}/{len(jobs)} succeeded", flush=True)
    sys.exit(0 if ok == len(jobs) else 1)


if __name__ == "__main__":
    main()
