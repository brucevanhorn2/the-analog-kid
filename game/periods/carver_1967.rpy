## The Analog Kid — Period 1967
## Rev. Thomas Carver — "The Man Whose Answers Stop Working."
## Bobby Simmons' draft physical; Chambers' march.

label carver_1967_begin:

    $ current_period = 1967
    $ current_location = "first_baptist"
    $ mark_visited("first_baptist")

    scene bg_first_baptist_1967 with fade

    thought "Fifty years old."
    thought "First Baptist is still full on Sundays. But the fullness has a fault line through it now."
    thought "Half my deacons think Isaiah Chambers is a troublemaker. Half think I'm a coward."
    thought "They are both, in their way, paying attention."

    "The war is taking boys from both sides of the congregation. It is not taking them equally."
    "Carver knows about Marcus Beaumont. He knows about the factory owner's son with the deferment."
    "He knew about both in 1955, in their earlier shapes. He said nothing then."

    thought "The habit of silence is load-bearing now. You cannot remove it without asking what it was holding up."

    jump carver_1967_bobby


label carver_1967_bobby:

    "The side door. Bobby Simmons, who grew up in the third pew, who Carver baptized at twelve."
    "His draft physical is Thursday."

    bobby "Pastor. Can I ask you something and have it stay in this room?"

    carver "Always."

    bobby "Is it a sin to be afraid?"

    thought "There is a sermon answer to that. I have given it from the pulpit. It is true and it is useless."
    thought "Courage is not the absence of fear. Fear is the soil courage grows in. The Lord does not ask you not to tremble."
    thought "I could say all of it and send him to Thursday's physical with a verse in his pocket and nothing in his hands."

    $ mark_talked("bobby", "first_baptist", "afraid")

    if carver_samuel_connection:
        thought "Or I could remember that I know a doctor on the south side. Samuel Beaumont."
        thought "We built something across the tracks in 1955, quietly, over a man named Eddie Briggs."
        thought "Samuel has, more than once, found a legitimate medical reason a frightened boy should not be sent to die."

    jump carver_1967_chambers


label carver_1967_chambers:

    "Word comes the way it comes — through a deacon's wife, through the barbershop, through the air."
    "Isaiah Chambers is organizing a march to city hall about the draft. About whose sons go and whose stay."
    "He has asked, through a third party and then directly, whether Reverend Carver of First Baptist will stand beside him."

    thought "Isaiah and I have kept a respectful distance for twelve years. Two pastors, two churches, one set of tracks between us."
    thought "He is not asking me to agree with everything. He is asking me to stand where everyone can see me standing."
    thought "That is the whole of it. That is the entire question, and it is enormous."

    $ mark_talked("chambers", "mount_zion", "march")

    jump carver_1967_explore


label carver_1967_explore:

    $ current_location = "first_baptist"
    jump explore_1955


# --- 1967 LOCATIONS ---

label location_first_baptist_1967:
    $ mark_visited("first_baptist")
    scene bg_first_baptist_1967 with dissolve
    "First Baptist. The pews Harold Blanton donated in 1947. The fault line nobody names from the pulpit."
    if talked("chambers", "mount_zion", "march"):
        thought "Isaiah is waiting to hear whether I'll stand with him. The window of my study faces the route his march will take."
    return

label location_vfw_hall_1967:
    $ mark_visited("vfw_hall")
    scene bg_vfw_hall_1967 with dissolve
    "The VFW Hall. Eddie Briggs has been gone since '63. Other men sit where he sat."
    thought "The men here gave sons to two wars and are giving them to a third. They do not want to hear that the giving is uneven."
    thought "They are not wrong that it is hard to hear. They are wrong about what to do with it."
    return

label location_mount_zion_1967_carver:
    $ mark_visited("mount_zion")
    scene bg_mount_zion_1967 with dissolve
    "Mount Zion Baptist. Isaiah Chambers' church, on the south side."
    if not talked("carver", "mount_zion", "visit_1967"):
        $ mark_talked("carver", "mount_zion", "visit_1967")
        chambers "Thomas. You came across the tracks. People will have noticed."
        carver "People notice everything I do. I've stopped letting that decide things."
        chambers "Have you. That would be new."
        "It is said without cruelty. Isaiah Chambers has earned the right to be exact with him."
        chambers "I'm not asking you to become me. I'm asking you to be seen next to me for one afternoon."
        thought "Korea took something out of Isaiah and put something harder in its place. When he asks plainly, it is because plainness cost him."
    else:
        thought "Isaiah's church. Smaller than mine. Fuller, in the way that matters and can't be counted."
    return

label location_city_hall_1967_carver:
    $ mark_visited("city_hall")
    scene bg_city_hall_1967 with dissolve
    "City Hall. The steps where a march would end. The council chamber where June Holloway counts votes that never quite reach the south side."
    thought "If Isaiah marches here, the question of where I was standing becomes a matter of public record."
    return


