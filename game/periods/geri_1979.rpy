## The Analog Kid — Period 1979
## Dr. Geraldine Habicht — "The Woman The Town Finally Reads."
## The 18-month predictive analysis; Frank comes asking.

label geri_1979_begin:

    $ current_period = 1979
    $ current_location = "geri_office"
    $ mark_visited("geri_office")

    scene bg_geri_office_1979 with fade

    thought "Fifty-nine years old. My research is cited in three state policy documents now. One of them credited me as 'community health studies' in a footnote."
    thought "I noted that with the expression I use for everything."

    "She has switched to filtered cigarettes. Kent, or Viceroy. She hates them. She tells anyone who notices that the filtration data shows a statistically meaningful reduction in tar delivery. She says this while visibly enjoying them less."

    "The Blanton accident. Three dead."
    "Two years ago, after a statistical spike in worker injury claims that nobody else noticed, Geri pulled the county safety inspection records. She built a predictive analysis. She calculated the probability of a serious incident and found it significant."

    thought "I made no formal report. I had no institutional standing and I knew exactly how it would be received — as a sociologist's anxiety, filed and forgotten."
    thought "I was right about the probability. I was right about the dismissal. Three people are dead."

    $ mark_talked("geri", "geri_office", "analysis")

    jump geri_1979_explore


label geri_1979_explore:
    $ current_location = "geri_office"
    jump explore_1955


# --- 1979 LOCATIONS ---

label location_geri_office_1979:
    $ mark_visited("geri_office")
    scene bg_geri_office_1979 with dissolve
    "The office. The south window. The filtered cigarettes she resents in the ashtray."
    if not talked("geri", "geri_office", "frank_1979"):
        $ mark_talked("geri", "geri_office", "frank_1979")
        "Frank DeLuca comes to the college. He asks general questions about industrial safety statistics. Fishing. They have been circling each other since 1955."
        frank "I'm told you keep numbers on things before the things happen."
        geri "I keep numbers on everything. The order they happen in is the data's business, not mine."
        frank "Do you have anything relevant to what happened at Blanton."
        "She does not answer at once. She is deciding, in real time, how much of herself to hand a careful detective."
        thought "He came to me directly. That is either respect or a trap, and with Frank DeLuca it has always been respect wearing the shape of a trap so neither of us has to say the word."
    return


# --- NUDGE ---

label geri_1979_nudge:

    scene bg_geri_office_1979 with dissolve

    "The injury data is public record. The predictive analysis is hers, and eighteen months old, and a documented act of foresight she chose not to act on."

    thought "Three ways to answer Frank's question. Each one exposes a different amount of what I knew and when I knew it."

    menu geri_1979_nudge_choice:

        "Share the injury data. Keep the predictive analysis to yourself.":
            jump geri_nudge_conservative_1979

        "Give Frank the analysis privately. Let him decide how it enters the investigation." if talked("geri", "geri_office", "frank_1979"):
            jump geri_nudge_middle_1979

        "Give Frank everything — the analysis and a written statement on why you didn't report it.":
            jump geri_nudge_progressive_1979


label geri_nudge_conservative_1979:
    $ nudge_1979 = "conservative"
    $ policy_score -= 1
    "She gives Frank the injury claim data. Public record, all of it. She does not mention the eighteen-month analysis."
    thought "Evidence without exposure. Self-protective. Not dishonest, exactly. The data I hand him is true. The data I keep is also true."
    "She stubs out a filtered cigarette half-finished and looks at the ashtray."
    thought "I have spent thirty years telling this town what the numbers mean. I am aware of the particular irony of my own dataset."
    jump geri_1979_nudge_after


label geri_nudge_middle_1979:
    $ nudge_1979 = "middle"
    $ geri_frank_connection = True
    geri "Here's the analysis, Frank. Eighteen months old. You decide how it enters your investigation. You'll know better than I will what it can survive."
    frank "You understand what handing me this says about what you knew."
    geri "I understand it precisely. I calculated it. Take the file."
    thought "I trust his judgment about the courtroom because I have watched him exercise judgment in this town for twenty-four years without once spending it cheaply."
    thought "I give him the foresight and the cost of the foresight in the same folder. He carries both more carefully than I could."
    jump geri_1979_nudge_after


label geri_nudge_progressive_1979:
    $ nudge_1979 = "progressive"
    $ policy_score += 2
    $ geri_frank_connection = True
    "She gives Frank all of it — the analysis, the inspection records, and a written statement explaining why she made no formal report eighteen months ago."
    thought "Full exposure. If the dismissal of my work is part of why three men died, then the dismissal belongs in the record next to the deaths."
    thought "I am implicating the institutions that ignored me. I am also implicating myself for letting being ignored become a reason to stop. Both belong in the file."
    jump geri_1979_nudge_after


label geri_1979_nudge_after:
    scene bg_geri_office_1979 with dissolve
    "Evening. The department empties. The factory across the tracks is dark in a way it has never been dark before."
    jump geri_1979_period_end


label geri_1979_period_end:
    scene bg_geri_office_1979 with dissolve
    "Evening. The ledgers. The resented cigarettes. The south window onto the cold smokestacks."

    thought "I calculated firing solutions in a war nobody asks me about. I calculated this accident eighteen months before it happened in a town that wasn't listening."
    thought "Being right early and unheard is its own discipline. I have gotten very good at it. I would trade every bit of that skill for one report somebody read in time."

    "She picks up her pen. Goes back to work. There is always more work."

    scene black with dissolve
    pause 0.5
    "1979."

    if nudge_1979 == "conservative":
        "Dr. Habicht gave Frank the public injury data and kept her analysis."
        "The investigation proceeded on what anyone could have found. Her foresight stayed in the drawer where it had been since before the men died."
        pause 1.0
        "She was right about the probability and right about the dismissal. She added the accident to her dataset and said nothing."
    elif nudge_1979 == "middle":
        "Dr. Habicht gave Frank the analysis privately and trusted him to place it."
        "He found a way to make eighteen months of foresight legally relevant without putting her on trial for having had it."
        pause 1.0
        "It was the beginning of a working trust between a statistician and a detective that would matter again, later, about a casino."
    elif nudge_1979 == "progressive":
        "Dr. Habicht gave Frank everything, including the indictment of her own silence."
        "The record showed not just that the accident was foreseeable, but that someone had foreseen it and been ignored."
        pause 1.0
        "It changed how the county treated unsolicited analysis. Slowly. After. The way change always seems to arrive for her."

    pause 1.5
    "The numbers said what they said. She had said it first, and alone, and too quietly to matter. This time she had not been quiet."
    pause 2.0

    jump advance_to_1991
