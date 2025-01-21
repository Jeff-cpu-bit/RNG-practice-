#Jeffrey Hahner
#PVU249
#11362452
#CMPT 140 (1)
import random #imports random 
import string #imports lowercase characters 
start_pass = ""
pass_attempt = ""
failed_pass = False

def gen_pass(length): #makes the password
    letters = string.ascii_lowercase #makes sure password is only lowercase
    start_pass = ""  
    while len(start_pass) < length: #adds to string and loops until its 10 
        start_pass += random.choice(letters)  
    return start_pass
start_pass = gen_pass(10)# sets variable
#print(start_pass) #testing to see if pass gets gen in console

def setup(): # sets starting values
    global start_pass
    size(500,500)
    fill(255)
    textSize(20)
    

def draw():
    global pass_attempt, failed_pass
    fill(255)
    background(0)
    text("Your New Password Is: " + start_pass, 5, 30)
    rect(5, 40, 110,30) 
    fill(0)
    text(pass_attempt, 5, 60)
    if len(pass_attempt) == len(start_pass): #only compares when len is = 
        if pass_attempt != start_pass:
            failed_pass = True  # toggles fail message
            pass_attempt = ""  # reset pass_attempt
        else:
            print("Accepted Password") # prints to console
            exit() # exits program
    if failed_pass: # what to do if passwords dont match
        fill(255, 0, 0)
        text("Ah Ah Ah, You Didn't Say The Magic Word", 5, 90) # very funny jurassic park refrence 

def keyPressed():#allows input and backspaces
    global pass_attempt
    if key == BACKSPACE:
        pass_attempt = pass_attempt[0:-1]
    else:
        pass_attempt = pass_attempt + key
