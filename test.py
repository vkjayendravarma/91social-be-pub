from flask import json

try:
    import unittest
    from src import app

except Exception as e:
    print(e)


class FlaskTest(unittest.TestCase):

    id = ""
    ## tests subjects to antrctica region
    test_shop = {
        "name": "test_shop",
        "latitude": "-73.659745",
        "longitude": "20.566404"
    }

    # health check

    def test_health(self):
        tester = app.test_client(self)
        response = tester.get("/healthcheck")
        self.assertEqual(response.status_code, 200)

    # Functionality test
    def test_test_flow(self):
        tester = app.test_client(self)
        response = tester.post("/shops/create", data=json.dumps(self.test_shop), headers={'Content-Type': 'application/json'})
        result = json.loads(response.data)
        id = result['shop']["_id"]["$oid"]
        print("<<<<<< ID >>>>>>>", id)
        self.assertEqual(response.status_code, 200)
        
        # test update of same shop
        self.test_shop["name"] = "test_shop_update"
        url = str("/shops/update?id=" + id) 
        response = tester.put(url, data=json.dumps(self.test_shop), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        
        # get the updated shop
        response = tester.get("/shops/search?query=id&id="+id)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        name = result['data']["name"]
        self.assertEqual(name, "test_shop_update")
    
        # search for shop with 1 km range
        response = tester.get("/shops/search?query=range&range=1&latitude=-73.659745&longitude=20.566404")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        shops = result['data']
        self.assertGreater(len(shops), 0)
        
        # search for shop with 1 km range fail
        response = tester.get("/shops/search?query=range&range=1&latitude=-74.659745&longitude=20.566404")
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        shops = result['data']
        self.assertEqual(len(shops), 0)
        
        # delete shop
        url = str("/shops/delete?id=" + id) 
        response = tester.delete(url)
        self.assertEqual(response.status_code, 200)
        
        # check delete
        response = tester.get("/shops/search?query=id&id="+id)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        data = result['data']
        self.assertEqual(data, None)

if __name__ == "__main__":
    unittest.main()
