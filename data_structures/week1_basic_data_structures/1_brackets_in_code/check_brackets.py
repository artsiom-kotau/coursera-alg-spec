# python3
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def find_mismatch(text):
    opening_brackets_stack = []
    bracket_with_error = None
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))
        if next in ")]}":
            match = False
            if len(opening_brackets_stack) > 0:
                last_bracket = opening_brackets_stack.pop()
                last_bracket_symbol = last_bracket.char
                match = (last_bracket_symbol == '(' and next == ')') or \
                        (last_bracket_symbol == '{' and next == '}') or \
                        (last_bracket_symbol == '[' and next == ']')
            if match:
               bracket_with_error = None
            else:
                bracket_with_error = Bracket(next, i)
                break

    if not bracket_with_error and len(opening_brackets_stack) != 0:
        bracket_with_error = opening_brackets_stack.pop()

    return bracket_with_error.position+1 if bracket_with_error else -1

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == -1:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
