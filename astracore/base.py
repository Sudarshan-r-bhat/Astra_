from astracore.bot import AstraBot
from astracore.ui import AstraUI

app = AstraUI()
bot = AstraBot()
 
 
class Astra:
    def __init__(self):
        self.message = ""

    def create_app(self):
        app.start()
        while self.message != "bye":
            self.message = str(input())
            bot.send_message(self.message)
