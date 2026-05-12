## The Analog Kid — Period 1955
## Complete playable draft: Samuel Beaumont protagonist thread.
## Other five characters stubbed for future builds.

# ---------------------------------------------------------------------------
# PERIOD ENTRY
# ---------------------------------------------------------------------------

label period_1955_begin:

    $ current_period = 1955
    $ mark_visited("main_street")

    if player_char == "samuel":
        jump samuel_1955_begin
    elif player_char == "carver":
        jump carver_1955_begin
    elif player_char == "geri":
        jump geri_1955_begin
    elif player_char == "ray":
        jump ray_1955_begin
    elif player_char == "frank":
        jump frank_1955_begin
    elif player_char == "june":
        jump june_1955_begin
    else:
        jump location_main_street_1955


# ---------------------------------------------------------------------------
# SAMUEL 1955 — MAIN THREAD
# ---------------------------------------------------------------------------

label samuel_1955_begin:

    scene bg_main_street_1955 with fade
    # play music "audio/music/1955_main_street.ogg" fadein 2.0

    thought "Early. The light hasn't gotten hot yet."
    thought "I've been on my feet since five. Mrs. Tanner's blood pressure. Old man Cooper's knee."
    thought "It isn't even eight o'clock."

    scene bg_beaumont_practice_1955 with dissolve

    jump samuel_practice_open


label samuel_practice_open:

    $ mark_visited("beaumont_practice")
    call show_nav_bar

    "The waiting room is his living room with the good furniture pushed against the wall."
    "Three wooden chairs he found at the VFW sale. A table with last month's {i}Life{/i} magazine and a copy of {i}Ebony{/i} he orders himself."
    "They are waiting the way people wait when they have learned that waiting is the condition."

    "Mrs. Tanner is back — she forgot to ask about her prescription."
    "Old man Cooper is reading the magazine upside down. He doesn't notice."
    "And in the corner: Ada Whitehorse, with her oldest boy."

    thought "Thomas. He's ten."
    thought "She has his arm held against her side in a way that tells me everything before I reach them."

    samuel "Mrs. Tanner. Give me five minutes."

    "Mrs. Tanner nods. She has been giving Dr. Beaumont five minutes since 1948."

    jump samuel_examine_thomas


label samuel_examine_thomas:

    samuel "Thomas. Come on back."

    "Ada stands too. Samuel doesn't say anything about it."

    "In the back room — his actual examining room, which is his dining room — Samuel turns on the good lamp and looks at the arm."

    "Thomas holds it out. He has been holding it the same careful way for a while now. His face is controlled in the particular way of a child who has decided not to cry."

    samuel "How long?"

    "Ada answers."

    ada_whitehorse "Two weeks."

    samuel "Did you go to the hospital?"

    ada_whitehorse "We went."

    "A pause."

    ada_whitehorse "They said they couldn't — they said to try the following Monday. We went Monday. They said to try again the next week."

    samuel "I see."

    "He does see. He has seen this particular shape of thing many times."

    menu samuel_thomas_response:
        "Ask Ada directly.":
            $ mark_talked("ada", "beaumont_practice", "hospital")
            samuel "What exactly did they tell you, Mrs. Whitehorse?"
            ada_whitehorse "That without a referring physician with privileges there, they couldn't process us."
            ada_whitehorse "The man at the desk was very polite about it."
            samuel "Yes. They usually are."
            thought "I am on their list of non-privileged practitioners."
            thought "I have been on that list for six years."
            thought "I have filed three formal requests to be removed from it."
            thought "I have received three procedural denials."

        "Say nothing. Treat the boy.":
            $ mark_talked("ada", "beaumont_practice", "quiet")
            thought "Some things don't need to be said out loud to be understood by the people already living them."
            samuel "Alright, Thomas. I'm going to need you to hold very still."
            "Thomas nods once. He is already holding still."

    "Samuel sets the arm. He is good at this — not just technically, which he is, but in the specific way of a doctor who knows that competence is its own kind of reassurance."

    "Thomas makes one sound. Just one. Then he doesn't make any more."

    samuel "Good man."

    "He wraps the arm in a proper splint. Better than the north side hospital would have done, he knows, because he has been doing this since before some of their residents finished medical school."

    "Ada watches. When it's done she puts her hand on Thomas's shoulder."

    ada_whitehorse "How much do we—"

    samuel "We'll figure it out."

    "It is what he always says. He keeps a ledger. Most of it he never collects."

    "Ada is about to leave. Samuel clears his throat."

    samuel "Mrs. Whitehorse. How is your husband?"

    "She turns back. Something moves across her face — not surprise, exactly. More like: {i}I was wondering when you'd ask.{/i}"

    ada_whitehorse "He's not well."

    samuel "The drinking."

    ada_whitehorse "It got worse after Marcus Jennings passed. He and James were close."

    ada_whitehorse "But it's — I don't think it's just the grief."

    samuel "No. I don't think so either."

    thought "James Whitehorse came in four months ago. Complained of fatigue, cramping, episodes of confusion."
    thought "I documented everything. I know what I'm looking at."
    thought "What I'm looking at requires a specialist. Bloodwork I can't run here."
    thought "Equipment that lives at the north side hospital, which does not process referrals from my office."

    $ mark_talked("ada", "beaumont_practice", "james")

    ada_whitehorse "He won't come in."

    samuel "I know. I'll come to him."

    "Ada nods. She and Thomas leave."

    "Samuel stands for a moment in his examining room."
    "The good lamp is still on."

    thought "Thomas's arm will heal in six weeks. He's young."
    thought "James Whitehorse needs a referral that requires a physician with hospital privileges to co-sign."
    thought "I have three options. None of them are simple."

    jump samuel_1955_explore


