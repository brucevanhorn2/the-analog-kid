## The Analog Kid — Period 1979
## Raymond Coldwater — "The Man The System Started Listening To."
## Blanton; George Runningwater's unwritten complaint; the widow's toolbox.

label ray_1979_begin:

    $ current_period = 1979
    $ current_location = "tribal_office"
    $ mark_visited("tribal_office")

    scene bg_tribal_office_1979 with fade

    thought "Fifty-six years old. Tired in a way that has become structural rather than something a night's sleep touches."

    "The Blanton accident. Two of the three dead are south-side men. Their families came to Ray first. He knows how these things end without intervention."
    "He also knows something nobody else knows: George Runningwater — tribal member, one of the dead — filed a verbal complaint about the safety violations six months ago. To his foreman. Nothing written. The foreman is still employed. The complaint does not officially exist."

    thought "A spoken warning, six months early, to exactly the wrong person. It is the truest thing I know about that factory and it is legally almost nothing."

    "Thomas Whitehorse came back from Vietnam. He works at Blanton now. The morning after the accident he stood outside the gates, not sure if he still had a job, in a country he had just finished fighting for."

    $ mark_talked("ray", "tribal_office", "complaint")

    jump ray_1979_explore


label ray_1979_explore:
    $ current_location = "tribal_office"
    jump explore_1955


# --- 1979 LOCATIONS ---

label location_tribal_office_1979:
    $ mark_visited("tribal_office")
    scene bg_tribal_office_1979 with dissolve
    "The tribal office. The younger council members want to file a civil suit immediately. The elder Ray trusts is dying. The newer voices are louder."
    thought "Six months ago George said something true to a foreman who did nothing. I can keep that quiet, make it a banner, or hand it to a detective and let him find the law inside it."
    return

label location_ihs_clinic_1979_ray:
    $ mark_visited("ihs_clinic")
    scene bg_ihs_clinic_1979 with dissolve
    "The IHS clinic. George Runningwater's widow is here. Not sick. Somewhere to sit. She has his toolbox and doesn't know why she brought it."
    if not talked("ray", "ihs_clinic", "widow_1979"):
        $ mark_talked("ray", "ihs_clinic", "widow_1979")
        "She hands Ray the toolbox to hold. He holds it for longer than necessary. She lets him."
        thought "Surfacing what George said makes her the story. The grinding process, the reporters, the factory's lawyers, all of it landing on a woman holding a dead man's tools."
        thought "Keeping it quiet protects her and buries him a second time. There is no version of this that does not cost her something."
    return

label location_blanton_factory_1979_ray:
    $ mark_visited("blanton_factory")
    scene bg_blanton_factory_1979 with dissolve
    "Blanton. The smokestacks are cold. Thomas Whitehorse is at the gate, not working, not leaving."
    thought "He fought a war and came home to the one job in town that pays, in the building that just killed two of his neighbors. The country has a particular gift for that arrangement."
    return

label location_frank_office_1979_ray:
    $ mark_visited("frank_office")
    scene bg_frank_office_1979 with dissolve
    "Frank DeLuca's office. He is closer to the truth of the accident than Ray expected. Ray recalibrates."
    if not talked("ray", "frank_office", "frank_1979"):
        $ mark_talked("ray", "frank_office", "frank_1979")
        frank "I hear there was a complaint before. Verbal."
        ray "You hear a lot, Detective."
        frank "If it's background and not evidence, I can use it without the widow ever being named. If it's evidence, she becomes the case."
        thought "Twenty-four years of circling. He is offering to be the third option — the one between a drawer and a banner. I have spent all of those years deciding whether to trust exactly this."
    return


# --- NUDGE ---

