## The Analog Kid — Period 1967
## Dr. Samuel Beaumont — "The Man The System Is Starting To Tolerate."
## The Darnell case. Backgrounds reuse 1955 art as placeholders (TODO: 1967 art).

# ---------------------------------------------------------------------------
# SAMUEL 1967 — ENTRY
# ---------------------------------------------------------------------------

label samuel_1967_begin:

    $ current_period = 1967
    $ current_location = "beaumont_practice"
    $ mark_visited("beaumont_practice")
    $ marcus_status = "drafted"

    scene bg_beaumont_practice_1955 with fade
    # play music "audio/music/1967_morning.ogg" fadein 2.0

    thought "Forty-eight years old."
    thought "The hospital granted me privileges two years ago. Provisional, they called it."
    thought "Admitting rights. No surgical suite. No department eligibility. No on-call rotation."
    thought "The word provisional is doing a great deal of work."

    "The practice has moved. A small office building on the edge of the south side — still south side, but a step removed from the living room with the good furniture pushed against the wall."
    "One nurse now. Three times the patients."
    "The pocket Bible sits on the corner of the desk where it has sat since 1955."

    if leitmotif_received:
        thought "This is the day."
        thought "I say it under my breath before the first patient. I have said it every morning for twelve years."

    jump samuel_1967_marcus

# ---------------------------------------------------------------------------
# MARCUS'S MOTHER
# ---------------------------------------------------------------------------

label samuel_1967_marcus:

    "There is a letter on the desk that is not a medical record."
    "Selective Service. Marcus Beaumont. Report for induction."

    thought "Marcus. The boy who worked the crossing signal. My brother's son. I raised him without ever saying that out loud."
    thought "He is twenty-two now. He fixes nothing about this letter by being good, and he has always been good."

    "Samuel goes to see Marcus's mother. He sits with her for two hours."
    "He does not tell her what he knows about the draft numbers — that the south side addresses and the north side deferments do not balance, that he has seen the arithmetic of it in Geri Habicht's margins."
    "He just sits with her."

    samuel "He'll write. Marcus always writes."

    "She nods. She has been nodding since the letter came."

    $ mark_talked("samuel", "beaumont_practice", "marcus_mother")

    thought "Walking home alone afterward, I say the four words again."
    thought "This is the day."
    thought "In 1955 it was discipline. Today it is something closer to endurance."

    $ samuel_leitmotif_count += 1

    jump samuel_1967_darnell_intro

# ---------------------------------------------------------------------------
# DARNELL — THE 1967 PROBLEM
# ---------------------------------------------------------------------------

label samuel_1967_darnell_intro:

    "Back at the office. The nurse has gone home. The last chart is closed."

    thought "Darnell. Nineteen. A patient of mine since he was twelve — I set his collarbone the year I opened."
    thought "Arrested Tuesday. A burglary on the north side. The evidence is circumstantial and the timeline is wrong."
    thought "I know it's wrong because Darnell was in my waiting room Tuesday evening with his mother and a fever of a hundred and one."
    thought "I have it documented. Date, time, temperature, in my own hand."

    thought "Frank DeLuca is not the arresting officer. But Frank knows about the arrest."
    thought "I have a medical record that is also, if anyone will look at it that way, an alibi."

    thought "I have not decided who I am willing to be about this yet."

    $ mark_talked("samuel", "beaumont_practice", "darnell")

    jump samuel_1967_explore

# ---------------------------------------------------------------------------
# EXPLORE — hand off to the shared hub loop (period-aware)
# ---------------------------------------------------------------------------

label samuel_1967_explore:

    $ current_location = "beaumont_practice"
    jump explore_1955

# ---------------------------------------------------------------------------
# LOCATION: SAMUEL'S PRACTICE (1967)
# ---------------------------------------------------------------------------

label location_beaumont_practice_1967:

    $ mark_visited("beaumont_practice")
    scene bg_beaumont_practice_1955 with dissolve

    "The office. The good lamp. The pocket Bible on the corner of the desk."

    if talked("samuel", "frank_office", "darnell"):
        thought "I've shown Frank what I have. Now it's a question of how it enters the world."
    else:
        thought "Darnell's chart is in the top drawer. Tuesday. A hundred and one degrees."
        thought "I could take it to the police. I could take it to the newspaper. I could take it to Ray."

    return

# ---------------------------------------------------------------------------
# LOCATION: NORTH SIDE HOSPITAL (1967) — provisional privileges
# ---------------------------------------------------------------------------

label location_hospital_north_1967:

    $ mark_visited("hospital_north")
    scene bg_hospital_north_1955 with dissolve

    "Middletown General. Samuel has a staff badge now. It opens most of the doors."
    "Not all of them. The surgical suite still requires an escort he is never quite offered."

    if not talked("samuel", "hospital_north", "privileges_1967"):
        $ mark_talked("samuel", "hospital_north", "privileges_1967")
        "Carol is still at the admissions desk. Older. She nods at him the way you nod at someone whose name you finally learned to say without an apology in it."
        carol "Dr. Beaumont."
        samuel "Carol."
        thought "Twelve years ago she could not process my referral. Today she can."
        thought "The form changed. The building did not. I am admitted to it and not of it."
        thought "Whatever I do about Darnell, I will do it knowing exactly how much of this they can take back."
    else:
        thought "Provisional. The word follows me down every polished hallway."

    return