label samuel_1955_explore:

    call show_nav_bar
    scene bg_beaumont_practice_1955 with dissolve

    thought "The north side hospital. I could go back. Try the admissions desk again."
    thought "Or I could go to George Runningwater at the IHS clinic. He has connections I don't."
    thought "Or I could take a walk. Marcus works the crossing signal after school."

    "Mrs. Tanner is still waiting."
    samuel "Mrs. Tanner. Come on back."

    return


# ---------------------------------------------------------------------------
# LOCATION: BEAUMONT'S PRACTICE (1955)
# ---------------------------------------------------------------------------

label location_beaumont_practice_1955:

    $ mark_visited("beaumont_practice")
    call show_nav_bar
    scene bg_beaumont_practice_1955 with dissolve

    if not talked("ada", "beaumont_practice", "james"):
        jump samuel_practice_open

    "Dr. Beaumont's practice. The good lamp is still on."

    if not talked("runningwater", "ihs_clinic", "james_nudge"):
        thought "I need to figure out what to do about James Whitehorse."
    else:
        thought "The decision is made. Now we see what happens."

    return


# ---------------------------------------------------------------------------
# LOCATION: MAIN STREET (1955)
# ---------------------------------------------------------------------------

label location_main_street_1955:

    $ mark_visited("main_street")
    call show_nav_bar
    scene bg_main_street_1955 with dissolve

    "Main Street. The brick storefronts are warm in the afternoon light."
    "A few cars. A woman with a stroller. The sound of a radio from inside Earl's Diner."

    if player_char == "samuel":
        thought "I know every crack in this sidewalk. I grew up two blocks from here."
        thought "On this side of the tracks I'm Dr. Beaumont."
        thought "On the other side I'm still figuring out what I am to them."

    return


# ---------------------------------------------------------------------------
# LOCATION: SOUTH SIDE ENTRY (1955)
# ---------------------------------------------------------------------------

label location_south_side_entry_1955:

    $ mark_visited("south_side_entry")
    call show_nav_bar
    scene bg_main_street_1955 with dissolve

    "The south side of Middletown begins past the tracks."
    "The streets are narrower here. The houses are smaller but they are kept up."
    "There is a pride here that the north side reads as quaint and Samuel reads as hard-won."

    return


# ---------------------------------------------------------------------------
# LOCATION: NORTH SIDE HOSPITAL (1955)
# ---------------------------------------------------------------------------

