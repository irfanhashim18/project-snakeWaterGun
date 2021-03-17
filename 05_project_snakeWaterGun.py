import random




RandNo = random.randint(1,3)
#print(RandNo)


player1 = print("Comp has choose its value between snake(s),water(w) and gun(g)")
player2 =input("please choose a value between: snake(s),water(w) and gun(g)\n")
if RandNo == 1:
    player1= "s"
elif RandNo == 2:
    player1 = "w" 
elif RandNo == 3:
    player1 = "g"

inputtup = (player1,player2)


# tieing tuples (s,s)(w,w),(g,g)
#player1 /computer wining tuples(d,w),(g,s) and (w,g )
# player2 remaining tuples are winings

#def gameWin(player1,player2):
#    if player1 == player2:
#        return None
#    elif player 1 == 
 
if inputtup == ('s','s'):
    print("Match is A tie")
elif inputtup==('s','s'):
    print("Match is A tie")
elif inputtup ==('g','g'):
    print("Match is A tie")
elif inputtup == ('s','g'):
    print("PLAYER 2 WIN")
elif inputtup == ("g","w"):
    print("PLAYER 2 WIN") 
elif inputtup ==("w","s"):
    print("PLAYER 2 WIN")
else:
    print("player one win")
#elif inputtup == ("s","w"):
#    print ("player 1 win's")
#elif inputtup == ("g","s"):
#    print ("player 1 win's")
#elif inputtup ==("w","g"):
#    print ("player 1 win's")

    

