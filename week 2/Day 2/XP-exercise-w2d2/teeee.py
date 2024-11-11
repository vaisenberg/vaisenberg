class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def get_family_details(self):
        return self.members

    def family_presentation(self):
        # Print the family last name and details of all members
        print(f"Family Last Name: {self.last_name}")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Power: {member['power']}, Incredible Name: {member['incredible_name']}")

    def born(self, name):
        new_baby = {
            'name': name,
            'age': 0,
            'gender': 'Unknown',
            'is_child': True,
            'power': 'Unknown Power',
            'incredible_name': f'Baby{name}'
        }
        self.members.append(new_baby)

class TheIncredibles(Family):
    def __init__(self, members, last_name="SuperHeroesISR"):
        super().__init__(members, last_name)
        
    def use_power(self, member_name):
        member_found = False
        for member in self.members:
            if member['name'] == member_name:
                member_found = True
                if member['age'] >= 18:
                    print(f"{member['name']} uses their power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old, cannot use power.")
        if not member_found:
            print(f"Member named {member_name} not found in the family.")
    
    def incredible_presentation(self):
        print("Here is our powerful family:")
        print(f"Last Name: {self.last_name}")
        super().family_presentation()
members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'},
    {'name': 'Jack', 'age': 16, 'gender': 'Male', 'is_child': True, 'power': 'super speed', 'incredible_name': 'Speedster'}
]


incredible_family = TheIncredibles(members)
incredible_family.incredible_presentation()
incredible_family.born('Jack')
print("\nAfter adding Baby Jack:")
incredible_family.incredible_presentation()
