# импорт необходимых библиотек

def forecast(text: dict) -> dict:
    '''Логика педсказания'''
    res = {
        'group': 'group',
        'sub': 'sub',
        'location': 'location',
        'department': 'department',
        'text': text['text']
    }
    return res
