## The Analog Kid — Period 1967
## June Holloway — "The Woman Progress Left Behind."
## The community-development vote; the highway; the forty families.

label june_1967_begin:

    $ current_period = 1967
    $ current_location = "city_hall"
    $ mark_visited("city_hall")

    scene bg_city_hall_1967 with fade

    thought "Forty-six years old. Twelve years on the council. Two re-elections. Two other women in the chamber now — my most durable achievement, and the one nobody writes about."

    "The progress has been real. Housing ordinances. School boundary adjustments. Procurement policies that opened south-side businesses to city contracts."
    "The progress has been real and the pace has been glacial, and June has stopped pretending those two things cancel out."

    "On the table: federal funding for a south-side community development project. She has the votes. Almost."
    "One of them — an alderman — will only support it if June publicly backs his highway project."
    "The highway routes a new road through the south side. It displaces forty families."

    thought "Forty families for a clinic, a nutrition program, a paved street that floods less. A net positive. The arithmetic is defensible."
    thought "I have learned to be suspicious of every sentence I can say that contains the phrase net positive."

    jump june_1967_explore


label june_1967_explore:
    $ current_location = "city_hall"
    jump explore_1955


# --- 1967 LOCATIONS ---

label location_city_hall_1967_june:
    $ mark_visited("city_hall")
    scene bg_city_hall_1967 with dissolve
    "The council chamber. The seal older than the building. Her chair, third from the left."
    if not talked("june", "city_hall", "alderman_1967"):
        $ mark_talked("june", "city_hall", "alderman_1967")
        "The alderman with the highway project finds her before the session. He is not cruel. He is transactional, which in a small town is a kind of honesty."
        townsperson "Back my road, Councilwoman, and your development money sails through. Simple as that."
        june "Nothing in this building has ever been as simple as that."
        thought "He believes it is simple because the forty families are not names to him. They are a line item on a route map."
    return

label location_south_side_street_1967:
    $ mark_visited("south_side_entry")
    scene bg_south_side_street_1967 with dissolve
    "The south-side residential block the highway would take. June does not visit here often. She is aware that this is itself the problem."
    if not talked("june", "south_side_street", "families_1967"):
        $ mark_talked("june", "south_side_street", "families_1967")
        $ june_south_side_trust = june_south_side_trust + 1
        "Forty houses. Specific porches. A swing set. A man repairing a fence who nods at her without knowing who she is, which is its own kind of information."
        thought "On the route map they are a corridor. From this sidewalk they are forty front doors."
        thought "Ray Coldwater knows about this road. He has been waiting, I think, to see which kind of councilwoman I turn out to be. So have I."
    return

label location_holloway_derrick_1967:
    $ mark_visited("holloway_derrick")
    scene bg_holloway_derrick_1967 with dissolve
    "The Holloway derrick. Quieter than it was in 1955. The pump jack still moves, slower, in its long arc."
    "Her father is older. He has not said anything about the oil. Neither has she."
    thought "He financed my first campaign and called it an investment. He has never once asked for a return I could see coming. That is its own kind of debt, and I have been paying it in increments for twelve years."
    return


# --- NUDGE ---

label june_1967_nudge:

    scene bg_city_hall_1967 with dissolve

    "The vote is Thursday. The development money and the highway are, the alderman has made certain, the same vote now."

    thought "Three ways to cast it. Each one is a version of the word progress, and I said that word in every room in this county to get this chair."

    menu june_1967_nudge_choice:

        "Take the deal. The highway goes through. Forty families move. The money comes.":
            jump june_nudge_conservative_1967

        "Find the third way. Reroute the highway to spare most of the families." if june_south_side_trust >= 1:
            jump june_nudge_middle_1967

        "Refuse the deal. Lose the vote. Keep your conscience whole and your hands empty.":
            jump june_nudge_progressive_1967


label june_nudge_conservative_1967:
    $ nudge_1967 = "conservative"
    $ policy_score -= 1
    "June takes the vote. The development project is funded. The highway goes through. Forty families receive relocation notices in the spring."
    thought "A clinic will be built. Children I will never meet will be healthier for it. That is true."
    thought "Forty families will tell their grandchildren about the year the city decided their street was a corridor. That is also true."
    thought "I told myself this is how governing works. I am sitting with what it means that the sentence comes so easily."
    jump june_1967_nudge_after


label june_nudge_middle_1967:
    $ nudge_1967 = "middle"
    $ june_south_side_trust = june_south_side_trust + 1
    "June does the thing twelve years of relationships make possible. She reroutes the highway — a longer, costlier path that spares all but six of the families."
    "She makes the longer route cheaper to the alderman than her opposition would be. It is not generosity. It is leverage, applied precisely."
    if geri_samuel_connection or True:
        thought "Geri Habicht's displacement data told me which blocks would absorb a move and which would be devastated by it. I rerouted around the devastation."
    thought "Six families still move. I do not get to feel clean. I get to feel that I made it as small as a person in my chair could make it. Some nights that is enough. Some nights it isn't."
    jump june_1967_nudge_after


label june_nudge_progressive_1967:
    $ nudge_1967 = "progressive"
    $ policy_score += 2
    "June refuses the deal. The highway dies. So does the development money, on the same vote, by the same hand."
    thought "Forty families keep their street. A clinic that would have served thousands does not get built."
    thought "I kept my conscience and lost the outcome. I have argued both sides of whether that was courage or vanity, and I have not won the argument against myself."
    "Her father calls at six-fifteen. The conversation is careful. It is always careful when he is most serious."
    jump june_1967_nudge_after


label june_1967_nudge_after:
    scene bg_city_hall_1967 with dissolve
    "Evening. The chamber is empty. The seal catches the last light through the high windows."
    jump june_1967_period_end


label june_1967_period_end:
    scene bg_city_hall_1967 with dissolve
    "Evening. She is still at the long table, in the chair that is third from the left."

    thought "Progress. I meant it every time I said it. On the north side they heard roads and schools. On the south side they heard somebody is finally listening."
    thought "Twelve years in this chair has taught me that those two sentences are not the same sentence, and that my whole career has been the cost of pretending they were."

    "She has a clipping somewhere — first woman on the council, above the fold, 1955. Her father kept it. She keeps thinking about the word she ran on and what it bought."

    scene black with dissolve
    pause 0.5
    "1967."

    if nudge_1967 == "conservative":
        "Councilwoman Holloway took the vote. The clinic was funded. The highway went through."
        "Forty families received notices in the spring."
        pause 1.0
        "The clinic opened in 1969. It was good. June drove past the empty corridor where the houses had been and did not slow down."
    elif nudge_1967 == "middle":
        "Councilwoman Holloway found the third way and rerouted the road."
        "Six families moved instead of forty. The clinic was funded anyway."
        pause 1.0
        "Nobody thanked her, because the thing she prevented left no evidence. She had learned long ago that the best work in governing is invisible by design."
    elif nudge_1967 == "progressive":
        "Councilwoman Holloway refused the deal and lost the vote."
        "Forty families kept their street. The clinic was not built."
        pause 1.0
        "She paid for it with her father, with the alderman, with a year of the council's patience. She was never entirely sure she had been right. She was entirely sure she could not have done otherwise."

    pause 1.5
    "The clock on City Hall was still running. She made herself believe that meant something."
    pause 2.0

    jump advance_to_1979
