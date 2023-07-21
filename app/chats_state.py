import os.path
from enviroments import DATA_FILENAME


class Chats:

    def __init__(self):
        if not os.path.exists(f'./{DATA_FILENAME}'):
            open(DATA_FILENAME, 'x').close()

        self.state = open(f'./{DATA_FILENAME}', 'r').readlines()

    def _write(self):
        with open(DATA_FILENAME, 'w') as f:
            for chatId in self.state:
                f.write(f"{chatId}\n")

    def add(self, chatId):
        self.state.append(chatId)
        print(self.state)
        self._write()

    def rm(self, chatId):
        self.state.remove(chatId)
        print(self.state)
        self._write()
