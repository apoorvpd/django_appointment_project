from django.test import TestCase
from office_app.models import Physician

class PhysicianUnitTestSuite(TestCase):
    def setUp(self):
        self.nigel = Physician.objects.create(first_name='Nigel', last_name='Parris', speciality='Cardiologist')
        self.jacey = Physician.objects.create(first_name='Jacey', last_name='Kellen', speciality='Cardiologist')
        self.anna = Physician.objects.create(first_name='Annabelle', last_name='Jasper', speciality='Cardiologist')

        self.luke = Physician.objects.create(first_name='Luke', last_name='Peyton', speciality='Pediatrician')
        self.edytha = Physician.objects.create(first_name='Edytha', last_name='Melesina', speciality='Pediatrician')


    def test_list_cardiologist_length(self):
        cardiologists_list = Physician.objects.filter(speciality='Cardiologist')
        self.assertEqual(len(cardiologists_list), 3)

    def test_list_cardiologist_names(self):
        cardiologists_list = list(Physician.objects.filter(speciality='Cardiologist'))
        self.assertEqual(cardiologists_list, [self.nigel, self.jacey, self.anna])


    def test_list_pediatrician_length(self):
        pediatricians_list = Physician.objects.filter(speciality='Pediatrician')
        self.assertEqual(len(pediatricians_list), 2)


    def test_list_pediatrician_names(self):
        pediatricians_list = list(Physician.objects.filter(speciality='Pediatrician'))
        self.assertEqual(pediatricians_list, [self.luke, self.edytha])

    def test_edit_last_name(self):
        self.nigel.last_name = 'Donny'
        self.assertEqual(str(self.nigel), 'First Name: Nigel, Last Name: Donny')

    def test_delete_cardiologist(self):
        self.nigel.delete()
        self.assertEqual(len(list(Physician.objects.filter(speciality='Cardiologist'))), 2)
        cardiologists_list = list(Physician.objects.filter(speciality='Cardiologist'))
        self.assertEqual(cardiologists_list, [self.jacey, self.anna])