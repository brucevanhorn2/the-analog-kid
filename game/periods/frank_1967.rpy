## The Analog Kid — Period 1967
## Frank DeLuca — "The Man The Law Is Failing."
## His own draft list; Bobby Simmons; the Rotary Club deferment.

label frank_1967_begin:

    $ current_period = 1967
    $ current_location = "frank_office"
    $ mark_visited("frank_office")

    scene bg_frank_office_1967 with fade

    thought "Fifty-two years old. Chief's detective now — more visibility, less freedom. The leash is longer and it is still a leash."

    "In the bottom drawer of the metal desk, under the department forms, there is a list."
    "Frank came to it the way he comes to everything — through arrest records, injury reports, the paperwork nobody reads sideways."
    "South-side draft notices. North-side deferments. The arithmetic of who goes."

    thought "Coldwater has one too. We've never compared them. We didn't have to. We came to the same page from opposite ends of the same town."

    "Bobby Simmons shipped out last month. Frank knew Bobby — used to see him at the diner."
    "The factory owner's son who got the college deferment is in Frank's Rotary Club. Frank sat next to him last Tuesday and passed him the rolls."

    thought "The law I believe in and the law I enforce have been drifting apart for thirty years. This is the year I can see daylight between them."

    jump frank_1967_explore


label frank_1967_explore:
    $ current_location = "frank_office"
    jump explore_1955


# --- 1967 LOCATIONS ---

label location_frank_office_1967_frank:
    $ mark_visited("frank_office")
    scene bg_frank_office_1967 with dissolve
    "The detective's office. The bottom drawer. The list under the forms."
    thought "I can leave it where it is. I can take it to the county. Or I can use connections I'm not supposed to have to pull one specific boy back from the edge."
    return

label location_barbershop_1967:
    $ mark_visited("barbershop")
    scene bg_barbershop_1967 with dissolve
    "Joe Tolliver's barbershop. Joe is grayer. The radio plays the news now instead of the ballgame, and nobody asks him to change it."
    if not talked("frank", "barbershop", "rotary_1967"):
        $ mark_talked("frank", "barbershop", "rotary_1967")
        "Joe works the clippers without hurrying."
        townsperson "Heard the Simmons boy shipped out."
        frank "He did."
        townsperson "Heard the Blanton grandson didn't."
        frank "You hear a lot, Joe."
        townsperson "I hear what the chair tells me. Whether anybody listens, that's not my department, Detective."
        thought "He said the same thing to me in 1955 about Clarence Webb. He has been saying versions of it my whole career. He is always right and it never stops being heavy."
    return

label location_earls_diner_1967:
    $ mark_visited("earls_diner")
    scene bg_earls_diner_1967 with dissolve
    "Earl's. Dot is still behind the counter. There's a television on a shelf now, the war on it more often than not."
    if not talked("frank", "earls_diner", "bobby_mother_1967"):
        $ mark_talked("frank", "earls_diner", "bobby_mother_1967")
        "Bobby Simmons' mother is in the corner booth. She comes in about something unrelated — a parking matter, a small thing."
        "Frank helps her with the small thing. She mentions Bobby shipped out. Frank says the right words. He means them."
        thought "I said the right amount of the right thing. It was still the wrong amount, because the right amount does not exist for a mother whose boy went and the rich man's boy stayed."
    return


# --- NUDGE ---

label frank_1967_nudge:

    scene bg_frank_office_1967 with dissolve

    "After shift. The drawer is open. The list is on the desk in the light from the hallway."

    thought "My father came here in 1920 believing the law was the thing that made this country different. He needed to believe it. I'm still deciding what I need."
    thought "Three things I can do, and only one of them lets me keep telling myself the distinction between the law and the department is real."

    menu frank_1967_nudge_choice:

        "Leave the list in the drawer. Wait for a better moment.":
            jump frank_nudge_conservative_1967

        "Quietly facilitate Marcus Beaumont's reassignment. Use the connections.":
            jump frank_nudge_middle_1967

        "Take the draft inequity to the county DA. Put it on the record.":
            jump frank_nudge_progressive_1967


label frank_nudge_conservative_1967:
    $ nudge_1967 = "conservative"
    $ policy_score -= 1
    $ marcus_status = "drafted"
    "Frank closes the drawer. The list stays where it is."
    thought "I enforce the law as it's applied, not as it should be. I tell myself I'm waiting for a moment with better odds."
    thought "I have been waiting for that moment since 1955. I am beginning to suspect it is not coming, and that the waiting is itself the decision."
    jump frank_1967_nudge_after


label frank_nudge_middle_1967:
    $ nudge_1967 = "middle"
    $ marcus_status = "deferred"
    $ frank_ray_trust = min(frank_ray_trust + 1, 3)
    "Frank makes two phone calls he is not supposed to make. A reassignment. A boy named Marcus Beaumont moved off a list and onto a different one — stateside, a clerk's posting, alive."
    thought "It cost me something I can't itemize. A favor I'll never get back. A piece of the chief's trust I spent without telling him the price."
    thought "I saved one. I know exactly how that math works and exactly how little it changes. I did it anyway."
    jump frank_1967_nudge_after


label frank_nudge_progressive_1967:
    $ nudge_1967 = "progressive"
    $ policy_score += 1
    $ marcus_status = "drafted"
    "Frank takes the list to the county district attorney. Lays it on the desk. Explains what the two columns are."
    "The DA reads it. Acknowledges it. Does nothing official with it, because there is nothing official to do."
    thought "It's on the record now. A record that someone, someday, might find. That is the entire victory and it is not nothing."
    "Chief Harmon's successor calls Frank in on Friday. The conversation is short. It does not raise its voice. It does not need to."
    thought "My relationship with this department does not recover from this. I knew that when I walked to the DA's office. I walked anyway."
    jump frank_1967_nudge_after


label frank_1967_nudge_after:
    scene bg_frank_office_1967 with dissolve
    "Late. Shift change in the next room. The duty sergeant calling roll."
    jump frank_1967_period_end


label frank_1967_period_end:
    scene bg_frank_office_1967 with dissolve
    "Evening. Frank hasn't turned on the desk lamp. The hallway light is enough."

    thought "My father worked thirty years and died believing the law was worth believing in."
    thought "He wasn't wrong. He just didn't know all of what the law was doing while he believed in it."
    thought "I know. That's the difference between us, and it's the only inheritance I have to pass down, and I'm not sure who I'd pass it to."

    frank "What is it supposed to be for."

    "He says it quietly. Into the space where the question lives. The way a man asks something so he doesn't forget to keep asking it."

    scene black with dissolve
    pause 0.5
    "1967."

    if nudge_1967 == "conservative":
        "Detective DeLuca left the list in the drawer."
        "He told himself he was waiting for a better moment. The moment did not come."
        pause 1.0
        "Marcus Beaumont shipped out. Frank added his name to the list he was not using."
    elif nudge_1967 == "middle":
        "Detective DeLuca spent connections he wasn't supposed to have and pulled Marcus Beaumont off the line."
        "A clerk's posting. Stateside. Alive."
        pause 1.0
        "He never told Ray Coldwater or Samuel Beaumont what it cost. They never asked. The arithmetic of the war did not change. One boy came home anyway."
    elif nudge_1967 == "progressive":
        "Detective DeLuca took the inequity to the county DA. Nothing happened officially."
        "It went on the record. The record outlived the silence around it."
        pause 1.0
        "Frank and the chief worked six more years without mentioning the Friday they stopped trusting each other. They were professional about it. The word covers a great deal of ground in a small department."

    pause 1.5
    "What is it supposed to be for."
    pause 2.0

    jump advance_to_1979
