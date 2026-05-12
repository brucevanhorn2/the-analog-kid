## The Analog Kid — Detective Frank DeLuca, 1955 Thread
## Copyright (C) 2025 Blue Moon Foundry Software
## Licensed under the GNU Affero General Public License v3.0 (AGPL-3.0)
## https://www.gnu.org/licenses/agpl-3.0.html


# ---------------------------------------------------------------------------
# FRANK 1955 — ENTRY
# ---------------------------------------------------------------------------

label frank_1955_begin:

    $ current_period = 1955
    $ current_location = "frank_office"
    $ mark_visited("frank_office")

    scene bg_frank_office_1955 with fade
    # play music "audio/music/1955_morning_office.ogg" fadein 2.0

    "Morning. The office smells like cigarette smoke and the particular kind of boredom that accumulates in institutional spaces."
    "Metal desk. A bulletin board with three case notes and a map of the city's precincts that nobody has updated since 1948."
    "The linoleum is the color of old mustard."

    thought "Tuesday."
    thought "I have been a detective with Middletown PD for six years."
    thought "Before that I was a patrolman for eight. Before that I was my father's son in a factory town."
    thought "I know what this city looks like from every angle except the one angle it doesn't want me to look from."

    "The file landed on Frank's desk at eight-fifteen."
    "He has been reading it for twenty minutes."
    "He reads a file the way his father read a contract — slowly, looking for the thing that isn't there."

    thought "Break-in. Barbershop on the south side. Saturday night, two weeks ago."
    thought "Victim: Clarence Webb. Reported the break-in himself."
    thought "Responding officer: Kessler."

    "He sets the page down."
    "He picks it up again."

    thought "Nine PM to eleven PM."
    thought "Two hours. No account. No explanation."
    thought "Just a gap, sitting in the middle of the timeline like a missing tooth."

    "He reads the rest of the report. It is competent in the way that things are competent when competence is the point."
    "If you don't know what you're looking for, it reads fine."

    thought "Kessler moonlights."
    thought "I know this because I have made it my business to know this."
    thought "He pulls security shifts at Blanton Manufacturing, two nights a week."
    thought "I know that. The report doesn't mention it. The report doesn't need to mention it."
    thought "That's one kind of gap. The other kind is a two-hour hole in your timeline."

    "Chief Harmon called Frank in at nine."
    "The conversation was brief."

    townsperson "South side on south side. These things happen."
    townsperson "No leads. Close it unsolved. Move on."

    "The chief said it the way he says things — not unkindly, not cruelly. Administratively."
    "He has been running this department for fourteen years. He is good at his job."
    "Part of being good at his job is knowing which files to close."

    thought "He looked me in the eye when he said it."
    thought "He wasn't threatening me. He wasn't asking me to do anything dishonest."
    thought "He was asking me to do nothing."
    thought "I have been trying to figure out if that's the same thing."

    jump frank_1955_explore


# ---------------------------------------------------------------------------
# FRANK 1955 — EXPLORE
# ---------------------------------------------------------------------------

label frank_1955_explore:

    $ current_location = "frank_office"
    call show_nav_bar
    scene bg_frank_office_1955 with dissolve

    "The file is still on the desk."
    "It will be there when Frank gets back."

    thought "The office. The barbershop. Those are the two places I have right now."
    thought "The south side is a third place. I have not been there on official business that didn't involve putting someone in a car."
    thought "That is a fact I have not examined closely until this morning."

    return


# ---------------------------------------------------------------------------
# LOCATION: FRANK'S DETECTIVE OFFICE (1955)
# ---------------------------------------------------------------------------

