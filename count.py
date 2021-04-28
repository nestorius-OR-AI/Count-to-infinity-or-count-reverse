print("<== put R if you want to count reverse == put I if you want to count to infinity ==>")

num = int(input("Put your number: "))
funcc = input("What game do you want to play: ")

def count_reverse(num):
    while num > 0:
        num -= 1
        print(num)
        if num == 0:
            print("Done. Thanks for playing")
    
def count_infinity(num):
    while num > 0 or num < 0 or num == 0:
        num += 1
        print(num)
        
if funcc == "R":
    num = num - 1
    print(count_reverse(num))
    
elif funcc == "I":
    num = num - 1
    print(count_infinity(num))

else:
    print("Wrong answer. Try again")
