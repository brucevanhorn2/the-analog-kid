# THE ANALOG KID — Game Design Document (Technical Spec)
## Version 0.1

---

# PLATFORM & DISTRIBUTION

**Target platforms:** PC (Windows), Linux
**Distribution:** Steam
**Engine:** RenPy (latest stable)
**Target rating:** ESRB Teen / PEGI 12 (mature themes, no explicit content)

---

# RESOLUTION & DISPLAY

**Logical resolution:** 1920 × 1080 (coordinate space for all UI, click regions, text)
**Source asset resolution:** 2560 × 1440 (all images generated at this size)
**Scaling:** RenPy handles window scaling automatically — scales down to 1080p, native at 1440p
**Aspect ratio:** 16:9 locked
**Windowed/fullscreen:** Both supported, fullscreen default

**RenPy config.rpy settings:**
```python
config.screen_width = 1920
config.screen_height = 1080
config.window_title = "The Analog Kid"

# Allow window resize, maintain aspect ratio
config.gl_resize = True

# High quality scaling
config.prefer_screenshot_viewport = True
```

**Image pipeline:**
- Generate in ComfyUI at 2560×1440
- Store source assets at 2560×1440 in /source_assets/ (not shipped)
- Export game assets at 1920×1080 to /game/images/
- Exception: images used for zoom/pan effects stored at 2560×1440 for quality headroom

---

# PROJECT FILE STRUCTURE

```
the-analog-kid/
├── game/
│   ├── script.rpy              # Entry point, game start, character select
│   ├── config.rpy              # RenPy configuration
│   ├── variables.rpy           # ALL game variables defined here
│   ├── characters.rpy          # Character definitions (who says what color)
│   ├── screens.rpy             # UI screens (keepsakes, settings)
│   ├── navigation.rpy          # Navigation system logic
│   │
│   ├── periods/                # One file per time period
│   │   ├── period_1955.rpy
│   │   ├── period_1967.rpy
│   │   ├── period_1979.rpy
│   │   ├── period_1991.rpy
│   │   ├── period_normaltown.rpy
│   │   └── period_2008.rpy
│   │
│   ├── locations/              # One file per location
│   │   ├── main_street.rpy
│   │   ├── earls_diner.rpy
│   │   ├── mcswain_block.rpy
│   │   ├── town_square.rpy
│   │   ├── city_hall.rpy
│   │   ├── post_office.rpy
│   │   ├── tracks_crossing.rpy
│   │   ├── train_station.rpy
│   │   ├── bus_station.rpy
│   │   ├── south_side_entry.rpy
│   │   ├── mount_zion.rpy
│   │   ├── tribal_office.rpy
│   │   ├── beaumont_practice.rpy
│   │   ├── ihs_clinic.rpy
│   │   ├── blanton_factory.rpy
│   │   ├── college_campus.rpy
│   │   ├── library.rpy
│   │   ├── vfw_hall.rpy
│   │   ├── hospital_north.rpy
│   │   ├── first_baptist.rpy
│   │   ├── holloway_derrick.rpy
│   │   ├── high_school_road.rpy
│   │   └── barbershop.rpy
│   │
│   ├── npcs/                   # One file per NPC
│   │   ├── dot.rpy
│   │   ├── earl.rpy
│   │   ├── marcus.rpy
│   │   ├── chambers.rpy
│   │   ├── agnes.rpy
│   │   ├── harold_blanton.rpy
│   │   ├── thomas_whitehorse.rpy
│   │   ├── ruth_briggs.rpy
│   │   ├── eddie_briggs.rpy
│   │   ├── bobby_simmons.rpy
│   │   ├── june_father.rpy     # Holloway Sr.
│   │   ├── alex.rpy
│   │   ├── john_rutsey.rpy
│   │   └── david_broderick.rpy # Frame story sequences only
│   │
│   ├── images/
│   │   ├── locations/
│   │   │   ├── 1955/
│   │   │   ├── 1967/
│   │   │   ├── 1979/
│   │   │   ├── 1991/
│   │   │   ├── normaltown/
│   │   │   └── 2008/
│   │   ├── characters/         # Character portraits/sprites
│   │   ├── ui/                 # Interface elements
│   │   └── keepsakes/          # Keepsake item images
│   │
│   └── audio/
│       ├── music/
│       ├── ambient/            # Location ambient sound
│       └── sfx/
│
└── source_assets/              # NOT shipped with game
    ├── images_2560x1440/       # Full resolution source images
    └── comfyui_workflows/      # Saved ComfyUI workflows per location/period
```

