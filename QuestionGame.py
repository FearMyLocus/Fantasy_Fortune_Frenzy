import time

wrong = 0
score = 0

print('''
           _       _ 
 ___  _ _ <_>.___ | |
/ . || | || | / / |_/
\_  |`___||_|/___ <_>
  |_|  by @FearMyLocus                    
''')

print("\n\nQuestion Game...\n")
print("you will get 10 questions and get a score\n")

answr1 = input("1.): what is 10 x 10..: ")
if answr1 != "100":
    wrong += 1
elif answr1 == "100":
    score += 1

answr2 = input("2.): Who Was The President(Enter LastName)..: ").lower()
if answr2 != "washington":
    wrong += 1
elif answr2 == "washington":
    score += 1

answr3 = input("\n3.): what year did the United States go to the moon..: ")
if answr3 != "1969":
    wrong += 1
elif answr3 == "1969":
    score += 1

answr4 = input("4.): what is (7 x 7) / 2?...:  ")
if answr4 != "25.5" or "25":
    wrong += 1
elif answr4 == "25.5" or "25":
    score += 1

print("\n5.): How Many Star Are On The U.S Flag? ")
time.sleep(0.5)
print("\na.) 50")
time.sleep(0.4)
print("b.) 55")
time.sleep(0.3)
print("c.) 45")
time.sleep(0.2)
print("d.) 51")
answr5 = input("...: ").lower()
if answr5 != "a":
    wrong += 1
elif answr5 == "a":
    score += 1
time.sleep(0.6)
print('''\n6.): what programming language was used to make this...: )

a.) Golang
b.) Javascript
c.) Python
d.) C++''')
answr6 = input("...: ").lower()
if answr6 != "c":
    wrong += 1
elif answr6 == "c":
    score += 1

time.sleep(.05)
answr7 = input("\n7.): What Company Made IPhone...: ").lower()
if answr7 != "apple":
    wrong += 1
elif answr7 == "apple":
    score += 1

time.sleep(.05)
answr8 = input("8.): what animal says 'woof woof'...: ").lower()
if answr8 != "dog":
    wrong += 1
elif answr8 == "dog":
    score += 1

time.sleep(0.5)
answr9 = input("9.): Who Made This Quiz...: ").lower()
if answr9 != "fearmylocus":
    wrong += 1
elif answr9 == "fearmylocus":
    score += 1

print("\n10.): What Does 'NSA' Stand For...: ")
time.sleep(0.8)
print('''
a.) National Storage Affiliates Trust
b.) National Security Agency
c.) National Softball Association 
d.) Network SoftWare Architecture
''')
answr10 = input("...: ")
if answr10 != "b":
    wrong += 1
elif answr10 == "b":
    score += 1
print("\nCongrats...")
time.sleep(0.8)
print("\nYou Have Completed The Quiz")
bonus = input('''would you like a bonus question or just your results...?
Type "bonus" for extra credit or "skip" for your results...: ''').lower()
if bonus.isalpha() == True:
    if bonus.lower() == "skip":
        print("\n\nyou got ", score, " right and ", wrong, " wrong out of 10")
        time.sleep(0.5)
    if bonus.lower() == "bonus":
        print(
            "\n*BONUS*: Name a word thats four letters long, ends in u-n-t and is used to refer to some women? "
        )
    bonusOne = input("...: ").lower()
    if bonusOne == "aunt":
        print("correct")
        score += 1
    elif bonusOne != "aunt":
        print("incorrect")
        wrong += 1
    else:
        print("invalid input")
        time.sleep(0.5)
        quit()
    print("\n\nyou got ", score, " right and ", wrong, " wrong out of 10")
    quit()
