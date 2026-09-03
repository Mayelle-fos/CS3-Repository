class Lab:
    def __init__(self, room_number):
        self.room_number = room_number


class Technician:
    def __init__(self, name):
        self.name = name
        self.assigned_lab = None

    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj


# Create the Lab
chem_lab = Lab("302")

# Create the Technician
mr_cruz = Technician("Mr. Cruz")

# Assign the lab to the technician
mr_cruz.assign_lab(chem_lab)

# Access the lab's room number through the technician
print(mr_cruz.assigned_lab.room_number)