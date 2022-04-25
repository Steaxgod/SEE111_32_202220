def display_seat_map(aA, aB, aC, aD):
    for r in range (1, 8):
        print("   ", r,  " ", aA[r]," ", aB[r], "   ", aC[r], " ", aD[r])



def askUserRow()
    r = int(input("What row to you want to sit in? "))
    return r

def askUserSeat()
    s = input("What seat to you want to sit in? ")
    return s

ef check_seat(r, s, aA, aB, aC, aD):
    f = 0
    if(s == "A" and aA[r] != "A"):
        f = -1
    elif(s == "B" and aB[r] != "B"):
        f = -1
    elif(s == "C" and aC[r] != "C"):
        f = -1
    elif(s == "D" and aD[r] != "D"):
        f = -1

    return f



aisleA = ["","A","A","A","A","A","A","A"]
aisleB = ["","B","B","B","B","B","B","B"]
aisleC = ["","C","C","C","C","C","C","C"]
aisleD = ["","D","D","D","D","D","D","D"]

display_seat_map(row, seat, aisleA, aisleB, aisleC, aisleD)

row = askUserRow()
seat = askUserSeat()

if (
