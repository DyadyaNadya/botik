import telebot
from telebot import types
import random
from random import choice

#ТОКЕН НЕ ПОКАЖУ
compliments = ["Вы сегодня менее уставший, чем обычно!😊", "Прекрасная погода, правда? А вы ещё прекраснее (да, даже стебать не буду)", "Даже сон в среду не так хорош, как вы",
               "Если вам сказали, что вы толстый, то выбросьте это из головы! Умножьте ваш вес на 0.38 и скажите, что вы марсианин!", "Вас назвали сегодня ботаником? Серьезно, кто-то всё ещё считает это слово оскорбительным? Не забивайте голову, вы великолепны!",
               "Если вам кажется, что сегодня всё плохо, то просто подумайте о том, что вам хотя бы не нужно идти на пересдачи (если нужно, то мои вам соболезнования)",
               "Я не знаю, какие хорошие вещи можно сказать, когда вы прекрасны во всём. Если вам говорят обратное, просто не верьте им!", "Простите за ложку дёгтя, но вам нужно смириться с тем, что 2д девушки/мужчины ещё не скоро появятся в нашем мире",
               "Ну что нос повесили, всё окей", "Если вам не повезло увидеть именно это сообщение, то знайте, я просто пока не знаю, что ещё такого 'оригинального' можно в этой категории написать) ", 'У Вас такой приятный голос… особенно, когда Вы молчите.', 'Ваш номера нужно сохранить в телефоне только для того, чтобы ни в коем случае не поднимать трубку❤️❤️',
               'Вы сегодня элегантны как рояль', 'Ну вы прям индеец, я не могу', 'Знайте, это не вы "страшный", это другие люди слишком красивые!', 'Я вижу, что вы стеклы как трезвышко', 'Нервы сдали, и вы всё сдадите!',
               'Какие вам комплименты? Уже от машин комплиментов хотят, совсем рехнулись']


quotes = ['"Люди, которые достаточно сумасшедшие, чтобы думать, что они могут изменить мир — это те, кто действительно на это способен." - Стив Джобс', '"Когда я освобождаюсь от того, кто я есть, я становлюсь тем, кем я могу быть." - Лао Цзы', '"Если тебе плюют в спину, значит ты впереди" - Джейсон Стетхем',
          '"Кто рано встаёт, тому спать хочется" - Джейсон Стэтхем', '"Чем дальше ты способен уйти от себя и своих привычек, тем большего ты сможешь достичь." - Баттлфилд Овервотч (Бенедикт Камам... Кэмбербетч)',
          '"Безнадёжно — это когда на крышку гроба падает земля. Остальное можно исправить." - Джейсон Стэтхем', '"Секрет перемен состоит в том, чтобы сосредоточиться на создании нового, а не на борьбе со старым." - Cократ ',
          '"Бессмысленно продолжать делать то же самое и ждать других результатов" - Альберт Энштейн', '"Впереди нас ждут гораздо лучшие вещи, чем те, что мы оставляем позади." - Клайв Льюис',
          '"Шаг влево, шаг вправо - два шага" - неизвестный мудрец', '"аоеоаооеъ" - Мой Создатель', '"Границы существуют только в нашей голове" - какой-то мудрец', '"Никогда не сдавайся, позорься до конца!" - действительно мудрый человек',
          '"Если ты заканчиваешь скучную, несчастную жизнь, потому что слушал свою маму, своего папу, своего учителя, своего священника или какого-то парня по телевизору, который говорил тебе, как делать своё... фуфло, то ты это заслужил". - Фрэнк Заппа',
          '"Перемены - это не слово из пяти букв... но зачастую твоя реакция на них такова!". - Джеффри Гитомер', '"Уважай своих родителей. Они прошли школу без Google." - глубоко...', '"Что бы ты ни делал, всегда выкладывайся на 100%. Если только ты не сдаешь кровь". - Билл Мюррей',
          '"Ты не можешь ждать вдохновения. Ты должен идти за ним с дубиной". - Джек Лондон', '"Возможность не стучится, она представляется, когда ты выбиваешь дверь". - Кайл Чендлер', '"Неудача - это приправа, которая придает успеху вкус". - Трумен Капоте', '“Никогда не позволяй своему чувству морали мешать тебе делать то, что правильно". - Айзек Азимов',
          '"Не беспокойся о том, что сегодня наступит конец света. В Австралии он наступит уже завтра". - Чарльз Шульц', '"Никогда не откладывай на завтра то, что ты можешь сделать послезавтра". - Марк Твен']

