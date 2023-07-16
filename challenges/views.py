from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "January": "New Year, New You Challenge",
    "February": "Heart Health Month Challenge",
    "March": "Spring into Shape Challenge",
    "April": "April Abs Challenge",
    "May": "May Fitness Fiesta Challenge",
    "June": "Jumpstart June Challenge",
    "July": "Summer Sweat Challenge",
    "August": "Active August Challenge",
    "September": "September Strength Challenge",
    "October": "October Outdoor Adventures Challenge",
    "November": "No Excuses November Challenge",
    "December": "December Dash Challenge"
}

def index(request):
    link_lists = ''
    
    for month in list(monthly_challenges.keys()):
        url = reverse('month-challenge', args=[month.lower()])
        link_lists += f"<li><h3><a href='{url}'>{month.title()}</a></h3></li>"
    
    homepage = f"<h1>Your Monthly Challenges</h1> <hr> <ul>{link_lists}</ul>"

    return HttpResponse(homepage)

def monthly_challenge_int(request, month):

    if month > len(monthly_challenges.keys()):
        return HttpResponseNotFound("There are only 12 months you dum dum.")
    forward_month = list(monthly_challenges.keys())[month - 1]

    redirect_path = reverse('month-challenge', args=[forward_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        response_text = monthly_challenges[month.title()]
    except KeyError:
        response_text = f'You said what? Is {month} part of your calender?'
        return HttpResponseNotFound(response_text)
    
    return HttpResponse(response_text)