label location_hospital_north_1955:

    $ mark_visited("hospital_north")
    call show_nav_bar
    scene bg_hospital_north_1955 with dissolve

    "Middletown General Hospital. The north side."
    "Polished floors. A smell of antiseptic and institutional coffee."
    "The admissions desk is staffed by a woman in her forties named Carol, who has worked here for eleven years."

    if talked("carol", "hospital_north", "referral"):
        "Samuel has already been to this desk today."
        thought "There is nothing new here."
        return

    "Carol looks up when Samuel approaches. There is no malice in her face."
    "There is also no surprise."

    carol "Dr. Beaumont. Good afternoon."

    samuel "I have a patient who needs a specialist referral processed."

    carol "Of course. Can I ask — is the patient currently registered with us?"

    samuel "He is not. I am his primary physician."

    carol "I see. And you have — I'm sorry, Dr. Beaumont, I have to ask. Do you have co-signing privileges with us?"

    samuel "I do not."

    carol "Then for the referral to be processed, we'd need a co-signature from a physician who does have active privileges here."

    samuel "I am the referring physician."

    carol "Yes, of course. But the form requires—"

    samuel "The form requires a co-signature from a physician with active privileges at this institution."

    carol "That's correct."

    "A pause. Samuel looks at the form on the desk."

    samuel "I've filed three requests for staff privileges here. In 1949, 1951, and 1953."

    carol "I know, Dr. Beaumont. I processed the third one myself."

    "She holds his gaze. She is not unkind. She is also not going to change the form."

    samuel "Thank you, Carol."

    carol "I'm sorry I can't be more help."

    $ mark_talked("carol", "hospital_north", "referral")

    thought "She means it. That is almost harder to carry than contempt."
    thought "Contempt at least gives you something to push against."

    return


# ---------------------------------------------------------------------------
# LOCATION: TRACKS CROSSING (1955)
# ---------------------------------------------------------------------------

label location_tracks_crossing_1955:

    $ mark_visited("tracks_crossing")
    call show_nav_bar
    scene bg_tracks_crossing_1955 with dissolve

    "The crossing. The tracks run east to west, splitting Middletown clean in half."
    "At three-thirty every afternoon a boy named Marcus Beaumont works the signal."
    "He is fourteen. He does his homework on the crossing box between trains."

    if talked("marcus", "tracks_crossing", "whitehorse"):
        "Marcus is still at the post. He waves when he sees Samuel."
        marcus "Still at it, Uncle Sam."
        samuel "Still at it."
        return

    "Marcus looks up from his notebook when he hears footsteps."

    marcus "Uncle Sam. You're south side. Wrong direction."

    samuel "I was taking a walk."

    marcus "In your work clothes."

    "Samuel almost smiles."

    samuel "Have you seen the Whitehorse boy lately?"

    "Marcus considers this."

    marcus "Thomas? He hasn't been at school."

    samuel "No."

    marcus "His dad's been bad again."
    "A beat."
    marcus "Mr. Jennings dying hit him hard. Everybody knows."

    samuel "Everybody knows a lot of things on this street."

    marcus "The crossing is a good place to watch."

    thought "He's not wrong. Fourteen years old and he already understands that the people who run things aren't always the ones who know things."

    samuel "You finish your homework before the six o'clock freight."

    marcus "I always do."

    $ mark_talked("marcus", "tracks_crossing", "whitehorse")
    $ ray_samuel_connection = True

    thought "Ray Holloway stopped at the crossing last Tuesday. Marcus told me."
    thought "Ray has been going to the IHS clinic with case files. He's been doing this for three years."
    thought "We've been working in parallel without ever formally acknowledging it."

    return


# ---------------------------------------------------------------------------
# LOCATION: IHS CLINIC (1955) — THE NUDGE
# ---------------------------------------------------------------------------