# ---------------------------------------------------------------------------
# LOCATION: IHS CLINIC (1967) — Ray
# ---------------------------------------------------------------------------

label location_ihs_clinic_1967:

    $ mark_visited("ihs_clinic")
    scene bg_ihs_clinic_1955 with dissolve

    "The IHS clinic. George Runningwater retired in '64. The fluorescent tube still hums."
    "Ray Coldwater is at the folding table by the window with his case files, the way he has been on Tuesdays for fourteen years."

    if talked("ray", "ihs_clinic", "darnell_1967"):
        ray "Dr. Beaumont."
        samuel "Mr. Coldwater."
        "Some conversations only need to happen once."
        return

    ray "I heard about the Darnell boy."

    samuel "Everyone has heard about the Darnell boy."

    ray "I have county legal aid contacts. I've used them before. I'm tired of using them."

    "A pause. The two men who have been working the same problem from opposite ends of the same town for twelve years."

    if ray_samuel_connection:
        ray "We've done this dance before, you and I. James Whitehorse. 1955."
        samuel "I remember."
        ray "Then you know I'll move if you give me something to move with."
        thought "Ray Coldwater has never once asked me to trust him. He has only ever shown me that I already do."
    else:
        thought "We have never formally worked together. But we have been in this room at the same time too often to pretend."

    samuel "I have a chart. Tuesday evening. The boy was in my waiting room with a fever."

    ray "Then the boy has an alibi signed by a physician with hospital privileges."
    ray "That is a different thing in 1967 than it would have been in 1955."

    $ mark_talked("ray", "ihs_clinic", "darnell_1967")

    thought "He's right. My signature carries weight now that it did not used to carry."
    thought "Which means using it costs more than it used to, too."

    return

# ---------------------------------------------------------------------------
# LOCATION: POLICE STATION (1967) — Frank and the Darnell file
# ---------------------------------------------------------------------------

label location_frank_office_1967:

    $ mark_visited("frank_office")
    scene bg_frank_office_1955 with dissolve

    "The detective's office. The mustard linoleum. Frank DeLuca is fifty-two and has the particular stillness of a man who has stopped expecting the law to surprise him pleasantly."

    if talked("samuel", "frank_office", "darnell"):
        frank "Doctor."
        samuel "Detective."
        "The file is on the desk between them. Neither reaches for it."
        return

    "Frank looks up. He is not surprised to see Samuel. He has been half-expecting him since Tuesday."

    frank "I'm not the arresting officer."

    samuel "I know. That's why I came to you."

    "Frank turns a pencil over once. Sets it down."

    frank "The case is thin. I've read thinner cases that sent men to McAlester."
    frank "What have you got?"

    samuel "A medical record. The boy was in my waiting room at the time of the burglary. Documented. Temperature, time, my signature."

    "Frank is quiet for a moment. He is doing the arithmetic Samuel has already done — what it costs each of them to make this real."

    frank "You understand that if you hand me that, you've handed it to the department that arrested him."

    samuel "I understand that you are not the department."

    frank "No."
    "A beat."
    frank "I'm a man in it. There's a difference. I've spent thirty-two years insisting on it."

    $ mark_talked("samuel", "frank_office", "darnell")

    thought "There it is. The offer he didn't quite make and didn't quite withhold."
    thought "If I give Frank the chart, I am trusting a white detective with a Black boy's freedom."
    thought "I have reasons to. I have reasons not to."
    thought "Both lists are long. Both lists are honest."

    return

# ---------------------------------------------------------------------------
# LOCATION: TRACKS CROSSING (1967)
# ---------------------------------------------------------------------------

label location_tracks_crossing_1967:

    $ mark_visited("tracks_crossing")
    scene bg_tracks_crossing_1955 with dissolve

    "The crossing. The signal post has a civil rights poster on it. Torn at one corner. Taped. Torn again."
    "Marcus does not work the signal anymore. He is twenty-two and waiting on a bus to a war."

    thought "I used to find him here doing his homework between trains."
    thought "He told me once the crossing was the only place where both sides of town had to stop and wait together."
    thought "He was fourteen and he already understood the whole thing."

    return

# ---------------------------------------------------------------------------
# SAMUEL 1967 — THE NUDGE
# ---------------------------------------------------------------------------

