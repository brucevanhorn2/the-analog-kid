## The Analog Kid — Period 1955
## Dr. Geraldine "Geri" Habicht playable thread.
## Copyright (C) 2025 Blue Moon Foundry Software. Licensed under AGPL-3.0.

# ---------------------------------------------------------------------------
# GERI 1955 — MAIN THREAD
# ---------------------------------------------------------------------------

label geri_1955_begin:

    $ current_period = 1955
    $ mark_visited("geri_office")

    scene bg_geri_office_1955 with fade
    # play music "audio/music/1955_morning_quiet.ogg" fadein 2.0

    thought "Before seven. The department won't be in for another hour."
    thought "I prefer it this way."

    "The office faces south. On a clear morning, through the window, you can see the tracks."
    "Three file cabinets. A drafting table covered in ledger paper."
    "Columns of numbers in her own hand, going back to 1915."
    "A pack of Lucky Strikes at her right elbow. An ashtray that wants emptying."

    thought "Forty-two years of census cross-reference."
    thought "Property assessments. Mortality tables. Income quartiles."
    thought "All of it mapped. All of it split along a line you can draw with a ruler."

    "She taps a Lucky Strike loose and lights it. The first of the day. It will not be the last."

    "She is working through the 1950 census supplemental — the one nobody uses because the columns are difficult."
    "She has been working through it since January."

    "And then."

    thought "Wait."

    "She goes back. Re-reads the column header. Checks the year."
    "Checks it again."

    thought "That isn't right."
    thought "Or rather — it is right. That's the problem."
    thought "The model predicts a gradient. This is a step function."
    thought "Between 1947 and 1948 the south-side infant mortality rate drops by fourteen percent."
    thought "In one year. Not gradually. One year."
    thought "Nothing in the data explains it. Not income. Not the factory hire cycle. Not weather."
    thought "Something happened in 1947 that I haven't accounted for."

    "The cigarette burns down untouched in the ashtray. She does not reach for it."
    "When the numbers move, the hand forgets the habit."

    "She takes a blank index card from the desk drawer."
    "She writes the number in the center of the card in her clearest hand."
    "Then the year. Then a question mark."
    "She sets it on top of the stack."

    thought "I will find what it is."
    thought "I always find what it is."

    "On the corner of the desk: a sealed envelope."
    "Hand-delivered, the departmental secretary said. Not through the Dean's office."
    "The return name: Harold Blanton, Sr."

    "She has not opened it."

    thought "I know what it says."
    thought "I have known since Tuesday when Marion at the front desk gave me that particular look."
    thought "The one that means: something is happening and I am sorry you are the one it is happening to."

    "She picks up her pen. Goes back to the column."
    "The envelope can wait."

    jump geri_1955_explore


# ---------------------------------------------------------------------------
# GERI 1955 — EXPLORE
# ---------------------------------------------------------------------------

label geri_1955_explore:

    $ mark_visited("geri_office")
    call show_nav_bar
    scene bg_geri_office_1955 with dissolve

    "The index card is on top of the stack."
    "The envelope is still sealed."

    if not talked("agnes", "library", "field_notes"):
        thought "Agnes will be in by now. I should go to the library."
    elif not keepsake_index_card:
        thought "The index card. I keep looking at it."

    $ current_location = "geri_office"
    jump explore_1955


# ---------------------------------------------------------------------------
# LOCATION: GERI'S OFFICE AT MCC (1955)
# ---------------------------------------------------------------------------

