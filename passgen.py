import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
x = input('Account info : ')
passlen = int(input('Password lengath : '))
random.seed(x)
p =  "".join(random.sample(s,passlen ))
print (p)