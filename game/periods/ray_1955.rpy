## The Analog Kid
## Copyright (C) 2025 Blue Moon Foundry Software
## SPDX-License-Identifier: AGPL-3.0-or-later
##
## ray_1955.rpy — Raymond "Ray" Coldwater, 1955 thread.
## Social worker. Native American. South side base.
## The Simmons case.

# ---------------------------------------------------------------------------
# ENTRY
# ---------------------------------------------------------------------------

label ray_1955_begin:

    $ current_period = 1955
    $ mark_visited("tribal_office")
    $ current_location = "tribal_office"

    scene bg_tribal_office_1955 with fade
    # play music "audio/music/1955_south_side_morning.ogg" fadein 2.0

    thought "Early. Before the office gets its noise."
    thought "This used to be a shoe repair shop. You can still smell it under the government disinfectant."
    thought "I chose the metal desk against the far wall because it puts my back to the poster."

    "The poster: a smiling family in primary colors. {i}Your Future Is Our Priority.{/i}"
    "It arrived in 1952 in a federal envelope."
    "Ray set it up because the rules say to."

    thought "The Simmons file is open."
    thought "It has been open since yesterday afternoon."
    thought "It is not going to close itself."

    "Three children. Five, seven, eleven. The state's threshold for economic instability sits at a number Ray has memorized the way a man memorizes the depth of a ledge."
    "Bobby is seventeen and not counted in the threshold. He is the one who was supposed to push them over it safely."

    thought "Bobby applied at Holloway's hardware store two weeks ago."
    thought "Ray Holloway is not a bad man. That is part of what makes this hard."
    thought "Bobby knows it too. He applied anyway. He needed Ray Holloway to be the one to say no."

    "Ray closes the file. He opens it again."
    "The numbers do not change."

    thought "I went north. I learned the system."
    thought "I came back because I thought knowing the system was the same as being able to move inside it."
    thought "Some days I still think that."

    jump ray_1955_explore


# ---------------------------------------------------------------------------
# EXPLORATION HUB
# ---------------------------------------------------------------------------

label ray_1955_explore:

    $ current_location = "tribal_office"
    call show_nav_bar
    scene bg_tribal_office_1955 with dissolve

    "The Simmons file is on the desk."
    "It is Tuesday. The IHS clinic is open."

    jump explore_1955


# ---------------------------------------------------------------------------
# LOCATION: TRIBAL OFFICE (1955)
# ---------------------------------------------------------------------------

label location_tribal_office_1955:

    $ mark_visited("tribal_office")
    $ current_location = "tribal_office"
    call show_nav_bar
    scene bg_tribal_office_1955 with dissolve

    if not talked("ray", "tribal_office", "simmons_file"):
        $ mark_talked("ray", "tribal_office", "simmons_file")
        "The Simmons file. Bobby's application to Holloway's hardware store is paperclipped to the inside cover."
        "Ray's handwriting in the margin: {i}follow up wk of Oct 3.{/i}"
        thought "That was two weeks ago."
        thought "I have been following up in my head every day since."
    else:
        "The filing cabinet. The desk."
        "Government forms in triplicate."
        thought "Every form I fill out is a proof of address for a family the state half-sees."
        thought "I do not stop filling them out."

    return


# ---------------------------------------------------------------------------
# LOCATION: SOUTH SIDE STREET (1955)
# ---------------------------------------------------------------------------

label location_south_side_street_1955:

    $ mark_visited("south_side_entry")
    $ current_location = "south_side_entry"
    call show_nav_bar
    scene bg_south_side_street_1955 with dissolve

    "The block east of the tribal office."
    "Mrs. Delia Simmons lives four houses down. The house is the second-best-kept on the street."
    "The Simmons house has never been anything but."

    if not talked("delia", "south_side_street", "door"):
        $ mark_talked("delia", "south_side_street", "door")
        "Ray does not knock today."
        "He already knows what she will say. She will say she is managing. She will mean it."
        "Delia Simmons has been managing since 1948 and the managing has cost her things Ray cannot put in a case file."
        thought "She doesn't need me to knock on her door and ask how she is."
        thought "She needs the income line to hold."
    else:
        "The house is quiet in the way of a house where the children have been told to be quiet."
        thought "Delia is working a double at the laundry today."
        thought "The five-year-old is with a neighbor."
        thought "Everything accounted for. Everything."

    return


