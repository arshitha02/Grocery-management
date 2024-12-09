from app.models.database import items

def getItmes():
    result = items.find()
    if result is not None :
        return result
    else:
        return {}

def reduceQnty(cart):
    for item in cart:
        print(item)
        result=items.find_one({'name':item['name']})
        if result:
            new_quantity = result['qnty'] - item['quantity']
            if new_quantity < 0:
                new_quantity = 0  # Ensure quantity doesn't go below zero
            items.update_one({'name': item['name']}, {'$set': {'qnty': new_quantity}})