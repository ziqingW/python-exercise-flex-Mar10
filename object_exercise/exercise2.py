class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def print_info(self):
        print(self.year, self.make, self.model)
    
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.greeted = []
    
    def __str__(self):
        return 'Person {}: {}, {}'.format(self.name, self.email, self.phone)
    
    def greet(self, other_person):
        self._greet(other_person)
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        
    def _greet(self, other_person):
        self.greeting_count += 1
        self.greeted.append(other_person)
        
    def num_unique_people_greeted(self):
        print(len(set(self.greeted)))
        
    def print_contact_info(self):
        print("{0}'s email: {1}, {0}'s phone number: {2}.".format(self.name, self.email, self.phone))
    
    def add_friend(self, friend):
        self.friends.append(friend)
        
    def num_friends(self):
        return len(self.friends)
    
car = Vehicle('Nissan', 'Leaf', 2015)
print(car.make, car.model, car.year)
car.print_info()

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
dee_ann = Person("Dee Ann", "deeann@yahoo.com", "345-456-0987")
sonny.print_contact_info()
jordan.add_friend(sonny)
print(jordan.num_friends())
print(sonny.greeting_count)
sonny.greet(jordan)
print(sonny.greeting_count)
sonny.greet(jordan)
print(sonny.greeting_count)
print(jordan)
print(sonny)
print("=" * 20)
sonny.num_unique_people_greeted()
sonny.greet(jordan)
sonny.num_unique_people_greeted()
sonny.greet(jordan)
sonny.num_unique_people_greeted()
sonny.greet(dee_ann)
sonny.num_unique_people_greeted()
