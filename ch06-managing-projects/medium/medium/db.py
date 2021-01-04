def connect(*args, **kwargs):
    # Here goes some code to connect to a DB
    print("Successfully connected")


def get_users():
    # Mock reading users from a DB table
    return [
        {"name": "Alice", "city": "San Francisco"},
        {"name": "Bob", "city": "Chicago"},
    ]
