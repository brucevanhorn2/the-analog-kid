## The Analog Kid — Period 1955
## June Holloway playable thread.
## Copyright (C) 2025 Blue Moon Foundry Software. Licensed under AGPL-3.0.

# ---------------------------------------------------------------------------
# JUNE 1955 — MAIN THREAD
# ---------------------------------------------------------------------------

label june_1955_begin:

    $ current_period = 1955
    $ mark_visited("city_hall")

    scene bg_city_hall_1955 with fade
    # play music "audio/music/1955_morning_quiet.ogg" fadein 2.0

    "The council chambers. High windows that don't open easily."
    "The official seal on the wall is older than the building."
    "Seven chairs at the long table. Her chair is third from the left."
    "There are only four aldermen and a mayor. She has never asked why seven chairs."

    "The letter is on the table in front of her."
    "It arrived ten days ago. She has read it seven times."

    thought "Ada Whitehorse. South side. Her handwriting is careful — the kind of careful that knows someone might dismiss it."
    thought "A broken arm. Two weeks. Three trips to the north side hospital."
    thought "A boy named Thomas. Ten years old."

    "The letter does not use the word {i}injustice.{/i}"
    "It does not use the word {i}discrimination.{/i}"
    "It simply describes what happened, in order, with dates."
    "That is why she has read it seven times."

    thought "Anyone can dismiss an accusation."
    thought "Dates are harder to dismiss."

    "Alderman Pruett left his copy on the table when he walked out."
    "She knows because she found it there, unfolded, face up."
    "He hadn't written on it."

    thought "He didn't even get to the second paragraph."

    jump june_1955_explore


# ---------------------------------------------------------------------------
# JUNE 1955 — EXPLORE
# ---------------------------------------------------------------------------

label june_1955_explore:

    $ mark_visited("city_hall")
    $ current_location = "city_hall"
    call show_nav_bar

    scene bg_city_hall_1955 with dissolve

    "The letter is still on the table."
    "She has a motion to second on Thursday. Something about road assessments."

    if not talked("june", "city_hall", "aldermen"):
        thought "Pruett and Gifford will be in by nine."
        thought "I should know what I'm going to say before they are."

    jump explore_1955


# ---------------------------------------------------------------------------
# LOCATION: CITY HALL / COUNCIL CHAMBERS (1955)
# ---------------------------------------------------------------------------

label location_city_hall_1955:

    $ mark_visited("city_hall")
    $ current_location = "city_hall"
    call show_nav_bar

    scene bg_city_hall_1955 with dissolve

    if not talked("june", "city_hall", "aldermen"):
        jump june_city_hall_aldermen

    "The council chambers."
    "The letter is where she left it."

    if talked("june", "city_hall", "mayor") and not talked("june", "city_hall", "after_mayor"):
        $ mark_talked("june", "city_hall", "after_mayor")
        thought "Mayor Holt's door is closed."
        thought "It has been closed since Tuesday."

    return


label june_city_hall_aldermen:

    $ mark_talked("june", "city_hall", "aldermen")

    "Pruett comes in at nine-fifteen. Gifford is already there."
    "They are talking about the Blanton factory hiring cycle."
    "They stop when June comes through the door."
    "Not because they don't want her to hear. Because that is what they do."

    townsperson "June."

    june "Morning."

    "She sets her folder on the table. The letter is inside it."

    townsperson "You see the road assessment motion Clifford sent over?"

    june "I saw it."

    townsperson "Straightforward. We should be able to get through Thursday in an hour."

    thought "He means: nothing difficult on Thursday."
    thought "He means: let's have a short week."

    "Gifford is looking at the window."

    townsperson "That letter's still going around, is it?"

    june "It's in my folder."

    townsperson "County health matter, June. Not ours."

    june "It came to the council."

    townsperson "People send things to the council that aren't council matters."
    "He says it without turning from the window."
    townsperson "If they want north side hospital access they should live on the north side."

    "The room is very quiet for a moment."

    thought "He means it exactly the way it sounds."
    thought "That is the most honest thing Alderman Gifford has said in three months."
    thought "Honesty can be its own kind of closed door."

    june "I'll see you Thursday."

    "She takes her folder and goes down the hall."

    jump june_city_hall_mayor


