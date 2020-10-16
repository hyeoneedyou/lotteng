from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def show_team_profile(request):
    return render(request, 'team.html')