# ---------------------------------------------------------------------------
# LOCATION: TRACKS CROSSING (1955) — Ray's version
# ---------------------------------------------------------------------------

label location_tracks_crossing_1955_ray:

    $ mark_visited("tracks_crossing")
    $ current_location = "tracks_crossing"
    call show_nav_bar
    scene bg_tracks_crossing_1955 with dissolve

    "The crossing. Late afternoon. The light is going flat."
    "A boy named Marcus Beaumont works the signal after school."
    "He is doing homework on the crossing box. He doesn't look up until he hears footsteps."

    if talked("marcus", "tracks_crossing", "ray_stop"):
        "Marcus waves without turning from his notebook."
        marcus "Mr. Coldwater."
        ray "Marcus."
        "A freight passes. They wait it out."
        thought "He is fourteen and he already understands that some conversations happen between trains."
        return

    marcus "Mr. Coldwater."

    ray "Marcus. How's school."

    marcus "Same as last week."

    "A beat."

    marcus "Bobby Simmons hasn't been around."

    ray "No."

    "Marcus closes his notebook. He is thinking about something."

    marcus "My uncle — Dr. Beaumont — he comes down here sometimes. Takes the long way."
    marcus "He says the crossing is the one place where both sides have to wait together."

    thought "It is."
    thought "I stop here because it reminds me that the tracks are a fact, not a verdict."
    thought "Some days I need reminding."

    ray "You finish that homework before the six o'clock freight."

    marcus "I always do."

    $ mark_talked("marcus", "tracks_crossing", "ray_stop")

    thought "Marcus's uncle. Dr. Samuel Beaumont."
    thought "I've seen him at the IHS clinic. We have not formally introduced ourselves."
    thought "We don't need to. We already know what the other one is doing there."

    return


# ---------------------------------------------------------------------------
# LOCATION: IHS CLINIC (1955) — Ray's version
# ---------------------------------------------------------------------------

label location_ihs_clinic_1955_ray:

    $ mark_visited("ihs_clinic")
    $ current_location = "ihs_clinic"
    call show_nav_bar
    scene bg_ihs_clinic_1955 with dissolve

    "The IHS clinic. Ray's Tuesday desk is the folding table by the window."
    "His case files take up most of it."

    if talked("runningwater", "ihs_clinic", "simmons"):
        "Dr. Runningwater is at his desk. He does not look up."
        thought "He knows what I decided. He will not say whether he thinks it was right."
        thought "That is one of the things I respect about him."
        return

    "Dr. George Runningwater is reviewing a chart."
    "He does not acknowledge Ray's arrival, which is the same as a greeting."

    ray "George."

    runningwater "Ray."

    "Ray spreads the Simmons file on the folding table."

    "After a while:"

    runningwater "The threshold review."

    ray "October thirty-first."

    "Runningwater sets his chart down."

    runningwater "The children."

    ray "The three younger ones are fine. Thomas, Sarah, and the little one."
    ray "It's the income line. Without Bobby working, the household is sixty-two dollars below the state's threshold every month."

    runningwater "What did Holloway say."

    ray "He didn't say anything. He sent Bobby a letter. {i}Position has been filled.{/i}"
    ray "Standard form."

    "A pause."

    runningwater "Bobby applied knowing."

    ray "Bobby applied because he is out of other options."

    "Runningwater looks at the ceiling."

    runningwater "What are you going to do."

    $ mark_talked("runningwater", "ihs_clinic", "simmons")

    if ray_samuel_connection:
        "Through the window: a man crossing the south side street in a coat and hat."
        thought "Dr. Beaumont. He's been here before on Tuesdays."
        thought "We've never spoken about why we keep being in the same places."
        thought "We don't need to."

    jump ray_1955_nudge


