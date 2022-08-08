import requests


class Question:

    def __init__(self):
        r = requests.get("https://opentdb.com/api.php?amount=1&type=boolean")
        r = r.json()['results'][0]

        self.text = r['question']\
            .replace('&quot;', '\'')\
            .replace('&#039;', '\'')
        self.answer = r['correct_answer'].lower()
