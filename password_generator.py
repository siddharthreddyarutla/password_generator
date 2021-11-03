import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "#./''?{}[]()-_=+!@#$%^&*"

all = lower_case + upper_case + numbers + symbol
#here length depends on your wish
length = 10
#number of passwords also depends on your wish
#here i kept 20
for i in range(0,20):
    password = "".join(random.sample(all,length))
    print("\nThe password is: ",password)

