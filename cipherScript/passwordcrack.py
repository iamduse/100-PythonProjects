import  time
#Guesing Users Password

createdPassword = int(input("Create your ZAAD password "))
correct_password = createdPassword
print(" Now let me crack your password in seconds: watch me cook")
time.sleep(2)
for found in range(10000):
    print(f"Cracking Your Password {found}")
    if found == correct_password:
        print(f"Found your password: {found}")
        break









