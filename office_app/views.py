from django.shortcuts import render, redirect
from django.views import View
from office_app.models import Patient, Physician, Appointment, Secretary, Speciality

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

class PhysicianView(View):
    def get(self, request):
        if not request.session.get("username"):
            return redirect("home")

        physicians = Physician.objects.all()
        if len(physicians) < 1:
            return render(request, "main/physician/create_physician.html", {'error': 'No Physician exist yet...', 'specialities': Speciality.choices})


        return render(request, "main/physician/list_physicians.html", {'physicians': physicians})

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        speciality = request.POST['speciality']
        print(first_name, last_name, speciality)

        if first_name != '' and last_name != '' and speciality !='':
            print('working')
            Physician.objects.create(first_name=first_name, last_name=last_name, speciality=speciality)

        physicians = Physician.objects.all()
        return render(request, "main/physician/list_physicians.html", {'physicians': physicians, 'specialities': Speciality.choices})


