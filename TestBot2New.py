import requests
import mysql.connector
import json
import datetime
import time

url = "https://api.telegram.org/bot693890599:AAGbF6y6BFJGBgVJLNIGjnmxKfXzxJeKKnY/"

time_start =  1583660700

time_frozen = 1583704800

time_finish = 1583704800

keyboard_admin = json.dumps({'keyboard':[['Вопросы'], ['Сообщение участникам'], ['Зарегистрированные команды']],'resize_keyboard': True })
keyboard_admin_message = json.dumps({'keyboard':[['Все пользователи'], ['Все зарегистрированные пользователи'], ['Все пользователи в игре'], ['Назад']],'resize_keyboard': True })
keyboard_admin_send = json.dumps({'keyboard':[['Назад']],'resize_keyboard': True })

keyboard_user_not_reg = json.dumps({'keyboard':[['Создать команду', 'Присоединиться к команде'],['Задать вопрос'],['О боте']],'resize_keyboard': True })
keyboard_user_reg = json.dumps({'keyboard':[['Начать игру'],['Информация о команде', 'Покинуть команду'],['Задать вопрос'],['О боте']],'resize_keyboard': True })
keyboard_user_capitan = json.dumps({'keyboard':[['Начать игру'],['Информация о команде', 'Удалить команду'],['Задать вопрос'],['О боте']],'resize_keyboard': True })
keyboard_cancel = json.dumps({'keyboard':[['В главное меню']],'resize_keyboard': True })
keyboard_delete_team = json.dumps({'keyboard':[['Да','Нет']],'resize_keyboard': True })
keyboard_user_registration = json.dumps({'keyboard':[['Назад','В главное меню']],'resize_keyboard': True })
keyboard_user_registration_team_number = json.dumps({'keyboard':[['2', '3', '4'],['Назад','В главное меню']],'resize_keyboard': True })
keyboard_user_registration_accept_team = json.dumps({'keyboard':[['Да', 'Исправить'], ['Назад','В главное меню']],'resize_keyboard': True })
keyboard_default = json.dumps({'remove_keyboard': True })
keyboard_phone = json.dumps({'keyboard':[[{'text': 'Отправить свой номер', 'request_contact': True}], ['Назад']],'resize_keyboard': True })

button_results = {'text': 'Текущие результаты', 'url': 'http://energy-storm.com.ua/results'}
keyboard_results = json.dumps({'inline_keyboard': [[button_results]]})

keyboard_game = json.dumps({'keyboard':[['1', '2', '3', '4', '5'], ['6', '7', '8', '9', '10'], ['11', '12', '13', '14', '15'], ['16', '17', '18', '19', '20'],
                                        ['Задать вопрос']],'resize_keyboard': True })
keyboard_game_question = json.dumps({'keyboard':[['К списку вопросов']],'resize_keyboard': True })

game_keyboard = ['1', '2', '3', '4', '5']
game_keyboard2 = ['6', '7', '8', '9', '10']
game_keyboard3 = ['11', '12', '13', '14', '15']
game_keyboard4 = ['16', '17', '18', '19', '20']

questions = ['Столица Швеции - ... ? Формат ответа - слово кириллицей с заглавной буквы.',
             '2*3+5/5*4+1 = ... ? Формат ответа - число.',
             'Фамилия главного героя романа "Идиот". Формат ответа - слово кириллицей с заклавной буквы.',
             'Название последнего студийного альбома группы The Beatles. Формат ответа - предложение латиницей маленькими буквами.',
             'Единица измерения количества вещества в системе СИ. Формат ответа - слово кириллицей маленькими буквами.',
             'Фамилия футболиста, обладателя Золотого Мяча 1962 года. Формат ответа - слово кириллицей с заглавной буквы.',
             'Имя и фамилия физика, открывшего явление дифракции рентгеновских лучей на кристаллах. Формат ответа - три слова киллицей маленькими буквами.',
             'Фамилия второго чемпиона мира по шахматам. Формат ответа - слово кириллицей с заглавной буквы.',
             'Год начала Второй мировой войны. Формат ответа - число.',
             'Физическое явление, проявляющееся в резком увеличении амплитуды стационарных колебаний при совпадении частоты внешнего воздествия с собственными частотами системы. Формат ответа - слово кириллицей маленькими буквами.',
             'Фамилия обладателя премии Оскар за лучшую мужскую роль второго плана 1984 года. Формат ответа - слово кириллицей с большой буквы.',
             'Высокоуровневый язык программирования, на котором был написан данный бот. Формат ответа - слово латиницей с большой буквы.',
             'Музыкальный интервал шириной в пять ступеней. Формат ответа - слово кириллицей маленькими буквами.',
             'Луч, исходящий из вершины угла и делящий улог на два равных. Формат ответа - слово кириллицей маленькими буквами.',
             'Кроссплатформенный месседжер, в котором размещен данный бот. Формат ответа - слово латиницей маленькими буквами.',
             'Жаргонное прозвище, данное испанскими националистами советскому истребителю И-16 во время Гражданской войны в Испании. Формат ответа - слово латиницей маленькими буквами.',
             'Значение производной от постоянной функции в любой точке. Формат ответа - число.',
             'Псевдоним писателя, имя которого носил Харьковский университет с 1936 по 1999 год. Формат ответа - слово кириллицей с заглавной буквы.',
             'Струнно-смычковый инструмент, струны которого в классическом строе настроены на квинту ниже скрипичных. Формат ответа - слово кириллицей маленькими буквами.',
             '1-0= ...?'
             ]
answers = ['Стокгольм',
           '11',
           'Мышкин',
           'let it be',
           'моль',
           'Масопуст',
           'макс фон лауэ',
           'Ласкер',
           '1939',
           'резонанс',
           'Николсон',
           'Python',
           'квинта',
           'биссектриса',
           'telegram',
           'rata',
           '0',
           'Горький',
           'альт',
           '1'
           ]

def get_updates_json(request, offset_id='None'):  
    params = {'timeout': 10, 'offset': offset_id, 'allowed_updates': json.dumps(["message"])}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def get_update_results(request):
    result_data = get_updates_json(request)['result']
    if not result_data:
        return 0
    else:
        return result_data

def send_mess(chat, text, reply_markup=keyboard_default, parse_mode='None'):  
    params = {'chat_id': chat, 'text': text, 'parse_mode': parse_mode, 'reply_markup': reply_markup}
    response = requests.post(url + 'sendMessage', data=params)
    return response.json()

def send_mess_nokeyboard(chat, text, parse_mode='None'):  
    params = {'chat_id': chat, 'text': text, 'parse_mode': parse_mode}
    response = requests.post(url + 'sendMessage', data=params)
    return response.json()

def forward_mess(chat_id, from_chat_id, message_id):
    params = {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}
    response = requests.post(url + 'forwardMessage', data=params)
    return response