label june_city_hall_mayor:

    $ mark_talked("june", "city_hall", "mayor")

    "Mayor Holt is in his office with the door half open."
    "He is reading something when she knocks. He sets it down."

    townsperson "June. Come in."

    "He does not offer her the chair across the desk."
    "She sits in it anyway."

    june "I want to put the Whitehorse letter on the Thursday agenda."

    "A pause. Long enough to be deliberate."

    townsperson "What would that accomplish?"

    june "It would put it on the record."

    townsperson "It's already on the record. You received it. You logged it."

    june "Receiving a letter and reading it aloud in chambers are different things."

    "Mayor Holt leans back. He has been mayor for eleven years."
    "He is not a mean man. He is a careful man."
    "June has learned that carefulness can accomplish what meanness cannot."

    townsperson "June. I'd be careful about which hills you choose to die on."
    townsperson "You're in your first term. You have things you want to do."

    june "Yes."

    townsperson "This particular fight — and that's what it would be, a fight — doesn't help you do those things."
    townsperson "The hospital is a county institution. The county board has its process."

    june "The county board received Dr. Runningwater's report in March."
    june "Nothing came back."

    "Holt is quiet."

    thought "He knows that."
    thought "He knew it before I said it."
    thought "He is not the kind of man who doesn't know things."

    townsperson "You ran on progress."
    "He says it gently."
    townsperson "There are different kinds of progress. Some kinds are faster when they move quietly."

    june "I'll think about it."

    townsperson "That's all I'm asking."

    "She stands. She picks up her folder."
    "At the door she stops."

    june "Did you read the whole letter? The dates."

    "Holt looks at her."

    townsperson "I did."

    "A beat."

    townsperson "I have a daughter. She's eight."
    "He says it to the desk."
    townsperson "I read the whole letter."

    "She goes back to the chambers."
    "She sits with her folder open."
    "The letter is on top."

    thought "He read it. He has a daughter."
    thought "And he is still asking me to move quietly."
    thought "I don't know what that means about him."
    thought "I know what it means about the situation."

    return


# ---------------------------------------------------------------------------
# LOCATION: HOLLOWAY DERRICK (1955)
# ---------------------------------------------------------------------------

label location_holloway_derrick_1955:

    $ mark_visited("holloway_derrick")
    $ current_location = "holloway_derrick"
    call show_nav_bar

    scene bg_holloway_derrick_1955 with dissolve

    if not talked("june", "holloway_derrick", "father"):
        jump june_derrick_scene

    "The pump jack moves in its long slow arc."
    "Her father is not at the site today."
    "The company shack is locked."

    thought "The oil has been steady this year."
    thought "He said so at dinner. He said it the way men say things they want you to register as given."

    return


label june_derrick_scene:

    $ mark_talked("june", "holloway_derrick", "father")

    "Her father is at the shack with a man from the equipment company."
    "The man from the equipment company leaves when he sees June coming."
    "Her father watches the pump jack."

    townsperson "Junie."

    june "Dad."

    "She stands next to him."
    "The pump jack moves in its long slow arc."
    "It has been moving this way since she was twelve years old."
    "She finds it calming in a way she has never admitted to anyone."

    townsperson "How's the council treating you?"

    june "Fine. Road assessments on Thursday."

    townsperson "Mm."

    "A long silence. The kind that means he has something he wants to say and is deciding how."

    townsperson "I heard something about a letter."

    june "From Ada Whitehorse."

    townsperson "South side woman."

    june "Her son broke his arm. The hospital found reasons not to treat him for two weeks."

    "Her father looks at the pump jack."

    townsperson "That's a county matter, June. The hospital is county-chartered."

    june "That's what everyone keeps telling me."

    townsperson "Because everyone is right."

    "She doesn't say anything."

    townsperson "The hospital can't be responsible for every charity case that comes through."
    townsperson "That's what the IHS clinic is for. They have their own infrastructure."

    thought "Charity case."
    thought "He said it the way you say something that has always been true — not cruelly, just factually."
    thought "The way you say: {i}the sky is blue.{/i}"
    thought "As if the category settles the question."

    june "He was ten years old."

    "Her father turns to look at her. Not defensively. Carefully."

    townsperson "I know."

    june "Two weeks."

    townsperson "June."
    "His voice is not unkind."
    townsperson "You ran a good campaign. You ran on progress. You have things you can actually move."
    townsperson "Roads. The school board budget. The county annexation question."
    townsperson "These are things you can do in a first term. Things that don't cost you your second."

    june "And if the letter is just — filed."

    townsperson "Then the letter is filed."
    "He says it simply."
    townsperson "I didn't build this"
    "He gestures at the derrick."
    townsperson "by fighting every battle that came through. I built it by choosing."

    "She watches the pump jack."

    thought "He means what he says."
    thought "He loves me."
    thought "He financed the campaign. He called in a favor with the county chair."
    thought "He considers this an investment in the way that men consider things investments."
    thought "He is not wrong that it cost him something."
    thought "He is not wrong that he expects something back."

    thought "I have been thinking about Thomas Whitehorse for three days."
    thought "My father has not."
    thought "That tells me something."
    thought "I'm still deciding what."

    june "I'll be at dinner Sunday."

    townsperson "Good."

    "He pats her arm once — the gesture he has used since she was six."
    "She walks back to her car."

    "The pump jack moves in its long slow arc behind her."
    "She does not look back."

    return


