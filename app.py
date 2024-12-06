from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render the login page with a title
    return render_template('login.html', title="Login Page")

@app.route('/home')#, methods=['POST'])
def login():
    return  render_template('home.html',title="Home page")
    # Access form data
    #username = request.form['username']
    #password = request.form['password']

    # Simple validation (replace with actual authentication)
   # if username == 'admin' and password == 'admin123':
    #    return f"Welcome, {username}!"
    #else:
     #   return "Invalid credentials, please try again."'''

if __name__ == '__main__':
    app.run(debug=True)