## The Analog Kid — Period 1979
## Frank DeLuca — "The Man Spending His Credit."
## The Blanton investigation; Harold Jr. is not a stranger.

label frank_1979_begin:

    $ current_period = 1979
    $ current_location = "frank_office"
    $ mark_visited("frank_office")

    scene bg_frank_office_1979 with fade

    thought "Sixty-four years old. They called me in to investigate the Blanton accident. Three dead. I know this investigation. I know how it ends if I let it run its normal course."

    "Frank has spent thirty years building credit with both sides of Middletown — careful, strategic, never spending more than he had."
    "This investigation is going to cost him something significant regardless of what he does."

    "Harold Blanton Jr. is not a stranger. Their sons played baseball together. Frank has eaten dinner at the Blanton house."
    thought "That is not relevant to the investigation. It is completely relevant to the investigation. Both of those sentences are true and I have to hold them at the same time."

    "He has Geri Habicht's injury data, if she gave it to him. He has the shape of a verbal complaint Ray Coldwater knows about, if Ray trusts him with it. Separately, two dismissible things. Together, a case."

    $ mark_talked("frank", "frank_office", "blanton")

    jump frank_1979_explore


label frank_1979_explore:
    $ current_location = "frank_office"
    jump explore_1955


# --- 1979 LOCATIONS ---

label location_frank_office_1979_frank:
    $ mark_visited("frank_office")
    scene bg_frank_office_1979 with dissolve
    "The detective's office. The Blanton file thickens on the desk. The new chief — younger, political — wants a clean resolution. Frank knows what clean means."
    thought "Negligence, or criminal, or the narrow negotiated thing in between. Each one spends a different amount of the credit I've spent thirty years not spending."
    return

label location_blanton_factory_1979_frank:
    $ mark_visited("blanton_factory")
    scene bg_blanton_factory_1979 with dissolve
    "Blanton. The accident site. Frank walks it the way he walks everything — methodically, not performing the weight, carrying it anyway."
    if not talked("frank", "blanton_factory", "investigate_1979"):
        $ mark_talked("frank", "blanton_factory", "investigate_1979")
        "He finds the corners that were cut. He finds, in the records, the spike Geri Habicht saw two years early. He finds, in the silences, the warning George Runningwater gave a foreman six months out."
        thought "Geri's numbers and Ray's whisper and my own eyes. Three sources that are each deniable alone. I am the place they could stop being deniable, if I decide to be."
    return

label location_barbershop_1979:
    $ mark_visited("barbershop")
    scene bg_barbershop_1979 with dissolve
    "Joe Tolliver's barbershop. Joe is old now. He cuts slower and hears the same amount, which is everything."
    townsperson "Blanton boy and your boy played ball together, didn't they."
    frank "They did."
    townsperson "Hard thing, investigating a man you've had supper with."
    frank "Hardest part of the job, Joe. Always was."
    townsperson "Whether you do it anyway. That's not my department, Detective."
    return


# --- NUDGE ---

label frank_1979_nudge:

    scene bg_frank_office_1979 with dissolve

    "The file is built as far as it can be built. The chief is waiting. Harold is waiting. The families are waiting."

    thought "Thirty years of credit in this town. I get to spend it once, here, in one of three ways."

    menu frank_1979_nudge_choice:

        "Build the case you can — negligence, not criminal. Civil liability, settlements. Approximate justice.":
            jump frank_nudge_conservative_1979

        "Negotiate it — lesser plea, factory under real oversight, compensation that means something." if talked("frank", "blanton_factory", "investigate_1979"):
            jump frank_nudge_middle_1979

        "Pursue criminal charges. Use everything. Let the political fallout take your career.":
            jump frank_nudge_progressive_1979


label frank_nudge_conservative_1979:
    $ nudge_1979 = "conservative"
    $ policy_score -= 1
    $ harold_outcome = "protected"
    "Frank builds the case he can build cleanly. Negligence. Civil liability. Harold faces money, not prison. The families get settlements."
    thought "I tell myself justice was approximate. Approximate is a word I have used a great deal in thirty years and trusted less each time."
    thought "I had supper at that man's house. I am not certain whether that made me merciful or compromised. The file says negligence. The file does not say which."
    jump frank_1979_nudge_after


label frank_nudge_middle_1979:
    $ nudge_1979 = "middle"
    $ harold_outcome = "negotiated"
    $ frank_ray_trust = min(frank_ray_trust + 1, 3)
    $ geri_frank_connection = True
    "Frank negotiates the outcome. Harold pleads to a lesser charge. The factory stays open under real safety oversight. The families get compensation that means something."
    thought "It took everything Geri and Ray gave me, and the chief believing I could manage the result, and thirty years of accumulated trust spent in one room."
    thought "Nobody got everything. Harold got a record. The families got accountability and their jobs. The town got to keep its lungs and its conscience at the same time, barely."
    jump frank_1979_nudge_after


label frank_nudge_progressive_1979:
    $ nudge_1979 = "progressive"
    $ policy_score += 2
    $ harold_outcome = "prosecuted"
    "Frank pursues criminal charges. He uses Geri's analysis and Ray's lead and his own eyes. Harold Blanton Jr. is prosecuted."
    thought "My career does not survive the political fallout. I knew that when I signed the charges. The new chief made it clear and I signed them in front of him."
    thought "I had supper at that man's house. I charged him anyway, because three men are dead and the law I actually believe in does not have a clause for men you've eaten with."
    jump frank_1979_nudge_after


label frank_1979_nudge_after:
    scene bg_frank_office_1979 with dissolve
    "Late. Shift change. Frank retires in a few years and he can feel the shape of it coming."
    jump frank_1979_period_end


label frank_1979_period_end:
    scene bg_frank_office_1979 with dissolve
    "Evening. The hallway light is enough. It usually is now."

    thought "My father believed the law was the thing that made this country different. He died believing it. He never had to investigate a man he'd had supper with."
    thought "I did. That's the whole inheritance, right there — knowing what the law is doing while you still believe in it."

    frank "What is it supposed to be for."

    scene black with dissolve
    pause 0.5
    "1979."

    if nudge_1979 == "conservative":
        "Detective DeLuca built the case he could build. Negligence. Settlements. No prison."
        "Harold Blanton Jr. kept his freedom and his factory and lost something quieter."
        pause 1.0
        "Frank kept his career and lost something quieter too. He did not examine which of them had lost more. He suspected he knew."
    elif nudge_1979 == "middle":
        "Detective DeLuca negotiated the outcome — a plea, real oversight, real compensation."
        "He spent thirty years of credit in a single room and walked out with nobody fully satisfied and nobody destroyed."
        pause 1.0
        "It is the kind of result that leaves no monument and no scandal. Frank had come to believe those were the results worth having."
    elif nudge_1979 == "progressive":
        "Detective DeLuca pursued criminal charges and Harold Blanton Jr. was prosecuted."
        "Frank's career did not survive it."
        pause 1.0
        "He retired earlier than he'd planned, with the town divided about whether he was a man of principle or a man who'd forgotten his place. He knew which. He kept it to himself."

    pause 1.5
    "What is it supposed to be for."
    pause 2.0

    jump advance_to_1991
