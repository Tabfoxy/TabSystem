
import time
import datetime


def getnowdate():
    date = datetime.datetime(1, 1, 1).now()
    fulldate = f"{date.day}-{date.month}-{date.year}"
    return fulldate

def write_logs(log):
    logs_list = []
    save_logs = open(f"{getnowdate()}.txt", "w+", encoding = "utf-8")
    logs_list.append(log)
    save_logs.write(logs_list)
    save_logs.close()

def gettime():
    gettime = time.localtime() 
    current_time = time.strftime("%H:%M:%S", gettime)
    return current_time

current_time = gettime()

# "Сервисный ключ" #
SERVICE_KEY = '8639ed9c3cd6adbbc08a5ab4cbcafc3d9094449bc8b8d9f7a5aa35f8df810f212527cf5338b7844c98a42'

# "Идентификатор сообщества" #
GROUP_ID = 210921682

# "Системные логи" #
sessioin_log = f'[{current_time}](Role Bot): Session authorized'
longpoll_log = f'[{current_time}](Role Bot): Longpoll authorized'
event_log = f'[{current_time}](Role Bot): A new event has occurred'
type_message_log = f'[{current_time}](Role Bot)(event): This event is a message'
command_me_log = f'[{current_time}](Role Bot)(event): The /me command was used\n'
command_do_log = f'[{current_time}](Role Bot)(event): The /do command was used'


def message_log(chat_id, user_id, new_message):
    message_log_return = f'[{current_time}](Role Bot)(event): Message sent to {chat_id} by {user_id}, message: {new_message}'
    return message_log_return

logs = []

# "STR DATA" #
toss_data = ' бросил монетку'
help_command = "/role - RolePlay комманды\n/add - Дополнительные комманды\n/info - Информация о боте"
occ = "Non-RP: "









