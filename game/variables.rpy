## The Analog Kid — All Game Variables
## Define here. Never define inline in scene or location files.

# ---------------------------------------------------------------------------
# Player Character
# ---------------------------------------------------------------------------
default player_char = ""
# "carver" | "geri" | "ray" | "frank" | "june" | "samuel"

# ---------------------------------------------------------------------------
# Game State
# ---------------------------------------------------------------------------
default current_period = 1955
# 1955 | 1967 | 1979 | 1991 | "normaltown" | 2008

default current_location = "main_street"

# ---------------------------------------------------------------------------
# Policy Path
# ---------------------------------------------------------------------------
# Accumulated across all periods. Range: -10 (conservative) to +10 (progressive)
# -3 to +3 = middle path territory
default policy_score = 0

default nudge_1955 = None   # "conservative" | "middle" | "progressive"
default nudge_1967 = None
default nudge_1979 = None
default nudge_1991 = None
default nudge_2008 = None

# Calculated at 2008 end: "conservative" | "middle" | "progressive" | "crash"
default endpoint = None

# ---------------------------------------------------------------------------
# Exploration & Dialog Flags
# ---------------------------------------------------------------------------
default visited = set()
# Format: "location_period"  e.g. "earls_diner_1955"

default conversations = set()
# Format: "npc_location_period_topic"  e.g. "dot_earls_1955_sign"

init python:
    def seen(location):
        return "{}_{}".format(location, store.current_period) in store.visited

    def talked(npc, location, topic):
        key = "{}_{}_{}_{}" .format(npc, location, store.current_period, topic)
        return key in store.conversations

    def mark_visited(location):
        store.visited.add("{}_{}".format(location, store.current_period))

    def mark_talked(npc, location, topic):
        store.conversations.add(
            "{}_{}_{}_{}" .format(npc, location, store.current_period, topic)
        )

# ---------------------------------------------------------------------------
# NPC Relationship Flags
# ---------------------------------------------------------------------------
default frank_ray_trust = 0          # 0-3, increments per period
default geri_frank_connection = False
default geri_samuel_connection = False
default ray_samuel_connection = False
default carver_samuel_connection = False
default carver_chambers_friendship = 0   # 0-4
default ray_godson_trust = False
default june_south_side_trust = 0    # 0-3

# ---------------------------------------------------------------------------
# NPC Arc States
# ---------------------------------------------------------------------------
default eddie_outcome = None         # "private" | "public" | "samuel"
default bobby_outcome = None         # "shipped" | "real_answer" | "deferred"
default marcus_status = "crossing"   # "crossing" | "drafted" | "deferred" | "vet_ok" | "vet_broken"
default thomas_status = "garage"     # "garage" | "drafted_quiet" | "symbol" | "deferred"
default harold_outcome = None        # "protected" | "prosecuted" | "negotiated"
default runningwater_complaint = "buried"  # "buried" | "surfaced" | "frank_background"
default dot_status = "waitress"      # "waitress" | "owner"
default agnes_status = "active"      # "active" | "retired" | "deceased"
default diane_outcome = None         # "tribal_yes" | "tribal_hesitant" | "tribal_no"
default godson_outcome = None        # "warned" | "public" | "thread"
default alex_status = "here"         # 1955 only: "here" | "gone"
default john_arc = 0                 # 0-3

# ---------------------------------------------------------------------------
# Keepsakes
# ---------------------------------------------------------------------------
default keepsake_bible = False        # Samuel's pocket Bible
default keepsake_photo = False        # Normaltown photograph
default keepsake_newspaper = False    # Normaltown newspaper
default keepsake_letter = False       # Geri's letter to Geraldine
default keepsake_schedule = False     # Bus station departure board photo
default keepsake_notebook = False     # Frank's case notes

# ---------------------------------------------------------------------------
# Self-Awareness (AI discovering its own nature)
# ---------------------------------------------------------------------------
default self_awareness = 0   # 0-5

# Leitmotif tracking — "This is the day (the Lord has made)"
default samuel_leitmotif_count = 0
default leitmotif_received = False

# ---------------------------------------------------------------------------
# Frame Story
# ---------------------------------------------------------------------------
default david_contacted = False      # Has David Broderick appeared?
default normaltown_visited = False
default simulation_revealed = False

# ---------------------------------------------------------------------------
# Photo Wall (between-period transition)
# ---------------------------------------------------------------------------
default photos_unlocked = []
# Populated at end of each period; blurred until self_awareness >= 3
