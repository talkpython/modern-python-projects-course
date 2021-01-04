from medium.db import connect, get_users
from medium.utils import list_users


def main():
    # Connect to a DB
    connect()
    # Print users' information
    users = get_users()
    print(list_users(users))


if __name__ == "__main__":
    main()
