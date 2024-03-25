import random

def password_generator(len):
    ran=['a','b','c','d','e','f','g','h','i','j','k',
            'l','m','n','o','p','q','r','s','t','u','v','w',
            'x','y','z','0','1','2','3','4','5','6','7','8','9']
    password=""
    while len > 0:
        pas=random.choice(ran)
        len-=1
        password+=pas
    return password

print()
len=int(input("Enter the length of the password : "))
print("your password of length",len,"is :\n\"",password_generator(len),"\"")
print()