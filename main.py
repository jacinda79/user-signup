from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

def username_val(username):
    username_error = ""
    if len(username) not in range(3, 21):
        username_error = 'Username must be between 3 and 20 characters.'
    if ' ' in username:
        username_error = "Username can't contain spaces."
    return username_error

def pass_val(password, verify):
    pass_error = ""
    if password != verify:
        pass_error = "Passwords don't match."
    if len(password) not in range(3, 21):
        pass_error = 'Passwords must be between 3 and 20 characters.'
    return pass_error

def email_val(email):
    email_error = ""
    if ' ' in email:
        email_error = "Email can't contain spaces."
    if '@' and '.' not in email and email:
        email_error = 'Email has to contain @ and .'
    return email_error

@app.route('/welcome', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email'].strip()

        username_error = username_val(username)
        pass_error = pass_val(password, verify)
        email_error = email_val(email)

        if not all(x is "" for x in (username_error, pass_error, email_error)):
            return redirect("/?username_error=" + username_error + "&pass_error=" + pass_error + "&email_error=" + email_error + "&username=" + username + "&email=" + email)

        return render_template('welcome.html', title='welcome', username=username)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.args.get("username") is None:
        username = ""
    else:
        username = request.args.get("username")
    
    if request.args.get("email") is None:
        email = ""
    else:
        email = request.args.get("email")
    
    username_error = request.args.get("username_error")
    pass_error = request.args.get("pass_error")
    email_error = request.args.get("email_error")

    return render_template('index.html', title='signup', username=username, email=email, username_error=username_error, pass_error=pass_error, email_error=email_error)

if __name__ == '__main__':
    app.run(debug=True)