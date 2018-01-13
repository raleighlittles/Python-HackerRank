def capitalize(string):
    # We can't use title() here, consider the case: "123name" -> "123Name", which isn't correct.
    for substring in string.split():
        string = string.replace(substring, substring.capitalize())
    return string   