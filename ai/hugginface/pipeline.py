from transformers import pipeline


def sentiment():
    classifier = pipeline("sentiment-analysis")
    classif = classifier("I love marshmallow, especially in winter")

    return classif


def zerohot():
    classifier = pipeline("zero-shot-classification")
    text = """
Takaichi, who took office in October after being elected leader of the governing Liberal Democratic Party (LDP), surpassed the 310 seats needed for a supermajority in the 465-seat lower house, Japanese public broadcaster NHK reported from the official election count on Sunday evening. The supermajority allows her ruling coalition to override the upper house, where it lacks a majority.

An NHK exit poll as voting ended earlier on Sunday projected the LDP would win between 274 and 326 seats. The party and its coalition partner Ishin were projected to win a combined 302-366 seats, as voters turned out amid freezing temperatures in a rare winter election.

The far-right Sanseito party, which promises to put “Japanese first,” was projected to take up to 14 seats, according to the exit poll, which would quadruple its numbers but fall short of the 30 seats it had targeted.

Speaking from LDP headquarters as the results came in, Takaichi said her party’s coalition with Ishin would continue, adding that she would place importance on fiscal sustainability and had no plans for a major cabinet reshuffle.

In Japanese tradition, a candidate’s victory is marked with a paper flower. The scale of the win was visible on a board behind Takaichi filled with red paper roses for LDP candidates.
"""
    classif = classifier(
        text,
        candidate_labels=["education", "politics", "business", "gambling"],
    )
    return classif


if __name__ == "__main__":
    print(zerohot())
