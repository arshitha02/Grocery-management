# auth.py
from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt_identity,get_jwt
from datetime import timedelta
from functools import wraps
from flask import request, jsonify, make_response

def create_token(username):
    """
    Create a JWT token for the user with an expiration time of 1 hour.
    """
    access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
    return access_token

def token_required(f):
    """
    Custom decorator to require a valid JWT token in cookies.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            # Manually verify the JWT token from the cookies
            verify_jwt_in_request()
            username = get_jwt_identity();
            claims = get_jwt()
      
        except Exception as e:
            return jsonify({'message': 'Invalid token: ' + str(e)}), 401
        
        return f(*args, **kwargs)

    return decorated

def set_jwt_cookie(response, username,password,role):
    """
    Set JWT token in an HTTP-only cookie
    """
    print("role = ",role)
    # Create access token
    access_token = create_access_token(
        identity=username,  # Primary identity remains username
        additional_claims={
            'username': username,
            'password': password,
            'role':role  # Caution: storing password in token is generally not recommended
        }
    )
    
    # Set cookie in the response
    response.set_cookie(
        'access_token_cookie', 
        access_token, 
        httponly=True,  # Prevents JavaScript access
        secure=False,   # Allow HTTP (change to True in production)
        samesite='Lax', # More permissive for HTTP
        max_age=3600    # 1 hour expiration
    )
    
    return response