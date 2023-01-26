import time

name = input("Enter A UserName...: ").lower()
if name.isalpha() == True:
    print('\nLets Begin... ' + name)
elif name.isalpha != True:
    print("invalid input")
    time.sleep(0.8)
    print("QUITTING!!!!")
    quit()

print("\nSelect one of the following:")
time.sleep(0.2)
print("1.) Calculator")
time.sleep(0.3)
print("2.) Rock Paper Scissors")
time.sleep(0.4)
print("3.) BlackJack")
time.sleep(0.5)
print("4.) Quiz Game\n")
while True:
    answr = input(name + " What Will You Pick..: ")
    if answr == "1":
        import calculator as calculator
    elif answr == "2":
        import RockPaperScissors as RockPaperScissors
    elif answr == "3":
        import BlackJack as games
    elif answr == "4":
        import QuestionGame as QuestionGame
    else:
        print("ENTER 1-4!!!")
        time.sleep(0.5)
        print("QUITTING..")
        time.sleep(0.7)
        quit()
