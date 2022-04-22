from office_app.models import Physician

class PhysicianClass:
    def __init__(self, first_name, last_name, speciality):
        self.first_name = first_name
        self.last_name = last_name
        self.speciality = speciality

    def save_details(self):
        physician = Physician.objects.create(first_name=self.first_name, last_name=self.last_name, speciality=self.speciality)
        return f"{physician.first_name, physician.last_name} with {physician.problem} saved to the db"