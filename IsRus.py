from re import search


def is_rus_text(text=''):
        template = r'[а-я0-9 .,-_!?<>{}\[\]()]*'
        if text == '':
                text = input('Введите текст: ')
        text = text.lower()  # Приведение текста к одному регистру
        parse = search(template, text)  # Поиск строки по шаблону
        # parse будет искать все вхождения руских букв, цифр и знаков препинания из шаблона
        # если найденный текст совпадает с длиной исходного текста - исходный текст
        return len(text) == parse.end()  # полностью русский


assert (is_rus_text('Привет') == True)

assert (is_rus_text('Чо как?))0)') == True)

assert (is_rus_text('How do u do?') == False)

assert (is_rus_text('あなたは蓮の花') == False)

assert (is_rus_text(' ') == True)

assert (is_rus_text(r'Люб, лю п0куш\\\ать') == True)
