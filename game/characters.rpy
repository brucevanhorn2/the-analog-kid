## The Analog Kid — Character Definitions

define _ctc = "ctc"
define _ctcp = "nestled"

# ---------------------------------------------------------------------------
# Player Characters (voice color used when their internal thoughts appear)
# ---------------------------------------------------------------------------
define carver  = Character("Rev. Carver",  color="#D4A017", ctc=_ctc, ctc_position=_ctcp)
define geri    = Character("Geraldine",    color="#C85A8A", ctc=_ctc, ctc_position=_ctcp)
define ray     = Character("Ray",          color="#5A8AC8", ctc=_ctc, ctc_position=_ctcp)
define frank   = Character("Frank",        color="#8AC85A", ctc=_ctc, ctc_position=_ctcp)
define june    = Character("June",         color="#C8A05A", ctc=_ctc, ctc_position=_ctcp)
define samuel  = Character("Dr. Beaumont", color="#A0C8A0", ctc=_ctc, ctc_position=_ctcp)

# Player inner monologue
define narrator = Character(None, kind=nvl)
define thought  = Character(None, what_italic=True, what_color="#AAAAAA", ctc=_ctc, ctc_position=_ctcp)

# ---------------------------------------------------------------------------
# Supporting Characters
# ---------------------------------------------------------------------------
define dot           = Character("Dot",              color="#E8C87A", ctc=_ctc, ctc_position=_ctcp)
define earl          = Character("Earl",             color="#C87A50", ctc=_ctc, ctc_position=_ctcp)
define marcus        = Character("Marcus",           color="#7AC8A0", ctc=_ctc, ctc_position=_ctcp)
define chambers      = Character("Rev. Chambers",    color="#C8C87A", ctc=_ctc, ctc_position=_ctcp)
define agnes         = Character("Agnes",            color="#A07AC8", ctc=_ctc, ctc_position=_ctcp)
define harold        = Character("Harold Blanton",   color="#C87A7A", ctc=_ctc, ctc_position=_ctcp)
define thomas        = Character("Thomas",           color="#7AC8C8", ctc=_ctc, ctc_position=_ctcp)
define ruth          = Character("Ruth Briggs",      color="#E8A0A0", ctc=_ctc, ctc_position=_ctcp)
define eddie         = Character("Eddie Briggs",     color="#A0C8E8", ctc=_ctc, ctc_position=_ctcp)
define bobby         = Character("Bobby Simmons",    color="#C8A0E8", ctc=_ctc, ctc_position=_ctcp)
define alex          = Character("Alex",             color="#E8E87A", ctc=_ctc, ctc_position=_ctcp)
define john_r        = Character("John",             color="#7AE8C8", ctc=_ctc, ctc_position=_ctcp)
define frank_d       = Character("Frank DeLuca",     color="#8AC85A", ctc=_ctc, ctc_position=_ctcp)
define diana_c       = Character("Diana Chambers",   color="#C87AC8", ctc=_ctc, ctc_position=_ctcp)
define david         = Character("David Broderick",  color="#FFFFFF", ctc=_ctc, ctc_position=_ctcp)
define ada_whitehorse = Character("Ada Whitehorse",  color="#C8B87A", ctc=_ctc, ctc_position=_ctcp)
define runningwater  = Character("Dr. Runningwater", color="#7AC8A0", ctc=_ctc, ctc_position=_ctcp)
define carol         = Character("Carol",            color="#B0B0B0", ctc=_ctc, ctc_position=_ctcp)

# Generic / unnamed
define townsperson = Character("Townsperson", color="#AAAAAA", ctc=_ctc, ctc_position=_ctcp)
define sign        = Character(None, what_prefix="[", what_suffix="]", what_color="#BBBBBB")
