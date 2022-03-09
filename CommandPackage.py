import random
from data import *
from database import DataBase


class CommandPackageList:
    def __init__(self):
        self.database = DataBase()
        self.me = '/me'
        self.do = '/do'
        self.try_ = '/try'
        self.toss = '/toss'
        self.menu = '/help'
        self.n = '/n'
        self.getnick = '/getnick'
        self.print_logs = '/print_logs'
        self.delnick = '/delnick'

    def check_command(self, command_text, command):
        if command in command_text:
            return "вы не ввели действие"
        else:
            return command_text
    
    def check_nick(self, chat_id, user_id, fullname):
        if self.database.get_nick(str(chat_id), str(user_id)) == None:
            return fullname
        else:
            name = self.database.get_nick(chat_id, user_id)
            return name
    
    def command_me(self, new_message, fullname, user_id, chat_id):
        command_text = (new_message[new_message.find(" ") + 1 : ])
        me_response = (f"@id{user_id} ({self.check_nick(chat_id, user_id, fullname)})" + " " + self.check_command(command_text, "/me"))
        return me_response

    def command_do(self, new_message, fullname, user_id, chat_id):
        command_text = (new_message[new_message.find(" ") + 1 : ])
        do_response = (self.check_command(command_text, "/do") + " " + f"@id{user_id}" + " " + f"([{self.check_nick(chat_id, user_id, fullname)})]")
        return do_response
    
    def command_try(self, new_message, fullname, user_id):
        command_text = (new_message[new_message.find(" ") + 1 : ])
        try_random = random.choice(["Удачно", "Не удачно"])
        try_response = (f"@id{user_id} ({fullname})" + " " + command_text + " " + f"({try_random})")
        return try_response
    
    def command_toss(self, fullname, user_id):
        toss_random = random.choice(["Орел", "Решка"])
        toss_response = (f"@id{user_id} ({fullname})" + toss_data + f"[{toss_random}]")
        return toss_response 

    def command_n(self, new_message, fullname, user_id):
        command_text = (new_message[new_message.find(" ") + 1 : ])
        n_response = (f"{occ}" + f"({command_text})" + " " + f"@id{user_id} («{fullname}»)")
        return n_response
    
    def command_get_nickname(self, new_message, chat_id, user_id):
        command_text = (new_message[new_message.find(" ") + 1 : ])
        if self.database.check_database(chat_id,user_id) == "Есть":
            return "Такая запись есть"
        elif self.database.check_database(chat_id,user_id) == "Нет":
            self.database.create_nickname(command_text, chat_id, user_id)
        elif self.database.check_database(chat_id,user_id) == None:
            self.database.create_nickname(command_text, chat_id, user_id)

    def command_print_logs(self):
        pass


