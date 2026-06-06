## The Analog Kid — Period 1967
## Raymond Coldwater — "The Man Holding Two Worlds Together."
## The folded draft list; Thomas Whitehorse.

label ray_1967_begin:

    $ current_period = 1967
    $ current_location = "tribal_office"
    $ mark_visited("tribal_office")

    scene bg_tribal_office_1967 with fade

    thought "Forty-four years old. Twelve years of standing between my people and systems built without them in mind."

    "In his breast pocket, folded twice: a list."
    "Every draft notice sent to a south-side address since 1965. Beside each one, a north-side deferment from the same months."
    "The two columns do not balance. They were never going to balance. That is the entire point of the list."

    thought "I haven't decided what to do with it. A list is not a weapon until you hand it to someone."

    "Thomas Whitehorse got his notice."
    "The oldest Whitehorse boy — Samuel set his arm when he was ten, the year the hospital wouldn't. He's twenty-two now. Fixes cars at a garage on Main Street. Saving money."
    "He hasn't told his mother yet."

    thought "Ada Whitehorse has held that family together with both hands since before I had this desk. This will be the thing that finally asks more than she has."

    jump ray_1967_thomas


label ray_1967_thomas:

    "There is a thing Ray has never said to anyone."
    "He did not serve in Korea. Student deferment. He was the one the system let stay."

    thought "It sits in me at a particular angle. It has sat there for fourteen years."
    thought "I built a life out of standing between people and the machine. The first time the machine reached for me, a piece of paper from a university held it back."
    thought "I am not allowed to forget that when I look at Thomas Whitehorse's notice. I do not let myself forget it."

    $ mark_talked("ray", "tribal_office", "list")

    jump ray_1967_explore


label ray_1967_explore:
    $ current_location = "tribal_office"
    jump explore_1955


# --- 1967 LOCATIONS ---

label location_tribal_office_1967:
    $ mark_visited("tribal_office")
    scene bg_tribal_office_1967 with dissolve
    "The tribal office. The federal poster, more faded than it was. The list in his breast pocket, where it stays."
    thought "I could get Thomas a quiet deferment and keep the list to myself. I could make Thomas a symbol. Or I could hand the list to a man with a badge and trust him to find the law inside it."
    return

label location_ihs_clinic_1967_ray:
    $ mark_visited("ihs_clinic")
    scene bg_ihs_clinic_1967 with dissolve
    "The IHS clinic. Ray's Tuesday table by the window, the case files spread across it."
    thought "Thomas's file is thin and correct. Correct has never once been enough by itself on this side of the tracks."
    return

label location_mount_zion_1967_ray:
    $ mark_visited("mount_zion")
    scene bg_mount_zion_1967 with dissolve
    "Mount Zion. Isaiah Chambers is organizing around the draft, and he would put Thomas Whitehorse's name at the front of it in a heartbeat."
    if not talked("ray", "mount_zion", "chambers_1967"):
        $ mark_talked("ray", "mount_zion", "chambers_1967")
        chambers "You have a list, Raymond. The whole south side knows you have a list."
        ray "Everyone seems to know what's in my pocket."
        chambers "Give it to me and it becomes a movement. Keep it and it stays your private grief."
        thought "He's not wrong. He's also asking me to spend Thomas Whitehorse to do it. Isaiah would spend himself first — but it isn't himself on offer."
    return

label location_frank_office_1967_ray:
    $ mark_visited("frank_office")
    scene bg_frank_office_1967 with dissolve
    "The detective's office. Frank DeLuca has, Ray is fairly sure, a list very much like his own. He came to it through arrest records and injury reports."
    if not talked("ray", "frank_office", "list_1967"):
        $ mark_talked("ray", "frank_office", "list_1967")
        frank "Coldwater. We've been circling each other for twelve years."
        ray "Thirteen. I count from the Clara Mae file."
        "Frank almost smiles. It doesn't quite arrive."
        frank "If you've got something that makes one of these notices into a legal question, I can move on it without your name on it."
        thought "He's offering to be the place the list goes that isn't a march and isn't a drawer. I have spent twelve years deciding whether to trust exactly this offer."
    return


# --- NUDGE ---