# ---------------------------------------------------------------------------
# LOCATION: IHS CLINIC (1955) — optional June visit for middle/progressive seeds
# ---------------------------------------------------------------------------

label location_ihs_clinic_1955_june:

    $ mark_visited("ihs_clinic")
    $ current_location = "ihs_clinic"
    call show_nav_bar

    scene bg_ihs_clinic_1955 with dissolve

    if june_south_side_trust >= 1:
        "The IHS clinic. Dr. Runningwater is at his desk."
        runningwater "Councilwoman."
        june "I just — I wanted to see it."
        "He nods. He does not ask her to explain."
        thought "He has been here for eight years."
        thought "He has seen the county board's response to every request they have sent."
        thought "He is not surprised that someone from the council came."
        thought "He may be slightly surprised it was me."
        return

    "The IHS clinic. A converted storefront on the south side."
    "A government poster on the wall. Metal chairs. A fluorescent tube."

    "Dr. Runningwater is at his desk. He looks up without surprise."

    runningwater "Councilwoman Holloway."

    june "Dr. Runningwater. I'm sorry to come without — I didn't call ahead."

    runningwater "That's fine."

    "A beat."

    june "I received a letter. From Ada Whitehorse."

    runningwater "I know Ada."

    june "Her son Thomas—"

    runningwater "I know Thomas."
    "He says it quietly."
    runningwater "He's doing better. Dr. Beaumont set the arm."

    thought "Dr. Beaumont. A name in the letter."
    thought "He treated Thomas when the hospital wouldn't."
    thought "He operates out of his own home."

    june "Can I ask — the county health request your office filed in March—"

    runningwater "Nothing came back."

    june "I know."

    "He studies her for a moment."

    runningwater "What are you going to do with the letter, Councilwoman?"

    "She doesn't answer right away."

    june "I'm still figuring that out."

    runningwater "That's honest."
    "He nods once."
    runningwater "If you decide to do something, we'll be here."
    "He picks up his case file."
    runningwater "We're always here."

    $ mark_talked("runningwater", "ihs_clinic", "june_visit")

    thought "He did not ask me to promise anything."
    thought "He has met politicians before."
    thought "He is waiting to see which kind I am."
    thought "I am also waiting to see which kind I am."

    return


# ---------------------------------------------------------------------------
# JUNE 1955 — THE NUDGE
# ---------------------------------------------------------------------------

label june_1955_nudge:

    scene bg_city_hall_1955 with dissolve

    "Thursday morning. Before the aldermen arrive."
    "The letter is on the table."
    "The road assessment motion is in her folder."

    thought "I ran on a word."
    thought "I said {i}progress{/i} in Rotary Club halls and at the Grange and at the VFW and at the county fairgrounds."
    thought "On the north side they heard: roads, schools, managed growth."
    thought "On the south side they heard: recognition, access, somebody listening."
    thought "I let both of them hear what they needed to hear."
    thought "I didn't think that was dishonest. I thought that was politics."

    thought "Ada Whitehorse didn't write to ask for politics."
    thought "She wrote down what happened to her son. With dates."
    thought "She sent it to the only institution that is supposed to represent her."
    thought "And I am that institution."

    thought "Three things I can do."
    thought "Each one is a version of me I have to choose."

    menu june_1955_nudge_choice:

        "Refer it properly. Write to the county health committee.":
            jump june_nudge_conservative_1955

        "Go to the south side. See it yourself.":
            jump june_nudge_middle_1955

        "Put it on the agenda. Read the letter aloud.":
            jump june_nudge_progressive_1955


