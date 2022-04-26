from django.test import TestCase
from django.test import Client
from office_app.models import Physician, Secretary, Patient

class TestPhysicianCreationSuite(TestCase):
    def setUp(self):
        self.client = Client()
        self.secretary = Secretary.objects.create(username='admin', password='admin')

    def test_no_physicians(self):
        response = self.client.post('/', {'username': self.secretary.username, 'password': self.secretary.password})
        self.assertEqual(response.url, '/appointments/')

        response = self.client.get('/add_physician/', {'username': self.secretary.username})
        self.assertEqual(response.context['error'], 'No Physician exist yet...')

    def test_initial_physician_creation(self):
        response = self.client.post('/', {'username': self.secretary.username, 'password': self.secretary.password})
        self.assertEqual(response.url, '/appointments/')

        response = self.client.get('/add_physician/', {'username': self.secretary.username})
        self.assertEqual(response.context['error'], 'No Physician exist yet...')

        self.physician = Physician(first_name='john', last_name='doe', speciality='Cardiologist')
        response = self.client.post('/add_physician/', {'first_name': self.physician.first_name, 'last_name': self.physician.last_name, 'speciality': self.physician.speciality})
        self.assertEqual(response.context['message'], "('john', 'doe') with Cardiologist saved to the db")

        response = self.client.get('/list_physician/', {'username': self.secretary.username})
        all_physicians = []
        for i in response.context['physicians']:
            all_physicians.append(str(i))
        self.assertEqual(all_physicians, [str(self.physician)])