label location_ihs_clinic_1955:

    $ mark_visited("ihs_clinic")
    call show_nav_bar
    scene bg_ihs_clinic_1955 with dissolve

    "The Indian Health Service clinic on the south side. A converted storefront."
    "A government poster on the wall: a smiling family, everyone looking slightly to the right of the camera."
    "Metal folding chairs. A metal desk. A fluorescent tube that hums."

    if talked("runningwater", "ihs_clinic", "james_nudge"):
        "Dr. Runningwater is still at his desk."
        runningwater "Samuel."
        samuel "George."
        "There is nothing more to say right now."
        return

    "Dr. George Runningwater is at the desk. He does not look up immediately."
    "He is reading a case file with the attention of a man who has learned to read everything twice."

    runningwater "Samuel."

    samuel "George. Do you have a few minutes?"

    "Runningwater sets the file down. He has been expecting this visit — maybe not today specifically, but this conversation."

    runningwater "James Whitehorse."

    samuel "I've been treating him since April. The drinking is—"

    runningwater "Not just the drinking."

    samuel "No."

    "Runningwater leans back."

    runningwater "I've seen it too. He came in here in March. Blood pressure through the roof, hand tremors."
    runningwater "I documented it. Sent a request to the county."
    runningwater "You know what came back."

    samuel "Nothing came back."

    runningwater "The county health office processes forty-seven requests a week. For the south side they process about nine."

    "A pause. The fluorescent tube hums."

    if talked("carol", "hospital_north", "referral"):
        samuel "I went to the admissions desk at the north side hospital this afternoon."
        runningwater "How did that go."
        samuel "The way it always goes."
        runningwater "The form."
        samuel "The form."
        thought "George Runningwater has been practicing medicine in this town for eight years longer than I have."
        thought "He has filed more forms than I have. He knows exactly where they go."
    else:
        thought "I could have gone to the north side hospital first. I know what they would have said."
        thought "George already knows too."

    "Samuel stands at the window."

    samuel "James Whitehorse needs a specialist. The kind that lives at a hospital with equipment I don't have."
    samuel "The north side won't process my referrals. The county sits on requests."
    samuel "What are our options, George?"

    "Runningwater looks at him a long moment."

    jump samuel_1955_nudge


label samuel_1955_nudge:

    ## Ray may be present depending on what the player has done.
    ## If marcus_talked (which sets ray_samuel_connection), Ray is here doing case reviews.

    if ray_samuel_connection and not talked("ray", "ihs_clinic", "present"):
        $ mark_talked("ray", "ihs_clinic", "present")
        "The back door opens. A man comes in with a folder of papers."
        "Ray Holloway. Korean War vet. Runs the hardware store on Main Street."
        "He comes to the IHS clinic on Tuesdays to review welfare case files."
        "He stops when he sees Samuel."

        ray "Dr. Beaumont."

        samuel "Mr. Holloway."

        "They have seen each other at this clinic on four separate occasions."
        "They have never formally introduced themselves because they have both understood for some time that they are already acquainted."

        ray "James Whitehorse?"

        samuel "James Whitehorse."

        "Ray sets his folder on the counter and leans against the wall."

    thought "Three options. Each one costs something different."
    thought "The question is what I can afford to pay."

    menu samuel_1955_nudge_choice:

        ## CONSERVATIVE — official channels, protect the license
        "Continue through official channels. File again. Build the paper record.":
            jump samuel_nudge_conservative_1955

        ## MIDDLE — Ray, IHS federal hospital (requires ray_samuel_connection OR Ray is present)
        "Ask Ray about routing James through the federal IHS hospital." if ray_samuel_connection:
            jump samuel_nudge_middle_1955

        ## PROGRESSIVE — sympathetic north side physician, gray area
        "Find a sympathetic north side physician to co-sign the referral.":
            jump samuel_nudge_progressive_1955


label samuel_nudge_conservative_1955:

    $ nudge_1955 = "conservative"
    $ policy_score -= 2
    $ thomas_status = "deferred"

    samuel "I'm going to file again. With the county and with the hospital board."
    samuel "I'm going to document everything — James's case, the timeline, the prior requests."
    samuel "If I do this right, in two or three years there will be a record that can't be ignored."

    runningwater "Two or three years."

    samuel "I know."

    "Runningwater looks out the window. He doesn't say what they are both thinking."

    if ray_samuel_connection:
        "Ray picks up his folder."
        ray "I'll keep his welfare case open. That buys him some time with the county."
        samuel "Thank you."

    thought "James Whitehorse may not have two or three years."
    thought "What I am protecting is the principle — that the system should work the way it claims to."
    thought "What I am paying for that principle is James Whitehorse's health."
    thought "I will file the papers tomorrow. I will document everything."
    thought "I will be right and I may be too late."

    $ mark_talked("runningwater", "ihs_clinic", "james_nudge")
    jump samuel_1955_nudge_after


