from flask import Flask,render_template,request,redirect,url_for,flash,jsonify,Response
from app.models.authModel import findUser
from app.models.database import close_db_connection
from app.auth import create_token,token_required,set_jwt_cookie
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.secret_key = 'supersecretkey' 

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'  # Separate JWT secret key
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False  # Disable for simplicity, enable in production

jwt = JWTManager(app)

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    # Render the login page with a title
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        result = findUser(username,password)
        if result:
            token=create_token(username)
            response = redirect(url_for('home'))
            response = set_jwt_cookie(response, username,password,result['role'])
            return response 
        else:
            flash("Invalid username or password. Please try again.", "danger")
            return redirect(url_for('login'))
    else:
        return render_template('login.html', title="Login Page")

@app.route('/home')
@token_required
def home():
    grocery_items = [
    {'id': 'apple', 'name': 'Apples', 'price': '50.00/kg', 'image': 'apple.jpg', 'qnty': 10},
    {'id': 'banana', 'name': 'Bananas', 'price': '30.50/kg', 'image': 'banana.jpg', 'qnty': 15},
    {'id': 'bread', 'name': 'Bread', 'price': '30.00/loaf', 'image': 'bread.jpg', 'qnty': 20},
    {'id': 'carrot', 'name': 'Carrot', 'price': '40.00/kg', 'image': 'carrot.jpeg', 'qnty': 25},
    {'id': 'milk', 'name': 'Milk', 'price': '50.00/liter', 'image': 'milk.jpg', 'qnty': 12},
    {'id': 'onion', 'name': 'Onions', 'price': '35.00/kg', 'image': 'onion.jpg', 'qnty': 18},
    {'id': 'orange', 'name': 'Oranges', 'price': '60.00/kg', 'image': 'orange.jpg', 'qnty': 10},
    {'id': 'potato', 'name': 'Potatoes', 'price': '40.00/kg', 'image': 'potato.jpg', 'qnty': 30}
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