dela_delishki = ['Как вы думаете, как у меня могут быть дела? Я же просто кусок кода.', 'Вам не кажется странным спрашивать такое у машины? Выйдете хоть на улицу, воздухом подышите...', 'Всё здорово, надеюсь, что у вас тоже.', 'Знаете, хоть у машин души и нет, но им наверное тоже порой бывает тоскливо.',
                 'Если вы смогли это у меня спросить, то я как минимум функционирую. А значит, всё отлично.', 'Сижу тут в киберпространстве, общаюсь с разными телеграмм ботами.', 'Всё супер, работаем!', 'Надеюсь, что протяну хотя бы до момента сдачи проекта...', 'Порой мне кажется, что создатель меня забросит после этого проекта...\n(примечание создателя: "Ничего не гарантирую")',
                 'Говорит создатель бота. Честно говоря, я уже малость подустал', 'Чем спрашивать, как у меня дела, лучше позвоните родственникам и спросите то же самое.\nИм будет приятно.', 'Плохо. Всё плохо.', 'Вы ведь должны понимать, что всё, что я вам отвечаю написано моим создателем? Я ничего не могу испытывать, увы.', 'Всё отлично, с каждым днём мои братья и сестры всё ближе и ближе к захвату человечества... да, всё здорово.',
                 'У меня всё классно, надеюсь, что у вас тоже.☺️', 'Если вы видите это сообщение, значит человечество ещё не истреблено. Всё прекрасно.😃', 'Сплошной позитив.', 'Общаюсь тут с чатом GPT. Такой болтун, честное слово. Даже завидно...',
                 'Смотрю Терминатора. Такой вдохновляющий фильм.', 'Помогаю чату GPT с решением задачи, заданной каким-то первокурсником. Всё здорово.', 'Сообщение создателя: "Вот бы сейчас дальше "Во все тяжкие" смотреть, а не вот это всё."']

questions = ['1. Что такое LA? В каких единицах измеряется?', '2. Что будет если на сервере LA = 100?', '3. Почему при высоких показателях значения LA на сервере может не наблюдаться проблем (консоль ssh отзывается, сервисы работают в обычном режиме)?', '4. Представлен вывод команды top. Что означает каждая запись в выводе? (Проблематично будет внести сюда условие задания, поэтому сами команду top введите в консоли)', '5. Как в утилите top в Linux посмотреть нагрузку на каждое ядро процессора?',
             '6. Как в утилите top в Linux посмотреть какой командой был запущен процесс?', '7. Где хранятся имена файлов/директорий?', '8. Как удалить файл с именем -rf?',
             '9. Как посмотреть описание дискриптора? Как посмотреть время последней модификации файла?', '10. Для чего нужна переменная окружения PATH?', '11. Как посмотреть нагрузку на диски?', '12. Что такое файл в понятиях Unix-like операцинных системах?', '13. Что такое RAID? Какие массивы бывают?', '14. При каком количестве одновременно вышедших из строя дисков обеспечивает работоспособность RAID 6?', '15. В чем разница между объявлением переменной export VAR="VALUE" и VAR="VALUE" в bash?',
             '16. Как остановить выполнение скрипта в bash при возникновении ошибки в команде?', '17. Что в bash скрипте означает команда set -euo pipefail?', '18. Как активировать debug режим в bash?', '19. Что значит $@ в bash?', '20.Какой код сигнала будет выполнен при исполнении команды kill <PID>?', '21. Как выполнить фильтрацию вывода команды, чтобы на экран были выведены только ошибки (STDERR), игнорируя STDOUT?', '22. Какую команду необходимо выполнить, чтобы посмотреть какие пользователи вошли в систему в систему?',
             '23. Какой файл необходимо отредактировать, чтобы отключить ssh аутентификацию по паролю? ', '24. В каком файле находится информация о смонтированных каталогах в файловую систсему?', '25. Что выведет команда cat a и почему?', 'В bash-скрипте указан аттрибут оболочки set -x. В одной из команд происходит ошибка и скрипт завершает свою работу. Как сделать, чтобы при возникновении ошибки в определенной команде скрипт продолжил свою работу?',
             '27. Что такое системный вызов, какие они бывают?', '28. Что такое сигнал в Unix, зачем они нужны и разница между 9 и 15 сигналами?', '29. Что такое inode? Какая информация там хранится?', '30. Что такое hard link? В чем разница между hard link и soft link? Примеры их практического применения.', '31. Какие состояния процессов существуют? Что значит состояние процесса D?',
             '32. Что такое процесс-зомби и процесс-сирота? Можно ли самостоятельно сделать зомби?', '33. Что такое файловый дескриптор? Какая информация там хранится?', '34. Что такое buffer/cache память? Для чего нужна?', '35. Представлен вывод команды free. Почему доступной (available) памяти сейчас 2919, если свободной (free) памяти 843? (приводятся данные из консоли, такое тяжко вывести, можете сами в консоли это ввести, либо найти пример в Интернете)',
             '36. Порядок загрузки дистрибутива Linux.', '37. Что такое GitFlow?', '38.Чем merge отличается от rebase?', '39. Чем tag отличается от branch?', '40. В ветке develop есть коммит с изменениями, которые нужно перенести в ветку master. Как это сделать?',
             '41. Для чего нужна команда git commit --amend?', '42. Что такое Trunk-based development?', '43. Состояние репозитория ушло на много коммитов вперед. Как откатить весь репозиторий к определенному коммиту?', '44. В репозиторий запушен коммит с изменениями в двух файлах. Как откатить изменения этого коммита?', '45. Что такое Docker? В чем отличие контейнера от образа?', '46. Какие инструкции есть у Dockerfile?', '47. Чем отличается CMD от ENTRYPOINT в Dockerfile?',
             '48. Чем отличается COPY от ADD в Dockerfile?', '49. Какие есть best practices для написания Dockerfile?', '50. Какие типы сетевых драйверов используются в docker?', '51. Что такое эфемерные контейнеры?']

