import time
username = ""
while username=="":
    username = input("What is your name?")
time.sleep(1)
print("Good Morning "+ username)
time.sleep(1)
print("Good Morning %s" %username)
time.sleep(1)
print("Good Morning {0}".format(username))
password = "shinigami"
passguess = ""
time.sleep(1)
while passguess != password:
    passguess = input("Password?")
print("Well done")

