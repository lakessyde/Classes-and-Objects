from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('hello i am', self.name)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
