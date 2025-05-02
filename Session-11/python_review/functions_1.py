def ask_user_for_text(prompt="Enter some text: ",
                      min_length=5, max_length=20):
    """
    Ask user to enter some text.

    When the user enters text, it is stripped of whitespace from the
    beginning and end, then it is checked to see if the length is less
    than the minimum length or greater than the maximum length.

    If it is not of the required length then an error message is shown.

    If the text is of the required length then the function returns the
    entered text.

    Parameters
    ----------
    prompt     : the text to show to the user when asking for input
                 (default 'Enter some text:')
    min_length : the minimum number of characters to be entered
                 (default 5)
    max_length : the maximum number of characters to be entered
                 (default 20)

    Returns
    -------
    string     : text of the required length


    Examples
    ________
    # Python Doct Tests cannot work with input so NO Doc Tests
    # are shown, only code examples

    player_name = ask_user_for_text("Enter your name:", 2, 25)
    guess = ask_user_for_text("Enter your guess:", 5, 5)
    print(f"{player_name} just guessed {guess}...")
    """

    entered_text = ""

    while entered_text == "":
        entered_text = input(prompt)
        entered_text = entered_text.strip()

        if len(entered_text) < min_length:
            print(f"ERROR: Minimum length is {min_length} characters")
            entered_text = ""
        elif len(entered_text) > max_length:
            print(f"ERROR: Maximum length is {max_length} characters")
            entered_text = ""

    return entered_text


player_name = ask_user_for_text("Enter your name: ", 2, 25)

guess = ask_user_for_text("Enter your guess: ", 5, 5)

print(f"{player_name} just guessed {guess}...")
