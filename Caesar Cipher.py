def encrypt(data,shift):
        en_text=''
        for i in data:
            if i in alphabet:
                index = alphabet.index(i)+shift
                index %= len(alphabet)
                en_text += alphabet[index]
            else:
                en_text+=i
        print(f"encoded text is {en_text}")

def decrypt(data,shift):
    de_text=''
    for i in data:
        if i  in alphabet:
            index=alphabet.index(i)-shift
            index %= len(alphabet)
            de_text+=alphabet[index]
        else:
            de_text+=i
    print(f"Decoded text is:{de_text}")

execute = True
while execute:
    alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction = input("enter encode or decode : ").lower()
    data = input("enter your message : ").lower()
    shift = int(input("enter the shift number : "))
     
    run =True
    while run:
        if direction == "encode":
            encrypt(data,shift)
            run=False
        elif direction=="decode":
            decrypt(data,shift)
            run = False
        else:
            print('Invalid input!! Try Again!')
            run=False
        
    
    while True:
        a=input("do you want to continue(yes or no) : ").lower()   
        if a=="yes":
            execute=True
            break
        elif a=="no":
            execute=False
            print("Thank you for using Caesar Cipher!")
            break
            
        else:
            print("invalid input try again!!!")