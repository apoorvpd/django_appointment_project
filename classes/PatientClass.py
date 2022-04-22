from office_app.models import Patient

class PatientClass:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def specify_problem(self, problem):
        self.problem = problem

    def save_details(self):
        patient = Patient.objects.create(first_name=self.first_name, last_name=self.last_name, age=self.age, problem=self.problem)
        return f"{patient.first_name, patient.last_name} with {patient.problem} saved to the db"
