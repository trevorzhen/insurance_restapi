##################################### Option 1 ######################################

#Excute following command in CMD
#curl -i -H "Content-Type: application/json" -X POST --data "{ \"Age\": 29, \"BMI\": 22, \"Sex\": 1, \"Children\": 3, \"Smoker\": 1, \"Region\": 4 }" http://127.0.0.1:1080/predict

#################################### Option 2 ######################################

#Post + Body + json in Postman

#################################### Option 3 ######################################
import requests

url = 'http://127.0.0.1:1080/predict'  # localhost and the defined port + endpoint
body = {
    "Age":29,
    "BMI":22,
    "Sex":0,
    "Children":3,
    "Smoker":1,
    "Region":2
}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(url, data=body)
response.json()