import random
rnum = random.randint (1000, 9999)
print (rnum)
#guesses vriable
guesses = 5

strnum = str (rnum)
rnumlist = []
guesslist = []
for digit in strnum:
    rnumlist.append (int(digit))
print (rnumlist)

usersuccess=["-","-","-","-"]
print usersuccess
if indexguess==indexrando:


#nothing for now
while guesses != 0:
    userinput1 = input ("Enter 4 numbers: ")

    for digit in userinput1 :
        guesslist.append(int(digit))
    if guesslist == rnumlist:
        print("correct")
        guesses = 0

    else:
        for i in rnumlist:
            for j in guesslist:
                if i == j :
                    if rnumlist.index(i) == guesslist.index(j):

                        print (usersuccess)
                else:
                    print ("incorrect")
    guesslist.clear()
