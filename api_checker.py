import requests
import json

url = 'http://127.0.0.1:8000/api/StudentApi/'


def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = url,data=json_data)
    data = r.json()
    print(data)
    
    
# get_data()        

def post_data():
    data = {
        'name':'SinghKumari',
        'RollNo':13,
        'city':'alwar'
    }
    json_data = json.dumps(data)
    r = requests.post(url = url,data=json_data)
    data = r.json()
    print(data)
    
# post_data()



def update_data():
    data = {
        'id':1,
        'name':'Ravi',
        'city':'khajauli',
        'RollNo':101,  
    }
    
    json_data = json.dumps(data)
    r = requests.put(url=url,data=json_data)
    data = r.json()
    print(data)
    
# update_data() 
    
    
def delete_data(id):
    data = {
        'id': id
    }
  
    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    data = r.json()
    print(data)  
    
    
delete_data(5)    