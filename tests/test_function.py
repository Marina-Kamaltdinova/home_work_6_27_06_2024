from datetime import time


def test_dark_theme_by_time():
    current_time = time(hour=23)

    if time(hour=22) <= current_time or current_time < time(hour=6):
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True

    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """

    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """

    def is_dark_theme(current_time=time(hour=16), dark_theme_enabled_by_user=True):
        if dark_theme_enabled_by_user is None:
            if current_time.hour >= 22 or current_time.hour < 6:
                return True
            else:
                return False
        else:
            return dark_theme_enabled_by_user

        # TODO переключите темную тему в зависимости от времени суток,
        #  но учтите что темная тема может быть включена вручную

    assert is_dark_theme(current_time=time(hour=16), dark_theme_enabled_by_user=True) is True
    assert is_dark_theme(current_time=time(hour=16), dark_theme_enabled_by_user=False) is False
    assert is_dark_theme(current_time=time(hour=16), dark_theme_enabled_by_user=None) is False
    assert is_dark_theme(current_time=time(hour=23), dark_theme_enabled_by_user=None) is True
    assert is_dark_theme(current_time=time(hour=22), dark_theme_enabled_by_user=None) is True
    assert is_dark_theme(current_time=time(hour=6), dark_theme_enabled_by_user=None) is False


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"

    for user in users:
        if user['name'] == 'Olga':
            suitable_users = user

            assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет

    suitable_users = []
    for user in users:
        if user['age'] < 20:
            suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = read_function(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = read_function(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = read_function(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


def read_function(function, *args):
    func = function.__name__.replace('_', ' ').title()
    arg = ", ".join([*args])
    print(f"{func} [{arg}]")
    return f"{func} [{arg}]"
