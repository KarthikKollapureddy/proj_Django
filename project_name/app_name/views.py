from django import forms
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from .forms import CreateUserForm,MoMForm,feedbackForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app_name.models import MoM,User;

def home(request):
    return render(request,'app_name/home.html')

@login_required
def logged_in(request):
    return render(request,'app_name/logged_in.html')

def registerPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print('saved')
            return redirect('login')
    context = {'form':form}
    return render(request,'app_name/register.html',context)

def loginPage(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('logged_in')
    return render(request,'app_name/login.html',{'form':form})

def logoutPage(request):
    logout(request)   
    return redirect('home')

@login_required
def MoMPage(request):
    # users_list = User.objects.order_by('id')
    userId = request.user.id
    mom_list = MoM.objects.order_by('id')
    form = MoMForm()
    print("req method: ",request.method)
    if request.method == 'POST':
        form = MoMForm(request.POST)
        # form = MoMForm.objects.create(user_id=userId, **request.POST)
        print(form)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            print("save")
            messages.success(request, 'MoM submitted successfully.')
            return redirect('logged_in')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    context = {'form':form,'mom_list':mom_list,'userId':userId}
    return render(request,'app_name/mom_form.html',context)

@login_required
def feedbackPage(request):
    form = feedbackForm()
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Feedback submitted successfully.')
            return redirect('logged_in')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    context = {'form':form}
    return render(request,'app_name/feedback_form.html',context)

def mentor_register(request):
    context =  {}
    # if request.method == 'POST':
    #     form = MentorForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.is_mentor = True
    #         user.save()
    #         mentor = Mentor.objects.create(user=user, expertise=form.cleaned_data.get('expertise'), experience=form.cleaned_data.get('experience'))
    #         login(request, user)
    #         return redirect('home')
    # else:
    #     form = MentorForm()
    return render(request, 'app_name/mentor_register.html',context)

def mentee_register(request):
    context =  {}
    # if request.method == 'POST':
    #     form = MenteeForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.is_mentee = True
    #         user.save()
    #         mentee = Mentee.objects.create(user=user, interests=form.cleaned_data.get('interests'), goals=form.cleaned_data.get('goals'))
    # else:
    #     form = MenteeForm()
    return render(request, 'app_name/mentee_register.html',)