label location_frank_office_1955:

    $ mark_visited("frank_office")
    $ current_location = "frank_office"
    call show_nav_bar
    scene bg_frank_office_1955 with dissolve

    if not talked("frank", "frank_office", "file_read"):
        $ mark_talked("frank", "frank_office", "file_read")

        "Frank pulls the case file again."
        "He has read it four times. He reads it a fifth."

        "Clarence Webb. Age fifty-three. Runs a numbers operation out of the back of a barbershop."
        "The report says: {i}illegal gambling establishment.{/i}"
        "That is one name for it."

        thought "The other name for it is: a credit pool."
        thought "Small amounts in. Borrow against the balance. Pay back with a little on top."
        thought "No collateral required. No credit history. No branch office on the south side."
        thought "The bank doesn't go there. This is what goes there instead."

        "Clarence Webb reported the break-in."
        "Frank underlines this with a pencil."
        "Most people running a numbers operation don't call the police. They absorb the loss."
        "Clarence Webb called the police."

        thought "He called because he thought it would matter."
        thought "That's the detail that keeps finding me."

        "The gap in Kessler's report. Nine to eleven."
        "Frank writes the times on a separate sheet of paper. He folds it and puts it in his shirt pocket."

        thought "I'm keeping this separate from the file."
        thought "I don't know yet why I'm doing that. I know that I'm doing it."

    else:
        "The file on the desk. The same file."
        "Frank has added nothing to it. He has not signed the closure form."

        thought "The form is still in the top drawer."
        thought "It will keep."

    return


# ---------------------------------------------------------------------------
# LOCATION: JOE'S BARBERSHOP — NORTH SIDE (1955)
# ---------------------------------------------------------------------------

label location_barbershop_1955:

    $ mark_visited("barbershop")
    $ current_location = "barbershop"
    call show_nav_bar
    scene bg_barbershop_1955 with dissolve

    "Joe Tolliver's barbershop. North side, two blocks off Main."
    "A barber chair and a waiting bench and a radio in the corner that plays at a volume designed for the waiting bench."
    "Three mirrors. An oscillating fan. The smell of witch hazel and hair tonic."
    "Joe has been cutting hair in this town for twenty-two years."

    if talked("joe", "barbershop", "webb"):
        "Joe is finishing a cut."
        "He nods when Frank comes in."
        townsperson "Detective."
        frank "Joe."
        "Frank sits on the bench. The radio fills the silence."
        thought "He told me what he's going to tell me. The rest is what I do with it."
        return

    "There is one man in the chair. Frank doesn't recognize him."
    "Joe Tolliver works without hurrying. He cuts hair the way a man cuts hair when he knows there is no reason to rush."

    "He sees Frank in the mirror. His hands do not pause."

    townsperson "Detective DeLuca."

    frank "Joe. When you've got a minute."

    "The man in the chair is done in four minutes. He pays and leaves."
    "Joe puts the cape away. He looks at Frank in the mirror again."

    townsperson "South side job."

    "Not a question."

    frank "How'd you know?"

    townsperson "Because it's the only kind of south side job that comes in here instead of going south."

    "Frank sits down in the barber chair. Joe doesn't pick up the scissors. This is not that kind of conversation."

    frank "Clarence Webb."

    "Joe looks at the floor. A small pause — the kind that is not hesitation, but consideration."

    townsperson "I know Clarence. Not personally. By way of people who know him."

    frank "The operation out of the back of the barbershop."

    townsperson "That's what it is."
    townsperson "But I expect you know what it also is."

    frank "A credit pool."

    townsperson "A lot of families in that neighborhood have borrowed from Clarence Webb."
    townsperson "Paid back. Borrowed again when they needed it."
    townsperson "He runs it straight. Charges less than the loan sharks that come through from Tulsa."
    townsperson "The bank—"

    frank "I know about the bank."

    "A pause."

    townsperson "The break-in took out a week's cash. Maybe more."
    townsperson "There are people on the south side right now who put money in that pool and don't know if it's gone."
    townsperson "That's what the break-in cost. Not just Clarence."

    thought "He's telling me why it matters."
    thought "He's telling me because he doesn't know if I already know, and because it's worth saying either way."

    frank "The responding officer. Kessler."

    "Joe sets a hand on the barber chair arm. He does not look at Frank directly."

    townsperson "I don't know anything about Kessler."

    frank "Doesn't mean you haven't heard things."

    "A long pause. The radio plays something Frank doesn't recognize."

    townsperson "I've heard that Kessler works nights."
    townsperson "I've heard the place he works nights is on the west end of the factory district."
    townsperson "I have not heard that from anyone who would put their name to it."

    frank "I'm not asking for names."

    "Joe nods. Once."

    townsperson "Clarence reported it because he thought someone would listen."
    townsperson "I know he thought that because I know Clarence Webb would not call otherwise."
    townsperson "Whether someone listens — that's not my department, Detective."

    thought "He said it without weight. Without accusation."
    thought "That is almost harder to carry than accusation."

    $ mark_talked("joe", "barbershop", "webb")

    return


