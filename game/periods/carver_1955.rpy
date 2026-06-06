## The Analog Kid — Reverend Thomas Carver, 1955 Thread
## Copyright (C) 2025 Blue Moon Foundry Software
## Licensed under the GNU Affero General Public License v3.0 (AGPL-3.0)
## https://www.gnu.org/licenses/agpl-3.0.html


# ---------------------------------------------------------------------------
# CARVER 1955 — ENTRY
# ---------------------------------------------------------------------------

label carver_1955_begin:

    $ current_period = 1955
    $ current_location = "first_baptist"
    $ mark_visited("first_baptist")

    scene bg_first_baptist_1955 with fade
    # play music "audio/music/1955_morning_church.ogg" fadein 2.0

    thought "Tuesday morning. The furnace is out again."
    thought "I've been here since six-thirty trying to fix it with a wrench and the Psalms."
    thought "The wrench is helping more."

    "The sanctuary is empty this hour. The light comes through the east windows at a low angle and makes the pews look like they mean something."
    "They are pine pews. They were donated by Harold Blanton Sr. in 1947."
    "Carver has been the pastor here for six years. He is aware of the difference between what the pews mean and who paid for them."

    thought "Thirty-eight years old. Korean vet. Former sergeant, 1st Cavalry, Pacific before that."
    thought "I came home from one war and walked into another one about the color of the new carpet."
    thought "The carpet stayed beige."

    "He sets the wrench down. He is standing near the back of the church when he hears the door."

    scene bg_first_baptist_1955 with dissolve

    "Ruth Briggs."
    "She comes in the way she has been coming in for three months — like she is not sure if she is interrupting something, and like she would come in anyway."

    ruth "Pastor Carver. I'm sorry. I saw the light."

    carver "Come in, Ruth."

    "She does. She sits in the third pew from the front — her pew, the one Eddie used to sit in beside her."
    "She is still wearing her coat."

    thought "She went to the post office again this morning. I can tell by the hour."
    thought "There is nothing at the post office for her. She knows there is nothing at the post office."
    thought "She goes anyway."

    carver "How is he?"

    "Ruth folds her hands in her lap. She has been folding her hands in her lap since September."

    ruth "He's home."

    carver "I know he's home."

    "A pause. She looks at her hands."

    ruth "He doesn't sleep. He sits in the kitchen at three in the morning and I can hear him breathing."
    ruth "I get up. He tells me to go back to bed. I go back to bed."
    ruth "In the morning the ashtray is full."

    thought "Eddie Briggs. Twenty-nine years old. Seventy-eighth Infantry, Korea."
    thought "He came home in March. He came to church twice."
    thought "The second time he sat in the back row and left before the final hymn."
    thought "That was in May. It is now October."

    carver "Has he spoken to Dr. Halliday?"

    "Ruth shakes her head."

    ruth "He says he doesn't need a doctor."

    carver "Men who don't need doctors say that."

    "Ruth almost smiles. Almost."

    ruth "Pastor. The VFW Hall."

    "A beat."

    ruth "He goes there Tuesday and Thursday. He doesn't — he's not causing trouble. He just sits."
    ruth "I don't know what I'm asking you to do about it. I don't know that I'm asking you to do anything."

    thought "She is asking me to do something."
    thought "She came here before eight in the morning to ask me."

    carver "I hear you, Ruth."

    "He does hear her. The question is what he is going to do with what he hears."

    jump carver_1955_explore


# ---------------------------------------------------------------------------
# CARVER 1955 — EXPLORE
# ---------------------------------------------------------------------------

label carver_1955_explore:

    $ current_location = "first_baptist"
    call show_nav_bar
    scene bg_first_baptist_1955 with dissolve

    "The morning moves the way mornings in October move — slowly and then all at once."

    if not talked("harold", "first_baptist", "board"):
        "Harold Blanton Sr. is not here yet. He comes to the church office on Tuesdays."
        "He always comes on Tuesdays."
        thought "I have twenty minutes before he arrives to tell me about the gutters."

    if not seen("vfw_hall"):
        thought "I know where the VFW Hall is. I've walked past it a hundred times."
        thought "I have never walked in."

    jump explore_1955


# ---------------------------------------------------------------------------
# LOCATION: FIRST BAPTIST CHURCH (1955)
# ---------------------------------------------------------------------------