# ---------------------------------------------------------------------------
# THE NUDGE
# ---------------------------------------------------------------------------

label ray_1955_nudge:

    thought "What are you going to do."
    thought "Three options. Not moral options. Practical options."
    thought "Each one produces a different outcome for the same family."

    menu ray_1955_nudge_choice:

        "Follow the protocol. Document. Report at threshold.":
            jump ray_nudge_conservative_1955

        "Go see Ray Holloway. Have the conversation.":
            jump ray_nudge_middle_1955

        "Challenge the criteria. Write to the state welfare director.":
            jump ray_nudge_progressive_1955


# ---------------------------------------------------------------------------
# CONSERVATIVE
# ---------------------------------------------------------------------------

label ray_nudge_conservative_1955:

    $ bobby_outcome = "shipped"
    $ policy_score -= 1

    thought "The threshold is the threshold."
    thought "I apply it the same way to every family. That is the rule I made for myself."
    thought "It is the only version of this job that doesn't become something else."

    "Ray closes the Simmons file. He makes a notation in the margin."
    "{i}Oct 31 review — threshold criteria met — mandatory report to follow.{/i}"

    "His handwriting is very neat. It has always been neat. He learned it because sloppy paperwork gets lost and families pay for it."

    runningwater "Ray."

    ray "I know."

    runningwater "You could—"

    ray "I know. I have thought about all of it."

    "Runningwater says nothing more. He knows Ray has thought about it."

    thought "The law is the law."
    thought "I applied it to the Harrington family in 1953. White family, north side, father out of work for eight months."
    thought "I applied it then. I will apply it now."
    thought "Bobby Simmons may be placed with the county. The younger children may follow."
    thought "Delia will fight it. She will lose."
    thought "This is the system working exactly as designed."
    thought "I will go home tonight and not sleep."

    $ mark_talked("runningwater", "ihs_clinic", "simmons_nudge")
    jump ray_1955_nudge_after


# ---------------------------------------------------------------------------
# MIDDLE
# ---------------------------------------------------------------------------