# ---------------------------------------------------------------------------
# FRANK 1955 — THE NUDGE
# ---------------------------------------------------------------------------

label frank_1955_nudge:

    scene bg_frank_office_1955 with dissolve

    "Afternoon. The office is quieter now."
    "The closure form is on the desk. Frank has taken it out of the drawer."
    "The file is beside it."

    thought "Three things in front of me."
    thought "The file. The form. The sheet of paper in my shirt pocket with Kessler's hours written on it."

    thought "The chief wants the form signed."
    thought "Joe Tolliver told me what he told me."
    thought "Clarence Webb went through proper channels and is waiting to see what happens."

    "Frank picks up the form. He holds it. He sets it back down."

    thought "My father came here in 1920."
    thought "He spent thirty years believing that the law was the thing that made this place worth being in."
    thought "He said: in the old country, the law is for people with money. Here it is for everyone."
    thought "He believed that. He needed to believe that."
    thought "I am trying to figure out what I need."

    menu frank_1955_nudge_choice:

        ## CONSERVATIVE
        "Write 'unsolved, no leads.' Close the file. Do what the chief asked.":
            jump frank_nudge_close_1955

        ## MIDDLE
        "Mark it 'active investigation.' Go to the south side. Build a file quietly.":
            jump frank_nudge_active_1955

        ## PROGRESSIVE
        "Take the Kessler discrepancy to the district attorney's office.":
            jump frank_nudge_da_1955


label frank_nudge_close_1955:

    $ runningwater_complaint = "buried"
    $ policy_score -= 1
    $ nudge_1955 = "conservative"

    "Frank picks up the pen."

    thought "Unsolved. No leads."
    thought "That is true enough. I don't have a witness who'll sign a statement. I don't have physical evidence."
    thought "I have a two-hour gap and a name."
    thought "That is not enough for a case."

    "He writes the words. His handwriting is careful — he has always written carefully, the way his father did, as if the words are going somewhere that matters."

    thought "I am choosing the institution."
    thought "I am choosing the institution because I am part of it and because breaking from it over this particular file — with this particular victim and this particular officer — is a cost I cannot calculate right now."
    thought "I know what I'm doing."
    thought "Knowing what you're doing is not the same as it being right."

    "He signs the form."

    "He does not put it in the out-box immediately."
    "He puts it face-down on the corner of the desk and looks at it for a moment."

    thought "Kessler's name."
    thought "I'm going to remember it."
    thought "I don't know what I'm going to do with remembering it."
    thought "That is the best I have right now."

    "He puts the form in the out-box."

    jump frank_1955_nudge_after