label ray_1979_nudge:

    scene bg_tribal_office_1979 with dissolve

    thought "George said something true and nobody wrote it down. Now I decide whether the truth of it costs his widow or the factory."

    menu ray_1979_nudge_choice:

        "Keep the verbal complaint quiet. It's legally useless and surfacing it grinds the widow down.":
            jump ray_nudge_conservative_1979

        "Give it to Frank as background, not evidence. Let him find a use that doesn't name her." if talked("ray", "frank_office", "frank_1979"):
            jump ray_nudge_middle_1979

        "Surface it publicly. Shift the burden onto the factory. Accept that the widow becomes the story.":
            jump ray_nudge_progressive_1979


label ray_nudge_conservative_1979:
    $ nudge_1979 = "conservative"
    $ policy_score -= 1
    if runningwater_complaint == "buried":
        $ runningwater_complaint = "buried"
    "Ray keeps it quiet. The verbal complaint stays a thing only he and a foreman know, and the foreman is not talking."
    thought "I protect the widow from the grinding. I also let George's warning die the same way he did — unheard, on the record of nothing."
    thought "I have made this trade before. Protect the living person in front of me, lose the larger thing. I am never sure it is wrong. I am never sure it is right."
    jump ray_1979_nudge_after


label ray_nudge_middle_1979:
    $ nudge_1979 = "middle"
    $ runningwater_complaint = "frank_background"
    $ frank_ray_trust = min(frank_ray_trust + 1, 3)
    ray "Frank. George Runningwater warned his foreman six months ago. That's all I've got and it isn't written anywhere. Use it as background. The widow's name stays out of it."
    frank "Understood. It's enough to know where to dig. It won't be enough to put her on a stand, which is the point."
    thought "I have handed a detective my people's grief as a map and trusted him not to make a monument of the widow to read it."
    thought "He earned that across twenty-four years. So did I. The bridge holds one more crossing."
    jump ray_1979_nudge_after


label ray_nudge_progressive_1979:
    $ nudge_1979 = "progressive"
    $ policy_score += 2
    $ runningwater_complaint = "surfaced"
    "Ray surfaces it. The widow testifies that her husband warned them six months before the building killed him. She becomes the story, the grinding process, the photograph in the paper."
    thought "The burden shifts onto Blanton, where it belongs. It also lands on a woman holding a toolbox, which is where it should never have to land and always does."
    thought "She agreed. She said George would have wanted his warning to mean something even six months late. I am holding her to a courage she chose, and I will carry what it costs her."
    jump ray_1979_nudge_after


label ray_1979_nudge_after:
    scene bg_tribal_office_1979 with dissolve
    "Evening. Daniel is grown and gone to college — the first in the family. Ray walks home past the cold factory."
    jump ray_1979_period_end


label ray_1979_period_end:
    scene bg_tribal_office_1979 with dissolve
    "Evening. The office. The toolbox, if Ray kept it, sits on the corner of the desk."

    thought "The tribal council has changed. Younger, more aggressive, less patient with my careful navigation of white institutions."
    thought "Maybe they're right. Maybe twenty-four years of careful was twenty-four years of slow. I built a bridge. I am no longer certain a bridge was what the moment needed."

    scene black with dissolve
    pause 0.5
    "1979."

    if nudge_1979 == "conservative":
        "Ray Coldwater kept George Runningwater's warning quiet."
        "The widow was spared the grinding. George's warning died as unheard as he had."
        pause 1.0
        "The civil suit settled small. The factory reopened. Ray added it to the list of things he had protected people from by letting them stay invisible."
    elif nudge_1979 == "middle":
        "Ray gave the warning to Frank as background. The widow was never named."
        "It told the investigation where to dig, and the digging found things that did not need her testimony to stand."
        pause 1.0
        "Frank never said what it cost him. Ray never asked. The factory reopened under real oversight."
    elif nudge_1979 == "progressive":
        "Ray surfaced the warning. The widow testified, and became the story whether she wanted to or not."
        "George Runningwater's six-month-old sentence finally did something."
        pause 1.0
        "It cost her a year of her life to reporters and lawyers. She said, afterward, that she would do it again. Ray believed her and grieved that she had to."

    pause 1.5
    "The tracks are a fact, not a verdict. Some days, that year, he could not make himself believe it."
    pause 2.0

    jump advance_to_1991