label location_first_baptist_1955:

    $ mark_visited("first_baptist")
    $ current_location = "first_baptist"
    call show_nav_bar
    scene bg_first_baptist_1955 with dissolve

    if not talked("harold", "first_baptist", "board"):
        jump carver_harold_board_meeting

    "The sanctuary. The pine pews. Harold Blanton's donation."
    "The furnace is still not entirely fixed."

    thought "This is my church."
    thought "I say that the way a man says a thing he has to keep deciding is true."

    if not seen("vfw_hall") and not talked("harold", "first_baptist", "board"):
        thought "I have a sermon to write. I have a leaking roof to quote."
        thought "I have a man sitting at the end of a bar twice a week who used to sit in the third pew."
    elif seen("vfw_hall") and not talked("harold", "first_baptist", "board"):
        thought "I've been to the VFW Hall now."
        thought "I know what I know."

    return


label carver_harold_board_meeting:

    $ mark_talked("harold", "first_baptist", "board")

    "Harold Blanton Sr. arrives at ten past nine."
    "He is a large man who moves like he owns the room — which he partially does, in the sense that he donated the pews and underwriters the roof fund."

    harold "Thomas."

    "It is not disrespect, exactly. Harold Blanton has called every pastor of this church by his first name since 1938."

    carver "Harold. Come in."

    "They sit in the pastor's study. A small room off the narthex. Two chairs, a desk, a window that looks onto the side yard."

    harold "Board meeting Wednesday."
    harold "I've got the Briggs situation on the agenda."

    thought "I knew he would."

    carver "What situation is that?"

    harold "Ruth's been coming here before eight in the morning. She was here again today — I passed her on the sidewalk."
    harold "Eddie's not showing up. Whatever's going on with him, the congregation is going to notice if the pastor is making house calls to the VFW Hall."

    carver "I haven't made any house calls to the VFW Hall."

    harold "I'm saying if you were thinking about it."

    "A pause. Harold leans back. He is not a cruel man. He is a man who has organized his world around certain principles and defends them with the energy of someone who has never had to question whether the principles were built for him."

    harold "These boys who come back — some of them handle it and some of them don't."
    harold "That's the truth of it. Eddie went, which is more than some others did."
    harold "But a man who can't come home needs to deal with that privately. Not have the church following him around."
    harold "We've got the denomination's veterans ministry. There's a pamphlet. An address in Tulsa."

    carver "I know about the pamphlet."

    harold "Then use it. That's what it's there for."
    harold "The board's concern — my concern — is that if you make this a public thing, a pulpit thing, we're going to have problems."
    harold "People in this congregation gave sons to that war. Not everybody came home with the same troubles."
    harold "It's not helpful to suggest the ones who are struggling did something wrong or the ones who are fine did something right."

    thought "He's not wrong about that part."
    thought "He is wrong about the answer."
    thought "Or maybe he's right about the answer and I'm the one who's wrong."
    thought "Or maybe the question isn't one answer."

    carver "I appreciate you coming in, Harold."

    harold "Wednesday. Seven o'clock."

    "He leaves."

    "Carver sits in the study for a moment."
    "The side yard window looks onto a maple. The maple is going yellow."

    thought "Denomination's veterans ministry."
    thought "A pamphlet. An address in Tulsa."
    thought "I sent two men from this congregation to that address in the last four years."
    thought "One of them wrote back. The other one I don't know about."

    return


# ---------------------------------------------------------------------------
# LOCATION: VFW HALL (1955)
# ---------------------------------------------------------------------------