label ray_nudge_middle_1955:

    $ bobby_outcome = "deferred"

    thought "Ray Holloway is not a bad man."
    thought "That is a fact I have confirmed enough times to use."
    thought "He can't put Bobby behind the counter. His regulars would make that conversation happen once and it would end his business."
    thought "But the stockroom. Deliveries. Work that isn't visible."
    thought "It is not what Bobby deserves."
    thought "It is sixty-two dollars a month and the state review date is October thirty-first."

    "Ray picks up his hat."

    runningwater "Holloway's."

    ray "I'm not going to pressure him."

    runningwater "I know you're not."

    ray "I'm going to tell him what's in the file and let him decide what kind of man he is."

    "Runningwater almost says something. He decides against it."

    "Ray walks to Holloway's Hardware."
    "It is on Main Street. The north side."
    "Ray has been on Main Street before. He always knows, on Main Street, exactly which version of himself other people are seeing."

    scene bg_main_street_1955 with dissolve

    "The hardware store smells of oil and sawdust."
    "Ray Holloway is behind the counter. He is a large man, not unfriendly, whose eyes go careful when Ray walks in."

    townsperson "Mr. Coldwater."

    thought "He knows my name. He has always known my name."
    thought "This is a small town."

    ray "Ray. I wanted to talk to you about Bobby Simmons."

    "Holloway sets down what he's doing. He does not pretend he doesn't know what this is about."

    townsperson "I sent the boy a letter."

    ray "I know. I have his file."
    ray "Three younger siblings. His mother is working doubles at the laundry."
    ray "The state threshold review is October thirty-first."
    ray "I'm not here to tell you your business."

    "A silence."

    ray "The stockroom. Deliveries. Something that doesn't put him out front."

    "Holloway looks at the counter. He is working through something."

    townsperson "What you're asking — my regulars—"

    ray "I know what I'm asking."

    "Another silence."

    townsperson "It's not visible, he keeps his head down, and he comes in through the alley."

    "Ray doesn't say it is what Bobby deserves. It isn't."
    "He says:"

    ray "Thank you."

    "Holloway nods once. The conversation is over."

    scene bg_ihs_clinic_1955 with dissolve
    $ current_location = "ihs_clinic"

    thought "Bobby will hear about this before evening."
    thought "He will take it. He will know exactly what it is and what it isn't."
    thought "Sixty-two dollars a month. The income line holds."
    thought "The state review passes. The family stays together."
    thought "In ten years Bobby will have something to tell his own children about what people are capable of and what they are not."
    thought "That is what I have done here."
    thought "I'm not sure whether to be proud of it."

    if not ray_samuel_connection:
        $ ray_samuel_connection = True
        "Back at the clinic, Dr. Runningwater is still at his desk."
        "And in the doorway: the man Ray has seen here before on Tuesdays."
        "Dr. Samuel Beaumont. He has a patient file under his arm."
        "He stops when he sees Ray."
        samuel "Mr. Coldwater."
        ray "Dr. Beaumont."
        "They have met, in the way of men who have been in the same rooms enough times to know each other without introduction."
        thought "We have been working in parallel for three years."
        thought "We have never spoken about it."
        thought "We both know that speaking about it would change something."

    $ mark_talked("runningwater", "ihs_clinic", "simmons_nudge")
    jump ray_1955_nudge_after


# ---------------------------------------------------------------------------
# PROGRESSIVE
# ---------------------------------------------------------------------------

label ray_nudge_progressive_1955:

    $ bobby_outcome = "real_answer"
    $ policy_score += 1

    thought "The criteria were written in 1948."
    thought "I have read the source document. I found it in the state archive. It took two months to request."
    thought "The man who wrote the household threshold had never been to the south side of any town."
    thought "He used wage data from manufacturing sectors that do not exist here."
    thought "He excluded domestic labor. He excluded seasonal work."
    thought "He excluded the kind of work that the Delia Simmonses of this state have always done."

    "Ray puts the Simmons file in his briefcase."
    "He takes out a legal pad."

    "He writes for forty-five minutes."
    "The letter is to the state welfare director. He names the criteria. He shows the math."
    "He cc's the county board and the IHS regional administrator."

    "It is specific. It is documented. It is the kind of letter that cannot be ignored by saying {i}we'll take that under advisement{/i} because every follow-up request will cite the date it was sent."

    runningwater "What are you doing."

    ray "Writing a letter."

    runningwater "To."

    ray "Everyone who should have written it already."

    "Runningwater reads it over his shoulder."
    "He is quiet for a long time."

    runningwater "This will take months. The review process—"

    ray "I know. The family stays on the tightrope until the criteria change."

    runningwater "And if the threshold date comes before the review."

    "Ray caps his pen."

    ray "Then I write another letter. And another."
    ray "Eventually the math is too visible to ignore."

    thought "This is the thing I cannot stop believing."
    thought "I believed it when I was at the state university, a Native kid in the back of the lecture hall."
    thought "I believe it now."
    thought "The Simmons family will carry the cost of me believing it."
    thought "I do not know a way around that."

    $ mark_talked("runningwater", "ihs_clinic", "simmons_nudge")
    jump ray_1955_nudge_after


# ---------------------------------------------------------------------------
# AFTER THE NUDGE
# ---------------------------------------------------------------------------