label ray_1967_nudge:

    scene bg_tribal_office_1967 with dissolve

    "The list is on the desk, unfolded, for the first time in months."

    thought "Three things I can do with it. None of them are clean. Each one spends a different person."

    menu ray_1967_nudge_choice:

        "Get Thomas a quiet deferment. Keep the list in your pocket.":
            jump ray_nudge_conservative_1967

        "Give the list to Frank privately. Let the law find the case in it." if talked("ray", "frank_office", "list_1967"):
            jump ray_nudge_middle_1967

        "Take the list public. Give it to Chambers. Thomas becomes the symbol.":
            jump ray_nudge_progressive_1967


label ray_nudge_conservative_1967:
    $ nudge_1967 = "conservative"
    $ policy_score -= 1
    $ marcus_status = "drafted"
    "Ray works a quiet channel. A sympathetic clerk, a misfiled hardship claim that happens to be true, a delay that becomes a deferment."
    thought "Thomas stays. His mother never learns how close it came, which is the kindest version and also a kind of lie."
    thought "The list goes back in my pocket. One boy protected. The two columns still don't balance. They never will if I only ever save one name at a time."
    jump ray_1967_nudge_after


label ray_nudge_middle_1967:
    $ nudge_1967 = "middle"
    $ frank_ray_trust = min(frank_ray_trust + 1, 3)
    ray "Frank. The list. I'm giving it to you as background, not as a banner."
    ray "If there's a legal question in here, you find it. The Whitehorse boy doesn't become a headline to do it."
    frank "Understood. It costs me something to use this. I'm not going to tell you what."
    ray "I didn't ask."
    thought "I have handed a white detective a list of my people's grief and trusted him to spend his own standing on it."
    thought "Twelve years ago I could not have done that. He earned it one careful exchange at a time, and so did I."
    jump ray_1967_nudge_after


label ray_nudge_progressive_1967:
    $ nudge_1967 = "progressive"
    $ policy_score += 2
    "Ray gives the list to Isaiah Chambers. Within a week the two columns are read aloud from the Mount Zion pulpit and printed in a mimeographed sheet that travels the south side hand to hand."
    if geri_samuel_connection or talked("geri", "geri_office", "report"):
        thought "Geri Habicht's data arrives alongside it, the statistical spine under the names. Numbers and faces in the same document. Harder to look away."
    thought "Thomas Whitehorse becomes a symbol he never asked to be. He carries it the way he carries everything — quietly, and at a cost I can see and he won't name."
    jump ray_1967_nudge_after


label ray_1967_nudge_after:
    scene bg_tribal_office_1967 with dissolve
    "Evening. The south-side street has gone quiet. Ray's son Daniel is sixteen now, doing homework at the kitchen table."
    jump ray_1967_period_end


label ray_1967_period_end:
    scene bg_tribal_office_1967 with dissolve
    "Evening. The office. The list is wherever Ray decided it should be."

    thought "I came back in 1955 because someone had to know the paperwork and also know the people."
    thought "Daniel is sixteen. In two years the machine will reach for him too, and I will find out what all this careful bridge-building was actually load-rated to carry."

    scene black with dissolve
    pause 0.5
    "1967."

    if nudge_1967 == "conservative":
        "Ray Coldwater got Thomas Whitehorse a quiet deferment."
        "Thomas stayed home. His mother never knew how close it came."
        pause 1.0
        "The list went back in Ray's pocket. He added four names to it that winter."
    elif nudge_1967 == "middle":
        "Ray gave the list to Frank DeLuca as background, not evidence."
        "Two notices became legal questions that quietly went away. The Whitehorse boy was one of them."
        pause 1.0
        "Nobody marched. Nobody's name was in the paper. Ray was not sure, some nights, whether that was wisdom or cowardice. He kept the bridge standing either way."
    elif nudge_1967 == "progressive":
        "Ray gave the list to Isaiah Chambers, and the south side read its own grief out loud."
        "Thomas Whitehorse's name went to the front of it."
        pause 1.0
        "Some of the machine flinched. Some of it hardened. Thomas carried what it cost. Ray carried what it cost Thomas."

    pause 1.5
    "The tracks are a fact, not a verdict. Some days he still needed reminding."
    pause 2.0

    jump advance_to_1979
