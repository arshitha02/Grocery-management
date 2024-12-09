from app.models.database import users

def findUser(username,password):
    result = users.find_one({"username":username})
    if result is not None and result['password']==password:
        return result
    else:
        return None