label ray_1955_nudge_after:

    scene bg_ihs_clinic_1955 with dissolve

    "Ray puts his coat on."
    "It is four-thirty. The clinic light has gone from white to yellow."

    if bobby_outcome == "shipped":
        thought "The form is filed. October thirty-first."
        thought "I have done this correctly."
    elif bobby_outcome == "deferred":
        thought "Bobby will hear by this evening."
        thought "It buys time. Time is not a solution."
        thought "It is what I had."
    elif bobby_outcome == "real_answer":
        thought "The letter is in the outbox."
        thought "It will arrive Tuesday. The director will read it Wednesday or let it sit until Friday."
        thought "Either way, it is in the world now."

    jump ray_1955_period_end


# ---------------------------------------------------------------------------
# PERIOD END
# ---------------------------------------------------------------------------

label ray_1955_period_end:

    scene bg_south_side_street_1955 with dissolve
    # stop music fadeout 2.0
    # play music "audio/music/1955_south_side_evening.ogg" fadein 2.0

    "Evening. The south side street has gone quiet."
    "Ray's house is three blocks from the tribal office. He has made this walk for three years."

    thought "I came back because someone had to know the paperwork and also know the people."
    thought "The north side sees my state salary and thinks: manageable."
    thought "The south side sees my state salary and thinks: compromised."
    thought "They are both half right."

    "His son is in the front room when Ray opens the door."
    "Four years old. His name is Daniel."
    "He is lying on his stomach on the floor with a picture book, which he is looking at very seriously."

    "He does not look up."
    "Then he does."

    ray "Hey, Dan."

    "Daniel holds up the picture book. It has a bear on the cover."

    thought "Bear."
    thought "He knows the word. He just wants to show me."

    "Ray sits on the floor beside him."
    "Not on the chair. The floor."
    "He looks at the bear."

    ray "Yeah. That's a bear."

    "Daniel turns the page. There is another bear."

    thought "He is four."
    thought "When he is fourteen, he will go to a school on this side of the tracks."
    thought "When he is fourteen, the kind of town this is will be determined by choices being made right now."
    thought "By me, and by people like me, and by people who are nothing like me and are also making choices."

    "Daniel closes the book. He sets it carefully on the floor."
    "He climbs into Ray's lap without asking, which is the only way he ever does it."

    "Ray puts his arm around him."
    "Outside, a dog barks once and goes quiet."
    "The light from the kitchen is the particular yellow of a house where someone is cooking."

    thought "His mother is making supper."
    thought "This is the day."
    thought "I don't know yet if it was enough."
    thought "I am going to do it again tomorrow."

    ## Period summary
    scene black with dissolve
    pause 0.5

    "1955."

    if bobby_outcome == "shipped":
        "Ray Coldwater documented the Simmons case correctly."
        "The threshold review ran on October thirty-first."
        "Bobby Simmons was placed with the county the following week."
        pause 1.0
        "The three younger children remained with Delia."
        "The paperwork was exactly right."
        "Ray did not sleep well for a long time."

    elif bobby_outcome == "deferred":
        "Ray Holloway put Bobby Simmons on the stockroom schedule starting Monday."
        "Deliveries on Thursday mornings. In through the alley."
        pause 1.0
        "The income line held."
        "The state threshold review found the Simmons household economically stable."
        "Bobby worked the stockroom for fourteen months."
        "He did not go in the front."

    elif bobby_outcome == "real_answer":
        "The letter arrived at the state welfare director's office on Tuesday."
        "The director forwarded it to the policy review committee on Thursday."
        pause 1.0
        "The committee met in January."
        "The threshold criteria were revised in March, effective the following fiscal year."
        "The Simmons family held on until spring."
        "It was closer than Ray had said it would be."

    pause 1.5

    "This is the day."

    pause 2.0

    jump advance_to_1967


# ---------------------------------------------------------------------------
# END OF ray_1955.rpy
# ---------------------------------------------------------------------------