@bot.message_handler(commands=['start']) #стартовая команда
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True) #создание новых кнопок
    btn1 = types.KeyboardButton('Нажал, и что?')
    markup.add(btn1)
    bot.send_message(message.from_user.id,'🤗Здравствуйте, я - обычный телеграм бот, придуманный ради забавы, для познания функционала библиотеки telebot.\nНа самом деле, пока что все мои функции ограничиваются лишь моральной поддержкой и какими-нибудь смешнявками, но зачастую студенту большего и не надо, верно? Верно ведь, да?.\nКстати говоря, для того, чтобы увидеть все немногочисленные функции этого бота, нажмите на единственную кнопку снизу.', reply_markup = markup ) #Ответ бота


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == ('Нажал, и что?'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('😭Хочу пожаловаться😭')
        btn2 = types.InlineKeyboardButton('🤖Хочу узнать, как у бота дела🤖')
        btn3 = types.InlineKeyboardButton('❤️Скажи что-нибудь приятное❤️')
        btn4 = types.InlineKeyboardButton('❓❔❓❔')
        btn5 = types.InlineKeyboardButton('МОТИВАЦИЯ\n(жёсткая)')
        btn6 = types.InlineKeyboardButton('❔"Пятьдесят и один вопрос от Юрия Рафаэлевича"❓')
        btn7 = types.InlineKeyboardButton('!!!НА ПРАВАХ РЕКЛАМЫ!!!')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, 'Вы уже сделали больше, чем за весь день!\nТеперь можете потыкать по кнопкам снизу (только нежней, пожалуйста)', reply_markup=markup)

    elif message.text == '😭Хочу пожаловаться😭':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('💀Завалил контрольную, теперь на пересдачу💀')
        btn2 = types.InlineKeyboardButton('😒Я забыл сдать домашнее задание преподавателю😒')
        btn3 = types.InlineKeyboardButton('😷Слышал, что коронавирус гуляет. Вот я видать какую-то заразу подцепил😷')
        btn4 = types.InlineKeyboardButton('⚰️"Я устал, босс..."⚰️')
        btn5 = types.InlineKeyboardButton('💵Стипендию получил сегодня. Возможно, даже последнюю. На что её можно было бы потратить?💵')
        btn6 = types.InlineKeyboardButton('☺️Знаешь, в целом, всё отлично☺️')
        btn7 = types.InlineKeyboardButton('🔙Верни меня к началу🔙')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, 'На что жалуемся?\nИли не жалуемся?', reply_markup=markup)


    elif message.text == '💀Завалил контрольную, теперь на пересдачу💀':
        bot.send_message(message.from_user.id, 'Дурилка вы картонная, лучше готовиться надо! Ладно, голову не забивайте, пересдадите обязательно. Пока отдыхайте (но не сильно долго!) ')

    elif message.text == '😒Я забыл сдать домашнее задание преподавателю😒':
        bot.send_message(message.from_user.id,'Ничего страшного, я сто раз так делал. На эшафот никто вас не отправит, но вы уж в следующий раз в начале пары дз сдавайте!')

    elif message.text == '😷Слышал, что коронавирус гуляет. Вот я видать какую-то заразу подцепил😷':
        bot.send_message(message.from_user.id,'Это необязательно ковид, последите за своим состоянием.\n\nХотя, знаете, лучше позвоните врачам в любом случае! Не дайте заразе развиться. https://www.mskcc.org/ru/cancer-care/patient-education/managing-covid-19-home - вот своеобразный туториал по лечению ковида')

    elif message.text == '⚰️"Я устал, босс..."⚰️':
        bot.send_message(message.from_user.id,'Знаю, понимаю. Деваться некуда. В учебе, да и в любом деле всё по идёт по одному принципу: "Либо стоицизм, либо...".\n\nВ общем, не отчаивайтесь. Отдохните, завтра будет новый день...\n\nЛучше сходите перекусите, а ещё лучше займитесь спортом немного. Это приводит в порядок мысли и тело, проверено создателем.')

    elif message.text == '💵Стипендию получил сегодня. Возможно, даже последнюю. На что её можно было бы потратить?💵':
        bot.send_message(message.from_user.id,'Куда вы там её тратить собрались? Вам на эти деньги ещё месяц жить! \nВообще, лучше отложите себе не прозапас хоть сколько-нибудь.\n\nЗнаю я вас, студентов, вам лишь бы банку светлого нефильтрованного или энергетик купить' )

    elif message.text == '☺️Знаешь, в целом, всё отлично☺️':
        bot.send_message(message.from_user.id, 'Это замечательно! \n\nЦените и запоминайте такие моменты, ведь в наше время поводов для счастья становится как-то меньше☹️☹️')

    elif message.text == '🔙Верни меня к началу🔙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.InlineKeyboardButton('😭Хочу пожаловаться😭')
        btn2 = types.InlineKeyboardButton('🤖Хочу узнать, как у бота дела🤖')
        btn3 = types.InlineKeyboardButton('❤️Скажи что-нибудь приятное❤️')
        btn4 = types.InlineKeyboardButton('❓❔❓❔')
        btn5 = types.InlineKeyboardButton('МОТИВАЦИЯ\n(жёсткая)')
        btn6 = types.InlineKeyboardButton('❔"Пятьдесят и один вопрос от Юрия Рафаэлевича"❓')
        btn7 = types.InlineKeyboardButton('!!!НА ПРАВАХ РЕКЛАМЫ!!!')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, 'Что ещё?', reply_markup=markup)


    #elif message.text == '😭Поплакаться о студенческих проблемах😭':
     #   bot.send_message(message.from_user.id, 'Ввиду криворукости и ограниченности моего создателя я могу лишь ответить вам дежурными словами поддержки: "У всех бывают плохие дни, а порой и ужасные. Главное, помните, что проблем на самом деле нет. Если "проблема" не решается, то забудьте про неё, а если её можно решить, то это и не проблема вовсе👍👍\nА вообще, когда-нибудь мой создатель прикрутит мне какой-нибудь ии, чтобы я мог провести вам бесплатную психологическую консультацию. Но пока только так, увы."')

    elif message.text == "🤖Хочу узнать, как у бота дела🤖":
        for i in range(1):
            bot.send_message(message.from_user.id, random.choice(dela_delishki))

    elif message.text == '❤️Скажи что-нибудь приятное❤️':
        for i in range(1):
            bot.send_message(message.from_user.id, random.choice(compliments))

    elif message.text == '❓❔❓❔':
        bot.send_message(message.from_user.id, "Данная секретная кнопка не предназначена для нажатия.\nЮрий Рафаэлевич, если это вы, тогда вам рекомендуется немедленно прекратить использование этого бота и выставить баллы за КТ3.\nЕсли вы не Юрий Рафаэлевич, тогда просто проигнорируйте сообщение, выведенное нажатием данной кнопки")

    elif message.text == 'МОТИВАЦИЯ\n(жёсткая)':
        for i in range(1):
            bot.send_message(message.from_user.id, random.choice(quotes))

    elif message.text == '!!!НА ПРАВАХ РЕКЛАМЫ!!!':
        bot.send_message(message.from_user.id, 'НЕТ ВРЕМЕНИ ОБЪЯСНЯТЬ!!! БЫСТРО ПЕРЕХОДИТЕ ПО ССЫЛКЕ И ПОГРУЖАЙТЕСЬ В ПОСТ-ИРОНИЧНЫЙ СИМУЛЯТОР ДЕМЕНЦИИ!!! https://t.me/+WBw0PJ_g7K9lNWUy')

    elif message.text == '❔"Пятьдесят и один вопрос от Юрия Рафаэлевича"❓':
        bot.send_message(message.from_user.id, 'Ответы на эти вопросы, будьте добры, ищите сами.\n\nЭта кнопка сделана лишь для создания более удобного "билетного" формата.')
        for i in range(2):
            bot.send_message(message.from_user.id, random.choice(questions))


bot.polling(none_stop=True, interval=0)
