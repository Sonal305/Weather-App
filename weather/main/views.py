
from django.shortcuts import render,redirect
import requests
from main.models import City
from main.forms import CityForm
from django.http import Http404
# Create your views here.

# http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=171770d2e338b26c7be389ac48271b9f
def index(request):


    url="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=171770d2e338b26c7be389ac48271b9f"
    err_msg = ''
    message = ''
    message_class = ''
    weather=[]

    if request.method=='POST':

        form=CityForm(request.POST)

        if form.is_valid():
            newcity = form.cleaned_data['name'].capitalize()
            #print("****************************")

            check_exist=City.objects.filter(name=newcity).count()
            if check_exist==0:
                city=requests.get(url.format(newcity)).json()
                if city['cod']==200:
                    form1=form.save(commit=False)
                    form1.name=str(newcity)
                    form1.save()
                else:
                    err_msg='No Such City Exist!!!'
            else:
                err_msg='City already Exists!'
        if err_msg:
            message=err_msg
            message_class='alert-danger'
        else:
            message='City Added Successfully!!'
            message_class="alert-success"
    form=CityForm()
    city=City.objects.all()

    for c in city:
        cityinfo=requests.get(url.format(c)).json()
        #print(cityinfo)
        citydata={
            'name':c.name,
            'description':cityinfo['weather'][0]['description'],
            'icon': cityinfo['weather'][0]['icon'],
            'temperature':cityinfo['main']['temp'],

        }

        #(32°F − 32) × 5/9

        weather.append(citydata)
    context={'weather':weather,'form':form,'message':message,'message_class':message_class}
    return render(request,'main/index.html',context)



def delete_city(request,city_name):
    getcity=City.objects.get(name=city_name)
    getcity.delete()
    return redirect('index')
