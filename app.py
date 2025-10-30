from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to CI/CD Automated Flask App!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_info = {'username': 'admin', 'password': '1234'}
    message = ""
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if user == login_info['username'] and pwd == login_info['password']:
            message = "Login Successful!"
        else:
            message = "Invalid Credentials, Try Again."
    return render_template('login.html', login_info=login_info, message=message)

if __name__ == '__main__':
    app.run(debug=True)

