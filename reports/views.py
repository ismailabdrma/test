from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report
import folium
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm, LoginForm

def index(request):
    return render(request, 'reports/index.html')

@login_required(login_url='login')
def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('index')
    else:
        form = ReportForm()
    return render(request, 'reports/report.html', {'form': form})

def map_view(request):
    reports = Report.objects.all()
    m = folium.Map(location=[33.5415, -7.6735], zoom_start=13)

    for report in reports:
        if report.latitude is not None and report.longitude is not None:
            folium.Marker(
                location=[report.latitude, report.longitude],
                popup=report.description,
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)
        else:
            print(f"Skipping report {report.id} due to missing location data")

    m = m._repr_html_()
    return render(request, 'reports/map.html', {'map': m})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('report')  # Redirect to the report page after signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('report')  # Redirect to the report page after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def view_reports(request):
    reports = Report.objects.all()
    return render(request, 'reports/view_reports.html', {'reports': reports})

@user_passes_test(lambda u: u.is_superuser)
def admin_view_reports(request):
    reports = Report.objects.all()
    return render(request, 'reports/admin_dashboard.html', {'reports': reports})






