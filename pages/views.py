from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, "signup.html", {})
def home(request):
    from pages.namer import display
    return render(request, "home.html", {"my_stuff": display})

def about(request):
    my_name = "About Brook Cherith Christian Learning Center"
    return render(request, "about.html", {"my_name": my_name})

def enrollment(request):
    return render(request, "enrollment.html", {})