---

# VARIABLE ARCHITECTURE

All variables defined in **variables.rpy**. Never defined inline in scene files.

## Player Character
```python
default player_char = ""
# Values: "carver" | "geri" | "ray" | "frank" | "june" | "samuel"
```

## Current Game State
```python
default current_period = 1955
# Values: 1955 | 1967 | 1979 | 1991 | "normaltown" | 2008

default current_location = "main_street"
```

## Policy Path Tracking
```python
# Accumulated across all periods
# Range: -10 (full conservative) to +10 (full progressive)
# -3 to +3 = middle path territory
default policy_score = 0

# Per-period nudge outcomes (set when hinge event resolves)
default nudge_1955 = None   # "conservative" | "middle" | "progressive"
default nudge_1967 = None
default nudge_1979 = None
default nudge_1991 = None
default nudge_2008 = None

# Derived endpoint (calculated at 2008)
# "conservative" | "middle" | "progressive" | "crash" (held middle all the way)
default endpoint = None
```

## Exploration & Dialog Flags
```python
# Tracks every location visited per period
# Format: "location_period" e.g. "earls_diner_1955"
default visited = set()

# Tracks every conversation completed
# Format: "npc_location_period_topic" e.g. "dot_earls_1955_sign"
default conversations = set()

# Helper: has player visited this location this period?
# Called as: seen("earls_diner")  (auto-appends current period)
```

## NPC Relationship Flags
```python
# Trust/relationship levels per key NPC pair
# These unlock dialog options and nudge choices

# Frank/Ray trust — built across periods, required for middle path 1967+
default frank_ray_trust = 0       # 0-3, increments per period

# Geri/Frank connection — required for middle path 1979
default geri_frank_connection = False

# Geri/Samuel connection — required for middle path 1967
default geri_samuel_connection = False

# Ray/Samuel connection — required for middle path 1955
default ray_samuel_connection = False

# Carver/Samuel connection — established 1955 via Eddie Briggs middle path
default carver_samuel_connection = False

# Carver/Chambers friendship — develops across periods
default carver_chambers_friendship = 0  # 0-4, one increment per period

# Ray/godson trust — required for middle path 1991
default ray_godson_trust = False

# June/south_side relationships — required for middle path 1979
default june_south_side_trust = 0  # 0-3
```

## NPC Arc States
```python
# Eddie Briggs
default eddie_outcome = None  # "private" | "public" | "samuel"

# Bobby Simmons
default bobby_outcome = None  # "shipped" | "real_answer" | "deferred"

# Marcus Beaumont
default marcus_status = "crossing"
# Values: "crossing" | "drafted" | "deferred" | "vet_ok" | "vet_broken"

# Thomas Whitehorse
default thomas_status = "garage"
# Values: "garage" | "drafted_quiet" | "symbol" | "deferred"

# Harold Blanton Jr.
default harold_outcome = None  # "protected" | "prosecuted" | "negotiated"

# George Runningwater complaint
default runningwater_complaint = "buried"
# Values: "buried" | "surfaced" | "frank_background"

# Dot (diner)
default dot_status = "waitress"
# Values: "waitress" | "owner" (changes 1991)

# Agnes Pruitt
default agnes_status = "active"
# Values: "active" | "retired" | "deceased" (2005, between 1991 and 2008)

# Diane Chambers
default diane_outcome = None  # "tribal_yes" | "tribal_hesitant" | "tribal_no"

# Ray's godson
default godson_outcome = None  # "warned" | "public" | "thread"

# Alex / John
default alex_status = "here"   # 1955 only: "here" | "gone" (after bus scene)
default john_arc = 0           # Nudgeable arc 0-3
```