label location_vfw_hall_1955:

    $ mark_visited("vfw_hall")
    $ current_location = "vfw_hall"
    call show_nav_bar
    scene bg_vfw_hall_1955 with dissolve

    if talked("eddie", "vfw_hall", "carver_visit"):
        "The VFW Hall. Evening."
        "The same arrangement as before — the bar, the light, the jukebox not playing anything."
        thought "I was here already."
        thought "What I did with it — that's done now."
        return

    "Tuesday evening. The VFW Hall on Wilmont Street."
    "Carver has never been inside. It is exactly what he expected and different from what he expected."
    "Dark wood. A bar along one wall. A jukebox that is not playing anything."
    "Three men at a table in the back playing cards."
    "One man at the end of the bar."

    thought "Eddie Briggs."
    thought "He looks like he always looked. Korea didn't take anything from him you can see."
    thought "That's the problem with the kind of wound he has."

    "Carver does not wear his collar tonight."
    "He is wearing the gray jacket he wore on weekends before he was ordained, the one he has kept in the back of the closet for reasons he hasn't examined."

    "He sits down two stools from Eddie."

    "The bartender looks at Carver. Carver orders a ginger ale. The bartender brings it without comment."

    "A few minutes pass."

    eddie "Pastor."

    "Not surprise. Eddie Briggs has recognized him and decided not to pretend he hasn't."

    carver "Eddie."

    "Another minute."

    eddie "You're not going to tell me I should be in church."

    carver "I'm not here about church."

    "Eddie looks at him from the corner of his eye."

    eddie "Then what are you here about?"

    thought "The Pacific. 1944. The way a beach looks when there are men on it who are no longer moving."
    thought "The smell. The weight of a rifle when you've been carrying it for sixteen hours."
    thought "I have not talked about this in nine years."

    carver "I was in the Pacific. Forty-four, forty-five. Leyte."

    "Silence."

    carver "I came home in forty-six. I didn't talk about it for two years."

    "Eddie stares at his glass."

    carver "Didn't sleep much either."

    "A long pause. The card game murmurs in the background."

    eddie "It's not the same thing."

    carver "No. It wasn't the same war."

    eddie "I mean — I know men who had it worse. Chosin."

    carver "I know men who had it worse too. That's not a competition."

    "Eddie picks up his glass. Sets it back down without drinking."

    eddie "Ruth thinks I need to talk to somebody."

    carver "Ruth's right."

    eddie "You're not going to suggest that Tulsa address."

    thought "He knows about the Tulsa address."
    thought "He's been given the pamphlet."

    carver "Not tonight."

    "Eddie almost laughs. It doesn't quite make it all the way to his face."

    "They sit for a few more minutes. Carver finishes the ginger ale. The jukebox stays quiet."

    carver "I know a doctor on the south side. Samuel Beaumont."
    carver "He's not a — he's a physician. He's also a vet. He came home from Korea too."
    carver "I could put you in touch."

    "Eddie is quiet."

    eddie "South side doctor."

    carver "Good one."

    "Another pause."

    eddie "I'll think about it."

    "Carver stands. He puts two dollars on the bar for the ginger ale and the stool."

    carver "I'm not going to tell you what to do, Eddie."
    carver "I'm going to tell you I'll be here. Not the church. Me."
    carver "You know where the church is. You know where I am."

    "He walks out."
    "The night air is cold. October."

    thought "That is either the beginning of something or it's nothing."
    thought "I can't tell yet."
    thought "I told Harold I hadn't been to the VFW Hall."
    thought "I hadn't, when I said it."

    $ mark_talked("eddie", "vfw_hall", "carver_visit")

    return


# ---------------------------------------------------------------------------
# CARVER 1955 — NUDGE
# ---------------------------------------------------------------------------

label carver_1955_nudge:

    scene bg_first_baptist_1955 with dissolve

    "Wednesday morning. Board meeting tonight."
    "Carver is in the study. The denomination's veterans ministry pamphlet is on the desk."
    "It has been on the desk since October 1952, when he ordered a supply of them from Tulsa."
    "He has given out four. He has kept one."

    thought "Ruth came by again this morning."
    thought "She didn't ask me anything. She sat in the third pew for twenty minutes and then left."
    thought "I watched her go."

    if seen("vfw_hall") and talked("eddie", "vfw_hall", "carver_visit"):
        thought "I've already been to the VFW Hall. I know what Eddie looks like at ten o'clock on a Tuesday."
        thought "The question is what I do with that."

    thought "The board meets at seven."
    thought "Harold Blanton is going to ask me what I've done about the Briggs situation."
    thought "I need to have an answer."

    menu carver_1955_nudge_choice:

        ## CONSERVATIVE
        "Fill out the referral form. Give it to Ruth. Let the denomination handle it.":
            jump carver_nudge_private

        ## MIDDLE — available always (Carver has already identified Samuel in the VFW scene;
        ## if player skipped VFW Hall, he knows Samuel by reputation)
        "Go to the VFW Hall on Tuesday. Don't wear the collar. Reach out to Samuel Beaumont.":
            jump carver_nudge_samuel

        ## PROGRESSIVE
        "Write the sermon. Say from the pulpit what the board won't say in private.":
            jump carver_nudge_public


