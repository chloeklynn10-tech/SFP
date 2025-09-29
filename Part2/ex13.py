# TODO:
# Create a function called check_string that takes one string argument
# If the string starts with the letters "The", return "Found it!"
# Otherwise, return "Nope."

# Insert your code here
# def ...
def check_string(str):
    if str.startswith('The'):
        print("found it!")
    else:
        print("nope.")


# Test cases
str1 = 'The'
str2 = 'Thumbs up'
str3 = 'Theatre can be boring'

(check_string(str1))   
(check_string(str2))   
(check_string(str3))    