## Keepsakes
```python
default has_geri_index_card = False
default has_marcus_token = False
default has_yearbook_page = False
default has_samuel_bible = True   # Samuel always has it; set False when given away

# Normaltown-specific
default normaltown_geri_nudged = False  # Did player successfully leave the anomaly?
default index_card_returned = False     # Does Geri have it back in 2008?
```

## Player Self-Awareness (AI Discovery Arc)
```python
# Player's growing understanding of their own nature
# 0 = no awareness | 1 = something feels wrong | 2 = actively questioning
# 3 = suspects the truth | 4 = knows | 5 = has accepted it
default self_awareness = 0

# Portal interaction attempts
default portal_attempts = 0  # Increments each time player tries the portal pre-1991

# Has player been to Normaltown
default visited_normaltown = False
```

## Samuel's Leitmotif
```python
# Tracks when "This is the day" has been heard
default heard_this_is_the_day_1955 = False
default heard_this_is_the_day_1967 = False
default heard_this_is_the_day_1979 = False
default heard_this_is_the_day_1991 = False
default heard_this_is_the_day_2008 = False

# Carver/Samuel phrase completion moment
default phrase_completed_together = False  # Set True in 1991 deathbed scene
default full_phrase_spoken = False         # Set True in 2008 before final four words
```

## Frame Story (David Broderick)
```python
# Frame story sequences shown between periods
default frame_sequences_shown = []
# Values added: "david_starts" | "david_checks_log" | "david_confused"
# | "david_psw_error" | "david_waits" | "david_gets_answer"
```

---

# NAVIGATION SYSTEM

## How It Works
Each location has a background image with invisible hotspot regions. Clicking a region transitions to the connected location. No map screen — exits are implied by the scene composition.

**RenPy implementation:**
```python
# In each location label, show background then navigation screen
label earls_diner_1955:
    scene bg_earls_diner_1955
    call screen location_nav("earls_diner", 1955)
```

**Navigation screen (screens.rpy):**
```python
screen location_nav(location, period):
    # Hotspot regions defined per location per period
    # Each hotspot: area (x, y, w, h), destination label, hover highlight
    for exit in get_exits(location, period):
        imagebutton:
            idle exit.idle_image      # Usually transparent
            hover exit.hover_image    # Subtle highlight or directional arrow
            action Jump(exit.destination)
            area exit.area
```

**Exit definitions** stored in navigation.rpy as a dictionary:
```python
# exits["location"]["period"] = list of Exit objects
# Exit: area, destination, hover_image, available_condition
```

**Availability conditions** — some exits only appear based on flags:
```python
# Hospital north side only available to certain characters
# Frank can enter; Samuel in 1955 cannot enter freely
Exit(
    area=(1400, 200, 300, 400),
    destination="hospital_north",
    condition="player_char != 'samuel' or samuel_hospital_privileges != 'none'"
)
```

## Location State System
Each location label checks current period and flags to determine which version to show:

```python
label earls_diner:
    # Determine which background to use
    $ bg = get_location_bg("earls_diner", current_period, get_flags())
    scene expression bg

    # Determine which NPCs are present
    $ npcs_present = get_npcs("earls_diner", current_period)

    # Show available interactions
    call screen location_interactions(npcs_present)
```

---

# DIALOG SYSTEM

## NPC Conversation Structure
Each NPC conversation is a label that checks flags to determine available dialog:

```python
label dot_earls_1955:
    # What Dot says depends on what player has already done
    if "samuel_beaumont_practice_1955" in visited:
        # Player has been to south side — Dot's dialog opens up
        jump dot_earls_1955_knows_south
    else:
        jump dot_earls_1955_baseline
```

## Conversation Tracking
```python
# Mark conversation as seen when completed
$ conversations.add("dot_earls_1955_sign")

# Check before showing dialog option
if "dot_earls_1955_baseline" not in conversations:
    textbutton "Ask about the sign":
        action [
            SetVariable("...", "..."),
            Jump("dot_earls_1955_sign_dialog")
        ]
```

## Character Voice Definitions (characters.rpy)
```python
define carver = Character("Rev. Carver",
    color="#8B7355",        # Warm brown
    what_font="fonts/georgia.ttf")

define geri = Character("Dr. Habicht",
    color="#4A6FA5",        # Steel blue
    what_font="fonts/georgia.ttf")

define ray = Character("Ray",
    color="#6B8E6B",        # Muted green
    what_font="fonts/georgia.ttf")

define frank = Character("Frank",
    color="#7A7A7A",        # Grey
    what_font="fonts/georgia.ttf")

define june = Character("June",
    color="#9B6B9B",        # Muted purple
    what_font="fonts/georgia.ttf")

define samuel = Character("Dr. Beaumont",
    color="#C8A96E",        # Warm gold
    what_font="fonts/georgia.ttf")

# NPCs
define dot = Character("Dot", color="#B85C38")
define earl = Character("Earl", color="#5C4033")
define marcus = Character("Marcus", color="#4A7C59")
define chambers = Character("Rev. Chambers", color="#2C5F2E")
define agnes = Character("Agnes", color="#7B6B8D")
define frank_chief = Character("Chief DeLuca",   # Normaltown version
    color="#8B0000")

# Narrator / Player inner voice
define narrator = Character(None, what_italic=True)
define inner = Character(None,
    what_color="#AAAAAA",
    what_italic=True,
    what_size=28)
```

---

# PERIOD TRANSITION SYSTEM

## Transition Triggers
Each period ends when:
1. The hinge event has resolved (nudge committed)
2. A minimum exploration threshold is met (player has visited required locations)
3. Player triggers the transition scene (visits the transition location)

```python
# Hinge event resolved flag
default hinge_1955_resolved = False

# Minimum exploration threshold per period
# Player must have X conversations to unlock the transition
default exploration_1955 = 0  # Increments with each new conversation

# Threshold to unlock hinge event
define HINGE_THRESHOLD_1955 = 5  # Must have 5 conversations before hinge available
```

## Transition Sequences
Each transition is a unique scene:

```python
label transition_1955_to_1967:
    # Fourth of July fireworks
    scene bg_main_street_1955_night
    play sound "sfx/fireworks_distant.ogg"
    
    inner "The sky above Middletown fills with light."
    
    # Flash sequence
    scene bg_white with flash
    pause 0.5
    scene bg_white
    
    inner "Twelve years."
    
    pause 1.0
    
    # Increment self-awareness slightly
    $ self_awareness = max(self_awareness, 1)
    
    # Update period
    $ current_period = 1967
    
    jump period_1967_start
```

---

# PERIOD HINGE EVENT SYSTEM

## How Nudges Work
The nudge is never a single menu choice. It's the result of accumulated conversation flags combined with a final decision moment.

```python
label hinge_1955_cornerstone:
    # Available options depend on what player has done
    
    menu:
        # Option always available
        "Support Cornerstone. The economic argument is sound.":
            $ nudge_1955 = "conservative"
            $ policy_score -= 2
            jump hinge_1955_conservative
        
        # Only available if player talked to Ray AND Geri
        "There are conditions that could make this work for everyone." if ray_samuel_connection and "geri_office_1955" in visited:
            $ nudge_1955 = "middle"
            $ policy_score += 0
            jump hinge_1955_middle
        
        # Only available if player visited south side merchants
        "Cornerstone will hollow out Main Street. Block it." if "south_side_entry_1955" in visited:
            $ nudge_1955 = "progressive"
            $ policy_score += 2
            jump hinge_1955_progressive
```