label carver_nudge_private:

    $ eddie_outcome = "private"
    $ policy_score -= 1
    $ nudge_1955 = "conservative"

    "He fills out the referral form. It is two pages. The second page has a line for the referring pastor's signature."
    "He signs it."

    thought "This is the correct thing to do. The denomination built this resource for exactly this situation."
    thought "Eddie is not my patient. He is my congregant. There is a difference."
    thought "The difference is that I am leaving this to a pamphlet and an address in Tulsa."

    "He puts the form in an envelope. He writes Ruth's name on it."
    "He sets it on the corner of the desk."

    carver "Lord."

    "He says it quietly. The study is empty."

    carver "I don't know if this is right. I know it's the shape of right. I know it follows the correct form."

    "He closes his eyes."

    thought "I will give Ruth this envelope on Sunday."
    thought "I will pray for Eddie in this study every morning until I hear something."
    thought "I will not go to the VFW Hall."
    thought "The board will not have cause for complaint."
    thought "Eddie Briggs will receive a pamphlet."
    thought "This will be enough, or it will not be enough, and I will not know which for a long time."

    "He picks up the envelope. He puts it in the desk drawer."
    "He does not pray for the next twenty minutes. He sits at the desk with his hands folded and lets the silence do what silence does."

    jump carver_1955_nudge_after


label carver_nudge_samuel:

    $ eddie_outcome = "samuel"
    $ carver_samuel_connection = True
    $ nudge_1955 = "middle"

    "He does not wear the collar."
    "He wears the gray jacket and he goes on Tuesday evening."

    "He sits with Eddie for an hour. He does not talk about God. He talks about the beach at Leyte."
    "Eddie does not say much. He does not need to, exactly. He listens."

    "When Carver stands to leave he says what he says."

    carver "I know a doctor on the south side. His name is Samuel Beaumont. He was in Korea."

    "Eddie looks up."

    carver "I'm not going to tell you what to do. I'm telling you he's there."

    "Eddie nods. One nod."

    "Outside, Carver walks three blocks before he stops."

    thought "I told Harold I hadn't been to the VFW Hall."
    thought "I hadn't, when I said it. I have now."
    thought "The board meets tonight."
    thought "I am going to walk into that meeting and say that I've provided appropriate pastoral guidance."
    thought "That is true. It is also not the whole truth."
    thought "I have decided that is a price I can carry."

    "The following Thursday, Carver goes to the post office to mail a letter."
    "Ruth is there. She is not there for anything practical."
    "They nod at each other. She has been crying, or is about to."

    ruth "He said he might call someone."

    "Carver doesn't ask who. He knows who."

    carver "Good."

    thought "Samuel Beaumont is a physician. He is also a man who understands what war does to a man's sleep."
    thought "I have never had a real conversation with him."
    thought "I know him by reputation — the south side doctor who trained at Howard, who filed those hospital privilege requests."
    thought "We share a theology that lands in different rooms."
    thought "Maybe someday we'll talk about it."

    jump carver_1955_nudge_after


label carver_nudge_public:

    $ eddie_outcome = "public"
    $ policy_score += 1
    $ nudge_1955 = "progressive"

    "Sunday morning."
    "He stands at the pulpit."

    "Ruth is in the third row. Three other women — he knows their names, he married two of their children — are in the third row too."
    "Harold Blanton Sr. is in the fifth row. His arms are crossed."

    "Carver's sermon is not about Eddie Briggs."
    "He does not mention Eddie Briggs."
    "He talks about Ezekiel — the valley of dry bones. The question the Lord puts to the prophet."
    "{i}Can these bones live?{/i}"
    "And Ezekiel says: {i}Lord God, thou knowest.{/i}"

    carver "Ezekiel doesn't say yes. He doesn't say no."
    carver "He says: I don't know, but you do."
    carver "That is a different kind of faith than certainty."
    carver "It is harder. It requires you to look at the bones."
    carver "There are men in this town who came home from a war and nobody asked them what the bones looked like."
    carver "We gave them a pamphlet."
    carver "I'm not sure that's what the church is for."

    "He sees Harold's face change."
    "He keeps going."

    carver "The bones were very dry. That is what the text says."
    carver "It doesn't say they were too dry."

    "After the service, Ruth is standing by the door."
    "She is not crying. She looks like she has been not crying for most of the sermon."

    thought "I don't know if that helped Eddie."
    thought "It may have helped Ruth."
    thought "It has not helped me with the board."

    "The board meets Wednesday."
    "Harold Blanton Sr. is in the room when Carver arrives."
    "He is not alone."

    harold "Thomas."

    carver "Harold."

    "A beat."

    harold "That was quite a sermon."

    carver "I thought it was appropriate."

    harold "The denomination has a veterans ministry."

    carver "I mentioned that."

    "A silence."

    harold "I'm going to ask you directly: are you suggesting the church has been handling this wrong?"

    thought "Yes. But not only this."

    carver "I'm suggesting we could do more."

    "Harold looks at him."

    harold "We'll discuss it Wednesday."

    "They discuss it Wednesday."
    "It goes the way Carver expected."
    "He has said what he needed to say and will now spend the next several months in conversations about the color of the carpet."

    jump carver_1955_nudge_after


