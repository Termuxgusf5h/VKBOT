from re import S
import vk_api
import random
import sys
import datetime
import time
from pyfiglet import Figlet
from threading import Thread
import vk
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('vkbot'))

animation = "|/-\\"

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
    #do something
print("Скрипт запущен!")


def mig(id, text):
    vk_sesion.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0})

def sender(id, text):
	vk_seson.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})

while True:
    print("1. VKBOT(Для группы)")
    print("2. VKBOT(Для беседы)")
    print("3. VKBOT(ВсегдаОнлайн)")
    print("4. VKBOT(АвтоСтатус)")
    print("5. VKBOT(РЕЙД БОТ ВК)")
    print("0.")
    cmd = input('Выберите пункт:')

    if cmd =='1':
        a = input('Ваш токен->')
        r1 = input('1. Ваше сообщение->')
        r2 = input('1. Ответ бота->')
        r3 = input('2. Ваше сообщение->')
        r4 = input('2. Ответ бота->')
        r5 = input('3. Ваше сообщение->')
        r6 = input('3. Ответ бота->')
        r7 = input('4. Ваше сообщение->')
        r8 = input('4. Ответ бота->')
        r9 = input('5. Ваше сообщение->')
        r10 = input('5. Ответ бота->')
        vk_sesion = vk_api.VkApi(token = a)
        session_api = vk_sesion.get_api()
        longpoll = VkLongPoll(vk_sesion)

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:

                    msg = event.text.lower()
                    id = event.user_id

                    if msg ==r1:
                        mig(id, r2)
                    elif msg ==r3:
                        mig(id, r4)
                    elif msg ==r5:
                        mig(id, r6)
                    elif msg ==r7:
                        mig(id, r8)
                    elif msg ==r9:
                        mig(id, r10)


    if cmd == '2':
        w = input('Ваш токен->')
        rt = input('1. Ваше сообщение->')
        pomh = input('1. Ответ бота->')
        ro = input('2. Ваше сообщение->')
        rr = input('2. Ответ бота->')
        az = input('3. Ваше сообщение->')
        vf = input('3. Ответ бота->')
        pu = input('4. Ваше сообщение->')
        ylk = input('4. Ответ бота->')
        brf = input('5. Ваше сообщение->')
        tvn = input('5. Ответ бота->')
        rfsf = input('6. Ваше сообщение->')
        vvb = input('6. Ответ бота->')
        mpj = input('7. Ваше сообщение->')
        rtty = input('7. Ответ бота->')
        yyu = input('8. Ваше сообщение->')
        ttmh = input('8. Ответ бота->')
        wqeaa = input('9. Ваше сообщение->')
        ttqw = input('9. Ответ бота->')
        zasl = input('10. Ваше сообщение->')
        poill = input('10. Ответ бота->')
        vk_seson = vk_api.VkApi(token = w)
        longpoll = VkLongPoll(vk_seson)

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    if event.from_chat:

                        msg = event.text.lower()
                        id = event.chat_id

                        if msg in ['привет']:
                            sender(id, 'привет')
                        if msg in [rt]:
                            sender(id, pomh)
                        if msg in [ro]:
                            sender(id, rr)
                        if msg in [az]:
                            sender(id, vf)
                        if msg in [pu]:
                            sender(id, ylk)
                        if msg in [brf]:
                            sender(id, tvn)
                        if msg in [rfsf]:
                            sender(id, vvb)
                        if msg in [mpj]:
                            sender(id, rtty)
                        if msg in [yyu]:
                            sender(id, ttmh)
                        if msg in [wqeaa]:
                            sender(id, ttqw)
                        if msg in [zasl]:
                            sender(id, poill)
                        




    if cmd == '3':
        tok = input('Ваш токен->')
        session = vk.Session(access_token = tok)
        api = vk.API(session, v = "5.95")
        while True:
            exit = api.actokcount.setOnline(voip = 0)
            time.sleep(180)

    if cmd == '4':
        token = input('Ваш токен->')
        vki = vk_api.VkApi(token = token)

        delte = datetime.timedelta(hours=3, minutes=0)
        qw = (datetime.datetime.now(datetime.timezone.utc) + delte)

        nowtime = qw.strftime("%H:%M")
        nowdate = qw.strftime("%d.%m.%Y")

        on = vki.method("friends.getOnline")
        counted = len(on)

        vki.method("status.set", {"text": nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(counted)})

        time.sleep(30)

    if cmd == '5':
        tokk = input('Ваш токен->')
        idf = input('ID группы->')
        vk = vk_api.VkApi(token = tokk)

        vk._auth_token()

        vk.get_api()

        DEBUG = True 
        MESSAGES_DELAY = 0.05  
        START_RAID_AFTER_CERTAIN_MESSAGE = False 
        longpoll = VkBotLongPoll(vk, idf)


        def raid(chat_id):
            if DEBUG: print("New Chat:", chat_id)
            while True:
                vk.method("messages.send", {"peer_id": event.object.peer_id,
                                            "message": "dgrgd grrdg drgd gdr gdg drg drgd rg rdgdr grd gdr grg rdg dg dr gd gdr gd gdr gdr gd rgd gdr gdr gd gdrg rd gr5 yd e5 y dh h 5dh5" + str(
                                                random.randint(0, 163664527287)),
                                            "random_id": 0})
                time.sleep(MESSAGES_DELAY)


        if DEBUG: print("Bot Started")
        while True:
            for event in longpoll.listen():

                if event.type == VkBotEventType.MESSAGE_NEW:
                    if event.object.peer_id != event.object.from_id:
                        if START_RAID_AFTER_CERTAIN_MESSAGE and "start" in event.object.text:
                            th = Thread(target=raid, args=(event.object.peer_id, ))
                            th.start()
                        else:
                            th = Thread(target=raid, args=(event.object.peer_id, ))
                            th.start()