label frank_nudge_active_1955:

    $ runningwater_complaint = "frank_background"
    $ keepsake_notebook = True
    $ nudge_1955 = "middle"

    "Frank does not sign the form."
    "He puts it back in the drawer."

    "He takes a fresh notebook from the supply cabinet. The department-issue ones, tan cover."
    "He writes on the inside front: {i}Case notes — Webb, C. — D. DeLuca.{/i}"
    "He puts the date."

    thought "This is not going in the file. The file stays thin."
    thought "This is mine."

    "He drives south that afternoon."
    "Across the tracks. The streets are narrower. The houses are smaller but kept."
    "He finds the barbershop — the actual south side barbershop, the one in the report."
    "He parks a block away. He does not wear the badge on his lapel."

    "Clarence Webb is a man in his fifties. He is sweeping the floor of the empty shop when Frank walks in."
    "He looks at Frank and knows immediately what Frank is."

    townsperson "Officer."

    frank "Detective. DeLuca. I'm not here officially."

    "A pause. Webb keeps the broom in his hands. He does not look afraid. He looks watchful."
    "There is a difference."

    townsperson "The report said unsolved."

    frank "The report says what it says."
    frank "I'm asking what you saw."

    "Webb sets the broom against the wall."
    "He talks for twenty minutes."
    "He is precise. He has a good memory and he has been turning this over since it happened."
    "He saw the responding officer arrive. He saw him walk the perimeter of the building."
    "He saw him sit in his patrol car from nine-twelve to eleven-oh-four."
    "He knows the time because he was watching the clock on the wall of the shop."

    townsperson "I wasn't going to say that to just any officer."

    frank "Why are you saying it to me?"

    "Webb looks at him. A long, level look."

    townsperson "Because you came down here."
    townsperson "Because you parked a block away."

    thought "He is telling me he saw the parking. He was watching."
    thought "A man who has been sitting on information for two weeks, watching to see who shows up."

    "Frank writes in the notebook. He documents Kessler's shift logs — he has already pulled them from the department's records, the moonlighting hours that aren't secret but aren't broadcast."
    "He writes down what Webb told him."
    "He does not close the file. He marks it: {i}Active investigation — pending additional evidence.{/i}"

    thought "The file stays open. The chief will see that."
    thought "I am not going to the DA. Not yet."
    thought "Not yet is doing a lot of work in that sentence."

    "He puts the notebook in his coat's inside pocket."
    "It fits against his ribs like a thing that was always going to be there."

    jump frank_1955_nudge_after


label frank_nudge_da_1955:

    $ runningwater_complaint = "surfaced"
    $ policy_score += 1
    $ keepsake_notebook = True
    $ nudge_1955 = "progressive"

    "Frank does not sign the form."
    "He puts it back in the drawer."

    "He takes the sheet of paper from his shirt pocket. The times. Kessler's hours."
    "He writes two more pages of notes and puts them all in an envelope."

    "The district attorney's office is three blocks from the precinct."
    "He walks."

    "He does not call ahead. He asks for the DA personally."
    "The receptionist tells him the DA is available for fifteen minutes."
    "Frank takes fifteen minutes."

    "He lays the envelope on the DA's desk."
    "He explains what the envelope contains."
    "He says: a two-hour gap in the responding officer's timeline. A moonlighting arrangement at Blanton Manufacturing. A victim who is willing to give a statement."

    "The DA reads the envelope's contents without speaking."
    "He is a careful man — a man who has learned to be careful in the way that people learn when they have been doing a job for twenty years and have watched what happens to the people who are not."

    townsperson "Detective DeLuca."

    frank "Sir."

    townsperson "You understand that this file came from the chief's desk."

    frank "I do."

    townsperson "You understand what I mean when I say that."

    frank "I do."

    "A long pause."

    townsperson "I'm going to acknowledge this meeting in the record."
    townsperson "I am not going to act on it today."
    townsperson "I am going to acknowledge that a file exists and that it was brought to my attention."

    frank "That's enough for now."

    "The DA looks at him."

    townsperson "Is it."

    thought "No. But it's what he can do."
    thought "I am not asking for more than he can do."

    "Frank walks back to the precinct."

    "Chief Harmon calls him in on Friday."
    "The meeting is brief. The chief does not raise his voice."
    "He does not threaten Frank's job. He does not threaten anything directly."
    "He says: {i}I told you how I wanted it handled.{/i}"
    "He says: {i}You're a good detective. I want you to stay a good detective.{/i}"

    "Frank says: {i}Yes sir.{/i}"

    "He says nothing else."

    "In the hallway after, Frank stands by the water fountain for a long moment."

    thought "I have been a detective in this department for six years."
    thought "I thought we wanted the same thing — me and the department."
    thought "I thought the law was the thing we both served."
    thought "The chief serves the department."
    thought "I think I serve the law."
    thought "I am now aware those are not always the same office."

    "He takes the notebook out of his coat."
    "He adds two lines."
    "He puts it back."

    jump frank_1955_nudge_after


# ---------------------------------------------------------------------------
# FRANK 1955 — AFTER THE NUDGE
# ---------------------------------------------------------------------------

