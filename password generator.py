import random
print("welcome to password generator")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['@','#','!','$','%','&','*','(',')']
num_letters = int(input("enter the number of letters do you want"))
num_numbers=int(input("how many numbers do you want"))
num_symbols=int (input("how many no.of symbols do you want"))
password=[]
for i in range(0,num_letters+1):
    password.append(random.choice(letters))
for i in range(0,num_numbers+1): 
    password.append(random.choice(numbers))
for i in range(0,num_symbols+1):
    password.append(random.choice(symbols))

print(password)

random.shuffle(password)
new_password=''
for i in password:
    new_password+=i
print(new_password)
