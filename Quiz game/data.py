import requests as rq
params = {
    "amount": 10,
    "type": "boolean"
}


response = rq.get(url="https://opentdb.com/api.php" , params=params)
response.raise_for_status()
data = response.json()
question_data = data["results"]
print(question_data)