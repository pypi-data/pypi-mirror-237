from blessings import Terminal

term = Terminal()

print(term.cyan + term.on_green + 'Red on green? Ick!' + term.normal)
print(term.on_cyan(term.underline(term.magenta('I can barely see it.'))))

def add_one(number):
    return number + 1
    
    # print term.bright_red + term.on_bright_blue + 'This is even worse!' + term.normal