class Cat:
    def __init__(self, name='', gender='', age=0, breed=''):
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed

    def get_from_dict(self, cat_from_dict):
        self.name = cat_from_dict.get('name')
        self.gender = cat_from_dict.get('gender')
        self.age = cat_from_dict.get('age')
        self.breed = cat_from_dict.get('breed')

================================================================================ 
Cats = [{"breed": "siberian",
         "gender": 'boy',
         "name": "Sam",
         "age": 2},
        {"breed": "abyssinian",
         "gender": 'boy',
         "name": "Bob",
         "age": 1},
        {"breed": "british",
         "gender": 'girl',
         "name": "Ciara",
         "age": 3},
        {"breed": "scottish",
         "gender": 'girl',
         "name": "Liz",
         "age": 1}]

from <file> import Cat

for cat in Cats:
    cat_obj = Cat()
    cat_obj.get_from_dict(cat)
    print(cat_obj.name, cat_obj.gender, cat_obj.age, cat_obj.breed)
