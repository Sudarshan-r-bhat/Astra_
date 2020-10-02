import datetime
import os

import crayons as cr
import pyfiglet


class AstraUI:
    def __init__(self):
        self.username = ""
        self.bot_template = "BOT : {0}"
        self.user_template = "USER : {0}"

    @staticmethod
    def title():
        result = pyfiglet.figlet_format("Astra_", font="isometric1")
        print(cr.green(result))
        print(
            cr.green(
                " --------------------------------DEVELOPMENT_v1.0--------------------------------",
                bold=True,
            )
        )

    def start(self):
        timestamp = datetime.datetime.now()
        self.title()
        print(cr.green("USER: "), end="")
        self.username = str(input())
        if len(self.username) == 0:
            self.clear()
            self.start()
        self.clear()
        self.title()
        print(
            cr.green(self.user_template.format(self.username)),
            "                                       ",
            cr.green(timestamp),
        )
        print(
            cr.green(
                " --------------------------------------------------------------------------------\n",
                bold=True,
            )
        )

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "printf '\033c'")

    # def bot(self):
    # astra = Astra(self.username)
    # while True:
    #     print(cr.green('>'), end='')
    #     message = input()
    #     astra.send_message(message)

    def run(self):
        self.start()
        # self.bot()
