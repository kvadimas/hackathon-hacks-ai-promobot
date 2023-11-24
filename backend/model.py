# импорт необходимых библиотек

def forecast(message: str) -> dict:
    '''Логика педсказания'''
    res: dict = {
        'group': 'group',
        'sub': 'sub',
        'location': 'location',
        'department': 'department',
        'text': message,
    }
    return res
