from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) < 1 or len(sys.argv) > 3 or sys.argv[1] != "-f":
    sys.exit("Invalid Usage")
text = input("Input: ")

if len(sys.argv) < 2:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(text))
elif len(sys.argv) >= 2 and sys.argv[1] == "-f":
    f = sys.argv[2]
    figlet.setFont(font=f)
    print(figlet.renderText(text))