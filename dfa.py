states = []
language = []
transitions = {}
start_state = ''
accept_states = []
w = ''

print("Please Enter State of DFA (Enter without input to continue)")
while True:
    new_state = input("\t: ")
    if (new_state == ''):
        if len(states) == 0:
            print('!--Please enter at least one state--!')
            continue
        else:
            break
    elif (new_state in states):
        print('Duplicate states, Please try again')
    else:
        states.append(new_state)

print("\nPlease Enter Character in The Language of DFA (Enter without input to continue)")
while True:
    new_char = input("\t: ")
    if (new_char == ''):
        if len(language) == 0:
            print('!--Please enter at least one char--!')
            continue
        else:
            break
    elif (new_char in language):
        print('Duplicate character, Please try again')
    else:
        language.append(new_char)

for state in states:
    transitions[state] = {}
    for ch in language:
        transitions[state][ch] = None

print("\nNow Program will ask you what a transition function of eash state look like")
for state in transitions:
    print("\tState", state)
    for ch in transitions[state]:
        while True:
            destination_state = input(
                f'\t  When input(w) is "{ch}" what is destination state of this function: ')
            if destination_state not in states:
                print('\t  Your answer is not state in this DFA, Please try again')
                continue
            else:
                transitions[state][ch] = destination_state
                break

while(True):
    new_state = input("\nPlease Enter start state: ")
    if new_state == '':
        print("Please Enter at least one state")
    elif new_state not in states:
        print("Your answer is not state in this DFA, Please try again")
    else:
        start_state = new_state
        break

print("\nPlease Enter Accept State of DFA (Enter without input to continue)")
while True:
    new_state = input("\t: ")
    if (new_state == ''):
        if len(accept_states) == 0:
            print('!--Please enter at least one state--!')
            continue
        else:
            break
    elif new_state not in states:
        print("Your answer is not state in this DFA, Please try again")
    elif (new_state in accept_states):
        print('Duplicate states, Please try again')
    else:
        accept_states.append(new_state)


def print_table():
    char_maxlen = 0
    state_name_maxlen = 0

    for ch in language:
        char_maxlen = max(len(ch), char_maxlen)
    for state in states:
        state_name_maxlen = max(len(state), state_name_maxlen)

    table_char_width = max(state_name_maxlen, char_maxlen)
    print()
    print("!------- Transitions table -------!")

    print(f"+-{'-'*table_char_width}-+", end='')
    for ch in language:
        print(f"-{'-'*table_char_width}-+", end='')
    print()

    print(f"| {' '*table_char_width} |", end='')
    for ch in language:
        print(f" {ch.center(table_char_width, ' ')} |", end='')
    print()

    print(f"+-{'-'*table_char_width}-+", end='')
    for ch in language:
        print(f"-{'-'*table_char_width}-+", end='')
    print()

    for state in transitions:
        print(f"| {state.center(table_char_width, ' ')} |", end='')
        for ch in transitions[state]:
            print(
                f" {transitions[state][ch].center(table_char_width, ' ')} |", end='')
        print()

    print(f"+-{'-'*table_char_width}-+", end='')
    for ch in language:
        print(f"-{'-'*table_char_width}-+", end='')
    print()


print_table()

current_state = start_state

while True:
    pass_flag = True
    w = input('Please Enter Input String(w): ')
    for ch in w:
        if ch not in language:
            pass_flag = False
            print('Invalid input, Please try again')
            break
    if pass_flag:
        break

for ch in w:
    current_state = transitions[current_state][ch]

if current_state in accept_states:
    print('ACCEPT')
else:
    print('REJECT')