label location_geri_office_1955:

    $ mark_visited("geri_office")
    call show_nav_bar
    scene bg_geri_office_1955 with dissolve

    "The south-facing window. The tracks in the middle distance."
    "On a clear day she can see the Blanton factory smokestack on the south side."
    "It is a clear day."

    if talked("agnes", "library", "field_notes") and not talked("geri", "geri_office", "envelope"):
        $ mark_talked("geri", "geri_office", "envelope")
        "She picks up the envelope."
        "Opens it with a letter knife. Does not rush."

        "The handwriting is careful. The kind of careful that means someone drafted it twice."

        harold "Dear Dr. Habicht. I have long admired the work you do at this institution."
        harold "I would welcome the opportunity to discuss a matter of some mutual interest."
        harold "Specifically, a proposed endowment for the Nursing Education program."
        harold "I believe your name attached to such a program would be a meaningful legacy."
        harold "I will be at the Faculty Club Thursday at three o'clock and would be grateful for thirty minutes of your time."

        thought "Mutual interest."
        thought "He means his interest."
        thought "The nursing program."
        thought "It has been the Dean's suggestion for two semesters. Now Harold Blanton is involved."
        thought "Which means someone told Harold something."
        thought "Or Harold already knew something and decided it was time to act on it."

        "She sets the letter on her desk."
        "She does not throw it away."

        thought "A man like Harold Blanton doesn't write letters he expects to be ignored."
        thought "He writes letters that establish a record of having been civil."

    elif talked("geri", "geri_office", "envelope"):
        "The letter sits open on her desk."
        "Thursday. Three o'clock. Faculty Club."
        thought "I have not responded."

    if not keepsake_index_card:
        "The index card is still on top of the stack."
        menu:
            "Leave the card on the desk.":
                thought "It will still be here in the morning."
                thought "The number will still be true in the morning."
            "Put it in your pocket.":
                $ keepsake_index_card = True
                thought "The card is small. It fits in the inside pocket of my jacket."
                thought "I have carried equations in this pocket before."
                thought "Under a clearance that no longer exists, on a ship that no longer puts out to sea."
                thought "The number on this card is smaller than those equations."
                thought "It is not less important."

    return


# ---------------------------------------------------------------------------
# LOCATION: COLLEGE LIBRARY (1955)
# ---------------------------------------------------------------------------

label location_library_1955:

    $ mark_visited("library")
    call show_nav_bar
    scene bg_library_1955 with dissolve

    "The MCC library. Agnes Pruitt has been its head librarian since 1938."
    "She keeps records the way other people keep secrets — carefully, and for good reason."
    "You do not smoke in Agnes Pruitt's library. You never have. It was never discussed."

    if talked("agnes", "library", "field_notes"):
        "Agnes is at her cataloguing station. She looks up when Geri enters."
        agnes "Back again."
        geri "I needed the quiet."
        agnes "You have an office."
        geri "You have better filing."
        "Agnes almost smiles. She goes back to the catalogue cards."
        return

    "Agnes looks up when Geri comes through the door."
    "She does not say anything. She waits."

    thought "That is why I trust her."
    thought "She always waits to hear what you actually need."

    geri "Agnes. I want to know where my field notes from the Kessler survey are catalogued."

    "Agnes sets down the card she is holding."

    agnes "Sociology supplementals. Miscellaneous regional studies."
    agnes "Cross-referenced under population health, unclassified."
    agnes "The shelf label says Middletown Area Survey Documentation, 1913–."

    "A pause."

    geri "Who else would know to look there?"

    agnes "Nobody who was looking for sociology research."
    agnes "Someone looking for it specifically would need to know how I file unclassified materials."
    agnes "And then they would need to ask me."

    thought "She moved them."
    thought "She moved them without being asked."
    thought "She didn't tell me she was going to do it because she didn't want me to feel obligated."

    geri "How long have they been there?"

    agnes "Since March."
    "She picks up the catalogue card again."
    agnes "I noticed the advisory committee meeting in February."
    agnes "Board liaison attendance includes Harold Blanton Sr."
    agnes "I notice things."

    geri "Agnes—"

    agnes "You don't need to say anything, Geraldine."

    $ mark_talked("agnes", "library", "field_notes")

    "Geri stands at the catalogue counter for a moment."

    thought "Forty years of data. Forty years."
    thought "Archived under a miscellaneous heading in a college library by a woman who noticed before I did that I needed protecting."
    thought "And all I gave her was the research itself."
    thought "She gave me time."

    agnes "The letter."
    "She says it without looking up."
    agnes "You'll have to decide."

    geri "I know."

    agnes "Whatever you decide, the notes will stay where they are."
    agnes "They are properly catalogued. Nobody can say otherwise."

    "Geri nods. She turns to go."

    agnes "Geraldine."
    "Geri stops."
    agnes "You did good work on the WAVES."
    "A pause."
    agnes "I know because my brother was on the {i}Hamul{/i} and he came home."

    "She says it to the catalogue cards."
    "Geri leaves without answering."

    thought "I calculated firing solutions for three years."
    thought "Under a secret clearance. In a room with no windows."
    thought "The Navy thanked me for my service and sent me home."
    thought "I came home and applied for the statistics department."
    thought "The Dean said the position had been filled."
    thought "It hadn't."

    return


