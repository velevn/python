user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}


def check_user(username, password):
    for i in user_database:
        if username == i:
            password == user_database[i]
            return True
        else:
            return False