label june_nudge_conservative_1955:

    $ nudge_1955 = "conservative"
    $ june_south_side_trust = 0
    $ policy_score -= 1

    "She opens her folder. She pulls out the council letterhead."

    thought "The county health committee has jurisdiction."
    thought "That is the correct answer."
    thought "The correct answer is also a way of making the letter someone else's problem."
    thought "I know that."
    thought "I'm choosing to let it be someone else's problem."

    "She writes the response. It is formal and correct."
    "She acknowledges the letter. She explains the jurisdictional process."
    "She copies it to the county health committee chair."
    "She does not go to the south side."

    "On Thursday the road assessment motion passes. She seconds it."
    "She goes home."

    "The letter is in the outgoing mail tray."

    thought "I chose the correct answer."
    thought "I am sitting with what that means."

    jump june_1955_nudge_after


label june_nudge_middle_1955:

    $ nudge_1955 = "middle"
    $ june_south_side_trust = 1

    "She does not call ahead."
    "She does not bring her folder."
    "She drives past the tracks on a Tuesday afternoon."

    scene bg_ihs_clinic_1955 with dissolve

    thought "I do not know this part of town well."
    thought "I should know it better."
    thought "That is the first honest thing I have thought about this in ten days."

    "She finds the IHS clinic. The sign is small."

    jump location_ihs_clinic_1955_june


label june_nudge_progressive_1955:

    $ nudge_1955 = "progressive"
    $ june_south_side_trust = 1
    $ policy_score += 2

    scene bg_city_hall_1955 with dissolve

    "She writes the letter to the county at home the night before."
    "She writes it at her kitchen table."
    "Then she sets it aside."
    "Then she writes something else."

    "On Thursday she arrives early."
    "She clips Ada Whitehorse's letter to the top of the agenda."

    "When the aldermen sit down she reads it aloud."

    thought "Not dramatically. Just out loud. The way you read something you want other people to actually hear."

    "Pruett stares at the table. Gifford stares at the window."
    "Mayor Holt is very still."

    "She reads the dates."
    "She reads the part about the admissions desk."
    "She reads: {i}Dr. Beaumont set Thomas's arm in his home on Maple Street. He has been there for four years. He is the only physician serving the south side community.{/i}"

    "She finishes."
    "The room is quiet."

    townsperson "June."
    "Pruett. Not unkind."
    townsperson "You know this is a county charter matter."

    june "I know."

    townsperson "There's nothing this council can formally—"

    june "I know."

    "A beat."

    june "But it's in the record now."
    june "And everyone in this room has heard it."

    "Gifford stands up and leaves."
    "Holt does not move."

    "The road assessment motion passes."
    "She goes home."

    "Her father calls at six-fifteen."

    jump june_father_call


label june_father_call:

    scene bg_holloway_derrick_1955 with dissolve

    "She answers on the second ring."

    townsperson "I heard what you did in chambers today."

    june "I read a letter."

    townsperson "You read it aloud. In the official record."

    june "Yes."

    "A long pause."

    townsperson "Do you understand what that does to the position I am in with Gifford?"
    townsperson "Gifford's brother-in-law is on the hospital board."

    june "I know."

    townsperson "June."
    "His voice is still not unkind. That is the thing about her father."
    "He is never unkind when he is most serious."
    townsperson "I put considerable money and considerable time into your campaign."
    townsperson "I did that because I believe in you. I need you to understand the shape of what I did."

    june "I understand the shape of it."

    townsperson "Do you?"

    "She does not say anything."

    thought "I do."
    thought "I have always understood the shape of it."
    thought "I just thought that when the moment came I would find a way to serve both debts at once."
    thought "Ada Whitehorse's letter clarified something."
    thought "There isn't always a way to serve both debts at once."

    townsperson "I'm not angry."
    "He says it."
    townsperson "I want you to know that."

    june "I know."

    townsperson "But we need to talk."

    june "Sunday dinner."

    townsperson "Yes."

    "She sets the phone down."

    thought "He loves me."
    thought "He financed me."
    thought "Both of those things are true."
    thought "A third thing is also true."
    thought "I read the letter aloud."
    thought "I am going to have to decide what kind of politician I am."
    thought "I am going to have to decide if those are different questions."

    jump june_1955_nudge_after