## Policy Score Calculation
```python
# At end of each period, policy_score shifts based on nudge
# Conservative nudges: -2 per period
# Middle nudges: 0 per period (but harder to achieve)
# Progressive nudges: +2 per period

# At 2008 endpoint:
# score <= -6: conservative endpoint
# -5 to +5: middle endpoint (but see escalation below)
# score >= +6: progressive endpoint

# ESCALATION: Middle path gets harder
# If nudge_1967 == "middle" AND nudge_1955 == "middle":
#   HINGE_THRESHOLD_1979 += 2  (need more conversations to unlock hinge)
# If all three == "middle":
#   2008 hinge has additional required flags (ray trust, frank connections, geri data, june capital)
# If all five == "middle":
#   Simulation crash ending
```

---

# KEEPSAKE UI SYSTEM

Accessible via a persistent button in the corner (or keyboard shortcut K).
Displays 3-4 item slots. Items show as illustrations with brief descriptions.
Items glow subtly when they become relevant to current scene.

```python
screen keepsakes():
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        
        vbox:
            text "Keepsakes" style "heading"
            
            hbox:
                spacing 40
                
                if has_geri_index_card:
                    imagebutton:
                        idle "images/keepsakes/index_card.png"
                        hover "images/keepsakes/index_card_hover.png"
                        action Show("keepsake_detail", item="index_card")
                
                if has_marcus_token:
                    imagebutton:
                        idle "images/keepsakes/crossing_token.png"
                        hover "images/keepsakes/crossing_token_hover.png"
                        action Show("keepsake_detail", item="crossing_token")
                
                if has_yearbook_page:
                    imagebutton:
                        idle "images/keepsakes/yearbook_page.png"
                        hover "images/keepsakes/yearbook_page_hover.png"
                        action Show("keepsake_detail", item="yearbook_page")
                
                if has_samuel_bible:
                    imagebutton:
                        idle "images/keepsakes/pocket_bible.png"
                        hover "images/keepsakes/pocket_bible_hover.png"
                        action Show("keepsake_detail", item="pocket_bible")
```

---

# PHOTO WALL SYSTEM (Earl's Diner)

The photo wall tracks Middletown's history. One photo per period, plus between-period photos that are slightly blurred.

```python
# Photo wall state per period
default photo_wall_state = {
    1955: ["photo_sports_field_1955"],
    1967: ["photo_sports_field_1955", "photo_march_1965_blurred",
           "photo_cornerstone_vote_1964_blurred", "photo_earls_1967"],
    1979: [...],  # etc
}

# In-scene: player can click the wall to examine photos
# Blurred photos have reduced opacity and no detail on hover
# Player may notice the blur pattern before understanding what it means
```

---

# SELF-AWARENESS SYSTEM

The player's gradual discovery of their own nature is tracked via `self_awareness` (0-5).

```python
# self_awareness increments from:
# - Period transitions (each one adds slight wrongness)
# - Portal interaction attempts
# - NPCs reacting to player not aging
# - Certain dialog choices that probe identity
# - Visiting Normaltown (jumps to 4 minimum)
# - Geri's folder scene (5)

# self_awareness gates certain inner monologue lines:
# Level 0: No self-reflection beyond normal
# Level 1: "Something feels different about how I move through time."
# Level 2: "I've been here before. Not a memory. Something else."
# Level 3: "These people age. I watch them age. I don't."
# Level 4: "I know what I am. I don't know if that changes anything."
# Level 5: "I am the question the math couldn't answer."
```

---

# NORMALTOWN SYSTEM

Normaltown uses the same location structure but with different backgrounds and NPC states.

