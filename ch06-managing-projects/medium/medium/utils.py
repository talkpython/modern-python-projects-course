def list_users(users):
    return "Users: \n* " + "\n* ".join([f"{user['name']} from {user['city']}" for user in users])

