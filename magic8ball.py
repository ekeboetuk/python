# %%
import random as rnd
#answer = int(input("Ask magic 8 ball a question >> "))
answer = rnd.randint(1,15)
if answer == 1:
    print(str(answer) + ": It is certain. \nThe end!")
elif answer == 2:
    print(str(answer) + ": Outlook good. \nThe end!")
elif answer == 3:
    print(str(answer) + ": You may rely on it. \nThe end!")
elif answer == 4:
    print(str(answer) + ": Ask again later. \nThe end!")
elif answer == 5:
    print(str(answer) + ": Concentrate and ask again. \nThe end!")
elif answer == 6:
    print(str(answer) + ": Reply hazy, try again. \nThe end!")
elif answer == 7:
    print (str(answer) + ": My reply is no. \nThe end!")
elif answer == 8:
    print (str(answer) + ": My sources say no. \nThe end!")
elif answer > 8:
    answer = answer-8
    print("You are " + str(answer) + " values above maximum ball number,")
    print("Please try again!")
else:
    print(str(answer) + ": Invalid entry")
    print("Please try again!")


# %%
