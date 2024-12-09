from flask import Flask,render_template,request,redirect,url_for,flash,jsonify
from app.models.authModel import findUser
from app.models.database import close_db_connection

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
        if findUser(username,password):
            return redirect(url_for('home'))  
        else:
            flash("Invalid username or password. Please try again.", "danger")
            return redirect(url_for('login'))
    else:
        return render_template('login.html', title="Login Page")

@app.route('/home')
def home():
    grocery_items = [
    {'id': 'apple', 'name': 'Apples', 'price': '50.00/kg', 'image': 'apple.jpg'},
    {'id': 'banana', 'name': 'Bananas', 'price': '30.50/kg', 'image': 'banana.jpg'},
    {'id': 'bread', 'name': 'Bread', 'price': '30.00/loaf', 'image': 'bread.jpg'},
    {'id': 'carrot', 'name': 'Carrot', 'price': '40.00/kg', 'image': 'carrot.jpeg'},
    {'id': 'milk', 'name': 'Milk', 'price': '50.00/liter', 'image': 'milk.jpg'},
    {'id': 'onion', 'name': 'Onions', 'price': '35.00/kg', 'image': 'onion.jpg'},
    {'id': 'orange', 'name': 'Oranges', 'price': '60.00/kg', 'image': 'orange.jpg'},
    {'id': 'potato', 'name': 'Potatoes', 'price': '40.00/kg', 'image': 'potato.jpg'}
    ]


    return  render_template('home.html',title="Home page",grocery_items=grocery_items)
    # Access form data
    #username = request.form['username']
    #password = request.form['password']

    # Simple validation (replace with actual authentication)
   # if username == 'admin' and password == 'admin123':
    #    return f"Welcome, {username}!"
    #else:


@app.route('/checkout', methods=['POST'])
def checkout():
    try:
        # Retrieve the cart data from the POST request
        cart = request.json.get('cart', [])
        
        # Ensure cart data is valid
        if not cart:
            return jsonify({'error': 'Cart is empty or invalid!'}), 400

        # Pass the cart data to the template for display
        return render_template('checkout.html', title="Checkout Page", cart=cart)

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': str(e)}), 500



'''@app.route('/product',method=['GET','POST'])
def product():




    return render_template('product.html', title="Product Page")


@app.route('/about')
def about():
    return render_template('about.html', title="About Page")



@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Page")

@'''