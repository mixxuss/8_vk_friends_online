import vk
import getpass


APP_ID = 5826559


def get_user_login():
    return input('Enter login: ')


def get_user_password():
    return getpass.getpass(prompt='Enter password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    online_list = api.users.get(user_ids=friends_online_ids)
    return online_list


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['last_name'], friend['first_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)