# ---------------------------------------------------------------------------
# POST-NUDGE
# ---------------------------------------------------------------------------

label june_1955_nudge_after:

    scene bg_city_hall_1955 with dissolve

    "Evening. The chambers are empty."
    "The official seal catches the last light through the high windows."

    jump june_1955_period_end


# ---------------------------------------------------------------------------
# PERIOD END — JUNE 1955
# ---------------------------------------------------------------------------

label june_1955_period_end:

    scene bg_city_hall_1955 with dissolve
    # stop music fadeout 2.0
    # play music "audio/music/1955_evening.ogg" fadein 2.0

    "Evening. The chambers have been empty for two hours."
    "She is still there."

    "Not working. There is nothing left to do today."
    "Just sitting at the long table in the chair that is third from the left."

    thought "Thirty-four years old."
    thought "First woman on this council."
    thought "They put that in the Middletown Courier. Above the fold."
    thought "My father kept the clipping."

    "She has Ada Whitehorse's letter out on the table again."
    "She has been reading it since six o'clock."

    "Not the dates this time."
    "The last paragraph."

    thought "{i}I am writing because I don't know who else to write to. I am not asking for anything extraordinary. I am asking for what was supposed to be already there.{/i}"

    "She reads it again."

    thought "What was supposed to be already there."
    thought "She wasn't making an accusation. She was naming an absence."
    thought "An absence is different. Harder to fight. Harder to defend against."
    thought "There is no one to hold responsible for a thing that was never built."

    thought "Progress."
    thought "I said it in every room."
    thought "I meant it every time."
    thought "I think I finally know what I meant."

    "She folds the letter."
    "She does not put it back in her folder."
    "She puts it in her coat pocket."

    thought "My fifth grade teacher was named Holloway. Different family, same name."
    thought "She taught us to read maps. Latitude, longitude. Where things actually are."
    thought "She said: {i}The map doesn't make the land. The map just tells the truth about it.{/i}"
    thought "I was nine years old."
    thought "I thought she was talking about geography."

    "She turns off the light in the council chambers."
    "She walks to her car in the dark."
    "The official seal is the last thing visible through the window glass — just the outline of it, the shape."

    thought "It was never about geography."

    ## Period summary
    scene black with dissolve
    pause 0.5

    "1955."

    if nudge_1955 == "conservative":
        "June Holloway wrote a formal response to Ada Whitehorse."
        "She copied the county health committee."
        "She explained the jurisdictional process correctly."
        pause 1.0
        "The county health committee received the referral."
        "They processed it at their next available meeting."
        "Thomas Whitehorse's arm had healed by then."
        pause 1.0
        "June voted present on three motions that year."
        "Her father was pleased with her second quarter."

    elif nudge_1955 == "middle":
        "June Holloway drove past the tracks on a Tuesday afternoon."
        "She did not call ahead."
        "She did not bring an aide."
        pause 1.0
        "She sat in a metal folding chair and listened to Dr. Runningwater explain what the county had not done."
        "She did not make any promises."
        "He did not ask her to."
        pause 1.0
        "She drove back across the tracks."
        "The road was the same in both directions."
        "She had not noticed that before."

    elif nudge_1955 == "progressive":
        "June Holloway read Ada Whitehorse's letter aloud in the council chambers."
        "The dates went into the official record."
        "Alderman Gifford left before she finished."
        pause 1.0
        "Her father called at six-fifteen."
        "They had dinner on Sunday."
        "It was uncomfortable and human on both sides."
        pause 1.0
        "The letter stayed in her coat pocket for three weeks."
        "Then she found a better place for it."
        "She is still deciding what that place is."

    pause 1.5

    if nudge_1955 == "conservative":
        "Ada Whitehorse did not write a second letter."
        "June thought about that sometimes."
    elif nudge_1955 in ["middle", "progressive"]:
        "Ada Whitehorse did not write a second letter."
        "She didn't need to."

    pause 2.0

    jump advance_to_1967
