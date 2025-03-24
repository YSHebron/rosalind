# I want to write a program that will allow me to grab PDF text without newlines and copy it immediately to my clipboard.
# It will be running in the terminal in the background.

import pyperclip
from typing import List

counter = 0

while True:
    print(">> [%d] Enter multiline string: " % counter)

    lines: List[str] = []

    while True:
        try:
            line = input()
            if len(line) == 0 or line == "exit":
                break
        except EOFError:
            break
        lines.append(line)

    cleaned = ''.join(x.strip()+' ' for x in lines)
    pyperclip.copy(cleaned)
    
    print(">> Selection copied to clipboard.\n")
    

