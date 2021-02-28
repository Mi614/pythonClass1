num_dict = {'zero': 'ноль',
            'one': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'четыре',
            'five': 'пять',
            'six': 'шеть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять'}


def num_translate(num_eng, **kwargs):
    google_translate = kwargs
    x = google_translate.get(num_eng.lower())
    if num_eng.istitle():
        return x.capitalize()
    else:
        return x


user_input = num_translate(num_eng=input('Введите число: '), **num_dict)
print(user_input)