# ---------------------------------------------------------------------------
# NUDGE: HAROLD'S MEETING REQUEST
# ---------------------------------------------------------------------------

label geri_1955_nudge:

    scene bg_geri_office_1955 with dissolve

    "Thursday morning. The meeting is this afternoon."
    "The index card is still on her desk, or in her pocket."
    "The field notes are in Agnes's archive, properly filed under a heading nobody searches."

    thought "Three options. I have been running the numbers since Monday."
    thought "Not because I don't know the math. Because I need to be certain I know the cost."

    thought "Option one: go to the meeting. Be gracious. Decline to commit."
    thought "Harold gets a cooperative conversation. The Dean gets a cooperative Geraldine."
    thought "I buy time. I move the data into a format that is less readable."
    thought "I keep my position. I keep my salary. I keep teaching."
    thought "The research exists. Nobody knows how to find it."
    thought "Cost: the research sits. I know what the data says. Nobody else does."

    thought "Option two: don't go to the meeting. Write a letter."
    thought "Decline the nursing chair formally. Propose something they can't easily refuse."
    thought "A joint program — statistics and sociology. Copy the Dean and the county board."
    thought "Harold can't move against that without making the research more visible, not less."
    thought "Cost: I become a problem they have to manage. Problems get managed."

    thought "Option three: don't wait."
    thought "The state statistics office accepts public health submissions."
    thought "That bypasses the MCC publication approval process entirely."
    thought "The data is in the public record before Harold can write a second letter."
    thought "Cost: I know exactly what that costs."

    "She stands at the south-facing window."
    "The smokestack is still there."

    menu geri_1955_nudge_choice:

        "Accept the meeting. Be gracious. Buy time.":
            jump geri_nudge_conservative_1955

        "Decline the chair. Write a letter. Copy everyone.":
            jump geri_nudge_middle_1955

        "Submit the data to the state statistics office. Now.":
            jump geri_nudge_progressive_1955


label geri_nudge_conservative_1955:

    $ nudge_1955 = "conservative"
    $ policy_score -= 1

    "Three o'clock. The Faculty Club."
    "Harold Blanton Sr. stands when she enters. He is well-dressed and he means it as a courtesy."
    "She accepts the courtesy. She sits across from him at the small table by the window."

    harold "Dr. Habicht. Thank you for coming."

    geri "Mr. Blanton. You were kind to invite me."

    "The pleasantries take four minutes. Harold is good at pleasantries."
    "He is also watching her the way men watch women they are not certain they understand."

    harold "The nursing program has needed leadership for some time. The Dean agrees."
    harold "I've spoken with the board about an endowed chair. Your name would carry real weight."

    geri "That's very generous."

    harold "The work you've done at this institution — the statistical methods, the community surveys —"
    harold "Frankly, Dr. Habicht, that kind of rigor applied to nursing education would be transformative."

    thought "He means it."
    thought "That is the worst part. He genuinely believes this is a gift."
    thought "He cannot see the shape of what he is asking."
    thought "Or he can, and he has decided not to look at it."

    geri "I'd want to think about it carefully. Something like this deserves serious consideration."

    harold "Of course. No rush."

    "He smiles. He is relieved."
    "He thinks this conversation went well."

    thought "It did go well. For him."
    thought "For me it went well in the sense that I am still employed."

    "She shakes his hand. She walks back to her office."

    "That evening, she opens the ledger sheets for the 1950 cross-reference."
    "She rearranges the column headers."
    "The data is still there. It is just harder to read if you don't already know what you're looking for."

    thought "I am not destroying it."
    thought "I am putting it somewhere safer."
    thought "That is what I am telling myself."
    thought "I am also telling myself that surviving is not the same as surrendering."
    thought "I am not certain those two things are as different as I need them to be."

    jump geri_1955_nudge_after


