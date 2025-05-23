FILENAME = "scores.txt"

name = None
score = None


def get_name():
    """
    Get a name from the user

    The name is a string or !q or !quit

    Returns
    -------
    string
    """
    the_name = ""
    while the_name.lower() == "":
        the_name = input("Name (!q or !quit to stop):")
    return the_name


def get_score():
    """
    Get a score from the user

    The score is a numeric value or !q or !quit

    Returns
    -------
    int|string
    """
    the_score = ""
    while the_score == "":
        the_score = input("Score (!q or !quit to stop):")
        try:
            the_score = int(the_score)
        except ValueError :
            if the_score not in  ['!q', "!quit"]:
                print("Score needs to be a number, or !q or !quit")

    return the_score


scores = []

# While name and score are not !q or !quit,
#   Ask the user for a name and a score
#   add the name and score to a list
while name not in ['!q', "!quit"] and score not in ['!q', "!quit"]:
    name = get_name()
    if name not in  ['!q', "!quit"]:
        score = get_score()
        if name not in ['!q', "!quit"] and score not in ['!q', "!quit"]:
            scores.append((name,score))


# Write the scores to a file in the format:
#   name, score
#
score_file = open(FILENAME,"w")
for score in scores:
    a_score = score[1]
    a_name = score[0]
    score_file.write(f"{a_name}, {a_score}\n")

score_file.close()
