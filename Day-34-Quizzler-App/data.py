import requests

categories_true_false = {
    "General Knowledge": 9,
    "Entertainment: Music": 12,
    "Entertainment: Television": 14,
    "Entertainment: Video Games": 15,
    "Science & Nature": 17,
    "Science: Computers": 18,
    "Geography": 22,
    "History": 23,
}

categories_multiple_choice = {
    "General Knowledge": 9,
    "Entertainment: Books": 10,
    "Entertainment: Film": 11,
    "Entertainment: Music": 12,
    "Entertainment: Musicals & Theatres": 13,
    "Entertainment: Television": 14,
    "Entertainment: Video Games": 15,
    "Entertainment: Board Games": 16,
    "Entertainment: Comics": 29,
    "Entertainment: Anime & Manga": 31,
    "Entertainment: Cartoon & Animation": 32,
    "Science & Nature": 17,
    "Science: Computers": 18,
    "Science: Mathematics": 19,
    "Science: Gadgets": 30,
    "Mythology": 20,
    "Sports": 21,
    "Geography": 22,
    "History": 23,
    "Politics": 24,
    "Art": 25,
    "Celebrities": 26,
    "Animals": 27,
    "Vehicles": 28,
}

parameters = {
    "amount": 10,
    "type": "boolean",
    "difficulty": "medium",
    "category": categories_true_false["Entertainment: Video Games"],
}

responses = requests.get("https://opentdb.com/api.php", params=parameters)
responses.raise_for_status()
question_data = responses.json()["results"]
