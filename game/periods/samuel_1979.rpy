## The Analog Kid — Period 1979
## Dr. Samuel Beaumont — "The Man The Hospital Still Won't Fully Open."
## The Blanton accident; the autopsies; the Runningwater respiratory file.

label samuel_1979_begin:

    $ current_period = 1979
    $ current_location = "hospital_north"
    $ mark_visited("hospital_north")

    scene bg_hospital_north_1979 with fade

    thought "Sixty years old. Full privileges now — for everything except the surgical suite and a department chair."
    thought "The language changed. The ceiling did not."

    "The Blanton factory accident. Three workers dead. Two of them his patients. The smokestacks have gone cold for the first time in thirty years."
    "Samuel performs the autopsies himself. The cause of death is not complicated. The manner — what led to the cause — is documented in his reports with the precision he brings to everything."

    "When he finishes, he sits for a moment before cleaning up. Just a moment."

    samuel "This is the day."

    $ samuel_leitmotif_count += 1

    thought "I say it over two men I could not save. Almost inaudible. The day the Lord has made, and these men did not live to the end of it."

    jump samuel_1979_runningwater


label samuel_1979_runningwater:

    "One of the dead was George Runningwater. Tribal member. Samuel had been treating him for a respiratory condition he believed was occupational in origin."
    "He documented it. He filed a report with the county health department eight months ago."
    "The report is in a drawer somewhere. It was filed and ignored, which is a different thing than lost."

    thought "This is not a rumor and it is not a hunch. It is medical documentation, in official channels, dated, signed."
    thought "I have been waiting for someone to ask me the right question. Frank DeLuca is the kind of man who asks the right question."

    $ mark_talked("samuel", "hospital_north", "autopsy")

    jump samuel_1979_explore


label samuel_1979_explore:
    $ current_location = "hospital_north"
    jump explore_1955


# --- 1979 LOCATIONS ---

label location_hospital_north_1979:
    $ mark_visited("hospital_north")
    scene bg_hospital_north_1979 with dissolve
    "The north-side hospital. The morgue is in the basement. Samuel knows the way without being shown anymore, which is its own kind of bitter progress."
    thought "Two of my patients are downstairs. I read their lungs like a sentence I had already written eight months ago and filed with the county."
    return

label location_ihs_clinic_1979_samuel:
    $ mark_visited("ihs_clinic")
    scene bg_ihs_clinic_1979 with dissolve
    "The IHS clinic. George Runningwater's widow is here. Not sick. Just somewhere to sit. She has his toolbox with her and doesn't seem to know why she brought it."
    if not talked("samuel", "ihs_clinic", "widow_1979"):
        $ mark_talked("samuel", "ihs_clinic", "widow_1979")
        "Samuel checks her blood pressure. Gives her something for the headaches. They do not talk about the accident."
        thought "She thanks me. I treated her husband's lungs for a year and could not treat the building he breathed them out in."
    return

label location_frank_office_1979_samuel:
    $ mark_visited("frank_office")
    scene bg_frank_office_1979 with dissolve
    "Frank DeLuca's office. Frank is sixty-four and investigating the accident with the particular methodical patience of a man who already knows it will cost him."
    if not talked("samuel", "frank_office", "frank_1979"):
        $ mark_talked("samuel", "frank_office", "frank_1979")
        frank "Doctor. You did the autopsies."
        samuel "I did. I also treated one of them for eight months before he became one of them."
        frank "Occupational?"
        samuel "I filed it with the county in the spring. You can guess what came back."
        frank "Nothing came back."
        samuel "Nothing came back."
        thought "He asked the right question. Now the only question left is mine — what I hand him, and through which door."
    return


# --- NUDGE ---