label samuel_nudge_middle_1955:

    $ nudge_1955 = "middle"
    $ thomas_status = "symbol"
    $ ray_samuel_connection = True

    "Samuel looks at Ray."

    samuel "The IHS federal hospital in McAlester processes referrals independently of the county system."
    samuel "I know they do because they've taken two of my patients in the last year."
    samuel "But James Whitehorse isn't enrolled. Technically he doesn't qualify."

    ray "Technically."

    "A silence."

    ray "I've been doing case reviews here for three years."
    ray "George's predecessor, Dr. Halbert, extended tribal courtesy to six non-enrolled patients in four years."
    ray "The paperwork said {i}adjacent community health consultation.{/i}"
    ray "Nobody looked at it very hard."

    runningwater "I can document James as a community health consultation case. Samuel provides the clinical notes."
    runningwater "Ray files the routing paperwork."

    samuel "If this is examined—"

    ray "Then I wrote the wrong thing on a form."

    "Ray says it simply. As if it were nothing. Samuel knows it is not nothing."

    samuel "It costs you a favor with someone."

    ray "It costs me a stamp."

    "Samuel looks at him."

    ray "I have a son. He's four."
    ray "The kind of town this is when he's fourteen matters."
    ray "Give me two weeks."

    thought "This is a rule being bent, not broken."
    thought "James Whitehorse will see a specialist. The record will not show exactly how."
    thought "In twelve years, when Thomas is old enough to get drafted, his family's file will be more complete."
    thought "That matters. I'm choosing to believe it matters."

    $ mark_talked("runningwater", "ihs_clinic", "james_nudge")
    $ carver_samuel_connection = True
    jump samuel_1955_nudge_after


label samuel_nudge_progressive_1955:

    $ nudge_1955 = "progressive"
    $ policy_score += 2
    $ thomas_status = "symbol"
    $ runningwater_complaint = "surfaced"

    samuel "There's a physician at the north side hospital. Dr. Elias Webb. He came out of Howard Medical School."
    samuel "He has full privileges. He trained under people who understand what we're dealing with."
    samuel "I could approach him. Ask him to co-sign referrals for my patients."
    samuel "The medicine is mine. His name is on the form."

    "Runningwater is quiet."

    runningwater "If that arrangement is discovered—"

    samuel "I know."

    runningwater "They won't come after you quietly, Samuel."

    samuel "I know that too."

    "Samuel stands at the window again."

    samuel "James Whitehorse is going to keep drinking until the underlying condition gets worse."
    samuel "I have watched three men in this community decline this way. Two of them died."
    samuel "I am not doing that again."

    runningwater "Webb will have to agree."

    samuel "I'm going to ask him. Today."

    thought "This is the line I said I wouldn't cross."
    thought "I said it because crossing it puts two careers at risk, not one."
    thought "I'm crossing it anyway."
    thought "Harold Blanton Sr. is on the county board. If he hears about this arrangement, he will make it his personal business."
    thought "I am choosing James Whitehorse over my own safety."
    thought "I hope that is the right choice. I believe it is the right choice."
    thought "Those are not the same thing."

    $ mark_talked("runningwater", "ihs_clinic", "james_nudge")
    jump samuel_1955_nudge_after


label samuel_1955_nudge_after:

    "Samuel says goodbye to Runningwater."

    if ray_samuel_connection and nudge_1955 == "middle":
        "Ray is still by the counter."
        ray "Two weeks."
        samuel "Two weeks."
        "They do not shake hands. They nod. It is sufficient."

    "Outside, the afternoon is tipping toward evening."
    "The light is going amber, the way it does here in summer."

    thought "Thomas's arm will heal."
    thought "Whether James Whitehorse gets what he needs — that depends on what happens next."

    jump samuel_1955_period_end


# ---------------------------------------------------------------------------
# PERIOD END — SAMUEL 1955
# ---------------------------------------------------------------------------

