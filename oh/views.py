from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *


# Create your views here.
def home(request):
	all_data = Data.objects.all
	context = {'all_data':all_data,}		
	return render(request,'home.html',context)

def addcity(request):
	form = CityForm()
	if request.method =='POST':
		form = CityForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {'form':form,}		
	return render(request,'cityform.html',context)

def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    context = {
    'states': states,
    }
    return render(request, 'state_dropdown.html', context)


def load_districts(request):
    state_id = request.GET.get('state')
    districts = District.objects.filter(state_id=state_id).order_by('name')
    context = {
    'districts': districts,
    }
    return render(request, 'district_dropdown.html', context)


def load_cities(request):
    district_id = request.GET.get('district')
    cities = City.objects.filter(district_id=district_id).order_by('name')
    context = {
    'cities': cities,
    }
    return render(request, 'city_dropdown.html', context)