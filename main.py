from flask import Flask, request, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

# COMPLETE: If errors, re=render the form with feedback 
#   next to the field it refers to
# COMPLETE: Username cannot be empty
# COMPLETE: Password cannot be empty
# COMPLETE: Verified password cannot be empty
# COMPLETE: Username cannot contain space character
# COMPLETE: Password cannot contain space character
# COMPLETE: Username consists of 3-20 characters
# COMPLETE: Password consists of 3-20 characters
# COMPLETE: Password and verified password must match
# COMPLETE: Preserve what user typed for username and email even if error
# COMPLETE: Clear password and verified password if error
# COMPLETE: Show a welcome page if everything is valid "Welcome, [username]"
# COMPLETE: Use templates for index/homepage
# COMPLETE: Make email a text input
# COMPLETE: If they enter an email, must contain a single @, a single ., 
#   no spaces, and between 3 and 20 characters long.

@app.route("/", methods=['POST'])
def validate_entry():
    
    username = request.form['username']
    password = request.form['password']
    verified_password = request.form['verified_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verified_password_error = ''
    email_error = ''

    if not username:
        username_error = "Please enter a username."
    elif " " in username:
        username_error = "Username cannot contain spaces."
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters."

    if not password:
        password_error = "Please enter a password."
        password = ''
    elif " " in password:
        password_error = "Password cannot contain spaces."
        password = ''
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters."
        password = ''

    if not verified_password:
        verified_password_error = "Please re-enter your password."
        verified_password = ''
    elif verified_password != password:
        verified_password_error = "Verified password must equal password."
        verified_password = ''

    if email:
        if email.count("@") < 1 or email.count("@") > 1:
            email_error = 'Email must contain a single "@".'
        if email.count(".") < 1 or email.count(".") > 1:
            email_error = 'Email must contain a single ".".'
        if " " in email:
            email_error = "Email cannot contain spaces."
        if len(email) < 3 or len(email) > 20:
            email_error = "Email must be between 3 and 20 characters."
    
    if not username_error and not password_error and not verified_password_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('base.html', username=username, email=email, username_error=username_error, password_error=password_error, verified_password_error=verified_password_error, email_error=email_error)
    

@app.route("/")
def index():
    return render_template('base.html')

app.run()