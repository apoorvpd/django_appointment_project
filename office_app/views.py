from django.shortcuts import render, redirect
from django.views import View
from office_app.models import Patient, Physician, Appointment, Secretary, Speciality
from classes.SecretaryClass import SecretaryClass
from classes.PhysicianClass import PhysicianClass
from classes.PatientClass import PatientClass

# Create your views here.
class Home(View):
    def get(self, request):
        #  For the get method of home, clear the current user as the first line of code. So going to the home page (via get) is equivalent to logging out.
        request.session.pop("username", None)
        return render(request, "main/home.html", {})

    def post(self, request):
        try:
            secretary = Secretary.objects.get(username=request.POST['username'])
        except Secretary.DoesNotExist:
            return render(request, "main/home.html", {'error': 'Something went wrong...'})

        if secretary.password == request.POST['password']:
            request.session['username'] = request.POST['username']
            return redirect('appointments')

        return render(request, "main/home.html", {'error': 'username/password incorrect'})

class AppointmentView(View):
    def get(self, request):
        if not request.session.get("username"):
            return redirect("home")

        appointments = Appointment.objects.all()

        if len(appointments) < 1:
            return render(request, "main/appointment.html", {"error": 'No appointments have been scheduled yet...'})


        return render(request, "main/appointment.html", {"appointments": appointments})


    def post(self, request):
        pass

class PhysicianCreateView(View):
    def get(self, request):
        if not request.session.get("username"):
            return redirect("home")

        physicians = Physician.objects.all()
        if len(physicians) < 1:
            return render(request, "main/physician/create_physician.html", {'error': 'No Physician exist yet...', 'specialities': Speciality.choices})

        return render(request, "main/physician/create_physician.html", {'specialities': Speciality.choices})

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        speciality = request.POST['speciality']
        print(first_name, last_name, speciality)
        message = ''

        if first_name != '' and last_name != '' and speciality !='':
            print('working')
            secretary_instance = Secretary.objects.get(username=request.session.get("username"))
            secretary_class_instance = SecretaryClass(secretary_instance.username, secretary_instance.password)
            message = secretary_class_instance.add_doctor(first_name=first_name, last_name=last_name, speciality=speciality)


        physicians = Physician.objects.all()
        return render(request, "main/physician/create_physician.html", {'physicians': physicians, 'specialities': Speciality.choices,
                                                                       'message': message})

class PhysicianListView(View):
    def get(self, request):
        if not request.session.get("username"):
            return redirect("home")

        physicians = Physician.objects.all()
        if len(physicians) < 1:
            return render(request, "main/physician/list_physicians.html", {'error': 'No Physician exist yet...', 'specialities': Speciality.choices})

        return render(request, "main/physician/list_physicians.html", {'specialities': Speciality.choices, 'physicians': physicians})

    def post(self, request):
        pass

class PhysicianEditView(View):
    def get(self, request, **kwargs):
        if not request.session.get("username"):
            return redirect("home")

        physician_instance = Physician.objects.get(id=self.kwargs['id'])
        print(self.kwargs)
        print(physician_instance)

        return render(request, "main/physician/edit_physician.html", {'physician': physician_instance})

    def post(self, request, **kwargs):
        physician_instance = Physician.objects.get(id=int(self.kwargs['id']))
        print(physician_instance)
        physician_instance.first_name = request.POST['first_name']
        physician_instance.last_name = request.POST['last_name']
        physician_instance.speciality = request.POST['speciality']
        physician_instance.save()
        return render(request, "main/physician/edit_physician.html", {'physician': physician_instance})