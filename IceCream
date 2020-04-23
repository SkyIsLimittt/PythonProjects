import random
import sys
import os


try:
    o = open("money820583205820.txt","x+")
except:
    o = open("money820583205820.txt","a+")


o1 = open("money820583205820.txt", "r")
k = o1.read()


class begin():
    
  
    print("Hey, welcome to my stupid little game to test your chances!")
    print("""You're a gambling addict who is pretty stupid. You want some
     really expensive ice cream of $10000, good luck with gambling!""")
    print("Ok, do you want to begin? (s for the ice cream shop) (y/n/s)")
    a = input()
    i = a.lower()
    if i == "n" :
        print("Ok so why did you come?")
        sys.exit()
    elif i == "s":
        print("""Mario: "Hey, hey, hey welcome to my shop, do you finally have the money?""")
        input()
        if int(k) < 10000:
            print("You stinky gambler, gamble some more!")
            input()
        elif int(k) >= 10000:
            print("Here is your yummy ice cream well done!")
            sys.exit()
    elif i != "y":
        print("No, no, no, little guy, follow the instructions y or n, no other instructions allowed!")
        sys.exit()

file_path = 'money820583205820.txt'
 
def empty():
    if os.path.getsize(file_path) == 0:
        print("Since you are really broke, the bank gave you a loan of $10")
        n = open("money820583205820.txt", "w")
        n.write("10")
        print(f"How much money do you want to bet? Your current balance = $10")
    elif os.path.getsize(file_path) > 0 :
        print(f"How much money do you want to bet? Your current balance = ${k}")

empty()
l = input()
if int(l) > int(k):
    print(f"Nope, you dont have so much money you can only bet ${k} or lower than ${k}")
    sys.exit()
else:
    print(f"Okay, you have bet ${l}, lets start the game!")

i = 0

while(1):
    m = random.randrange(0, 40)
    print(m)
    print("So what do you think, the value will be next time? Higher or Lower")
    h_1 = input()
    m1 = random.randrange(0, 40)
    write = open("money820583205820.txt", "w+")
    sumof = int(k) + int(l) * int(i) 

    
    if m < m1 and h_1 == "higher":
        print(f"Congratioulations, you won!! Your balance will raise with ${l}")
        i += 1
    elif m > m1 and h_1 == "lower":
        print(f"Congratioulations, you won!! Your balance will raise with ${l}")
        i += 1
    else: 
        print(f"Ohhhh, you lost {l} of your balance.")
        i -= 1
        sys.exit()
    write.write(str(sumof))
