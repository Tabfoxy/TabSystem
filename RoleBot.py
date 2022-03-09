from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from CommandPackage import CommandPackageList
from data import *
from database import DataBase
# я хуйня а не код
class RoleBot:
    def __init__(self):
        self.session = VkApi(token = SERVICE_KEY)
        print(sessioin_log)
        self.longpoll = VkBotLongPoll(self.session, GROUP_ID)
        print(longpoll_log)
        self.commandpackage = CommandPackageList()
        self.database = DataBase()  
    
    def send_message(self, id, text):
        self.session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})
    
    def get_fullname(self, user_id):
        user = self.session.method("users.get", {"user_ids": user_id})
        fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
        return fullname
    
    def start(self):
        for event in self.longpoll.listen():
            print(event_log)
            if event.type == VkBotEventType.MESSAGE_NEW:
                print(type_message_log)
                if event.from_chat:
                    chat_id = event.chat_id
                    user_id = event.object['message']['from_id']
                    self.get_fullname(user_id)
                    new_message = event.object['message']['text'].lower()
                    print(message_log(chat_id, user_id, new_message))
                    logs.append(message_log(chat_id, user_id, new_message))
                    new_message_do = event.object['message']['text']
                    fullname = self.get_fullname(user_id)
                    if self.commandpackage.me in new_message:
                        print(command_me_log)
                        logs.append(command_me_log)
                        #write_logs(command_me_log)
                        return_me = self.commandpackage.command_me(new_message, fullname, user_id, chat_id)
                        self.send_message(chat_id, return_me)
                    
                    if self.commandpackage.do in new_message:
                        print(command_do_log)
                        logs.append(command_me_log)
                        return_do = self.commandpackage.command_do(new_message_do, fullname, user_id, chat_id)
                        self.send_message(chat_id, return_do)
                    
                    if self.commandpackage.try_ in new_message:
                        return_try = self.commandpackage.command_try(new_message, fullname, user_id)
                        self.send_message(chat_id, return_try)
                    
                    if self.commandpackage.toss in new_message:
                        return_toss = self.commandpackage.command_toss(fullname, user_id)
                        self.send_message(chat_id, return_toss)
                    
                    if self.commandpackage.menu in new_message:
                        self.send_message(chat_id, help_command)
                    
                    if self.commandpackage.n in new_message:
                        return_n = self.commandpackage.command_n(new_message, fullname, user_id)
                        self.send_message(chat_id, return_n)
                    
                    if self.commandpackage.getnick in new_message:
                        if self.database.check_database(chat_id,user_id) == "Нет":
                            self.commandpackage.command_get_nickname(new_message, chat_id, user_id)
                            self.send_message(chat_id, "Запись создана")
                        elif self.database.check_database(chat_id,user_id) == "Есть":
                            self.send_message(chat_id, "У вас уже есть ник")
                        elif self.database.check_database(chat_id,user_id) == None:
                            self.commandpackage.command_get_nickname(new_message, chat_id, user_id)
                            self.send_message(chat_id, "Запись создана")

                    if self.commandpackage.delnick in new_message:
                        self.database.delete_nickname(user_id)
                        self.send_message(chat_id, "Ник удален")

if __name__ == "__main__":
    rolebot = RoleBot()
    rolebot.start()