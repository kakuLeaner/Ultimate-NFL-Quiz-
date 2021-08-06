# #!/usr/bin/env python
# NAME: Questionaiare Generator
# AUTHOR: Kakungulu, P
# DATE: 08/6/2021
# PURPOSE: Program will assess the user knowledge about the NFL. 

lineBreak = "*"*60
print(lineBreak)

#Introduce program to the owner
userName = input('Please enter your name: \n')
print(userName, 'Welcome to the Ultimate NFL Football Quiz!')
print(lineBreak, '\n')

qn1 = """1.When was the NFL created?
a.1918
b.1922
c.1920
d.1932"""
qn2 = """2.Who won the first ever SuperBowl in 1967?
a.Tampa Bay
b.Green Bay
c.Giants
c.Browns
d.Patriots"""
qn3 = """3.Which NFL team has the most SuperBowl Losses?
a.Patriots
b.Chargers
c.Seahawks
d.Panthers"""
qn4 = """4.Name the coach with the most wins and the only NFL perfect season?
a.Don Shula
b.Bill Belichick
c.Andy Reid
d.Jimmy Johnson""" 
qn5 = """5.Who won SuperBowl X?
a.Vikings
b.Eagles
c.Chargers
d.Steelers"""
qn6 = """6.Who has the most career rushing yards?
a.Barry Sanders
b.Jim Brown
c.Emmitt Smith
d.Adrian Paterson"""
qn7 = """7.Who has the most career receiving yards?
a.Jerry Rice
b.Chad Johnson
c.Terrell Owens
d.Larry Fitzgerald Jr."""
qn8 = """8.Who has thrown the most interceptions?
a.None below
b.George Blanda
c.Jameis Winston
d.Brett Favre"""
qn9 = """9.How many officials are assigned to each game?
a.8
b.7
c.9
d.6"""
qn10 = """10.Where was the first Pro Bowl played?
a.Texas
b.New York
c.California
d.Las Vegas"""
qn11 = """11.When did the Super Bowl start using Roman numerals?
a.Super Bowl XX
b.Super Bowl V
c.Super Bowl IV
d.Super Bowl X"""
qn12 = """12.How many points were scored in the highest scoring game in NFl history?
a.113
b.111
c.115
d.110"""
qn13 = """13.Who was the first professional football player?
a.Pete Henry
b.Paddy Driscoll
c.William Heffelfinger
d.Jim Thorpe"""
qn14 = """14.How many divisions are there in the NFL?
a.8
b.6
c.10
d.9"""
qn15 = """15.How many teams in the NFL have never been to the Super Bowl?
a.7
b.5
c.6 
d.4"""

def quizFun():
    quiz = {qn1:"c", qn2:"b", qn3:"a", qn4:"a", qn5:"d", qn6:"c", qn7:"a", qn8:"d", qn9:"b", qn10:"c", qn11:"b", qn12:"a", qn13:"c", qn14:"a", qn15:"d"}
    correct = 0
    incorrect = 0
    for qn in quiz:
        print()
        print(qn)
        userAns = input('Your answer enter A,B,C,or D: \n').lower()
        while userAns != "a" and userAns != "b" and userAns != "c" and userAns != "d":
            userAns = input('Please input a,b,c, or d: ')
        if userAns == quiz[qn]:
            correct = correct+1
            print('Correct')
        else:
            incorrect += 1
            print('Wrong')
            if incorrect == 9:
                quitOpt = input('Do you want quit too hard for you "y" or "n"? ')
                while quitOpt != "y" and quitOpt != "n":
                    quitOpt = input('Please enter "y" or "n": ')
                if quitOpt == "y":
                    break
                else:
                    continue

            
    print(userName, 'You scored', correct, 'out of 15 and got',incorrect, 'wrong.')
quizFun()
while True:
    playAgain = input('Do you want to play again "y" or "n"? ')
    while playAgain != "y" and playAgain != "n":
        playAgain = input('Please enter "y" or "n": ')
    if playAgain == "y":
        quizFun()
    else:
        print('Thanks for playing!')
        break
print(lineBreak, '\n')
print('Thanks for reading my code all feedback is welcome', end ='')
print(' God Bless you and your loved ones!')
            
    

#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))
