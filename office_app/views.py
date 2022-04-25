from django.shortcuts import render, redirect
from django.views import View
from office_app.models import Patient, Physician, Appointment, Secretary

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

class Appointment(View):
    def get(self, request):
        if not request.session.get("username"):
            return redirect("home")
        try:
            appointments = Appointment.objects.filter()
        except AttributeError:
            return render(request, "main/appointment.html", {'error': 'No Appointments have been scheduled yet..'})

        if len(appointments) > 0:
            return render(request, "main/appointment.html", {"appointments": appointments})


    def post(self, request):
        pass
