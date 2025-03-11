import random

alphabates = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols= ['!','@','#','$','%','^','&','*','+','-','/']

print("Hello and welcome!!, Here you can generate your new password...\n")

n_alphabates=int(input("How many letter you want to add in the password?\n"))
n_number=int(input("How many numbers you want to add in the password?\n"))
n_symbols=int(input("How many symbols you want to add in the password?\n"))

password=""
for l in range(1,n_alphabates+1):
    characters = random.choice(alphabates)
    password = password + characters
for l in range(1,n_number+1):
    characters = random.choice(numbers)
    password = password + characters
for l in range(1,n_symbols+1):
    characters = random.choice(symbols)
    password = password + characters
print("Your new Password is: ",password)
print("If you want new password then try again...")



