import random
ctr=0
print("welcome to snake and ladder game")
#game starts
print("your current position is",ctr)
#shows current position of player
while(ctr<100):
    i=random.radiant(1,6)
    #i is no on dice's faces
    j=input("press enter to roll the dice")
    #rolls the dice
    ctr=ctr+i
    print("your current position is",ctr)
    #shows positin of player after displacing from previous position
    if ctr==8:
        ctr=37
        print("you climbed the ladder from 8 to 37")
        #player climbs the ladder
    elif ctr==11:
        ctr=2
        print("snake bit you. . :(move down to 2")
        #snake bit player at 11 ,comesback to 2
    elif ctr==25:
        ctr=4
        print("snake bit you. . :(move down to 4")
        #snake bit player at 25, comesback to 4
    elif ctr==13:
        ctr=34
        print("you climbed the ladder from 13 to 34")
        #player climbed ladder at 13,
    elif ctr==38:
        ctr=9
        print("snake bit you. . :(move down to 9")
    elif ctr==40:
        ctr=68
        print("you climbed the ladder from 40 to 68")
    elif ctr==52:
        ctr=81
        print("you climbed the ladder from 52 to 81")
    elif ctr==65:
        ctr=46
        print("snake bit you. . :(move down to 46")
    elif ctr==76:
        ctr=97
        print("you climbed the ladder from 76 to 97")
    elif ctr==89:
        ctr=70
        print("snake bit you. . :(move down to 70")
    elif ctr==93:
        ctr=64
        print("snake bit you. . :(move down to 64")
    elif ctr>=100:
        print("you won")
        