label frank_1955_nudge_after:

    scene bg_frank_office_1955 with dissolve

    "Late afternoon."
    "The office is emptying out. Shift change. The sound of the duty sergeant calling roll in the next room."

    if nudge_1955 == "middle" or nudge_1955 == "progressive":
        "Frank is at his desk. The notebook is in his coat."
        "He thinks about Clarence Webb sweeping the floor of the empty shop."

        thought "He called the police because he thought someone would listen."
        thought "Someone listened."
        thought "I don't know yet if that's enough."

        if not keepsake_notebook:
            menu:
                "Leave the notes in the desk drawer for now.":
                    thought "They'll keep. The drawer locks."
                "Put the notebook in your coat.":
                    $ keepsake_notebook = True
                    thought "It fits against my ribs."
                    thought "My father used to carry a small New Testament in that pocket."
                    thought "He said he wanted something in there that told him what things were supposed to be for."
                    thought "I think he'd understand the notebook."

    else:
        "Frank is at his desk. The out-box is full."
        thought "The form is in there."
        thought "By tomorrow it'll be filed."
        thought "Kessler."
        thought "I'm going to remember that name for a long time."

    jump frank_1955_period_end


# ---------------------------------------------------------------------------
# PERIOD END — FRANK 1955
# ---------------------------------------------------------------------------

label frank_1955_period_end:

    scene bg_frank_office_1955 with dissolve
    # stop music fadeout 2.0
    # play music "audio/music/1955_evening.ogg" fadein 2.0

    "Evening. The precinct goes quiet the way precincts go quiet — not completely, never completely, but the quality of the noise changes."
    "Someone talking on the phone in the next office. A typewriter. The front door opening and closing."

    "Frank is still at his desk."
    "He has not turned on the desk lamp. The light from the hallway is enough."

    thought "Twenty years in this town."
    thought "I grew up on the north side, two streets from here."
    thought "My father's house is four blocks away."
    thought "He came here in 1920 and worked thirty years at a factory and died believing the law was worth believing in."

    "A sound from outside. A car passing on the street. Headlights moving across the wall."

    thought "He wasn't wrong."
    thought "He was right about the law. He just didn't know all of what the law was doing."
    thought "I'm starting to."

    "Frank reaches into the supply cabinet and pulls out an incident report form."
    "He does not fill it out."
    "He folds it and puts it in the file drawer."
    "He closes the drawer."

    thought "There is going to be a day when the thing I saw today becomes a thing I have to decide again."
    thought "I want to remember what it felt like the first time."
    thought "The feeling doesn't last. The decision does."

    "He turns off the desk lamp."
    "He sits in the dark for a moment — the specific dark of a room where the work is not done and is not going to be done tonight."

    frank "What is it supposed to be for."

    "He says it quietly. Not to anyone. Not to the dark. Just into the space where the question lives."
    "The way a man says something he needs to keep asking so he doesn't forget to ask it."

    ## Period summary
    scene black with dissolve
    pause 0.5

    "1955."

    if nudge_1955 == "conservative":
        "The Webb case was filed as unsolved, no leads."
        "It joined eleven other south side cases filed the same way that year."
        pause 1.0
        "Kessler continued his moonlighting arrangement at Blanton Manufacturing."
        "Frank remembered his name."
        "That was the cost of the file. That, and Clarence Webb, who had called the police and waited."

    elif nudge_1955 == "middle":
        "The Webb case stayed open."
        "Frank's notebook went into his inside coat pocket and stayed there."
        pause 1.0
        "He documented two more incidents over the following year."
        "He documented them in the same notebook."
        "He told no one."
        pause 1.0
        "Kessler transferred to a desk assignment in 1957."
        "Frank never found out why."
        "He kept the notebook anyway."

    elif nudge_1955 == "progressive":
        "The district attorney acknowledged the file existed."
        "Nothing happened for three months."
        pause 1.0
        "In January 1956, Kessler requested a transfer."
        "The transfer was approved."
        "No investigation was opened. No charges were filed."
        pause 1.0
        "Chief Harmon and Frank DeLuca worked together for six more years without either of them mentioning the conversation they had on a Friday afternoon in 1955."
        "They were professional about it."
        "The word {i}professional{/i} covers a great deal of ground in a small department."

    pause 1.5
    "What is it supposed to be for."
    pause 2.0

    jump advance_to_1967
