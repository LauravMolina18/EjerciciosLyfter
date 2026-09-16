from datetime import date


class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


def adults_only(func):
    def wrapper(user):
        if user.age < 18:
            raise ValueError("User must be at least 18 years old")

        return func(user)

    return wrapper


@adults_only
def show_user(user):
    print(f"User age: {user.age}")


my_user = User(date(2000, 5, 10))

show_user(my_user)