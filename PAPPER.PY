import sys
x=input("name")
y=input("name2")
x_answer=input("%s, do yo want to choose rock, paper or scissors?" % x)
y_answer =input("%s, do you want to choose rock, paper or scissors?" % y)
def compare(x , y):
    if x == y:
        print("It's a tie")
    elif x == 'rock':
        if y == 'scissors':
            print ("Rock wins")
        else:
            print("paper win")
    elif x == 'scissors':
        if y == 'paper':
            print("Scissors win")
        else:
            print("rocks win")
    elif x == 'paper':
        if y == 'rock':
            print("Paper wins")
        else:
            print("scissors win")
print(compare(x_answer, x_answer))
