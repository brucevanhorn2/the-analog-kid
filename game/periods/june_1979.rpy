## The Analog Kid — Period 1979
## June Holloway — "The Woman Whose Foundation Is Cracking."
## The oil bust; the budget vote; Dot behind the counter.

label june_1979_begin:

    $ current_period = 1979
    $ current_location = "city_hall"
    $ mark_visited("city_hall")

    scene bg_city_hall_1979 with fade

    thought "Fifty-eight years old. The oil bust is here. The Holloway family is not ruined. We are simply no longer comfortable in the way we were comfortable, which is its own kind of ruin for people who have never known anything else."

    "Her father's derrick is quiet. He has not said anything about it directly. Neither has she. The performance at the derrick in 1955 has calcified into a permanent mutual pretense."

    "The city budget is short — the bust has gutted the tax base. Something has to be cut."
    "The conservative faction wants to cut south-side services. The progressive faction wants to cut highway maintenance, which serves mostly north-side commuters. June holds the deciding vote. Again."

    thought "Everyone is angrier than usual because everyone is scared. Scared people vote like the thing they are about to lose is the only thing that was ever real."

    jump june_1979_explore


label june_1979_explore:
    $ current_location = "city_hall"
    jump explore_1955


# --- 1979 LOCATIONS ---

label location_city_hall_1979:
    $ mark_visited("city_hall")
    scene bg_city_hall_1979 with dissolve
    "The council chamber. Two factions, both frightened, both certain. Her chair, third from the left, the deciding one."
    thought "Cut the south side. Cut the highway. Or find the third thing that costs me the most and protects the people with the least."
    return

label location_earls_diner_1979:
    $ mark_visited("earls_diner")
    scene bg_earls_diner_1979 with dissolve
    "Earl's. Dot has been behind this counter for thirty years. There's a television on the shelf now, the bust on the news, the booths a little emptier."
    if not talked("june", "earls_diner", "dot_1979"):
        $ mark_talked("june", "earls_diner", "dot_1979")
        $ june_south_side_trust = june_south_side_trust + 1
        "June stops in. For the first time in thirty years of nodding at each other, she and Dot have a real conversation."
        dot "You're going to cut something, honey. Everybody can see it coming. Question is whether you cut the people who can drive to the next county for it, or the people who can't."
        june "That's the question I've been trying not to say out loud."
        dot "I've watched this town from behind this counter since before you had that chair. The ones who can't drive to the next county — they're the ones who've got nowhere else to be cut from."
        thought "Dot has the whole town's ledger in her head and no vote. I have a vote and have spent thirty years learning the ledger she keeps for free."
    return

label location_holloway_derrick_1979:
    $ mark_visited("holloway_derrick")
    scene bg_holloway_derrick_1979 with dissolve
    "The derrick. Quiet. The pump jack still, the way a thing is still when it has stopped rather than rested."
    "Her father is there, looking at it. He does not say anything practical. Neither does she. The performance finally cracks, just slightly."
    thought "He built this by choosing, he told me once. He chose well for forty years and then the price of oil chose for him. I am about to choose for forty families who do not get a vote in the price of anything."
    return


# --- NUDGE ---

label june_1979_nudge:

    scene bg_city_hall_1979 with dissolve

    "The budget vote is Thursday. The cut is hers to aim."

    thought "Three ways to cut. Each one is a sentence about who this town decides is load-bearing and who it decides is optional."

    menu june_1979_nudge_choice:

        "Cut south-side services. Protect the tax base. The logic is defensible and you know exactly what it costs.":
            jump june_nudge_conservative_1979

        "Across-the-board proportional cuts, with a protection floor for the three highest-impact south-side services." if june_south_side_trust >= 1:
            jump june_nudge_middle_1979

        "Cut highway maintenance. It's a north-side burden the north side can absorb. Lose the conservative faction for good.":
            jump june_nudge_progressive_1979


label june_nudge_conservative_1979:
    $ nudge_1979 = "conservative"
    $ policy_score -= 1
    "June cuts the south-side services. The tax base is protected. The logic holds together in the chamber, in daylight, on paper."
    thought "The clinic Dot's people use loses two days a week. The school nutrition program thins. The sanitation route stretches."
    thought "I protected the part of the town that can drive to the next county for what it needs. I know that sentence. I have heard myself become the kind of person who can say it without flinching, and the not-flinching is the part that frightens me."
    jump june_1979_nudge_after


label june_nudge_middle_1979:
    $ nudge_1979 = "middle"
    $ june_south_side_trust = june_south_side_trust + 1
    "June engineers across-the-board proportional cuts — everyone bleeds a little — with a protection floor under the three south-side services with the highest health impact: the clinic, school nutrition, sanitation."
    thought "Geri Habicht's data told me which three would be devastating to cut versus merely painful. Thirty years of south-side relationships told me she was right."
    thought "Everyone is unhappy, proportionally, which is the closest thing to fair a frightened council will hold still for. The people with nowhere else to be cut from keep the floor under them. Barely. On purpose."
    jump june_1979_nudge_after


label june_nudge_progressive_1979:
    $ nudge_1979 = "progressive"
    $ policy_score += 2
    "June cuts highway maintenance. The north side can absorb a rougher commute. The south-side services hold."
    thought "I lose the conservative faction permanently. The roads my own family's name is attached to start to crack, literally, under the weight of what I chose to stop maintaining."
    thought "I protected the people who couldn't protect themselves and spent the last of my inherited goodwill to do it. My father would not understand this vote. I am no longer sure I need him to."
    jump june_1979_nudge_after


label june_1979_nudge_after:
    scene bg_city_hall_1979 with dissolve
    "Evening. The chamber empties. The seal catches the last of a thinner, colder light."
    jump june_1979_period_end


label june_1979_period_end:
    scene bg_city_hall_1979 with dissolve
    "Evening. She is still at the long table. The clipping from 1955 — first woman on the council — feels like it is about a different person."

    thought "Progress. I ran on it. In a boom it meant roads and schools and everybody got a little. In a bust it means deciding, out loud, whose little gets taken first."
    thought "The bust did the conservative faction a cruelty I have been quietly waiting for since 1955: it asked their philosophy what the plan was when the boom ended. Their philosophy did not have one. Mine has only ever been the cost of pretending it did."

    scene black with dissolve
    pause 0.5
    "1979."

    if nudge_1979 == "conservative":
        "Councilwoman Holloway cut the south-side services. The tax base held."
        "The clinic lost two days a week. The people who used it had nowhere else to be cut from, exactly as Dot had said."
        pause 1.0
        "June drove a smoother road to a chamber that balanced its budget. She did not slow down at the clinic."
    elif nudge_1979 == "middle":
        "Councilwoman Holloway found the third way — proportional cuts with a floor under the three services that would have been devastating to lose."
        "Everyone bled a little. The people with the least kept the least taken."
        pause 1.0
        "It required Geri Habicht's data and thirty years of relationships to know which three. Nobody thanked her. The thing she prevented left no evidence."
    elif nudge_1979 == "progressive":
        "Councilwoman Holloway cut highway maintenance and held the south-side services whole."
        "The north-side roads cracked. So did the last of her standing with the conservative faction."
        pause 1.0
        "Her family's name was on some of those roads. She let them crack. She was not certain she had been right. She was certain she could not have done otherwise."

    pause 1.5
    "The clock on City Hall was still running. It cost more to keep it running now. She kept it running."
    pause 2.0

    jump advance_to_1991
