import random
import string

def random_choice_from_list(phrase_list):
    index = random.randint(0, len(phrase_list) - 1)
    return phrase_list[index]

def make_list_from_file(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def make_response_dictionary(response_list):
    response_dict = {}
    for line in response_list:
        parts = line.strip().split(",", 1)
        if len(parts) == 2:
            keyword, response = parts
            response_dict[keyword] = response
    return response_dict

class ChatBot:
    def __init__(self, greetings_file, responses_file, default_response):
        self.greetings = make_list_from_file(greetings_file)
        response_lines = make_list_from_file(responses_file)
        self.keyword_and_response = make_response_dictionary(response_lines)
        self.default_response = default_response

    def greet(self):
        return random_choice_from_list(self.greetings)

    def respond(self, human_text):
        text = human_text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()

        potential_responses = []
        for word in words:
            if word in self.keyword_and_response:
                potential_responses.append(self.keyword_and_response[word])

        if not potential_responses:
            return self.default_response
        else:
            return random_choice_from_list(potential_responses)