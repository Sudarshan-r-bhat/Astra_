import random
import re

import crayons as cr


class AstraBot:
    def __init__(self):
        self.username = ""
        self.bot_template = "BOT : {0}"
        self.user_template = "USER : {0}"

        self.name = "Astra"
        self.weather = "cloudy"
        self.rules = {
            "I want (.*)": [
                "What would it mean if you got {0}",
                "Why do you want {0}",
                "What's stopping you from getting {0}",
            ],
            "do you remember (.*)": [
                "Did you think I would forget {0}",
                "Why haven't you been able to forget {0}",
                "What about {0}",
                "Yes .. and?",
            ],
            "do you think (.*)": ["if {0}? Absolutely.", "No chance"],
            "if (.*)": [
                "Do you really think it's likely that {0}",
                "Do you wish that {0}",
                "What do you think about {0}",
                "Really--if {0}",
            ],
            "question": ["I don't know :(", "you tell me!", "Forget it!"],
            "default": [
                "tell me more!",
                "why do you think that?",
                "how long have you felt this way?",
                "I find that extremely interesting",
                "can you back that up?",
                "oh wow!",
                ":)",
            ],
        }

    def match_rule(self, rules, message):
        response, phrase = random.choice(rules["default"]), None

        if message.endswith("?"):
            return random.choice(self.rules["question"]), None

        for pattern, responses in rules.items():
            match = re.search(pattern, message)
            if match is not None:
                response = random.choice(responses)
                if "{0}" in response:
                    phrase = match.group(1)
        return response, phrase

    @staticmethod
    def replace_pronouns(message):
        message = str(message).lower()
        if "me" in message:
            return re.sub("me", "you", message)
        if "my" in message:
            return re.sub("my", "your", message)
        if "your" in message:
            return re.sub("your", "my", message)
        if "you" in message:
            return re.sub("you", "me", message)
        return message

    def respond(self, message):
        response, phrase = self.match_rule(self.rules, message)
        if "{0}" in response:
            phrase = self.replace_pronouns(phrase)
            response = response.format(phrase)
        return response

    def send_message(self, message):
        print(cr.magenta(self.user_template.format(message), bold=True))
        response = self.respond(message)
        print(cr.magenta(self.bot_template.format(response), bold=True))