label carver_1955_nudge_after:

    scene bg_first_baptist_1955 with dissolve

    "Late October. The maple in the side yard is mostly bare."

    thought "Eddie Briggs is still sitting at the end of that bar."
    thought "Or he isn't. I don't know for certain."
    thought "What I know is what I did about it."

    jump carver_1955_period_end


# ---------------------------------------------------------------------------
# PERIOD END — CARVER 1955
# ---------------------------------------------------------------------------

label carver_1955_period_end:

    scene bg_first_baptist_1955 with dissolve
    # stop music fadeout 2.0
    # play music "audio/music/1955_evening.ogg" fadein 2.0

    "Evening. The sanctuary is empty."
    "The furnace has been fixed — a man from the congregation named Bert came by on Thursday with the right wrench."
    "It is warm now. The pews hold their color in the lamp light."

    "Carver is at the pulpit. Not preaching. Just standing."
    "He does this sometimes when the church is empty."

    thought "Fifty-one years old."
    thought "I have been the pastor of this church for six years."
    thought "Before that I was a sergeant in two wars and then a man with a gray jacket who didn't talk about it."
    thought "I came to the church because I needed something that wasn't the army."
    thought "I am still figuring out if I found it."

    "The wind in the maple outside. The furnace ticking."

    "He is alone the way a man is alone when he has made a decision that can't be unmade and doesn't know yet if it was right."

    "On the pulpit: his Bible. He has been preaching from it for six years."
    "The cover is not worn. He replaced it when he took the call here."
    "The pages are worn."

    "He opens it. Not to anything. Just opens it the way you open something when you need it to have an answer."

    "Ezekiel 37. The valley."

    thought "Can these bones live."
    thought "It's not a question in the Hebrew. It's a question in the translation."
    thought "In the original it's more like: these bones — can they live."
    thought "The difference is subtle."
    thought "The difference is everything."

    "He closes the Bible."

    carver "Lord God, thou knowest."

    "He says it quietly. Not as defeat. Not as faith, exactly."
    "The way you say something that is the truest thing you have, even when the truest thing you have is: I don't know."

    ## Period summary
    scene black with dissolve
    pause 0.5

    "1955."

    if eddie_outcome == "private":
        "Ruth Briggs received an envelope on Sunday morning."
        "She read the pamphlet. She sent a letter to Tulsa."
        pause 1.0
        "Six weeks later a reply arrived."
        "She put it on the kitchen table. She said nothing to Eddie."
        "He picked it up and read it."
        pause 1.0
        "What happened after that, Carver did not learn for twelve years."

    elif eddie_outcome == "samuel":
        "Three weeks later, Eddie Briggs called a number Carver had written on the back of a church bulletin."
        "A south side physician. Dr. Samuel Beaumont."
        pause 1.0
        "They met on a Tuesday afternoon."
        "It was not a cure. Nothing was a cure."
        "But it was something."
        pause 1.0
        "Carver didn't know any of this until much later."
        "Ruth stopped going to the post office in November."

    elif eddie_outcome == "public":
        "The board met on Wednesday."
        "The conversation lasted two hours."
        "Harold Blanton Sr. called it inappropriate. Two other board members agreed."
        pause 1.0
        "A fourth board member — a woman named Helen, whose son had come home from Korea in 1952 and had not spoken about it since — said nothing during the meeting."
        "Afterward, in the parking lot, she told Carver she was glad he said it."
        pause 1.0
        "Eddie Briggs did not come back to church."
        "But Ruth brought him the bulletin. Every week."

    pause 1.5
    "Lord God, thou knowest."
    pause 2.0

    jump advance_to_1967