label geri_nudge_middle_1955:

    $ nudge_1955 = "middle"
    $ geri_samuel_connection = True

    "She does not go to the Faculty Club."
    "She goes to the library first."

    scene bg_library_1955 with dissolve

    "Agnes is at her station."

    geri "I'm writing a letter declining the chair."
    geri "I'm going to propose a joint research program. Statistics and sociology."
    geri "I'm copying the Dean, the county academic board, and the state college association."

    "Agnes sets down her pen."

    agnes "That will make it very difficult for anyone to act quietly."

    geri "That's the idea."

    "Agnes looks at her for a long moment."

    agnes "I'll have the field notes under a second cross-reference by tomorrow."
    agnes "Population health correlates. Properly documented."
    agnes "If anyone pulls the file, they'll find forty years of clean methodology."

    geri "Agnes. You don't have to—"

    agnes "I know I don't have to."
    "She picks up her pen."
    agnes "Write your letter."

    scene bg_geri_office_1955 with dissolve

    "Geri writes the letter that evening."
    "It is four paragraphs. Every sentence is precise."
    "She declines the nursing chair. She proposes the joint program."
    "She explains the value of combining census-level demographic data with sociological field methods."
    "She does not mention Harold Blanton."
    "She does not need to."

    thought "If this is read carefully by someone on the county board, they will see the data I'm describing."
    thought "They will understand what it implies."
    thought "Harold will understand what it implies."
    thought "He cannot suppress the proposal without making the research more visible."
    thought "He cannot ignore the proposal without making the Dean look unresponsive."
    thought "I have not been aggressive. I have been thorough."
    thought "There is a kind of armor in thoroughness."

    thought "Dr. Beaumont is on the south side."
    thought "His patient records are coming from the same population my census data describes."
    thought "We are looking at the same thing from different angles."
    thought "We haven't spoken."
    thought "We should speak."

    jump geri_1955_nudge_after


label geri_nudge_progressive_1955:

    $ nudge_1955 = "progressive"
    $ policy_score += 2
    $ geri_samuel_connection = True

    scene bg_geri_office_1955 with dissolve

    "She pulls the research."
    "Not the column rearrangements, not the coded ledgers — the clean version."
    "The one she has been keeping since 1948 in case this day came."

    thought "A public health report is not an academic paper."
    thought "The MCC publication approval process applies to academic papers."
    thought "It does not apply to public health submissions."
    thought "I checked. I checked twice. I had Agnes check."

    "She types the cover letter on her office typewriter."
    "A Lucky Strike burns in the ashtray beside the carriage. She types around it."
    "State Statistics Office. Public Health Data Submission."
    "Forty years of Middletown census correlation, income, mortality, infrastructure — split by geography."
    "She does not soften it."

    thought "The data says what it says."
    thought "I am a statistician."
    thought "My job is to tell the truth about numbers."

    "She mails it Wednesday morning."
    "She does not go to Harold's Thursday meeting."
    "She sends a brief note: {i}Prior commitment. Thank you for the kind invitation.{/i}"

    "The following Monday, the Dean's secretary calls."
    "There is a summons to the Dean's office."
    "The meeting is next week."

    thought "That's nine days."
    thought "Nine days for the state office to log the submission."
    thought "I calculated the timing."
    thought "Of course I calculated the timing."

    thought "Harold Blanton's factory employs south-side workers at two wage classifications below comparable north-side work."
    thought "The data shows it."
    thought "The mortality correlation shows it."
    thought "The property assessment data shows it."
    thought "He has known what my research implies for longer than I have been employed here."
    thought "He was hoping I would be easier to manage than I am."

    thought "He miscalculated."

    jump geri_1955_nudge_after


# ---------------------------------------------------------------------------
# POST-NUDGE BEAT
# ---------------------------------------------------------------------------

label geri_1955_nudge_after:

    scene bg_geri_office_1955 with dissolve

    "Evening. The department has emptied out."
    "The south-facing window is dark, but she can still make out the factory lights across the tracks."

    jump geri_1955_period_end


# ---------------------------------------------------------------------------
# PERIOD END — GERI 1955
# ---------------------------------------------------------------------------

