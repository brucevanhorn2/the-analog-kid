## The Analog Kid — Period 1979
## Rev. Thomas Carver — "The Man Learning New Questions."
## Burials on both sides; Harold Blanton Jr. at 11pm.

label carver_1979_begin:

    $ current_period = 1979
    $ current_location = "first_baptist"
    $ mark_visited("first_baptist")

    scene bg_first_baptist_1979 with fade

    thought "Sixty-two years old. Eddie Briggs died in 1971 — his heart, they said. Ruth is one of my most faithful now."
    thought "Bobby Simmons came back from Vietnam. He sits in the back pew where Eddie used to sit. Some pews hold their assignments across decades."

    "The Blanton accident. Three dead. Two of them from Carver's congregation. He buries people on both sides of the tracks in the same week."

    thought "I have stood at four gravesides in seven days. North side and south side. Different faces in each crowd, and the same hole in the ground."
    thought "My faith is not what it was in 1955. The institutional comfort is gone. What's left is rawer and stronger and very hard to explain on a Sunday morning."

    jump carver_1979_harold


label carver_1979_harold:

    "At eleven o'clock at night, there is a knock on the parsonage door."
    "Harold Blanton Jr. He is not the man who donated the pews. He is that man's son, and he is crying, and he has been crying for a while."

    harold "I'm not here for absolution, Thomas. I want to be clear about that."

    carver "All right."

    harold "I knew about the violations. Not all of them. Enough. I was cutting corners to keep the place open. To keep three hundred people working."
    harold "Three of them aren't working anymore. They aren't anything anymore."

    thought "He is not a monster. That is the hardest part. He is a frightened man who made a series of survivable decisions until three of them stopped being survivable for somebody else."
    thought "There is a confession in this room. The question is what a confession is for, and who it is for, and whether it is allowed to just sit here and be one."

    $ mark_talked("harold", "first_baptist", "confession")

    jump carver_1979_explore


label carver_1979_explore:
    $ current_location = "first_baptist"
    jump explore_1955


# --- 1979 LOCATIONS ---

label location_first_baptist_1979:
    $ mark_visited("first_baptist")
    scene bg_first_baptist_1979 with dissolve
    "First Baptist. The pews Harold Blanton Sr. donated in 1947. His son wept in the study an hour ago."
    thought "I can counsel him toward a quiet, private accountability. I can tell him to go to the authorities. Or I can give him a clock and sit with him while it runs."
    return

label location_mount_zion_1979:
    $ mark_visited("mount_zion")
    scene bg_mount_zion_1979 with dissolve
    "Mount Zion. Isaiah Chambers buried one of the dead this week. Carver buried two."
    if not talked("carver", "mount_zion", "chambers_1979"):
        $ mark_talked("carver", "mount_zion", "chambers_1979")
        chambers "We keep burying them in the same weeks, Thomas. Yours and mine."
        carver "We do."
        chambers "One of these years one of us is going to bury the other. I've made my peace with which order I'd prefer."
        "It is said almost lightly. Twenty years ago they kept a respectful distance. Now they keep each other."
        thought "Isaiah and I started this decade as adversaries. We are ending it as the two oldest men who understand what the other one carries."
    return


# --- NUDGE ---

label carver_1979_nudge:

    scene bg_first_baptist_1979 with dissolve

    "Harold is still in the study. He has not moved. The clock on the mantel is the loudest thing in the room."

    thought "Three men are dead and a fourth is weeping in my study and I am the only person he trusted with it."
    thought "What I do with that trust is the whole of my ministry, compressed into one night."

    menu carver_1979_nudge_choice:

        "Counsel quiet accountability — compensation to the families, privately. Keep the confession here.":
            jump carver_nudge_conservative_1979

        "Give Harold forty-eight hours to come forward himself. Sit with him in the silence first.":
            jump carver_nudge_middle_1979

        "Tell him to go to the authorities. Testify at the inquest yourself if it comes to it.":
            jump carver_nudge_progressive_1979


label carver_nudge_conservative_1979:
    $ nudge_1979 = "conservative"
    $ policy_score -= 1
    $ harold_outcome = "protected"
    carver "Make it right with the families, Harold. Quietly. Generously. As much as it takes and then more."
    thought "The confession stays in this room. Harold pays in money and in the thing money cannot reach."
    thought "The families are compensated. No one is charged. The town does not have to look at what it lets factories do to keep the lights on."
    thought "I have kept a man's secret and called it mercy. I am not certain it was mercy. I am certain it was quiet."
    jump carver_1979_nudge_after


label carver_nudge_middle_1979:
    $ nudge_1979 = "middle"
    $ harold_outcome = "negotiated"
    "Carver does not answer right away. He sits with Harold in the study for an hour, saying nothing, the clock counting."
    carver "Forty-eight hours, Harold. You go to them yourself, or I stop being the only person who knows."
    thought "I gave him a door and a deadline and I sat in the dark with him while he found the courage to walk through it, or didn't."
    thought "This is not absolution and it is not the law. It is the narrow thing in between, where I have spent most of my best work and almost none of my comfortable hours."
    jump carver_1979_nudge_after


label carver_nudge_progressive_1979:
    $ nudge_1979 = "progressive"
    $ policy_score += 1
    $ harold_outcome = "prosecuted"
    carver "Go to the authorities, Harold. Tonight or tomorrow, but go. I'll be at the inquest. I'll say what I have to say."
    "Harold leaves. They do not speak again as friends."
    thought "I testified. I told the truth about what I knew and when I knew it. A man who trusted me with the worst night of his life watched me do it."
    thought "Three men are dead. The law is a blunt instrument and it was the only instrument that fit the size of the wrong. I picked it up."
    jump carver_1979_nudge_after


label carver_1979_nudge_after:
    scene bg_first_baptist_1979 with dissolve
    "Late. The study is empty now. The clock keeps its count over no one."
    jump carver_1979_period_end


label carver_1979_period_end:
    scene bg_first_baptist_1979 with dissolve
    "Past midnight. Carver stands at the pulpit of the empty church. Not preaching. Just standing."

    thought "I came home from two wars and into a third about the color of a carpet. The carpet stayed beige and the wars kept coming in different clothes."
    thought "Samuel Beaumont says the first half of a verse on the south side. I say the second half on the north side. We are both saying it over the same three graves this year."

    carver "Let us rejoice and be glad in it."

    scene black with dissolve
    pause 0.5
    "1979."

    if nudge_1979 == "conservative":
        "Harold Blanton Jr. compensated the families generously and was never charged."
        "The factory stayed open. The confession stayed in the study."
        pause 1.0
        "Carver carried it. He was not sure, on Sundays, whether what he had given was mercy or cover. He preached anyway."
    elif nudge_1979 == "middle":
        "Harold Blanton Jr. came forward himself, inside Carver's forty-eight hours."
        "It was not a clean reckoning. It was a real one."
        pause 1.0
        "The factory survived under real oversight. The families got accountability with a name on it. Carver sat with what it cost all of them."
    elif nudge_1979 == "progressive":
        "Harold Blanton Jr. went to the authorities. Carver testified at the inquest."
        "They never spoke as friends again."
        pause 1.0
        "Carver preached that Sunday on the cost of telling the truth. The back pews understood it. So did the empty seats where Harold's allies used to sit."

    pause 1.5
    "Lord God, thou knowest."
    pause 2.0

    jump advance_to_1991
