def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string