```python
# Normaltown has its own set of backgrounds (same compositions, wrong details)
# bg_earls_normaltown (McSwane visible through window)
# bg_main_street_normaltown (Cornerstone already there, Main Street emptier)

# Normaltown NPCs are variants of Middletown NPCs
define frank_normal = Character("Chief DeLuca",
    color="#8B0000",        # Red — different from Middletown Frank
    what_font="fonts/georgia.ttf")

define geri_normal = Character("Dr. Habicht",
    color="#808080",        # Grey — diminished version
    what_italic=True)

# Normaltown sequence is linear — no free exploration
# Player moves through a fixed sequence of locations
# Portal return triggered by: reaching Geri + completing the anomaly scene
```

---

# STEAM INTEGRATION

**Planned achievements (examples):**
- "This Is The Day" — hear Samuel's phrase in all five periods
- "The Long Burn" — complete a full conservative path playthrough
- "Inconclusive" — achieve the simulation crash ending
- "Both Halves" — witness Carver and Samuel complete the phrase together (1991)
- "You Went Through" — visit Normaltown
- "The Analog Kid" — complete any full playthrough
- "Power Doesn't Redeem" — witness the Frank/Ray scene
- "Still Here" — complete all six character stories (six playthroughs)

**Steam Cloud:** Save files synced. Players can continue on different machines.

**Linux build:** RenPy exports directly. No additional work required beyond testing.

---

# VISUAL STYLE GUIDE

*(To be established with first ComfyUI test images)*

**Era color palettes (preliminary):**
- 1955: Warm Kodachrome — amber, cream, dusty blue. Slight vignette.
- 1967: Cooler, more contrasty. Early color photography feel.
- 1979: Grainier. Faded colors. The warmth is leaving.
- 1991: Flat early digital feel. Colors slightly oversaturated then corrected.
- Normaltown: Same compositions, desaturated 15%, slightly wrong contrast.
- 2008: Crisp. The warmth is gone. Clean but cold.

**Character portraits:**
- Semi-realistic illustration style
- Consistent lighting per era
- Aging visible between periods — same face, different weight of years

**UI:**
- Minimal. Period-appropriate typography.
- 1955 font: Slab serif, editorial feel
- Keepsake display: Simple illustrated style, warm paper texture
- No HUD during exploration — only accessible via keyboard shortcut

---

# AUDIO DESIGN (Preliminary)

**Ambient per location per period:**
- Main Street 1955: distant traffic, a radio through a window, birds
- Main Street 1979: fewer cars, wind, a television somewhere
- Main Street 2008: depends on path

**Music approach:**
- No licensed music (avoids royalty issues)
- Original compositions or royalty-free period-appropriate pieces
- Sparse — silence is used deliberately
- Theme: simple, recurring, varies in arrangement per era

**Sound design notes:**
- Blanton smokestacks: a low industrial hum audible from any outdoor location in 1955-1967. When they go quiet in 1979, the silence is noticeable.
- Train: heard but rarely seen after 1967
- Bus station flip board: mechanical clatter when updating
- The portal: a very subtle sound only the player can "hear" — not diegetic

---

# PROTOTYPE SCOPE

**First build target:** 1955, Samuel Beaumont, three locations

**Locations:**
1. Samuel's Practice (starting location)
2. IHS Clinic
3. North Side Hospital

**NPCs in prototype:**
- Marcus (crossing signal, brief)
- Ray Coldwater (IHS clinic)
- North side hospital admissions (unnamed, institutional)

**One complete conversation thread:**
The Whitehorse family nudge — Ray/Samuel connection, middle path

**What this proves:**
- Navigation system works
- Flag system works
- One complete nudge plays out
- Dialog branching based on exploration
- Visual style established

**Estimated prototype build time:** 2-3 sessions

---

*End of GDD Technical Spec v0.1*
*Next: Visual style test images → RenPy project scaffold → Prototype scene*
