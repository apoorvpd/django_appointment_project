from django.db import models

# Create your models here.

# SPECIALITY_CHOICES = (
#     ('Cardiologist', 'Cardiologist'),
#     ('Pediatrician', 'Pediatrician'),
#     ('Radiologist', 'Radiologist'),
# )

class Speciality(models.TextChoices):
    Cardiologist = 'Cardiologist'
    Pediatrician = 'Pediatrician'
    Radiologist = 'Radiologist'


class Physician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50, choices=Speciality.choices)

    def __str__(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name}"


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    problem = models.TextField()
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE, null=True)


class Appointment(models.Model):
    physician = models.ForeignKey(Physician, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()

class Secretary(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)