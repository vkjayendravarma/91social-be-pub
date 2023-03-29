from src import app
from flask import request
from flask_api import status
from src.models import Shop
from flask_mongoengine import mongoengine

@app.route('/shops/create', methods=['POST'])
def register():
    req = request.get_json()
    try:
        name = req['name']
        latitude = float(req['latitude'])
        longitude = float(req['longitude'])
    except KeyError:
        return {
            'success': False,
            'message': 'missing fields'
        }, status.HTTP_400_BAD_REQUEST

    newShop = Shop.Shop(name= name, coordinates = [latitude, longitude]).save()

    return {
        'success': True,
        'shop': newShop
    }, status.HTTP_200_OK


@app.route('/shops/update', methods=['PUT'])
def update():
    req = request.get_json()
    try:
        id = request.args.get("id")
        name = req['name']
        latitude = float(req['latitude'])
        longitude = float(req['longitude'])
    except KeyError:
        return {
            'success': False,
            'message': 'missing fields'
        }, status.HTTP_400_BAD_REQUEST

    updateShop = Shop.Shop.objects(id=id).first()
    updateShop.update(name= name, coordinates = [latitude, longitude])
    return {
        'success': True,
        'shop': updateShop
    }, status.HTTP_200_OK

    
@app.route('/shops/search', methods=['GET'])
def search():
    req = request.args
    findShops = []
    try:
        query = req["query"]
        if (query == 'all'):
            findShops = Shop.Shop.objects()
        elif (query == "id"):
            findShops = Shop.Shop.objects(id=req['id']).first()
        else:
            range = req['range']
            latitude = float(req['latitude'])
            longitude = float(req['longitude'])
            userLocation = {"type": "Point", "coordinates": [latitude, longitude]}
            findShops = Shop.Shop.objects(coordinates__near=userLocation,coordinates__max_distance=int(range)*1000)
    except KeyError:
        return {
            'success': False,
            'message': 'missing fields'
        }, status.HTTP_400_BAD_REQUEST
    
    return {
        'success': True,
        'data': findShops
    }, status.HTTP_200_OK
    


@app.route('/shops/delete', methods=['DELETE'])
def delete_shop():
    try:
        id = request.args.get("id")
    except KeyError:
        return {
            'success': False,
            'message': 'missing fields'
        }, status.HTTP_400_BAD_REQUEST

    updateShop = Shop.Shop.objects(id=id).first()
    updateShop.delete()
    return {
        'success': True,
        'shop': updateShop
    }, status.HTTP_200_OK