label samuel_1967_nudge:

    scene bg_beaumont_practice_1955 with dissolve

    "Evening. The chart is on the desk. Tuesday. A hundred and one degrees."

    thought "Darnell does not have time for me to be careful in the way that protects me."
    thought "He has time for me to be careful in the way that protects him. They are not the same care."

    thought "Three ways to use what I have."

    menu samuel_1967_nudge_choice:

        ## CONSERVATIVE — stay in the medical lane
        "Document it formally. Testify if called. Stay a physician.":
            jump samuel_nudge_conservative_1967

        ## MIDDLE — give Frank the chart as a medical statement (requires trust built)
        "Give Frank the chart. Let him decide how it enters the case." if talked("samuel", "frank_office", "darnell"):
            jump samuel_nudge_middle_1967

        ## PROGRESSIVE — go to the press
        "Take it to the newspaper. Use the authority they gave me against them.":
            jump samuel_nudge_progressive_1967


label samuel_nudge_conservative_1967:

    $ nudge_1967 = "conservative"
    $ policy_score -= 1

    samuel "I'll file the record through the proper channel. The defense can subpoena it."
    samuel "I will testify if I am called. I will answer exactly what I am asked."

    thought "This is correct. It is also slow, and slowness is its own verdict for a boy in a cell."
    thought "I am protecting my license, my privileges, the younger physicians who got in behind me because I stayed careful."
    thought "I am protecting everything except the speed Darnell needs."
    thought "I have made this trade before. I have never once felt clean about it."

    jump samuel_1967_nudge_after


label samuel_nudge_middle_1967:

    $ nudge_1967 = "middle"
    $ frank_ray_trust = min(frank_ray_trust + 1, 3)

    samuel "Frank. I'm giving you the chart. As a medical record, not a statement."
    samuel "What it is, it is. What you do with it is yours to carry."

    "Frank takes it. Reads it once. His face does not change, which is how Samuel knows it landed."

    frank "I can get this in front of the right person without your name leading the way."
    frank "It costs me something. I'm not going to itemize it for you."

    samuel "I didn't ask you to."

    thought "I have handed a white detective a Black boy's alibi and trusted him to spend his own credit on it."
    thought "Twelve years ago I would not have known how to make that sentence true."
    thought "Ray taught me. Frank earned it. I am choosing to believe both of those things."

    if ray_samuel_connection:
        thought "Ray will hear it went through Frank. He'll know what that means. He helped build the bridge I just walked across."

    jump samuel_1967_nudge_after


label samuel_nudge_progressive_1967:

    $ nudge_1967 = "progressive"
    $ policy_score += 2

    samuel "There's a reporter at the county paper who will run it. The medical authority gives the story a spine the rumor never had."
    samuel "I'm a doctor with hospital privileges saying this boy was in my care at the hour they say he was breaking a window."

    thought "The privileges they granted me provisionally become un-provisional the moment this prints."
    thought "They will find a procedural reason. They always find a procedural reason."
    thought "Darnell will be a name the whole town has to say out loud, which is the only thing that has ever moved this town."

    "Samuel picks up the telephone."

    thought "I trained in Chicago, where a Negro physician could practice without asking permission for every breath."
    thought "I came home anyway. I am about to remember, out loud and in print, why that was a decision and not a mistake."

    jump samuel_1967_nudge_after

# ---------------------------------------------------------------------------
# POST-NUDGE
# ---------------------------------------------------------------------------

label samuel_1967_nudge_after:

    scene bg_beaumont_practice_1955 with dissolve

    "Late. The office is dark except for the good lamp."
    "Samuel sets the pocket Bible in his coat. It still fits exactly where it has always fit."

    jump samuel_1967_period_end

# ---------------------------------------------------------------------------
# PERIOD END — SAMUEL 1967
# ---------------------------------------------------------------------------

label samuel_1967_period_end:

    scene bg_beaumont_practice_1955 with dissolve
    # stop music fadeout 2.0

    "Evening. The waiting room is empty. The nurse left hours ago."

    samuel "This is the day."

    $ samuel_leitmotif_count += 1

    thought "Forty-eight years old. Two wars behind the town and a third one taking its sons unevenly."
    thought "I have privileges I cannot fully use and a signature that finally means something and a nephew on a bus."
    thought "I said the four words this morning out of habit."
    thought "I'm saying them tonight on purpose."

    ## Period summary
    scene black with dissolve
    pause 0.5

    "1967."

    if nudge_1967 == "conservative":
        "Samuel Beaumont filed the record through the proper channel."
        "Darnell's defense subpoenaed it in the spring."
        pause 1.0
        "The boy spent four months in a cell waiting for the system to read its own paperwork."
        "He came home. The paperwork had been right the whole time."

    elif nudge_1967 == "middle":
        "Frank DeLuca got the chart in front of the district attorney without Samuel's name leading the way."
        "The charge was quietly dropped for insufficient evidence."
        pause 1.0
        "Nobody made a speech. Darnell was home in three weeks."
        "Frank never told Samuel what it cost him. Samuel never asked."

    elif nudge_1967 == "progressive":
        "The county paper ran it under Samuel's name and his title."
        "Darnell was released within the month. The town said his name out loud."
        pause 1.0
        "The hospital found a procedural reason to review Samuel's privileges that summer."
        "They were restored. The word provisional came back with them, and stayed."

    pause 1.5
    "This is the day."
    pause 2.0

    jump advance_to_1979
