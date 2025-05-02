# Ask user to enter some text.

When the user enters text, it is stripped of whitespace from the
beginning and end, then it is checked to see if the length is less
than the minimum length or greater than the maximum length.

If it is not of the required length then an error message is shown.

If the text is of the required length then the function returns the
entered text.

## Pseudocode

```text
set the entered text to an empty string

while the entered text is 'blank'...

    Ask for the user to enter text
    
    Strip away whitespace from each end
    
    Check the entered text is too short
        Show an error when too short
        Make entered text blank
        
    Check the entered text is too long
        Show an error when too long
        Make entered text blank
        
return entered_text
```

## Python

```python
def ask_user_for_text():
    # set the entered text to an empty string
    entered_text = ""
    # while the entered text is 'blank'...
    while entered_text == "":
        # Ask for the user to enter text
        entered_text = input("Enter text: ")
        # Strip away whitespace from each end
        entered_text = entered_text.strip()
        # Check the entered text is too short
        #     Show an error when too short
        #     Make entered text blank
        if len(entered_text) < 5:
            print("ERROR: Text is too short, minimum 5 characters")
            entered_text=""
        # Check the entered text is too long
        #     Show an error when too long
        #     Make entered text blank
        if len(entered_text) > 50:
            print("ERROR: Text is too long, maximum 50 characters")
            entered_text=""  
            
    # return entered_text
    return entered_text
```

## Make the function more reusable

To make it more reusable we need to make the:
- prompt,
- minimum length, and
- maximum length

variables, or more precisely, parameters!

```python
def ask_user_for_text(prompt="Enter text: ",
                      minimum_length=5,
                      maximum_length=50):
    entered_text = ""
    while entered_text == "":
        entered_text = input(prompt)
        entered_text = entered_text.strip()

        if len(entered_text) < minimum_length:
            print(f"ERROR: Text is too short, minimum {minimum_length} characters")
            entered_text = ""

        if len(entered_text) > maximum_length:
            print(f"ERROR: Text is too long, maximum {maximum_length}characters")
            entered_text = ""

    return entered_text
```


## Final Python including Doc Blocks

```python
def ask_user_for_text(prompt="Enter some text: ",
                      min_length=5, max_length=50):
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
                 (default 'Enter some text: ')
    min_length : the minimum number of characters to be entered
                 (default 5)
    max_length : the maximum number of characters to be entered
                 (default 50)

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


```