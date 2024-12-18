class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_firstname(self):
        print("Имя:", self.first_name)

    def print_lastname(self):
        print("Фамиля:", self.last_name)

    def print_fullname(self):
        print("Полное имя:", self.first_name, self.last_name)


vasily = User("Василий", "Иванов")

vasily.print_firstname()
vasily.print_lastname()
vasily.print_fullname()
