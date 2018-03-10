class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
sonny.greet(jordan)
jordan.greet(sonny)
print("{0}'s email address: {1}, \n{0}'s number: {2}.".format(sonny.name, sonny.email, sonny.phone))
print("{0}'s email address: {1}, \n{0}'s number: {2}.".format(jordan.name, jordan.email, jordan.phone))