label samuel_1955_period_end:

    scene bg_beaumont_practice_1955 with dissolve
    # stop music fadeout 2.0
    # play music "audio/music/1955_evening.ogg" fadein 2.0

    "Evening. The waiting room is empty. Mrs. Tanner got her prescription."
    "Old man Cooper went home. The last patient left an hour ago."

    "Samuel is at his desk with the ledger open. He is not looking at it."

    thought "Thirty-six years old."
    thought "I have been practicing medicine in this town for four years."
    thought "I have filed eleven formal requests through four different channels."
    thought "I have treated two hundred and forty-one patients."
    thought "I know the names of every one of them."

    "A sound from outside. An old woman passing the window, humming to herself."
    "It is well with my soul. He knows the hymn. He has known it since he was six years old."
    "He lets it pass."

    "He closes the ledger."
    "He turns off the good lamp."
    "He stands in the dark for a moment — the specific dark of a room where the day's work is done but not finished."

    samuel "This is the day."

    $ samuel_leitmotif_count += 1
    $ leitmotif_received = True

    "He says it quietly. Not triumphantly. The way you say something you need to be true."

    ## Keepsake
    "On the corner of the desk: a small black Bible."
    "The cover is worn soft. His mother gave it to him the morning he left for medical school."
    "He has carried it in his coat pocket for eleven years. He takes it out every night and sets it on the desk."

    if not keepsake_bible:
        menu:
            "The Bible stays on the desk. It will be there in the morning.":
                thought "It is always there in the morning."
            "Pick it up. Put it back in the coat pocket.":
                $ keepsake_bible = True
                thought "It fits exactly in the inside pocket."
                thought "I don't know why I notice that. I've been carrying it for eleven years."
                thought "Maybe I notice it because tonight I needed it to fit."

    ## Period summary
    scene black with dissolve
    pause 0.5

    "1955."

    if nudge_1955 == "conservative":
        "Samuel Beaumont filed four more forms."
        "They went into the county system."
        "One of them, eventually, would matter."
        pause 1.0
        "James Whitehorse's drinking got worse before it got better."
        "But Thomas's arm healed clean."

    elif nudge_1955 == "middle":
        "Two weeks later, James Whitehorse saw a specialist at the federal IHS hospital in McAlester."
        "The diagnosis was hemochromatosis — iron overload, genetic, treatable."
        "The drinking had a cause. The cause had a treatment."
        pause 1.0
        "Ray Holloway filed the paperwork as {i}adjacent community health consultation.{/i}"
        "Nobody looked at it very hard."
        "Thomas's arm healed clean."

    elif nudge_1955 == "progressive":
        "Dr. Elias Webb agreed to co-sign referrals for three of Samuel's patients."
        "James Whitehorse was the first."
        "The arrangement lasted eight months before the hospital board noticed an irregularity."
        pause 1.0
        "By then, James Whitehorse had a diagnosis and a treatment plan."
        "Webb's privileges were suspended for ninety days."
        "Samuel received a formal letter of censure from the county medical board."
        "He framed it and put it in the back of a drawer."

    pause 1.5
    "This is the day."
    pause 2.0

    jump advance_to_1967


# ---------------------------------------------------------------------------
# OTHER PLAYER CHARACTER THREADS — 1955
# Defined in dedicated files:
#   carver_1955.rpy  |  geri_1955.rpy  |  ray_1955.rpy
#   frank_1955.rpy   |  june_1955.rpy
# ---------------------------------------------------------------------------

label location_earls_diner_1955:
    $ mark_visited("earls_diner")
    call show_nav_bar
    scene bg_main_street_1955 with dissolve
    "Earl's Diner. The smell of coffee and griddle grease."
    "A sign above the service window says where colored customers are to sit."
    "The waitress named Dot moves around it like it isn't there."
    "The way she moves around it tells you everything."
    return

label location_mount_zion_1955:
    $ mark_visited("mount_zion")
    call show_nav_bar
    scene bg_main_street_1955 with dissolve
    "Mt. Zion Baptist Church. White clapboard, fresh paint."
    "A bell that hasn't rung since the war."
    return