# --- NUDGE ---

label carver_1967_nudge:

    scene bg_first_baptist_1967 with dissolve

    "Saturday night. The sermon for tomorrow is half-written. The march is Monday."

    thought "Bobby's physical is Thursday. Isaiah's march is Monday. My sermon is tomorrow."
    thought "Three things, and the town will read all three as one answer."

    menu carver_1967_nudge_choice:

        "Decline the march. Counsel wartime unity. Watch from the study window.":
            jump carver_nudge_conservative_1967

        "Don't march — but open First Baptist as a meeting place afterward.":
            jump carver_nudge_middle_1967

        "Stand with Chambers. Say it from the pulpit and mean it.":
            jump carver_nudge_progressive_1967


label carver_nudge_conservative_1967:
    $ nudge_1967 = "conservative"
    $ policy_score -= 1
    $ bobby_outcome = "shipped"
    carver "I told Isaiah I couldn't march. Not now. Not with the church the way it is."
    thought "I gave Bobby the sermon answer. He shipped out Thursday with a verse and nothing in his hands."
    thought "On Monday I watched Isaiah walk past my window. I did not move from behind the glass."
    thought "The congregation stayed whole. I am the one with the crack in me now."
    jump carver_1967_nudge_after


label carver_nudge_middle_1967:
    $ nudge_1967 = "middle"
    if carver_samuel_connection:
        $ bobby_outcome = "deferred"
    else:
        $ bobby_outcome = "shipped"
    carver "I won't march. But the doors of First Baptist are open Monday evening, to anyone who wants to talk about what the march was for."
    thought "Technically neutral. Everyone understood it was not neutral."
    if carver_samuel_connection:
        thought "And I called Samuel Beaumont about Bobby. Quietly. A frightened boy got a real examination instead of a verse."
        thought "Bobby stayed. I carry what I know about how that happened, and I carry it gladly."
    else:
        thought "Bobby I could not help. I had built no bridge to the south side that would carry his weight in time."
    thought "I lost a few deacons over the open doors. Not a third. Enough to feel."
    jump carver_1967_nudge_after


label carver_nudge_progressive_1967:
    $ nudge_1967 = "progressive"
    $ policy_score += 1
    if carver_samuel_connection:
        $ bobby_outcome = "deferred"
    else:
        $ bobby_outcome = "shipped"
    carver "I stood beside Isaiah Chambers on the city hall steps. The whole town saw where I was standing."
    "Sunday's sermon was Ezekiel again. The valley. The bones. The question that is not yes and is not no."
    thought "I lost a third of the congregation by the following Sunday. The pews Harold Blanton paid for have gaps in them now."
    thought "Isaiah and I did not become the same man. We became two men who had stood in the same place once, on purpose."
    if carver_samuel_connection:
        thought "Samuel found Bobby a deferment. Between the march and the boy, I spent more this year than I knew I had."
    jump carver_1967_nudge_after


label carver_1967_nudge_after:
    scene bg_first_baptist_1967 with dissolve
    "Late. The sanctuary is dark except for the lamp in the study."
    jump carver_1967_period_end


label carver_1967_period_end:
    scene bg_first_baptist_1967 with dissolve
    "Evening. The church is empty. The maple outside has nearly finished going yellow."

    "Carver opens his Bible. Not to anything. The way you open something you need to have an answer."

    carver "Let us rejoice and be glad in it."

    thought "Samuel Beaumont says the first half of that under his breath on the south side. I have heard him do it."
    thought "I say the second half on the north side. We have never once said the whole thing together."
    thought "I am beginning to think the whole thing is the only sermon I have left worth preaching."

    scene black with dissolve
    pause 0.5
    "1967."

    if nudge_1967 == "conservative":
        "Reverend Carver counseled patience and kept his congregation whole."
        "Isaiah Chambers marched without him."
        pause 1.0
        "Bobby Simmons shipped out Thursday. Carver wrote his mother a letter every month he was gone."
    elif nudge_1967 == "middle":
        "Reverend Carver opened his doors but kept his feet still."
        "It cost him a few families and bought him a few honest conversations."
        pause 1.0
        if bobby_outcome == "deferred":
            "Bobby Simmons stayed home, for a medical reason a south-side doctor happened to find in time."
        else:
            "Bobby Simmons shipped out. The doors being open did not reach him in time."
    elif nudge_1967 == "progressive":
        "Reverend Carver stood on the city hall steps beside Isaiah Chambers."
        "First Baptist lost a third of its pews by Sunday and found something it had been missing for longer than that."
        pause 1.0
        if bobby_outcome == "deferred":
            "Bobby Simmons stayed home. Carver never told anyone what it cost or who it cost."

    pause 1.5
    "Lord God, thou knowest."
    pause 2.0

    jump advance_to_1979