label samuel_1979_nudge:

    scene bg_hospital_north_1979 with dissolve

    "Evening. The respiratory file is on the desk beside the autopsy reports. Eight months old. Dated. Ignored. Now suddenly relevant."

    thought "Three ways this documentation enters the world. Each one is a different amount of myself."

    menu samuel_1979_nudge_choice:

        "Let it enter through Frank's investigation. Testify if called. Stay a physician.":
            jump samuel_nudge_conservative_1979

        "Submit it to the state medical board as a professional-standards matter.":
            jump samuel_nudge_middle_1979

        "Present the findings publicly — a medical conference, the press, whoever listens.":
            jump samuel_nudge_progressive_1979


label samuel_nudge_conservative_1979:
    $ nudge_1979 = "conservative"
    $ policy_score -= 1
    $ runningwater_complaint = "frank_background"
    "Samuel gives Frank the respiratory documentation. Voluntarily, before Frank asks. He has been waiting for someone to ask."
    samuel "It's a medical record. What it is, it is."
    thought "I stay in my lane. The lane is real and it is also a fence I built to keep my license safe."
    thought "Three men are dead. I documented the why of one of them eight months early. Staying careful did not save him. I am staying careful anyway."
    jump samuel_1979_nudge_after


label samuel_nudge_middle_1979:
    $ nudge_1979 = "middle"
    $ runningwater_complaint = "surfaced"
    "Samuel submits the documentation to the state medical board as a matter of professional standards — a separate track from Frank's criminal investigation."
    thought "Harder to bury. Slower to resolve. More durable than either a courtroom or a headline."
    thought "A criminal case can be lost. A medical-board finding becomes part of the record of what is and is not acceptable to do to a man's lungs for a paycheck."
    thought "I am 60. I have learned that the slow durable thing usually outlasts the fast loud one. Usually."
    jump samuel_1979_nudge_after


label samuel_nudge_progressive_1979:
    $ nudge_1979 = "progressive"
    $ policy_score += 2
    $ runningwater_complaint = "surfaced"
    "Samuel presents the findings publicly. A regional medical meeting. A reporter in the room. His name, his title, his eight-month-old county filing that nobody acted on."
    thought "My documentation becomes the moral center of the accountability argument, which is a heavy thing to ask a dead man's lungs to be."
    thought "The hospital will not enjoy this. The provisional ceiling they keep over me suddenly has my fingerprints on it, pushing up."
    thought "I trained where a physician did not have to ask permission to tell the truth. I am remembering that out loud."
    jump samuel_1979_nudge_after


label samuel_1979_nudge_after:
    scene bg_hospital_north_1979 with dissolve
    "Late. Samuel puts the pocket Bible in his coat. It fits where it has always fit."
    jump samuel_1979_period_end


label samuel_1979_period_end:
    scene bg_hospital_north_1979 with dissolve
    "Evening. The hospital quiets the way hospitals quiet — never fully."

    thought "Sixty years old. I have outlived two wars' worth of the men who told me I didn't belong here, and I am still on the wrong side of one locked surgical door."
    thought "George Runningwater is downstairs. I read his lungs eight months ago. The reading did not change. Only the number of people willing to look at it did."

    samuel "This is the day."

    scene black with dissolve
    pause 0.5
    "1979."

    if nudge_1979 == "conservative":
        "Dr. Beaumont's documentation entered the investigation through Frank DeLuca."
        "He testified at the inquest, answered exactly what he was asked, and went home."
        pause 1.0
        "The county that ignored his spring filing did not apologize for ignoring it. He had not expected them to."
    elif nudge_1979 == "middle":
        "Dr. Beaumont took the respiratory documentation to the state medical board."
        "It moved slowly. It did not get buried. Two years on, it was still on the record, still cited."
        pause 1.0
        "Occupational safety language in three county facilities changed because of a file a south-side doctor refused to let disappear."
    elif nudge_1979 == "progressive":
        "Dr. Beaumont presented his findings publicly, under his name and his title."
        "The story had a spine it would not otherwise have had."
        pause 1.0
        "The hospital reviewed his standing that winter. It survived the review. The word provisional survived it too."

    pause 1.5
    "This is the day."
    pause 2.0

    jump advance_to_1991
