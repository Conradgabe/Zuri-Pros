class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, add_name):
        self.name = add_name
        print(f'Your name is {self.name}')
    def change_age(self, add_age):
        self.age = add_age
        print(f'Your age is {self.age}')
    def add_track(self, track):
        self.tracks.append(track)
        print(f'This are your tracks {self.tracks} ')
    def get_score(self):
        print(f"Your final score is {self.score}")



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
