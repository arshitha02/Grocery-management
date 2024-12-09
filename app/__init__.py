from flask import Flask,render_template,request,redirect,url_for,flash,jsonify,Response
from app.models.authModel import findUser
from app.models.productsModel import getItmes,reduceQnty
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
   
    grocery_items=list(getItmes())
    
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
        print(cart)
        reduceQnty(cart[:-1])
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