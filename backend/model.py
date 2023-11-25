# импорт необходимых библиотек

def forecast(message: str) -> dict:
    '''Логика педсказания'''
    print(message)
    res: dict = {
        'group': 'group',
        'sub': 'sub',
        'location': 'location',
        'department': 'department',
        'text': message,
    }
    return res