def bot_messages(request, mycursor, mydb):
    
    results = get_update_results(request)
    if results!=0:
        k = 0
        while k<len(results):
            first_result = results[k]
            person_id = first_result['message']['from']['id']
            sql = "SELECT * FROM `bot_users` WHERE `telegram_id` = %(tg_id)s"
            mycursor.execute(sql, {'tg_id': person_id})
            user = mycursor.fetchall()
            if not user:
                status = []
                is_admin = []
                is_reg = []
            else:
                status = user[0][2]
                is_admin = user[0][3]
                is_reg = user[0][4]
            if 'text' in first_result['message'].keys():
                if not is_admin:
                    if not is_reg:
                        if not status or status == 1:
                            if first_result['message']['text']=='/start':
                                sql = "SELECT * FROM `bot_users` WHERE `telegram_id` = %(tg_id)s"
                                mycursor.execute(sql, {'tg_id': person_id})
                                myresult = mycursor.fetchall()
                                if not myresult:
                                    message = ('Привет, ' + first_result['message']['from']['first_name']+
                                               ', я бот, созданный Артёмом для тестовых целей.')
                                    send_mess(person_id, message, keyboard_user_not_reg)
                                    insert_person = ("INSERT INTO `bot_users` (`telegram_id`, `status`) "
                                                      "VALUES (%s, %s)")
                                    insert_data = (person_id, 1)
                                    mycursor.execute(insert_person, insert_data)
                                    mydb.commit()
                                else:
                                    message = (first_result['message']['from']['first_name']+
                                               ', зачем ты снова набрал команду /start? Выглядит так, как будто ты второй раз подряд' +
                                               ' со мной здороваешься, ты что, не запомнил меня?')
                                    send_mess(person_id, message, keyboard_user_not_reg)
                            elif first_result['message']['text']=='О боте':
                                message = ('Добро пожаловать в меню управления логичской игры "Энергетический штурм"!\nПользуясь данным меню Вы можете создать новую команду или ' +
                                            'добавиться в уже существующую для совместного прохождения турнира. Для участния в турнире в команде должно быть от двух до трех человек. ' +
                                            'После успешной регистрации новой команды капитану команды необходимо сообщить уникальный идентификатор остальным желающим для ' +
                                            'успешной регистрации в команде. При возникновении любых вопросов адресуйте вопросы администратору в соответствующей форме.\nУдачи!')
                                send_mess(person_id, message, keyboard_user_not_reg)
                            elif first_result['message']['text']=='Задать вопрос':
                                send_mess(person_id,'Сформулируйте, пожалуйста, свой вопрос главному администратору.', keyboard_cancel)
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 2, 'tg_id': person_id})
                                mydb.commit()
                            elif first_result['message']['text']=='Создать команду':
                                send_mess(person_id,'Введите название новой команды.', keyboard_cancel)
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 3, 'tg_id': person_id})
                                mydb.commit()
                            elif first_result['message']['text']=='Присоединиться к команде':
                                message = ('Введите идентификатор команды, к которой желаете присоединиться. Данный идентификатор был выдан ' +
                                           'капитану команды при регистрации.')
                                send_mess(person_id, message, keyboard_cancel)
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 7, 'tg_id': person_id})
                                mydb.commit()
                            else:
                                send_mess(person_id, 'Пожалуйста, выберите действие из предложенных.', keyboard_user_not_reg)
                        elif status == 2:
                            if first_result['message']['text']!='В главное меню':
                                message = ( 'Спасибо за Ваш вопрос! Мы свяжемся с Вами, как только главный администратор рассмотрит запрос.')
                                send_mess(person_id, message, keyboard_user_not_reg)
                                update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                                insert_question = ("INSERT INTO questions_to_admin (`telegram_id`, `text`) "
                                                 "VALUES (%(tg_id)s, %(text)s)")
                                insert_data = ({'tg_id': person_id, 'text': first_result['message']['text']})
                                mycursor.execute(insert_question, insert_data)
                                mydb.commit()
                                sql = "SELECT telegram_id FROM `bot_users` WHERE is_admin=1"
                                mycursor.execute(sql)
                                myresult = mycursor.fetchall()
                                for i in myresult:
                                    forward_mess(i[0], person_id, first_result['message']['message_id'])
                            else:
                                send_mess(person_id,'Действие отменено.', keyboard_user_not_reg)
                                update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                        elif status==3:
                            if first_result['message']['text']=='В главное меню':
                                send_mess(person_id,'Действие отменено.', keyboard_user_not_reg)
                                update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                                sql = "DELETE FROM `teams` WHERE creator=%(tg_id)s"
                                mycursor.execute(sql, {'tg_id': person_id})
                                mydb.commit()
                            else:
                                send_mess(person_id,'Введите название своего учебного заведения.', keyboard_user_registration)
                                update_status = ("UPDATE bot_users SET status = 4 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                                sql = "SELECT * FROM `teams` WHERE `creator` = %(tg_id)s"
                                mycursor.execute(sql, {'tg_id': person_id})
                                user = mycursor.fetchall()
                                if not user:
                                    insert_team = ("INSERT INTO teams (`team_name`, `creator`) "
                                                     "VALUES (%(name)s, %(tg_id)s) ")
                                    insert_data = ({'name': first_result['message']['text'], 'tg_id': person_id})
                                    mycursor.execute(insert_team, insert_data)
                                    mydb.commit()
                                else:
                                    update_team = ("UPDATE teams SET team_name = %(name)s WHERE creator = %(tg_id)s")
                                    mycursor.execute(update_team, {'name': first_result['message']['text'], 'tg_id': person_id})
                                    mydb.commit()
                        elif status==4:
                            if first_result['message']['text']=='В главное меню':
                                send_mess(person_id,'Действие отменено.', keyboard_user_not_reg)
                                update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                                sql = "DELETE FROM `teams` WHERE creator=%(tg_id)s"
                                mycursor.execute(sql, {'tg_id': person_id})
                                mydb.commit()
                            elif first_result['message']['text']=='Назад':
                                send_mess(person_id,'Введите название новой команды.', keyboard_cancel)
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 3, 'tg_id': person_id})
                                mydb.commit()
                            else:
                                sql = "SELECT * FROM `teams` WHERE `creator` = %(tg_id)s"
                                mycursor.execute(sql, {'tg_id': person_id})
                                user = mycursor.fetchall()
                                message = ( 'Вы подтверждаете создание команды?\n' + 'Название: ' +
                                             user[0][1] + '\n' + 'Учебное заведение: ' + first_result['message']['text'] + '\n')
                                send_mess(person_id, message, keyboard_user_registration_accept_team)
                                update_team = ("UPDATE teams SET school = %(school)s WHERE creator = %(tg_id)s")
                                mycursor.execute(update_team, {'school': first_result['message']['text'], 'tg_id': person_id})
                                mydb.commit()
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 5, 'tg_id': person_id})
                                mydb.commit()
                        elif status==5:
                            if first_result['message']['text']=='В главное меню':
                                send_mess(person_id,'Действие отменено.', keyboard_user_not_reg)
                                update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                                sql = "DELETE FROM `teams` WHERE creator=%(tg_id)s"
                                mycursor.execute(sql, {'tg_id': person_id})
                                mydb.commit()
                            elif first_result['message']['text']=='Назад':
                                send_mess(person_id,'Введите название своего учебного заведения.', keyboard_user_registration)
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 4, 'tg_id': person_id})
                                mydb.commit()
                            elif first_result['message']['text']=='Исправить':
                                send_mess(person_id,'Введите название новой команды.', keyboard_cancel)
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 3, 'tg_id': person_id})
                                mydb.commit()
                            elif first_result['message']['text']=='Да':
                                message = ('Новая команда успешно создана. ' +
                                           'Введите, пожалуйста, информацию о себе в формате: Имя Фамилия. \n' +
                                           'Например: Михаил Алексеев.' )
                                send_mess(person_id, message, keyboard_user_registration)
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 6, 'tg_id': person_id})
                                mydb.commit()
                            else:
                                send_mess(person_id, 'Пожалуйста, укажите корректный ответ.', keyboard_user_registration_accept_team)
                        elif status==6:
                            if first_result['message']['text']=='В главное меню':
                                send_mess(person_id,'Действие отменено.', keyboard_user_not_reg)
                                update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                                sql = "DELETE FROM `teams` WHERE creator=%(tg_id)s"
                                mycursor.execute(sql, {'tg_id': person_id})
                                mydb.commit()
                            elif first_result['message']['text']=='Назад':
                                sql = "SELECT * FROM `teams` WHERE `creator` = %(tg_id)s"
                                mycursor.execute(sql, {'tg_id': person_id})
                                user = mycursor.fetchall()
                                message = ( 'Вы подтверждаете создание команды?\n' +
                                            'Название: ' + user[0][1] + '\n' + 'Учебное заведение: ' + user[0][2] + '\n')
                                send_mess(person_id, message, keyboard_user_registration_accept_team)
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 5, 'tg_id': person_id})
                                mydb.commit()
                            else:
                                message = ( 'Регистрация команды успешна! Для того, чтобы Ваши друзья могли к Вам присоединиться, ' +
                                            'им следует выбрать пункт меню "Присоединиться к команде" и '
                                            'использовать идентификатор ' + str(person_id) +'.\nДля окончания регистрации отправьте свой номер телефона.')
                                send_mess(person_id, message, keyboard_phone)
                                sql = "SELECT * FROM `team_members` WHERE `telegram_id` = %(tg_id)s"
                                mycursor.execute(sql, {'tg_id': person_id})
                                user = mycursor.fetchall()
                                sql = "SELECT * FROM `teams` WHERE `creator` = %(tg_id)s"
                                mycursor.execute(sql, {'tg_id': person_id})
                                team = mycursor.fetchall()
                                if not user:
                                    insert_member = ("INSERT INTO team_members (`name`, `team_id`, `telegram_id`, `is_capitan`) "
                                                     "VALUES (%(name)s, %(t_id)s, %(tg_id)s, %(is_cap)s) ")
                                    insert_data = ({'name': first_result['message']['text'], 't_id': int(team[0][0]), 'tg_id': person_id, 'is_cap': 1})
                                    mycursor.execute(insert_member, insert_data)
                                    mydb.commit()
                                else:
                                    update_member = ("UPDATE team_members SET `name`=%(name)s, `team_id`=%(t_id)s, `is_capitan`=1 "
                                                     "WHERE telegram_id = %(tg_id)s ")
                                    insert_data = ({'name': first_result['message']['text'], 't_id': team[0][0], 'tg_id': person_id})
                                    mycursor.execute(update_member, insert_data)
                                    mydb.commit()
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 10, 'tg_id': person_id})
                                mydb.commit()
                        elif status==7:
                            if first_result['message']['text']=='В главное меню':
                                send_mess(person_id,'Действие отменено.', keyboard_user_not_reg)
                                update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                            elif first_result['message']['text'].isdigit():
                                sql = ("SELECT * FROM teams WHERE creator = %(tg_id)s")
                                data = ({'tg_id': int(first_result['message']['text'])})
                                mycursor.execute(sql, data)
                                myresult = mycursor.fetchall()
                                if not myresult:
                                    message = 'Пожалуйста, введите существующий идентификатор команды.'
                                    send_mess(person_id, message, keyboard_cancel)
                                else:
                                    if myresult[0][3]>=3:
                                        message = ('Число участников данной команды достигло максимального значения. ' +
                                                   'Пожалуйста, введите идентификатор другой команды или создайте свою в главном меню.')
                                        send_mess(person_id, message, keyboard_cancel)
                                    elif myresult[0][3]==0:
                                        message = ('Капитан данной команды еще не завершил регистрацию. ' +
                                                   'Пожалуйста, введите идентификатор другой команды или создайте свою в главном меню.')
                                        send_mess(person_id, message, keyboard_cancel)
                                    else:
                                        message = ('Вы действительно хотите присоединиться к команде *' + myresult[0][1] +
                                                   '*, представляющей учебное заведение *' + myresult[0][2] +
                                                   '*, капитан команды - *')
                                        sql2 = ("SELECT * FROM team_members WHERE telegram_id = %(tg_id)s")
                                        data2 = ({'tg_id': int(first_result['message']['text'])})
                                        mycursor.execute(sql2, data2)
                                        myresult2 = mycursor.fetchall()
                                        message = message + myresult2[0][1] + '*?'
                                        send_mess(person_id, message, keyboard_delete_team, 'Markdown')
                                        update_status = ("UPDATE bot_users SET status = 8 WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                        insert_member = ("INSERT INTO team_members (team_id, telegram_id) "
                                                         "VALUES (%(t_id)s, %(tg_id)s)")
                                        insert_data = ({'t_id':myresult[0][0], 'tg_id': person_id})
                                        mycursor.execute(insert_member, insert_data)
                                        mydb.commit()
                                        #update_status = ("UPDATE teams SET num=num+1 WHERE creator = %(tg_id)s")
                                        #mycursor.execute(update_status, {'tg_id': int(first_result['message']['text'])})
                                        #mydb.commit()
                            else:
                                message = 'Введите, пожалуйста, корректное значение идентификатора.'
                                send_mess(person_id, message, keyboard_cancel)
                        elif status==8:
                            if first_result['message']['text']=='Нет':
                                send_mess(person_id,'Действие отменено.', keyboard_user_not_reg)
                                update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                                
                                #update_status = ("UPDATE teams SET num=num-1 WHERE id = (SELECT team_id FROM team_members WHERE telegram_id = %(tg_id)s)")
                                #mycursor.execute(update_status, {'tg_id': person_id})
                                #mydb.commit()
                                sql = ("DELETE FROM team_members WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(sql, {'tg_id': person_id})
                                mydb.commit()
                            elif first_result['message']['text']=='Да':
                                message = ('Введите, пожалуйста, информацию о себе в формате: Имя Фамилия. \n' +
                                           'Например: Михаил Алексеев.' )
                                send_mess(person_id, message, keyboard_cancel)
                                update_status = ("UPDATE bot_users SET status = 9 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                            else:
                                message = 'Сделайте, пожалуйста, корректный выбор.'
                                send_mess(person_id, message, keyboard_delete_team)
                        elif status==9:
                            if first_result['message']['text']=='В главное меню':
                                send_mess(person_id,'Действие отменено.', keyboard_user_not_reg)
                                update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                                #update_status = ("UPDATE teams SET nun=num-1 WHERE id = (SELECT team_id FROM team_members WHERE telegram_id = %(tg_id)s)")
                                #mycursor.execute(update_status, {'tg_id': myresult2[0][1]})
                                #mydb.commit()
                                sql = ("DELETE FROM team_members WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                            else:
                                sql = ("SELECT num FROM teams WHERE id = (SELECT team_id FROM team_members WHERE telegram_id = %(tg_id)s)")
                                data = ({'tg_id': person_id})
                                mycursor.execute(sql, data)
                                myresult3 = mycursor.fetchall()
                                if myresult3[0][0]>=3:
                                    message = ('Число участников данной команды достигло максимального значения. ' +
                                                   'Пожалуйста, введите идентификатор другой команды или создайте свою в главном меню.')
                                    send_mess(person_id, message, keyboard_cancel)
                                    update_status = ("UPDATE bot_users SET status = 7 WHERE telegram_id = %(tg_id)s")
                                    mycursor.execute(update_status, {'tg_id': person_id})
                                    mydb.commit()
                                    sql = ("DELETE FROM team_members WHERE telegram_id = %(tg_id)s")
                                    mycursor.execute(update_status, {'tg_id': person_id})
                                    mydb.commit()
                                else:
                                    send_mess(person_id, 'Для окончания регистрации отправьте свой номер телефона.', keyboard_phone)
                                    #sql = ("SELECT creator FROM teams WHERE id = (SELECT team_id FROM team_members WHERE telegram_id = %(tg_id)s)")
                                    #mycursor.execute(sql, {'tg_id': person_id})
                                    #myresult = mycursor.fetchall()
                                    #message = ('В Вашу команду успешно добавлен *' + first_result['message']['text'] + '*.')
                                    #send_mess_nokeyboard(myresult[0][0], message, 'Markdown')
                                    update_status = ("UPDATE bot_users SET status = 11 WHERE telegram_id = %(tg_id)s")
                                    mycursor.execute(update_status, {'tg_id': person_id})
                                    mydb.commit()
                                    update_status = ("UPDATE team_members SET name = %(name)s WHERE telegram_id = %(tg_id)s")
                                    mycursor.execute(update_status, {'name': first_result['message']['text'], 'tg_id': person_id})
                                    mydb.commit()
                                    #update_status = ("UPDATE teams SET num=num+1 WHERE creator = %(tg_id)s")
                                    #mycursor.execute(update_status, {'tg_id': myresult[0][0]})
                                    #mydb.commit()
                                    #if myresult3[0][0]==1:
                                    #    insert_team = ("INSERT INTO tournament (team_id) "
                                    #                   "VALUES (%(team_id)s)")
                                    #    sql = ("SELECT team_id FROM team_members WHERE telegram_id = %(tg_id)s")
                                    #    mycursor.execute(sql, {'tg_id': person_id})
                                    #    myresult = mycursor.fetchall()
                                    #    mycursor.execute(insert_team, {'team_id': myresult[0][0]})
                                    #    mydb.commit()
                        elif status == 10:
                            if first_result['message']['text']=='Назад':
                                message = ('Введите, пожалуйста, информацию о себе в формате: Имя Фамилия. \n' +
                                           'Например: Михаил Алексеев.' )
                                send_mess(person_id, message, keyboard_user_registration)
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 6, 'tg_id': person_id})
                                mydb.commit()
                            else:
                                message = ('Сделайте, пожалуйста, корректный выбор.')
                                send_mess(person_id, message, keyboard_phone)
                        elif status == 11:
                            if first_result['message']['text']=='Назад':
                                message = ('Введите, пожалуйста, информацию о себе в формате: Имя Фамилия. \n' +
                                           'Например: Михаил Алексеев.' )
                                send_mess(person_id, message, keyboard_user_registration)
                                update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'stat': 9, 'tg_id': person_id})
                                mydb.commit()
                            else:
                                message = ('Сделайте, пожалуйста, корректный выбор.')
                                send_mess(person_id, message, keyboard_phone)
                    else:
                        sql = "SELECT * FROM `team_members` WHERE `telegram_id` = %(tg_id)s"
                        mycursor.execute(sql, {'tg_id': person_id})
                        myresult = mycursor.fetchall()
                        team_id = myresult[0][2]
                        capitan = myresult[0][4]
                        in_game = myresult[0][5]
                        current_time = first_result['message']['date']
                        if not in_game:
                            if capitan==1:
                                if status==1:
                                    if first_result['message']['text']=='/start':
                                        sql = "SELECT * FROM `bot_users` WHERE `telegram_id` = %(tg_id)s"
                                        mycursor.execute(sql, {'tg_id': person_id})
                                        myresult = mycursor.fetchall()
                                        message = (first_result['message']['from']['first_name']+
                                                   ', зачем ты снова набрал команду /start? ' +
                                                   'Выглядит так, как будто ты второй раз подряд со мной здороваешься, ты что, не запомнил меня?')
                                        send_mess(person_id, message, keyboard_user_capitan)
                                    elif first_result['message']['text']=='О боте':
                                        message = ('Добро пожаловать в меню управления логичской игры "Энергетический штурм"!\nПользуясь данным меню Вы можете создать новую команду или ' +
                                            'добавиться в уже существующую для совместного прохождения турнира. Для участния в турнире в команде должно быть от двух до трех человек. ' +
                                            'После успешной регистрации новой команды капитану команды необходимо сообщить уникальный идентификатор остальным желающим для ' +
                                            'успешной регистрации в команде. При возникновении любых вопросов адресуйте вопросы администратору в соответствующей форме.\nУдачи!')
                                        send_mess(person_id, message, keyboard_user_capitan)
                                    elif first_result['message']['text']=='Задать вопрос':
                                        send_mess(person_id,'Сформулируйте, пожалуйста, свой вопрос главному администратору.', keyboard_cancel)
                                        update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                        mycursor.execute(update_status, {'stat': 2, 'tg_id': person_id})
                                        mydb.commit()
                                    elif first_result['message']['text']=='Информация о команде':
                                        sql = ("SELECT * FROM `teams` WHERE id = %(t_id)s")
                                        data = ({'t_id': team_id})
                                        mycursor.execute(sql, data)
                                        myresult2 = mycursor.fetchall()
                                        message = ('Вы состоите в команде ' + '*' + myresult2[0][1] + '*'+
                                                   ', которая представляет учебное заведение '+ '*' + myresult2[0][2] + '*' +'.\n' +
                                                   'В Вашей команде в данный момент *'  + str(myresult2[0][3]) +  '* участник(а). Это:\n')
                                        sql = ("SELECT * FROM `team_members` WHERE team_id = %(team_id)s")
                                        data = ({'team_id': int(myresult2[0][0])})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        j = 1
                                        for i in myresult:
                                            if i[1]:
                                                message = message + str(j) + '. *' + i[1] +'*'
                                                if i[3]==person_id:
                                                    message = message + ' (Вы)'
                                                if i[4]==1:
                                                    message = message + ' (Капитан)'
                                                message = message + '\n'
                                            j = j+1
                                        message = message + 'Идентификатор команды - ' + '*' + str(person_id) +'*' +'.\n'
                                        message = message + 'Состояние команды: '
                                        if myresult2[0][3]==1:
                                            message = (message + '*Команда не может принимать участие в турнире, так как для этого в ней должно быть ' +
                                                       'от двух до трех человек.*')
                                        elif myresult2[0][3]==2:
                                            message = (message + '*Команда допущена для участия в турнире, но может принять еще одного человека.*')
                                        elif myresult2[0][3]==3:
                                            message = (message + '*Команда допущена для участия в турнире и полностью укомплектована.*')
                                        send_mess(person_id, message, keyboard_user_capitan, 'Markdown')
                                    elif first_result['message']['text']=='Удалить команду':
                                        sql = ("SELECT * FROM `teams` WHERE creator=%(tg_id)s")
                                        data = ({'tg_id': person_id})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        message = ('Вы действительно хотите удалить команду *' + myresult[0][1] +
                                                   '*, которая представляет учебное заведение *'+ myresult[0][2] +
                                                   '*? В случае удаления, Вам и другим членам Вашей команды необходимо будет создавать ' +
                                                   'команду заново, либо присоединяться к существующим.')
                                        send_mess(person_id, message, keyboard_delete_team, 'Markdown')
                                        update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                        mycursor.execute(update_status, {'stat': 3, 'tg_id': person_id})
                                        mydb.commit()
                                    elif first_result['message']['text']=='Начать игру':
                                        sql = ("SELECT num FROM `teams` WHERE creator=%(tg_id)s")
                                        data = ({'tg_id': person_id})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        if myresult[0][0]<2:
                                            message = 'Извините, но Ваша команда на данный момент имеет всего одного участника, а для участия в игре их должно быть минимум два.'
                                            send_mess(person_id, message, keyboard_user_capitan)
                                        else:
                                            if current_time<time_start:
                                                message = 'Извините, но соревнование еще не началось. Соревнование начнется '
                                                time_start_utc = datetime.datetime.utcfromtimestamp(time_start+ 7200)
                                                message = message + str(time_start_utc) + '.'
                                                send_mess(person_id, message, keyboard_user_capitan)
                                            elif current_time>time_finish:
                                                message = 'Извините, но соревнование уже закончилось.'
                                                send_mess(person_id, message, keyboard_user_capitan)
                                            else:
                                                sql = ("SELECT * FROM tournament WHERE team_id = %(t_id)s")
                                                mycursor.execute(sql, {'t_id': team_id})
                                                myresult2 = mycursor.fetchall()
                                                if myresult2[0][24]==20:
                                                    message = 'Ваша команда успешно ответила на все вопросы, ожидайте результатов!'
                                                    send_mess(person_id, message, keyboard_user_capitan)
                                                else:
                                                    message = 'Вперед, игра началась!'
                                                    sql = ("SELECT telegram_id FROM team_members WHERE team_id = %(t_id)s")
                                                    mycursor.execute(sql, {'t_id': team_id})
                                                    myresult = mycursor.fetchall()
                                                    for i in myresult:
                                                        sql = ("SELECT is_reg FROM bot_users WHERE telegram_id = %(tg_id)s")
                                                        mycursor.execute(sql, {'tg_id': i[0]})
                                                        myresult2 = mycursor.fetchall()
                                                        if myresult2[0][0]:
                                                            send_mess(i[0], message, keyboard_game)
                                                            send_mess(i[0], 'Текущие результаты!', keyboard_results)
                                                            update_status = ("UPDATE `team_members` SET `in_game` = 1 WHERE `telegram_id` = %(tg_id)s")
                                                            mycursor.execute(update_status, {'tg_id': i[0]})
                                                            mydb.commit()
                                                        else:
                                                            message2 = ("Команда, в которую Вы пытались добавиться, только что начала игру."
                                                                       " Введите, пожалуйста, идентификатор другой команды.")
                                                            send_mess(i[0], message2, keyboard_cancel)
                                                            sql = ("UPDATE bot_users SET status = 7 WHERE telegram_id = %(tg_id)s")
                                                            mycursor.execute(sql, {'tg_id': i[0]})
                                                            mydb.commit()
                                                            sql = ("DELETE FROM team_members WHERE telegram_id = %(tg_id)s")
                                                            mycursor.execute(sql, {'tg_id': i[0]})
                                                            mydb.commit()
                                                            
                                    else:
                                        send_mess(person_id, 'Пожалуйста, выберите действие из предложенных.', keyboard_user_capitan)
                                elif status==2:
                                    if first_result['message']['text']!='В главное меню':
                                        message = ( 'Спасибо за Ваш вопрос! Мы свяжемся с Вами, как только главный администратор рассмотрит запрос.')
                                        send_mess(person_id, message, keyboard_user_capitan)
                                        update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                        insert_question = ("INSERT INTO questions_to_admin (`telegram_id`, `text`) "
                                                         "VALUES (%(tg_id)s, %(text)s)")
                                        insert_data = ({'tg_id': person_id, 'text': first_result['message']['text']})
                                        mycursor.execute(insert_question, insert_data)
                                        mydb.commit()
                                        sql = "SELECT telegram_id FROM `bot_users` WHERE is_admin=1"
                                        mycursor.execute(sql)
                                        myresult = mycursor.fetchall()
                                        for i in myresult:
                                            forward_mess(i[0], person_id, first_result['message']['message_id'])
                                    else:
                                        send_mess(person_id,'Действие отменено.', keyboard_user_capitan)
                                        update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                elif status==3:
                                    if first_result['message']['text']=='Нет':
                                        message = ( 'Действие отменено.')
                                        send_mess(person_id, message, keyboard_user_capitan)
                                        update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                    elif first_result['message']['text']=='Да':
                                        message = ( 'Команда успешно удалена.')
                                        send_mess(person_id, message, keyboard_user_not_reg)
                                        sql = ("SELECT * FROM team_members WHERE team_id = (SELECT id FROM teams WHERE creator=%(tg_id)s)")
                                        mycursor.execute(sql, {'tg_id': person_id})
                                        myresult = mycursor.fetchall()
                                        if len(myresult)>1:
                                            for i in myresult:
                                                if i[3]!=person_id:
                                                    message = ('Ваша команда была удалена капитаном. Пожалуйта, выберите другую или ' +
                                                               'создайте свою.') 
                                                    send_mess(i[3], message, keyboard_user_not_reg)
                                                    update_status = ("UPDATE bot_users SET status = 1, is_reg = 0 WHERE telegram_id = %(tg_id)s")
                                                    mycursor.execute(update_status, {'tg_id': i[3]})
                                                    mydb.commit()
                                            sql = "DELETE FROM `tournament` WHERE team_id=(SELECT id FROM teams WHERE creator=%(tg_id)s)"
                                            mycursor.execute(sql, {'tg_id': person_id})
                                            mydb.commit()
                                        sql = "DELETE FROM `team_members` WHERE team_id=(SELECT id FROM teams WHERE creator=%(tg_id)s)"
                                        mycursor.execute(sql, {'tg_id': person_id})
                                        mydb.commit()
                                        sql = "DELETE FROM `teams` WHERE creator=%(tg_id)s"
                                        mycursor.execute(sql, {'tg_id': person_id})
                                        mydb.commit()
                                        update_status = ("UPDATE bot_users SET status = 1, is_reg = 0 WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                    else:
                                        send_mess(person_id, 'Пожалуйста, выберите действие из предложенных.', keyboard_delete_team)
                            else:
                                if status==1:
                                    if first_result['message']['text']=='/start':
                                        sql = "SELECT * FROM `bot_users` WHERE `telegram_id` = %(tg_id)s"
                                        mycursor.execute(sql, {'tg_id': person_id})
                                        myresult = mycursor.fetchall()
                                        message = (first_result['message']['from']['first_name']+
                                                   ', зачем ты снова набрал команду /start? ' +
                                                   'Выглядит так, как будто ты второй раз подряд со мной здороваешься, ты что, не запомнил меня?')
                                        send_mess(person_id, message, keyboard_user_reg)
                                    elif first_result['message']['text']=='О боте':
                                        message = ('Добро пожаловать в меню управления логической игры "Энергетический штурм"!\nПользуясь данным меню Вы можете создать новую команду или ' +
                                            'добавиться в уже существующую для совместного прохождения турнира. Для участния в турнире в команде должно быть от двух до трех человек. ' +
                                            'После успешной регистрации новой команды капитану команды необходимо сообщить уникальный идентификатор остальным желающим для ' +
                                            'успешной регистрации в команде. При возникновении любых вопросов адресуйте вопросы администратору в соответствующей форме.\nУдачи!')
                                        send_mess(person_id, message, keyboard_user_reg)
                                    elif first_result['message']['text']=='Задать вопрос':
                                        send_mess(person_id,'Сформулируйте, пожалуйста, свой вопрос главному администратору.', keyboard_cancel)
                                        update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                        mycursor.execute(update_status, {'stat': 2, 'tg_id': person_id})
                                        mydb.commit()
                                    elif first_result['message']['text']=='Информация о команде':
                                        sql = ("SELECT * FROM `teams` WHERE id =%(t_id)s")
                                        data = ({'t_id': team_id})
                                        mycursor.execute(sql, data)
                                        myresult2 = mycursor.fetchall()
                                        message = ('Вы состоите в команде ' + '*' + myresult2[0][1] + '*' +
                                                   ', которая представляет учебное заведение '+ '*' + myresult2[0][2] + '*.\n' +
                                                   'В Вашей команде в данный момент *' + str(myresult2[0][3]) + '* участник(а). Это:\n')
                                        sql = ("SELECT * FROM `team_members` WHERE team_id = %(team_id)s")
                                        data = ({'team_id': int(myresult2[0][0])})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        j = 1
                                        for i in myresult:
                                            if i[1]:
                                                message = message + str(j) + '. *' + i[1] +'*'
                                                if i[3]==person_id:
                                                    message = message + ' (Вы)'
                                                if i[4]==1:
                                                    message = message + ' (Капитан)'
                                                message = message + '\n'
                                            j = j +1
                                        message = message + 'Идентификатор команды - *' + str(myresult2[0][5]) +'*.\n'
                                        message = message + 'Состояние команды: '
                                        if myresult2[0][3]==1:
                                            message = (message + '*Команда не может принимать участие в турнире, так как для этого в ней должно быть ' +
                                                       'от двух до трех человек.*')
                                        elif myresult2[0][3]==2:
                                            message = (message + '*Команда допущена для участия в турнире, но может принять еще одного человека.*')
                                        elif myresult2[0][3]==3:
                                            message = (message + '*Команда допущена для участия в турнире и полностью укомплектована.*')
                                        send_mess(person_id, message, keyboard_user_reg, 'Markdown')
                                    elif first_result['message']['text']=='Покинуть команду':
                                        sql = ("SELECT * FROM `teams` WHERE id=%(t_id)s")
                                        data = ({'t_id': team_id})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        message = ('Вы действительно хотите покинуть команду *' + myresult[0][1] +
                                                   '*, которая представляет учебное заведение *'+ myresult[0][2] +'*?')
                                        send_mess(person_id, message, keyboard_delete_team, 'Markdown')
                                        update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                        mycursor.execute(update_status, {'stat': 3, 'tg_id': person_id})
                                        mydb.commit()
                                    elif first_result['message']['text']=='Начать игру':
                                        sql = ("SELECT num FROM `teams` WHERE id=%(t_id)s")
                                        data = ({'t_id': team_id})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        if myresult[0][0]<2:
                                            message = 'Извините, но Ваша команда на данный момент имеет всего одного участника, а для участия в игре их должно быть минимум два.'
                                            send_mess(person_id, message, keyboard_user_reg)
                                        else:
                                            if current_time<time_start:
                                                message = 'Извините, но соревнование еще не началось. Соревнование начнется '
                                                time_start_utc = datetime.datetime.utcfromtimestamp(time_start+7200)
                                                message = message + str(time_start_utc) + '.'
                                                send_mess(person_id, message, keyboard_user_reg)
                                            elif current_time>time_finish:
                                                message = 'Извините, но соревнование уже закончилось.'
                                                send_mess(person_id, message, keyboard_user_reg)
                                            else:
                                                sql = ("SELECT * FROM tournament WHERE team_id = %(t_id)s")
                                                mycursor.execute(sql, {'t_id': team_id})
                                                myresult2 = mycursor.fetchall()
                                                if myresult2[0][24]==20:
                                                    message = 'Ваша команда успешно ответила на все вопросы, ожидайте результатов!'
                                                    send_mess(person_id, message, keyboard_user_reg)
                                                else:
                                                    message = 'Вперед, игра началась!'
                                                    sql = ("SELECT telegram_id FROM team_members WHERE team_id = %(t_id)s")
                                                    mycursor.execute(sql, {'t_id': team_id})
                                                    myresult = mycursor.fetchall()
                                                    for i in myresult:
                                                        sql = ("SELECT is_reg FROM bot_users WHERE telegram_id = %(tg_id)s")
                                                        mycursor.execute(sql, {'tg_id': i[0]})
                                                        myresult2 = mycursor.fetchall()
                                                        if myresult2[0][0]:
                                                            send_mess(i[0], message, keyboard_game)
                                                            send_mess(i[0], 'Текущие результаты!', keyboard_results)
                                                            update_status = ("UPDATE `team_members` SET `in_game` = 1 WHERE `telegram_id` = %(tg_id)s")
                                                            mycursor.execute(update_status, {'tg_id': i[0]})
                                                            mydb.commit()
                                                        else:
                                                            message2 = ("Команда, в которую Вы пытались добавиться, только что начала игру."
                                                                       " Введите, пожалуйста, идентификатор ругой команды.")
                                                            send_mess(i[0], message2, keyboard_cancel)
                                                            sql = ("UPDATE bot_users SET status = 7 WHERE telegram_id = %(tg_id)s")
                                                            mycursor.execute(sql, {'tg_id': i[0]})
                                                            mydb.commit()
                                                            sql = ("DELETE FROM team_members WHERE telegram_id = %(tg_id)s")
                                                            mycursor.execute(sql, {'tg_id': i[0]})
                                                            mydb.commit()
                                                        
                                    else:
                                        send_mess(person_id, 'Пожалуйста, выберите действие из предложенных.', keyboard_user_reg)
                                elif status==2:
                                    if first_result['message']['text']!='В главное меню':
                                        message = ( 'Спасибо за Ваш вопрос! Мы свяжемся с Вами, как только главный администратор рассмотрит запрос.')
                                        send_mess(person_id, message, keyboard_user_reg)
                                        update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                        insert_question = ("INSERT INTO questions_to_admin (`telegram_id`, `text`) "
                                                         "VALUES (%(tg_id)s, %(text)s)")
                                        insert_data = ({'tg_id': person_id, 'text': first_result['message']['text']})
                                        mycursor.execute(insert_question, insert_data)
                                        mydb.commit()
                                        sql = "SELECT telegram_id FROM `bot_users` WHERE is_admin=1"
                                        mycursor.execute(sql)
                                        myresult = mycursor.fetchall()
                                        for i in myresult:
                                            forward_mess(i[0], person_id, first_result['message']['message_id'])
                                    else:
                                        send_mess(person_id,'Действие отменено.', keyboard_user_reg)
                                        update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                elif status==3:
                                    if first_result['message']['text']=='Нет':
                                        message = ( 'Действие отменено.')
                                        send_mess(person_id, message, keyboard_user_reg)
                                        update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                    elif first_result['message']['text']=='Да':
                                        message = ( 'Вы успешно покинули команду.')
                                        send_mess(person_id, message, keyboard_user_not_reg)
                                        sql = ("SELECT * FROM teams WHERE id = (SELECT team_id FROM team_members WHERE telegram_id = %(tg_id)s)")
                                        mycursor.execute(sql, {'tg_id': person_id})
                                        myresult = mycursor.fetchall()
                                        sql = ("SELECT name FROM team_members WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(sql, {'tg_id': person_id})
                                        myresult2 = mycursor.fetchall()
                                        message = ('Вашу команду покинул ' + myresult2[0][0] + '.')
                                        send_mess_nokeyboard(myresult[0][5], message)
                                        update_status = ("UPDATE teams SET num = num-1 WHERE id ="
                                                         "(SELECT team_id FROM team_members WHERE telegram_id = %(tg_id)s)")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                        if myresult[0][3]==2:
                                            sql = "DELETE FROM `tournament` WHERE team_id=(SELECT id FROM teams WHERE creator=%(tg_id)s)"
                                            mycursor.execute(sql, {'tg_id': myresult[0][5]})
                                            mydb.commit()
                                        sql = "DELETE FROM `team_members` WHERE telegram_id=%(tg_id)s"
                                        mycursor.execute(sql, {'tg_id': person_id})
                                        mydb.commit()
                                        update_status = ("UPDATE bot_users SET status = 1, is_reg=0 WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                    else:
                                        send_mess(person_id, 'Пожалуйста, выберите действие из предложенных.', keyboard_delete_team)
                        else:
                            if current_time<time_finish:
                                if status == 1:
                                    if first_result['message']['text'].isdigit() and int(first_result['message']['text'])>0 and int(first_result['message']['text'])<21:
                                        sql = ("SELECT * FROM tournament WHERE team_id=%(t_id)s")
                                        data = ({'t_id': team_id})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        if myresult[0][int(first_result['message']['text'])+1]<=0:
                                            send_mess(person_id, questions[int(first_result['message']['text'])-1], keyboard_game_question)
                                            update_status = ("UPDATE bot_users SET status = %(st)s WHERE telegram_id = %(tg_id)s")
                                            mycursor.execute(update_status, {'st': int(first_result['message']['text'])+1,'tg_id': person_id})
                                            mydb.commit()
                                        else:
                                            message = 'Ваша команда уже ответила на этот вопрос, пожалуйста, выберите другой.'
                                            sql = ("SELECT * FROM tournament WHERE team_id=%(t_id)s")
                                            data = ({'t_id': team_id})
                                            mycursor.execute(sql, data)
                                            myresult = mycursor.fetchall()
                                            i = 1
                                            v = [0, 0, 0, 0, 0]
                                            while i<=5:
                                                v[i-1] = myresult[0][i+1]
                                                i = i+1
                                            keyboard = ['','','','','']
                                            i = 0
                                            for j in v:
                                                if j>0:
                                                    keyboard[i] = '✅ '
                                                keyboard[i] = keyboard[i] + game_keyboard[i]
                                                i = i+1
                                            i = 6
                                            v2 = [0, 0, 0, 0, 0]
                                            while i<=10:
                                                v2[i-6] = myresult[0][i+1]
                                                i = i+1
                                            keyboard2 = ['','','','','']
                                            i = 5
                                            for j in v2:
                                                if j>0:
                                                    keyboard2[i-5] = '✅ '
                                                keyboard2[i-5] = keyboard2[i-5] + game_keyboard2[i-5]
                                                i = i+1
                                            i = 11
                                            v3 = [0, 0, 0, 0, 0]
                                            while i<=15:
                                                v3[i-11] = myresult[0][i+1]
                                                i = i+1
                                            keyboard3 = ['','','','','']
                                            i = 10
                                            for j in v3:
                                                if j>0:
                                                    keyboard3[i-10] = '✅ '
                                                keyboard3[i-10] = keyboard3[i-10] + game_keyboard3[i-10]
                                                i = i+1
                                            i = 16
                                            v4 = [0, 0, 0, 0, 0]
                                            while i<=20:
                                                v4[i-16] = myresult[0][i+1]
                                                i = i+1
                                            keyboard4 = ['','','','','']
                                            i = 15
                                            for j in v4:
                                                if j>0:
                                                    keyboard4[i-15] = '✅ '
                                                keyboard4[i-15] = keyboard4[i-15] + game_keyboard4[i-15]
                                                i = i+1
                                            json_keyboard = json.dumps({'keyboard': [keyboard, keyboard2, keyboard3, keyboard4, ['Задать вопрос']],'resize_keyboard': True })
                                            send_mess(person_id, message, json_keyboard)
                                    elif first_result['message']['text']=='Задать вопрос':
                                        send_mess(person_id,'Сформулируйте, пожалуйста, свой вопрос главному администратору.', keyboard_game_question)
                                        update_status = ("UPDATE `bot_users` SET `status` = %(stat)s WHERE `telegram_id` = %(tg_id)s")
                                        mycursor.execute(update_status, {'stat': 2000, 'tg_id': person_id})
                                        mydb.commit()
                                    else:
                                        message = 'Пожалуйста, введите корректный номер вопроса.'
                                        sql = ("SELECT * FROM tournament WHERE team_id=%(t_id)s")
                                        data = ({'t_id': team_id})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        i = 1
                                        v = [0, 0, 0, 0, 0]
                                        while i<=5:
                                            v[i-1] = myresult[0][i+1]
                                            i = i+1
                                        keyboard = ['','','','','']
                                        i = 0
                                        for j in v:
                                            if j>0:
                                                keyboard[i] = '✅ '
                                            keyboard[i] = keyboard[i] + game_keyboard[i]
                                            i = i+1
                                        i = 6
                                        v2 = [0, 0, 0, 0, 0]
                                        while i<=10:
                                            v2[i-6] = myresult[0][i+1]
                                            i = i+1
                                        keyboard2 = ['','','','','']
                                        i = 5
                                        for j in v2:
                                            if j>0:
                                                keyboard2[i-5] = '✅ '
                                            keyboard2[i-5] = keyboard2[i-5] + game_keyboard2[i-5]
                                            i = i+1
                                        i = 11
                                        v3 = [0, 0, 0, 0, 0]
                                        while i<=15:
                                            v3[i-11] = myresult[0][i+1]
                                            i = i+1
                                        keyboard3 = ['','','','','']
                                        i = 10
                                        for j in v3:
                                            if j>0:
                                                keyboard3[i-10] = '✅ '
                                            keyboard3[i-10] = keyboard3[i-10] + game_keyboard3[i-10]
                                            i = i+1
                                        i = 16
                                        v4 = [0, 0, 0, 0, 0]
                                        while i<=20:
                                            v4[i-16] = myresult[0][i+1]
                                            i = i+1
                                        keyboard4 = ['','','','','']
                                        i = 15
                                        for j in v4:
                                            if j>0:
                                                keyboard4[i-15] = '✅ '
                                            keyboard4[i-15] = keyboard4[i-15] + game_keyboard4[i-15]
                                            i = i+1
                                        json_keyboard = json.dumps({'keyboard': [keyboard, keyboard2, keyboard3, keyboard4, ['Задать вопрос']],'resize_keyboard': True })
                                        send_mess(person_id, message, json_keyboard)
                                elif status==2000:
                                    if first_result['message']['text']!='К списку вопросов':
                                        message = ( 'Спасибо за Ваш вопрос! Мы свяжемся с Вами, как только главный администратор рассмотрит запрос.')
                                        sql = ("SELECT * FROM tournament WHERE team_id=%(t_id)s")
                                        data = ({'t_id': team_id})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        i = 1
                                        v = [0, 0, 0, 0, 0]
                                        while i<=5:
                                            v[i-1] = myresult[0][i+1]
                                            i = i+1
                                        keyboard = ['','','','','']
                                        i = 0
                                        for j in v:
                                            if j>0:
                                                keyboard[i] = '✅ '
                                            keyboard[i] = keyboard[i] + game_keyboard[i]
                                            i = i+1
                                        i = 6
                                        v2 = [0, 0, 0, 0, 0]
                                        while i<=10:
                                            v2[i-6] = myresult[0][i+1]
                                            i = i+1
                                        keyboard2 = ['','','','','']
                                        i = 5
                                        for j in v2:
                                            if j>0:
                                                keyboard2[i-5] = '✅ '
                                            keyboard2[i-5] = keyboard2[i-5] + game_keyboard2[i-5]
                                            i = i+1
                                        i = 11
                                        v3 = [0, 0, 0, 0, 0]
                                        while i<=15:
                                            v3[i-11] = myresult[0][i+1]
                                            i = i+1
                                        keyboard3 = ['','','','','']
                                        i = 10
                                        for j in v3:
                                            if j>0:
                                                keyboard3[i-10] = '✅ '
                                            keyboard3[i-10] = keyboard3[i-10] + game_keyboard3[i-10]
                                            i = i+1
                                        i = 16
                                        v4 = [0, 0, 0, 0, 0]
                                        while i<=20:
                                            v4[i-16] = myresult[0][i+1]
                                            i = i+1
                                        keyboard4 = ['','','','','']
                                        i = 15
                                        for j in v4:
                                            if j>0:
                                                keyboard4[i-15] = '✅ '
                                            keyboard4[i-15] = keyboard4[i-15] + game_keyboard4[i-15]
                                            i = i+1
                                        json_keyboard = json.dumps({'keyboard': [keyboard, keyboard2, keyboard3, keyboard4, ['Задать вопрос']],'resize_keyboard': True })
                                        send_mess(person_id, message, json_keyboard)
                                        update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                        insert_question = ("INSERT INTO questions_to_admin (`telegram_id`, `text`) "
                                                         "VALUES (%(tg_id)s, %(text)s)")
                                        insert_data = ({'tg_id': person_id, 'text': first_result['message']['text']})
                                        mycursor.execute(insert_question, insert_data)
                                        mydb.commit()
                                        sql = "SELECT telegram_id FROM `bot_users` WHERE is_admin=1"
                                        mycursor.execute(sql)
                                        myresult = mycursor.fetchall()
                                        for i in myresult:
                                            forward_mess(i[0], person_id, first_result['message']['message_id'])
                                    else:
                                        message = 'Действие отменено.'
                                        sql = ("SELECT * FROM tournament WHERE team_id=%(t_id)s")
                                        data = ({'t_id': team_id})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        i = 1
                                        v = [0, 0, 0, 0, 0]
                                        while i<=5:
                                            v[i-1] = myresult[0][i+1]
                                            i = i+1
                                        keyboard = ['','','','','']
                                        i = 0
                                        for j in v:
                                            if j>0:
                                                keyboard[i] = '✅ '
                                            keyboard[i] = keyboard[i] + game_keyboard[i]
                                            i = i+1
                                        i = 6
                                        v2 = [0, 0, 0, 0, 0]
                                        while i<=10:
                                            v2[i-6] = myresult[0][i+1]
                                            i = i+1
                                        keyboard2 = ['','','','','']
                                        i = 5
                                        for j in v2:
                                            if j>0:
                                                keyboard2[i-5] = '✅ '
                                            keyboard2[i-5] = keyboard2[i-5] + game_keyboard2[i-5]
                                            i = i+1
                                        i = 11
                                        v3 = [0, 0, 0, 0, 0]
                                        while i<=15:
                                            v3[i-11] = myresult[0][i+1]
                                            i = i+1
                                        keyboard3 = ['','','','','']
                                        i = 10
                                        for j in v3:
                                            if j>0:
                                                keyboard3[i-10] = '✅ '
                                            keyboard3[i-10] = keyboard3[i-10] + game_keyboard3[i-10]
                                            i = i+1
                                        i = 16
                                        v4 = [0, 0, 0, 0, 0]
                                        while i<=20:
                                            v4[i-16] = myresult[0][i+1]
                                            i = i+1
                                        keyboard4 = ['','','','','']
                                        i = 15
                                        for j in v4:
                                            if j>0:
                                                keyboard4[i-15] = '✅ '
                                            keyboard4[i-15] = keyboard4[i-15] + game_keyboard4[i-15]
                                            i = i+1
                                        json_keyboard = json.dumps({'keyboard': [keyboard, keyboard2, keyboard3, keyboard4, ['Задать вопрос']],'resize_keyboard': True })
                                        send_mess(person_id, message, json_keyboard)
                                        update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'tg_id': person_id})
                                        mydb.commit()
                                else:
                                    if first_result['message']['text']==answers[status-2]:
                                        sql = ("SELECT * FROM tournament WHERE team_id=%(t_id)s")
                                        data = ({'t_id': team_id})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        if myresult[0][status]<=0:        
                                            i = 1
                                            v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                            while i<=20:
                                                v[i-1] = myresult[0][i+1]
                                                i = i+1
                                            v[status-2] = -myresult[0][status] + 1
                                            update_table=("UPDATE tournament SET q1 =%(v1)s,"
                                                        "q2 = %(v2)s,"
                                                        "q3 = %(v3)s,"
                                                        "q4 = %(v4)s,"
                                                        "q5 = %(v5)s,"
                                                        "q6 = %(v6)s,"
                                                        "q7 = %(v7)s,"
                                                        "q8 = %(v8)s,"
                                                        "q9 = %(v9)s,"
                                                        "q10 = %(v10)s,"
                                                        "q11 =%(v11)s,"
                                                        "q12 = %(v12)s,"
                                                        "q13 = %(v13)s,"
                                                        "q14 = %(v14)s,"
                                                        "q15 = %(v15)s,"
                                                        "q16 = %(v16)s,"
                                                        "q17 = %(v17)s,"
                                                        "q18 = %(v18)s,"
                                                        "q19 = %(v19)s,"
                                                        "q20 = %(v20)s,"
                                                        "complete = complete+1,"
                                                        "points = points + %(points)s,"
                                                        "complete_unfrozen = complete_unfrozen+1,"
                                                        "points_unfrozen = points_unfrozen + %(points)s WHERE team_id=%(t_id)s")
                                            update_data = ({'v1': v[0],
                                                            'v2': v[1],
                                                            'v3': v[2],
                                                            'v4': v[3],
                                                            'v5': v[4],
                                                            'v6': v[5],
                                                            'v7': v[6],
                                                            'v8': v[7],
                                                            'v9': v[8],
                                                            'v10': v[9],
                                                            'v11': v[10],
                                                            'v12': v[11],
                                                            'v13': v[12],
                                                            'v14': v[13],
                                                            'v15': v[14],
                                                            'v16': v[15],
                                                            'v17': v[16],
                                                            'v18': v[17],
                                                            'v19': v[18],
                                                            'v20': v[19],
                                                            'points':current_time-time_start+300*(-myresult[0][status]),
                                                            't_id': team_id})
                                            mycursor.execute(update_table, update_data)
                                            mydb.commit()
                                            if current_time>time_frozen:
                                                update_table = ("UPDATE tournament SET complete = complete-1,  points = points - %(points)s WHERE team_id=%(t_id)s")
                                                update_data = ({'points':current_time-time_start+300*(-myresult[0][status]),
                                                            't_id': team_id})
                                                mycursor.execute(update_table, update_data)
                                                mydb.commit()
                                            if myresult[0][24]!=19:
                                                update_status = ("UPDATE bot_users SET status = %(st)s WHERE telegram_id = %(tg_id)s")
                                                mycursor.execute(update_status, {'st': 1,'tg_id': person_id})
                                                mydb.commit()
                                                keyboard = ['','','','','']
                                                keyboard2 = ['','','','','']
                                                keyboard3 = ['','','','','']
                                                keyboard4 = ['','','','','']
                                                i = 0
                                                for j in v:
                                                    if i//5==0:
                                                        if j>0:
                                                            keyboard[i] = '✅ '
                                                        keyboard[i] = keyboard[i] + game_keyboard[i]
                                                    elif i//5==1:
                                                        if j>0:
                                                            keyboard2[i-5] = '✅ '
                                                        keyboard2[i-5] = keyboard2[i-5] + game_keyboard2[i-5]
                                                    elif i//5==2:
                                                        if j>0:
                                                            keyboard3[i-10] = '✅ '
                                                        keyboard3[i-10] = keyboard3[i-10] + game_keyboard3[i-10]
                                                    elif i//5==3:
                                                        if j>0:
                                                            keyboard4[i-15] = '✅ '
                                                        keyboard4[i-15] = keyboard4[i-15] + game_keyboard4[i-15]
                                                    i = i+1
                                                json_keyboard = json.dumps({'keyboard': [keyboard, keyboard2, keyboard3, keyboard4, ['Задать вопрос']],'resize_keyboard': True })
                                                message = 'Правильно!'
                                                send_mess(person_id, message, json_keyboard)
                                                send_mess(person_id, 'Текущие результаты!', keyboard_results)
                                            else:
                                                message = 'Ваша команда успешно ответила на все вопросы, ожидайте результатов!'
                                                sql = ("SELECT * FROM team_members WHERE team_id = %(t_id)s")
                                                mycursor.execute(sql, {'t_id': team_id})
                                                myresult = mycursor.fetchall()
                                                for i in myresult:
                                                    if i[4]:
                                                        send_mess(i[3], message, keyboard_user_capitan)
                                                        send_mess(person_id, 'Текущие результаты!', keyboard_results)
                                                    else:
                                                        send_mess(i[3], message, keyboard_user_reg)
                                                        send_mess(person_id, 'Текущие результаты!', keyboard_results)
                                                    update_status = ("UPDATE `team_members` SET `in_game` = 0 WHERE `telegram_id` = %(tg_id)s")
                                                    mycursor.execute(update_status, {'tg_id': i[3]})
                                                    mydb.commit()
                                                    update_status = ("UPDATE bot_users SET status = %(st)s WHERE telegram_id = %(tg_id)s")
                                                    mycursor.execute(update_status, {'st': 1,'tg_id': i[3]})
                                                    mydb.commit()
                                        else:
                                            message = 'Ваша команда уже ответила на этот вопрос, пожалуйста, выберите другой.'
                                            sql = ("SELECT * FROM tournament WHERE team_id=%(t_id)s")
                                            data = ({'t_id': team_id})
                                            mycursor.execute(sql, data)
                                            myresult = mycursor.fetchall()
                                            i = 1
                                            v = [0, 0, 0, 0, 0]
                                            while i<=5:
                                                v[i-1] = myresult[0][i+1]
                                                i = i+1
                                            keyboard = ['','','','','']
                                            i = 0
                                            for j in v:
                                                if j>0:
                                                    keyboard[i] = '✅ '
                                                keyboard[i] = keyboard[i] + game_keyboard[i]
                                                i = i+1
                                            i = 6
                                            v2 = [0, 0, 0, 0, 0]
                                            while i<=10:
                                                v2[i-6] = myresult[0][i+1]
                                                i = i+1
                                            keyboard2 = ['','','','','']
                                            i = 5
                                            for j in v2:
                                                if j>0:
                                                    keyboard2[i-5] = '✅ '
                                                keyboard2[i-5] = keyboard2[i-5] + game_keyboard2[i-5]
                                                i = i+1
                                            i = 11
                                            v3 = [0, 0, 0, 0, 0]
                                            while i<=15:
                                                v3[i-11] = myresult[0][i+1]
                                                i = i+1
                                            keyboard3 = ['','','','','']
                                            i = 10
                                            for j in v3:
                                                if j>0:
                                                    keyboard3[i-10] = '✅ '
                                                keyboard3[i-10] = keyboard3[i-10] + game_keyboard3[i-10]
                                                i = i+1
                                            i = 16
                                            v4 = [0, 0, 0, 0, 0]
                                            while i<=20:
                                                v4[i-16] = myresult[0][i+1]
                                                i = i+1
                                            keyboard4 = ['','','','','']
                                            i = 15
                                            for j in v4:
                                                if j>0:
                                                    keyboard4[i-15] = '✅ '
                                                keyboard4[i-15] = keyboard4[i-15] + game_keyboard4[i-15]
                                                i = i+1
                                            json_keyboard = json.dumps({'keyboard': [keyboard, keyboard2, keyboard3, keyboard4, ['Задать вопрос']],'resize_keyboard': True })
                                            send_mess(person_id, message, json_keyboard)
                                            send_mess(person_id, 'Текущие результаты!', keyboard_results)
                                            update_status = ("UPDATE bot_users SET status = %(st)s WHERE telegram_id = %(tg_id)s")
                                            mycursor.execute(update_status, {'st': 1,'tg_id': person_id})
                                            mydb.commit()
                                    elif first_result['message']['text']=='К списку вопросов':
                                        message = 'Пожалуйста, выберите вопрос.'
                                        sql = ("SELECT * FROM tournament WHERE team_id=%(t_id)s")
                                        data = ({'t_id': team_id})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        i = 1
                                        v = [0, 0, 0, 0, 0]
                                        while i<=5:
                                                v[i-1] = myresult[0][i+1]
                                                i = i+1
                                        keyboard = ['','','','','']
                                        i = 0
                                        for j in v:
                                            if j>0:
                                                keyboard[i] = '✅ '
                                            keyboard[i] = keyboard[i] + game_keyboard[i]
                                            i = i+1
                                        i = 6
                                        v2 = [0, 0, 0, 0, 0]
                                        while i<=10:
                                            v2[i-6] = myresult[0][i+1]
                                            i = i+1
                                        keyboard2 = ['','','','','']
                                        i = 5
                                        for j in v2:
                                            if j>0:
                                                keyboard2[i-5] = '✅ '
                                            keyboard2[i-5] = keyboard2[i-5] + game_keyboard2[i-5]
                                            i = i+1
                                        i = 11
                                        v3 = [0, 0, 0, 0, 0]
                                        while i<=15:
                                            v3[i-11] = myresult[0][i+1]
                                            i = i+1
                                        keyboard3 = ['','','','','']
                                        i = 10
                                        for j in v3:
                                            if j>0:
                                                keyboard3[i-10] = '✅ '
                                            keyboard3[i-10] = keyboard3[i-10] + game_keyboard3[i-10]
                                            i = i+1
                                        i = 16
                                        v4 = [0, 0, 0, 0, 0]
                                        while i<=20:
                                            v4[i-16] = myresult[0][i+1]
                                            i = i+1
                                        keyboard4 = ['','','','','']
                                        i = 15
                                        for j in v4:
                                            if j>0:
                                                keyboard4[i-15] = '✅ '
                                            keyboard4[i-15] = keyboard4[i-15] + game_keyboard4[i-15]
                                            i = i+1
                                        json_keyboard = json.dumps({'keyboard': [keyboard, keyboard2, keyboard3, keyboard4, ['Задать вопрос']],'resize_keyboard': True })
                                        send_mess(person_id, message, json_keyboard)
                                        send_mess(person_id,'Текущие результаты!', keyboard_results)
                                        update_status = ("UPDATE bot_users SET status = %(st)s WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(update_status, {'st': 1,'tg_id': person_id})
                                        mydb.commit()
                                    else:
                                        message = 'Ответ неправильный!'
                                        sql = ("SELECT * FROM tournament WHERE team_id=%(t_id)s")
                                        data = ({'t_id': team_id})
                                        mycursor.execute(sql, data)
                                        myresult = mycursor.fetchall()
                                        i = 1
                                        v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                        while i<=20:
                                            v[i-1] = myresult[0][i+1]
                                            i = i+1
                                        if myresult[0][status]<=0:
                                            v[status-2] = myresult[0][status] - 1
                                            update_table=("UPDATE tournament SET "
                                                         "q1 = %(v1)s,"
                                                         "q2 = %(v2)s,"
                                                         "q3 = %(v3)s,"
                                                         "q4 = %(v4)s,"
                                                         "q5 = %(v5)s, "
                                                         "q6 = %(v6)s,"
                                                         "q7 = %(v7)s,"
                                                         "q8 = %(v8)s,"
                                                         "q9 = %(v9)s,"
                                                         "q10 = %(v10)s, "
                                                         "q11 = %(v11)s,"
                                                         "q12 = %(v12)s,"
                                                         "q13 = %(v13)s,"
                                                         "q14 = %(v14)s,"
                                                         "q15 = %(v15)s, "
                                                         "q16 = %(v16)s,"
                                                         "q17 = %(v17)s,"
                                                         "q18 = %(v18)s,"
                                                         "q19 = %(v19)s,"
                                                         "q20 = %(v20)s "
                                                         "WHERE team_id=%(t_id)s")
                                            update_data = ({'v1': v[0],
                                                            'v2': v[1],
                                                            'v3': v[2],
                                                            'v4': v[3],
                                                            'v5': v[4],
                                                            'v6': v[5],
                                                            'v7': v[6],
                                                            'v8': v[7],
                                                            'v9': v[8],
                                                            'v10': v[9],
                                                            'v11': v[10],
                                                            'v12': v[11],
                                                            'v13': v[12],
                                                            'v14': v[13],
                                                            'v15': v[14],
                                                            'v16': v[15],
                                                            'v17': v[16],
                                                            'v18': v[17],
                                                            'v19': v[18],
                                                            'v20': v[19],
                                                            't_id': team_id})
                                            mycursor.execute(update_table, update_data)
                                            mydb.commit()
                                            send_mess(person_id, message, keyboard_game_question)
                                        else:
                                            message = 'Ваша команда уже ответила на этот вопрос, пожалуйста, выберите другой.'
                                            keyboard = ['','','','','']
                                            keyboard2 = ['','','','','']
                                            keyboard3 = ['','','','','']
                                            keyboard4 = ['','','','','']
                                            i = 0
                                            for j in v:
                                                if i//5==0:
                                                        if j>0:
                                                            keyboard[i] = '✅ '
                                                        keyboard[i] = keyboard[i] + game_keyboard[i]
                                                elif i//5==1:
                                                        if j>0:
                                                            keyboard2[i-5] = '✅ '
                                                        keyboard2[i-5] = keyboard2[i-5] + game_keyboard2[i-5]
                                                elif i//5==2:
                                                        if j>0:
                                                            keyboard3[i-10] = '✅ '
                                                        keyboard3[i-10] = keyboard3[i-10] + game_keyboard3[i-10]
                                                elif i//5==3:
                                                        if j>0:
                                                            keyboard4[i-15] = '✅ '
                                                        keyboard4[i-15] = keyboard4[i-15] + game_keyboard4[i-15]
                                                i = i+1
                                            json_keyboard = json.dumps({'keyboard': [keyboard, keyboard2, keyboard3, keyboard4, ['Задать вопрос']],'resize_keyboard': True })
                                            send_mess(person_id, message, json_keyboard)
                                            send_mess(person_id, 'Текущие результаты!', keyboard_results)
                                            update_status = ("UPDATE bot_users SET status = %(st)s WHERE telegram_id = %(tg_id)s")
                                            mycursor.execute(update_status, {'st': 1,'tg_id': person_id})
                                            mydb.commit()
                            else:
                                message = 'Соревнование уже закончилось.'
                                if capitan:
                                    send_mess(person_id, message, keyboard_user_capitan)
                                else:
                                    send_mess(person_id, message, keyboard_user_reg)
                                update_status = ("UPDATE bot_users SET status = %(st)s WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'st': 1,'tg_id': person_id})
                                mydb.commit()
                                update_status = ("UPDATE `team_members` SET `in_game` = 0 WHERE `telegram_id` = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                else:
                    if status == 1:
                        if first_result['message']['text']=='Вопросы':
                            sql = "SELECT * FROM `questions_to_admin`"
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            if not myresult:
                                send_mess(person_id,'Новых вопросов нет.', keyboard_admin)
                            else:
                                update_status = ("UPDATE bot_users SET status = 2 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                                message = ('Перед Вами полный список оставленных пользователями вопросов. ' +
                                           'Для того, чтобы ответить на один из них, отправьте мне номер вопроса,'
                                        ' например 3 для ответа на третий вопрос.\n')
                                for i in myresult:
                                    message = message + str(i[0]) + '. ' + '*id' + str(i[1]) + '*: ' + '_' + i[2] + '_' + ';\n'
                                send_mess(person_id, message, keyboard_cancel, 'Markdown')
                        elif first_result['message']['text']=='Сообщение участникам':
                            update_status = ("UPDATE bot_users SET status = 4 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            message = ('Выберите адресатов вашего сообщения.')
                            send_mess(person_id, message, keyboard_admin_message)
                        elif first_result['message']['text']=='Зарегистрированные команды':
                            sql = ("SELECT * FROM teams")
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            if not myresult:
                                send_mess(person_id,'Зарегистрированных команд пока нет.', keyboard_admin)
                            else:
                                message = 'Список зарегистрированных команд:\n№ id_team Название команды Школа Количество'
                                j = 1
                                for i in myresult:
                                    message = message + '\n' + str(j) + '. ' + str(i[0]) + ' ' + i[1] + ' ' + i[2] + ' ' + str(i[3])
                                    j = j + 1
                                send_mess(person_id, message, keyboard_admin)
                    elif status == 2:
                        if first_result['message']['text']!='В главное меню':
                            sql = "SELECT * FROM `questions_to_admin`"
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            if ((not (first_result['message']['text']).isdigit()) or
                                               int(first_result['message']['text'])>int(myresult[len(myresult)-1][0])
                                               or int(first_result['message']['text'])<int(myresult[0][0])):
                                send_mess(person_id, 'Пожалуйста, выберите корректное значение для номера вопроса.', keyboard_cancel)
                            else:
                                send_mess(person_id,'Введите, пожалуйста, ответ на данный вопрос.', keyboard_cancel)
                                update_status = ("UPDATE questions_to_admin SET admin_id = %(tg_id)s WHERE id = %(id)s")
                                mycursor.execute(update_status, {'tg_id': person_id, 'id': int(first_result['message']['text'])})
                                mydb.commit()
                                update_status = ("UPDATE bot_users SET status = 3 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(update_status, {'tg_id': person_id})
                                mydb.commit()
                        else:
                            send_mess(person_id,'Действие отменено.', keyboard_admin)
                            update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                    elif status == 3:
                        if first_result['message']['text']!='В главное меню':
                            sql = "SELECT * FROM `questions_to_admin` WHERE admin_id=%(tg_id)s"
                            mycursor.execute(sql, {'tg_id': person_id})
                            myresult = mycursor.fetchall()
                            message = ('Поступил ответ на Ваш вопрос! Вы спрашивали:\n' + '_' +
                                       myresult[0][2] + '_' + '\n' + 'Ответ:\n' + '_' + first_result['message']['text'] + '_')
                            send_mess_nokeyboard(myresult[0][1], message, 'Markdown')
                            send_mess(person_id,'Спасибо за Ваш ответ!', keyboard_admin)
                            sql = "DELETE FROM `questions_to_admin` WHERE admin_id=%(tg_id)s"
                            mycursor.execute(sql, {'tg_id': person_id})
                            mydb.commit()
                            update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                        else:
                            send_mess(person_id,'Действие отменено.', keyboard_admin)
                            update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            update_status = ("UPDATE questions_to_admin SET admin_id = 0 WHERE admin_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                    elif status == 4:
                        if first_result['message']['text']=='Все пользователи':
                            update_status = ("UPDATE bot_users SET status = 5 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            message = ('Введите текст сообщения.')
                            send_mess(person_id, message, keyboard_admin_send)
                        elif first_result['message']['text']=='Все зарегистрированные пользователи':
                            update_status = ("UPDATE bot_users SET status = 6 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            message = ('Введите текст сообщения.')
                            send_mess(person_id, message, keyboard_admin_send)
                        elif first_result['message']['text']=='Все пользователи в игре':
                            update_status = ("UPDATE bot_users SET status = 7 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            message = ('Введите текст сообщения.')
                            send_mess(person_id, message, keyboard_admin_send)
                        elif first_result['message']['text']=='Назад':
                            update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            message = ('Действие отменено.')
                            send_mess(person_id, message, keyboard_admin)
                    elif status == 5:
                        if first_result['message']['text']!='Назад':
                            update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            sql = ('SELECT `telegram_id` FROM `bot_users`')
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            if not myresult:
                                send_mess(person_id,'У бота еще нет пользователей.', keyboard_admin)
                            else:
                                for i in myresult:
                                    send_mess_nokeyboard(i[0], first_result['message']['text'])
                                message = ('Сообщение отправлено.')
                                send_mess(person_id, message, keyboard_admin)
                        else:
                            update_status = ("UPDATE bot_users SET status = 4 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            message = ('Выберите адресатов вашего сообщения.')
                            send_mess(person_id, message, keyboard_admin_message)
                    elif status == 6:
                        if first_result['message']['text']!='Назад':
                            update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            sql = ('SELECT `telegram_id` FROM `bot_users` WHERE `is_reg` = 1')
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            if not myresult:
                                send_mess(person_id,'У бота еще нет зарегистрированных пользователей.', keyboard_admin)
                            else:
                                for i in myresult:
                                    send_mess_nokeyboard(i[0], first_result['message']['text'])
                                message = ('Сообщение отправлено.')
                                send_mess(person_id, message, keyboard_admin)
                        else:
                            update_status = ("UPDATE bot_users SET status = 4 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            message = ('Выберите адресатов вашего сообщения.')
                            send_mess(person_id, message, keyboard_admin_message)
                    elif status == 7:
                        if first_result['message']['text']!='Назад':
                            update_status = ("UPDATE bot_users SET status = 1 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            sql = ('SELECT `telegram_id` FROM `team_members` WHERE `in_game` = 1')
                            mycursor.execute(sql)
                            myresult = mycursor.fetchall()
                            if not myresult:
                                send_mess(person_id,'Никто не проходит квест.', keyboard_admin)
                            else:
                                for i in myresult:
                                    send_mess_nokeyboard(i[0], first_result['message']['text'])
                                message = ('Сообщение отправлено.')
                                send_mess(person_id, message, keyboard_admin)
                        else:
                            update_status = ("UPDATE bot_users SET status = 4 WHERE telegram_id = %(tg_id)s")
                            mycursor.execute(update_status, {'tg_id': person_id})
                            mydb.commit()
                            message = ('Выберите адресатов вашего сообщения.')
                            send_mess(person_id, message, keyboard_admin_message)
            else:
                if 'contact' in first_result['message'].keys():
                    if not is_admin:
                        if not is_reg:
                            if status == 10:
                                message = ('Регистрация успешна!')
                                send_mess(person_id, message, keyboard_user_capitan)
                                sql = ("UPDATE bot_users SET status = 1, is_reg = 1 WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(sql, {'tg_id': person_id})
                                mydb.commit()
                                sql = ("UPDATE team_members SET phone_number = %(phone)s WHERE telegram_id = %(tg_id)s")
                                mycursor.execute(sql, {'phone': first_result['message']['contact']['phone_number'],'tg_id': person_id})
                                mydb.commit()
                                sql = ("UPDATE teams SET num=num+1 WHERE creator = %(tg_id)s")
                                mycursor.execute(sql, {'tg_id': person_id})
                                mydb.commit()
                            elif status == 11:
                                sql = ("SELECT num FROM teams WHERE id = (SELECT team_id FROM team_members WHERE telegram_id = %(tg_id)s)")
                                data = ({'tg_id': person_id})
                                mycursor.execute(sql, data)
                                myresult3 = mycursor.fetchall()
                                if myresult3[0][0]>=3:
                                    message = ('Число участников данной команды достигло максимального значения. ' +
                                                   'Пожалуйста, введите идентификатор другой команды или создайте свою в главном меню.')
                                    send_mess(person_id, message, keyboard_cancel)
                                    update_status = ("UPDATE bot_users SET status = 7 WHERE telegram_id = %(tg_id)s")
                                    mycursor.execute(update_status, {'tg_id': person_id})
                                    mydb.commit()
                                    sql = ("DELETE FROM team_members WHERE telegram_id = %(tg_id)s")
                                    mycursor.execute(update_status, {'tg_id': person_id})
                                    mydb.commit()
                                else:
                                    message = ('Регистрация успешна! Вы вошли в состав команды!')
                                    send_mess(person_id, message, keyboard_user_reg)
                                    sql = ("SELECT creator FROM teams WHERE id = (SELECT team_id FROM team_members WHERE telegram_id = %(tg_id)s)")
                                    mycursor.execute(sql, {'tg_id': person_id})
                                    myresult = mycursor.fetchall()
                                    sql = ("SELECT name FROM team_members WHERE telegram_id = %(tg_id)s")
                                    mycursor.execute(sql, {'tg_id': person_id})
                                    myresult5 = mycursor.fetchall()
                                    message = ('В Вашу команду успешно добавлен *' + myresult5[0][0] + '*.')
                                    send_mess_nokeyboard(myresult[0][0], message, 'Markdown')
                                    sql = ("UPDATE bot_users SET status = 1, is_reg = 1 WHERE telegram_id = %(tg_id)s")
                                    mycursor.execute(sql, {'tg_id': person_id})
                                    mydb.commit()
                                    update_status = ("UPDATE teams SET num=num+1 WHERE creator = %(tg_id)s")
                                    mycursor.execute(update_status, {'tg_id': myresult[0][0]})
                                    mydb.commit()
                                    sql = ("UPDATE team_members SET phone_number = %(phone)s WHERE telegram_id = %(tg_id)s")
                                    mycursor.execute(sql, {'phone': first_result['message']['contact']['phone_number'],'tg_id': person_id})
                                    mydb.commit()
                                    if myresult3[0][0] == 1:
                                        insert_team = ("INSERT INTO tournament (team_id) "
                                                       "VALUES (%(team_id)s)")
                                        sql = ("SELECT team_id FROM team_members WHERE telegram_id = %(tg_id)s")
                                        mycursor.execute(sql, {'tg_id': person_id})
                                        myresult = mycursor.fetchall()
                                        mycursor.execute(insert_team, {'team_id': myresult[0][0]})
                                        mydb.commit()
                                
                                
                            
            k = k+1
            if 'text' in first_result['message'].keys():
                try:
                    print(str(datetime.datetime.utcfromtimestamp(first_result['message']['date'])) + ' '
                          + first_result['message']['from']['first_name']+': '+first_result['message']['text'] + ' ' + str(int(time.time())-first_result['message']['date'])) 
                except UnicodeEncodeError:
                    print(str(datetime.datetime.utcfromtimestamp(first_result['message']['date'])) + ' '
                          + first_result['message']['from']['first_name']+': '+'Unsupported text (smile)')
            else:
                print(str(datetime.datetime.utcfromtimestamp(first_result['message']['date'])) + ' '
                      + first_result['message']['from']['first_name']+': '+'No text')
        get_updates_json(request, results[k-1]['update_id']+1)
        

def main():
    mydb = mysql.connector.connect(
      host="energy-storm.com.ua",
      user="energ2_telegram_bot_admin",
      passwd="Fef2020*",
      database="energ2_telegram_bot_test"
    )
    mycursor = mydb.cursor()
    while True:
        bot_messages(url, mycursor, mydb)
        
main()
