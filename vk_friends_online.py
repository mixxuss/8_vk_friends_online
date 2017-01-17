import vk


APP_ID = 5826559


def get_user_login():
    return input('Enter login: ')


def get_user_password():
    return input('Enter password:')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    return api.friends.getOnline


def output_friends_to_console(friends_online):
    print(friends_online)

if __name__ == '__main__':
    # login = get_user_login()
    # password = get_user_password()
    friends_online = get_online_friends('mixxuss@gmail.com', 'Arshavin-93')
    type(friends_online)
    # output_friends_to_console(friends_online)
