words = {
    'a': [],
    'b': [],
    'c': [],
    'd': [],
    'e': [],
    'f': [],
    'g': [],
    'h': [],
    'i': [],
    'j': [],
    'k': [],
    'l': [],
    'm': [],
    'n': [],
    'o': [],
    'p': [],
    'q': [],
    'r': [],
    's': [],
    't': [],
    'u': [],
    'v': [],
    'w': [],
    'x': [],
    'y': [],
    'z': [],
}

def new_word():
    new_word = input('Type a new word: ')
    for key, value in words.items():
        if new_word.startswith(key):
            value.append(new_word)

def show_words():
    print(words)
    
    
def show_words_with_letter(letter):
    print(letter)
    for key, value in words.items():
        if key == letter:
            print(value)
            break
    
            
def run():
    global words
    
    while True:
        op = input(''' 
        [N]ew word
        [S]how words
        [W]ords with letter 
        [E]xit
        ''')
        op = op.upper()
        
        if op == 'N':
            new_word()
        elif op == 'S':
            show_words()
        elif op == 'W':
            letter = input('Which letter? ')
            show_words_with_letter(letter)
        else:
            break


if __name__ == "__main__":
    run()