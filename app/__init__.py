from flask import Flask,render_template,request,redirect,url_for,flash

app = Flask(__name__)
app.secret_key = 'supersecretkey' 

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    # Render the login page with a title
    if request.method == 'POST':
        print("yes")
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "admin123":
            return redirect(url_for('home'))  # Replace 'dashboard' with your post-login route
        else:
            flash("Invalid username or password. Please try again.", "danger")
            return redirect(url_for('login'))
    else:
        return render_template('login.html', title="Login Page")

@app.route('/home')#, methods=['POST'])
def home():
    grocery_items = [
    {'id': 'apple', 'name': 'Apples', 'price': 'Rs.50.00/kg', 'image': 'apple.jpg'},
    {'id': 'banana', 'name': 'Bananas', 'price': 'Rs.30.50/kg', 'image': 'banana.jpg'},
    {'id': 'bread', 'name': 'Bread', 'price': 'Rs.30.00/loaf', 'image': 'bread.jpg'},
    {'id': 'carrot', 'name': 'Carrot', 'price': 'Rs.40.00/kg', 'image': 'carrot.jpeg'},
    {'id': 'milk', 'name': 'Milk', 'price': 'Rs.50.00/liter', 'image': 'milk.jpg'},
    {'id': 'onion', 'name': 'Onions', 'price': 'Rs.35.00/kg', 'image': 'onion.jpg'},
    {'id': 'orange', 'name': 'Oranges', 'price': 'Rs.60.00/kg', 'image': 'orange.jpg'},
    {'id': 'potato', 'name': 'Potatoes', 'price': 'Rs.40.00/kg', 'image': 'potato.jpg'}
    ]


    return  render_template('home.html',title="Home page",grocery_items=grocery_items)
    # Access form data
    #username = request.form['username']
    #password = request.form['password']

    # Simple validation (replace with actual authentication)
   # if username == 'admin' and password == 'admin123':
    #    return f"Welcome, {username}!"
    #else:
