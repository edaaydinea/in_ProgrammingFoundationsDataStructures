user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


# Create a function that takes in a dictionary and creates a new dictionary without the empty values.
def update_preferences(user_pref):
    updated_preferences = {}
    for key, value in user_pref.items():
        if value is not None:
            updated_preferences[key] = value


print(update_preferences(user_preferences))