label geri_1955_period_end:

    scene bg_geri_office_1955 with dissolve
    # stop music fadeout 2.0
    # play music "audio/music/1955_evening.ogg" fadein 2.0

    "Evening. The office is quiet."
    "The column ledgers are stacked on the drafting table."
    "Forty years of numbers, compiled on evenings and weekends and summers."

    "She is at her desk."
    "Not working. Just sitting."
    "The way you sit when the day's work is done and you need a moment before you go home."

    "She lights the day's last Lucky Strike."

    thought "I have spent four years mapping how this town dies."
    thought "Income. Address. The water main that stops at the tracks."
    thought "There is no column in my data for this one."

    "She turns the cigarette a quarter-turn between two fingers, the way you examine a specimen."

    thought "The studies exist. I've read them. The samples are small and the methods are thin."
    thought "When the evidence is conclusive, I will account for it. I account for everything."
    thought "It is not conclusive yet."
    thought "It is 1955. I have time."

    thought "Forty-three years old."
    thought "I have been teaching sociology at this institution for four years."
    thought "I applied for the statistics department."
    thought "The Dean said the position had been filled."
    thought "It hadn't."

    thought "I calculated firing solutions for the Navy."
    thought "Torpedoes move through water. The variables are velocity, bearing, current, depth."
    thought "You account for all of them. You run the numbers. You give the solution."
    thought "You don't get to choose whether the numbers are convenient."
    thought "I learned that in the first week."

    thought "The same principle applies to census data."
    thought "The numbers say what they say."
    thought "My job is to say it clearly."

    "On her desk, or in her pocket — the index card."
    "The number in the center."
    "The year. The question mark."

    if not keepsake_index_card:
        menu:
            "Leave the card on the desk.":
                thought "It will still be here in the morning."
                thought "The number will still be true in the morning."
            "Put it in your pocket.":
                $ keepsake_index_card = True
                thought "The card is small. It fits in the inside pocket of my jacket."
                thought "I have carried equations in this pocket before."
                thought "Under a clearance that no longer exists, on a ship that no longer puts out to sea."
                thought "The number on this card is smaller than those equations."
                thought "It is not less important."

    if keepsake_index_card:
        thought "Fourteen percent."
        thought "In one year."
        thought "I will find what it is."
    else:
        thought "It will still be there in the morning."

    "She turns off the desk lamp."
    "She stands for a moment in the dark with the south-facing window."
    "The tracks are invisible in the dark. But she knows exactly where they are."

    thought "The line runs east to west."
    thought "I could draw it from memory."
    thought "I have drawn it from memory."
    thought "Forty-two years of data, split along a line you can draw with a ruler."
    thought "And one number that doesn't fit the model."
    thought "One number that means something is there that I haven't found yet."

    thought "Good."

    ## Period summary
    scene black with dissolve
    pause 0.5

    "1955."

    if nudge_1955 == "conservative":
        "Geraldine Habicht attended a meeting at the Faculty Club."
        "She was gracious."
        "She did not commit to anything."
        pause 1.0
        "The research was rearranged into a format that was less legible."
        "It was not destroyed."
        "She kept teaching."
        "The Dean was satisfied."
        "Harold Blanton was satisfied."
        pause 1.0
        "The data knew what it knew."

    elif nudge_1955 == "middle":
        "Geraldine Habicht wrote a letter declining the nursing chair."
        "She proposed a joint statistics and sociology research program."
        "She copied the Dean, the county board, and the state college association."
        pause 1.0
        "Harold Blanton did not respond."
        "The Dean scheduled a meeting."
        "The meeting was inconclusive."
        pause 1.0
        "The field notes stayed in Agnes's archive, properly catalogued."
        "The proposal stayed in the record."
        "Nobody could act quietly anymore."

    elif nudge_1955 == "progressive":
        "The state statistics office received a public health data submission on November 14, 1955."
        "Forty years of Middletown census correlation."
        "Income, mortality, infrastructure — split by geography."
        pause 1.0
        "The Dean summoned her."
        "She went."
        "By then the submission was logged."
        pause 1.0
        "Harold Blanton Sr. did not write a third letter."
        "He made a phone call instead."
        "She had anticipated that too."

    pause 1.5
    "The number was fourteen percent."
    "She would find what it meant."
    pause 2.0

    jump advance_to_1967
