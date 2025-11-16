import  time
#Guesing Users Password

createdPassword = int(input("Create your ZAAD password "))
correct_password = createdPassword
print(" Now let me crack your password in seconds: watch me cook")
time.sleep(2)
#this time function will give a time to see the above print message it is not nessessary for the program
for found in range(10000):
    print(f"Cracking Your Password {found}")
    if found == correct_password:
        print(f"Found your password: {found}")
        break









