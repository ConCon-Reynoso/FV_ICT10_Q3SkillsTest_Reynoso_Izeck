from pyscript import document, display

def output(e):
    
    document.getElementById("output").innerHTML = " "

    username = document.getElementById("username").value
    password = document.getElementById("password").value

    user_length = len(username)
    pass_length = len(password)

    if user_length < 7:
        display(f"Your username is too short. Username must be at least 7 characters long. Please add at least {7 - user_length} more character/s to proceed. Try again", target='output')
    
    elif not any(char.isalpha() for char in password):
        display("Your password contains no letters. Password must contain at least one letter. Please add at least one letter to proceed. Try again.", target='output')
    
    elif not any(char.isdigit() for char in password):
        display("Your password contains no numbers. Password must contain at least one number. Please add at least one number to proceed. Try again.", target='output')
    
    elif pass_length < 10:
        display(f"Your password is too short. Password must be at least 10 characters long. Please add at least {10 - pass_length} more character/s to proceed. Try again.", target='output')
    
    else:
        display("Account created successfully!", target='output')