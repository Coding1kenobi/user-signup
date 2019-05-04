from flask import Flask, request
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/register", methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']
    
    username_error = ""
    password_error = ""
    verifypassword_error = ""
    email_error = ""


    if not username:
        username_error = 'Username was left empty'
    
    if not password:
        password_error = 'password was left empty'
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Username must be between 3 and 20 characters'
    for char in password:
        if char == " ":
            password_error = 'password cannot contain spaces'    

    if password != verifypassword:
        verifypassword_error = 'passwords do not match'

    period = 0
    for char in email:
        if char == "." or char == "@":
            period += 1
    if period < 2:
        email_error = "email must be formated such as example@dothis.com"
    if period > 2:
        email_error = "email must be formated such as example@dothis.com"

    for char in email:
        if char == " ":
            email_error = "email cannot contain a space"
    
    if password_error or email_error or verifypassword_error or username_error:
        content = jinja_env.get_template('signup.html')
        return content.render(email=email,email_error=email_error,
                            username=username,username_error=username_error,password_error=password_error,
                            verifypassword_error=verifypassword_error)

    validated = jinja_env.get_template('thanks.html')
    return validated.render(name=username)

@app.route("/")
def index():
    body = jinja_env.get_template('signup.html')
    return body.render(body=body)

@app.route("/register", methods=['GET'])
def register_page():
    body = jinja_env.get_template('signup.html')
    return body.render(body=body)




app.run()