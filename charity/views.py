# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Cause, Event, News, Donation, Profile
from .forms import VolunteerForm, DonationForm, UserRegistrationForm, UserLoginForm, ProfileForm

def home(request):
    causes = Cause.objects.filter(is_active=True)
    events = Event.objects.all().order_by('-date')[:3]
    news = News.objects.all().order_by('-date')[:3]
    registered_phone = None
    
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save()
            registered_phone = volunteer.phone
        else:
            registered_phone = None
    else:
        form = VolunteerForm()
    
    context = {
        'causes': causes,
        'events': events,
        'news': news,
        'form': form,
        'registered_phone': registered_phone,
    }
    return render(request, 'charity/home.html', context)

def donation_form(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation_data = form.cleaned_data.copy()
            donation_data['amount'] = str(donation_data['amount'])
            request.session['donation_data'] = donation_data
            return redirect('donation_confirmation')
    else:
        form = DonationForm()
    return render(request, 'charity/donate.html', {'form': form})

def donation_confirmation(request):
    donation_data = request.session.get('donation_data')
    if not donation_data:
        return redirect('donation_form')
    del request.session['donation_data']
    return render(request, 'charity/confirmation.html', {'donation': donation_data})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'charity/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'charity/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)
    donations = Donation.objects.filter(user=user).order_by('-donation_date')
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    context = {
        'user': user,
        'profile': profile,
        'donations': donations,
        'form': form,
    }
    return render(request, 'charity/profile.html', context)

def causes(request):
    causes = Cause.objects.filter(is_active=True)
    return render(request, 'charity/causes.html', {'causes': causes})

def events(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'charity/events.html', {'events': events})

def news(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'charity/news.html', {'news': news})

def contact(request):
    return render(request, 'charity/contact.html')
