# a simple rock paper and scissors game

permitted = ["rock", "paper", "scissors"]
p1 = input("what is your name? ")
p2 = input("and yours? ")
def begin():
    a = input("%s, What do you choose rock, paper or scissors?" %p1)
    b = input("%s, and you - rock, paper or scissors?" %p2)
    def compare(a,b):
        if a == b:
            print("it is a draw")
        elif a == "rock":
            if b == "paper":
                print("%s won" %p2)
            elif b == "scissors":
                print("%s won" %p1)
        elif a == "paper":
            if b == "rock":
                print("%s won" %p1)
            elif b == "scissors":
                print("%s won" %p2)
        elif a == "scissors":
            if b == "rock":
                print("%s won" %p2)
            elif b == "paper":
                print("%s won" %p1)

    if a in permitted and b in permitted:
        compare(a,b)

        if input("wanna play again? yes/no ")=="yes":
            begin()
    else:
        print()
        print("please type correctly this time")
        begin()
        
begin()




    