import requests

parameters = {
    "amount": 10,
    "category": 9,
    "difficulty": "easy",
    "type": "boolean",
}

quiz = requests.get(url="https://opentdb.com/api.php", params=parameters)
quiz.raise_for_status()
data = quiz.json()
question_data = data["results"]

