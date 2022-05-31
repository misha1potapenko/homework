translate = {
    'one': 'один',
    'two': 'два',
    'free': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}



def num_translate(num):
    try:
        print(translate[num])
    except:
        print(None)



num_translate('six')
num_translate('nine')
num_translate('ten')
num_translate('tenee')


