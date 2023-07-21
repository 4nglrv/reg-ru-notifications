import os.path
from enviroments import DATA_FILENAME
from utils import strip_file_lines


class State:
    def __init__(self):
        if not os.path.exists(f'./{DATA_FILENAME}'):
            open(DATA_FILENAME, 'x').close()

        self.chats = strip_file_lines(open(f'./{DATA_FILENAME}', 'r').readlines())

    def _write(self):
        with open(DATA_FILENAME, 'w') as f:
            for chat_id in self.chats:
                f.write(f"{chat_id}\n")

    def is_chat_exist(self, chat_id: str):
        if chat_id in self.chats:
            return True
        else:
            return False

    def add(self, chat_id: str):
        if chat_id in self.chats:
            return

        self.chats.append(chat_id)
        self._write()
        print('Added new chat_id:\n', self.chats)

    def rm(self, chat_id: str):
        if not chat_id in self.chats:
            return

        self.chats.remove(chat_id)
        self._write()
        print('Removed chat_id:\n', self.chats)
