from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm
import joblib
import pandas as pd
from .models import Model, TitanicSurvivalPrediction, LaptopPricePrediction, AllPredictions
from utilities import titanicMW
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import date
from django.contrib.admin.views.decorators import staff_member_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')

def titanic_survival(request):
    if request.method == 'POST':
        passenger_id = request.POST.get('passengerId')
        passenger_class = request.POST.get('passenger_class')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        siblings_spouses = request.POST.get('siblings_spouses')
        parents_children = request.POST.get('parents_children')
        ticket = request.POST.get('ticket')
        fare = request.POST.get('fare')
        cabin = request.POST.get('cabin')
        embarked = request.POST.get('embarked')

        request.session['form_data'] = request.POST.dict()
        
        data = {
            'PassengerId': [passenger_id],
            'Pclass': [passenger_class],
            'Name': [name],
            'Sex': [sex],
            'Age': [age],
            'SibSp': [siblings_spouses],
            'Parch': [parents_children],
            'Ticket': [ticket],
            'Fare': [fare],
            'Cabin': [cabin],
            'Embarked': [embarked],
        }
        df = pd.DataFrame(data)

        pipeline_path = 'C:/Users/Lenovo/Desktop/SmartPredict/smartpredict/app/pipeline.pkl'
        pipeline = joblib.load(pipeline_path) 
        model_path = ('C:/Users/Lenovo/Desktop/SmartPredict/smartpredict/app/model.pkl')
        model = joblib.load(model_path)
        scaler_path = ('C:/Users/Lenovo/Desktop/SmartPredict/smartpredict/app/scaler.pkl')
        scaler = joblib.load(scaler_path)

        df = pipeline.transform(df)
        print(df)
        scaled_df = scaler.transform(df)
        print(scaled_df)
        prediction = model.predict(df)

        request.session['prediction'] = int(prediction[0])
        return redirect('titanic-results')
    else:
        return render(request, 'titanicsurvival.html')

def titanic_results(request):
    if 'prediction' in request.session:
        prediction_value = request.session['prediction']
        user = request.user

        if user.is_authenticated:
            form_data = request.session.get('form_data', None)

            if form_data:
                with transaction.atomic():
                    prediction_instance = TitanicSurvivalPrediction(
                        user=user,
                        survived=bool(prediction_value), 
                        passenger_id=form_data.get('passengerId'),
                        pclass=form_data.get('passenger_class'),
                        name=form_data.get('name'),
                        gender=form_data.get('sex'),
                        age=form_data.get('age'),
                        sib_sp=form_data.get('siblings_spouses'),
                        parch=form_data.get('parents_children'),
                        ticket=form_data.get('ticket'),
                        fare=form_data.get('fare'),
                        cabin=form_data.get('cabin'),
                        embarked=form_data.get('embarked')
                    )
                    prediction_instance.save()

                    model = Model.objects.get(model_name='Titanic Survival Prediction')
                    all_predictions_instance = AllPredictions(user=user, model=model, created_at=date.today())
                    all_predictions_instance.save()

            del request.session['form_data']

        del request.session['prediction']

        return render(request, 'titanicresults.html', {'prediction': prediction_value})
    else:
        return redirect('titanicsurvival')

def profile(request):
    return render(request, 'profile.html')


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST' and request.user == user:
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        messages.success(request, 'Your profile was updated successfully.')
        return redirect('user-profile', username=user.username)

    predictions = TitanicSurvivalPrediction.objects.filter(user=user)
    laptop_predictions = LaptopPricePrediction.objects.filter(user=user)
    print(predictions)
    print(laptop_predictions)
    return render(request, 'profile.html', {'user': user, 'predictions': predictions, 'laptop_predictions' : laptop_predictions})

@login_required
def change_password(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was updated successfully.')
        else:
            messages.error(request, 'Passwords do not match.')
        return redirect('user-profile', username=user.username)

def laptop_price_prediction(request):
    if request.method == 'POST':
        msi = request.POST.get('MSI')
        amd_cpu = request.POST.get('AMD_CPU')
        intel_cpu = request.POST.get('Intel_CPU')
        intel_gpu = request.POST.get('Intel_GPU')
        amd_gpu = request.POST.get('AMD_GPU')
        acer = request.POST.get('Acer')
        weight = request.POST.get('Weight')
        flash = request.POST.get('Flash')
        razer = request.POST.get('Razer')
        workstation = request.POST.get('Workstation')
        ultrabook = request.POST.get('Ultrabook')
        nvidia_gpu = request.POST.get('Nvidia_GPU')
        gaming = request.POST.get('Gaming')
        hdd = request.POST.get('HDD')
        cpu_frequency = request.POST.get('CPU_Frequency')
        ssd = request.POST.get('SSD')
        notebook = request.POST.get('Notebook')
        screen_height = request.POST.get('Screen_Height')
        screen_width = request.POST.get('Screen_Width')
        ram = request.POST.get('Ram')

        request.session['form_data'] = request.POST.dict()
        
        data = {
            'MSI': [msi],
            'AMD_CPU': [amd_cpu],
            'Intel_CPU': [intel_cpu],
            'Intel_GPU': [intel_gpu],
            'AMD_GPU': [amd_gpu],
            'Acer': [acer],
            'Weight': [weight],
            'Flash': [flash],
            'Razer': [razer],
            'Workstation': [workstation],
            'Ultrabook': [ultrabook],
            'Nvidia_GPU': [nvidia_gpu],
            'Gaming': [gaming],
            'HDD': [hdd],
            'CPU Frequency': [cpu_frequency],
            'SSD': [ssd],
            'Notebook': [notebook],
            'Screen Height': [screen_height],
            'Screen Width': [screen_width],
            'Ram': [ram],
        }
        df = pd.DataFrame(data)

        model_path = ('C:/Users/Lenovo/Desktop/SmartPredict/smartpredict/app/laptop_model.pkl')
        model = joblib.load(model_path)
        scaler_path = ('C:/Users/Lenovo/Desktop/SmartPredict/smartpredict/app/forest_scaler.pkl')
        scaler = joblib.load(scaler_path)

        scaled_df = scaler.transform(df)
        prediction = model.predict(scaled_df)

        request.session['prediction'] = int(prediction[0])
        return redirect('laptop-results')
    else:
        return render(request, 'laptop.html')

def laptop_results(request):
    if 'prediction' in request.session:
        prediction_value = request.session['prediction']
        user = request.user

        if user.is_authenticated:
            form_data = request.session.get('form_data', None)

            if form_data:
                with transaction.atomic():
                    prediction_instance = LaptopPricePrediction(
                        user=user,
                        price=prediction_value,
                        msi=form_data.get('msi'),
                        amd_cpu=form_data.get('amd_cpu'),
                        intel_cpu=form_data.get('intel_cpu'),
                        intel_gpu=form_data.get('Intel_GPU'),
                        amd_gpu=form_data.get('AMD_GPU'),
                        acer=form_data.get('Acer'),
                        weight=form_data.get('Weight'),
                        flash=form_data.get('Flash'),
                        razer=form_data.get('Razer'),
                        workstation=form_data.get('Workstation'),
                        ultrabook=form_data.get('Ultrabook'),
                        nvidia_gpu=form_data.get('Nvidia_GPU'),
                        gaming=form_data.get('Gaming'),
                        hdd=form_data.get('HDD'),
                        cpu_frequency=form_data.get('CPU_Frequency'),
                        ssd=form_data.get('SSD'),
                        notebook=form_data.get('Notebook'),
                        screen_height=form_data.get('Screen_Height'),
                        screen_width=form_data.get('Screen_Width'),
                        ram=form_data.get('Ram')
                    )
                    prediction_instance.save()

                    model = Model.objects.get(model_name='Laptop Price Prediction')
                    all_predictions_instance = AllPredictions(user=user, model=model, created_at=date.today())
                    all_predictions_instance.save()

            del request.session['form_data']

        del request.session['prediction']

        return render(request, 'laptopresults.html', {'prediction': prediction_value})
    else:
        return redirect('laptop')

@staff_member_required
def admin_dashboard(request):
    users = User.objects.all()
    predictions = AllPredictions.objects.all()

    context = {
        'users': users,
        'predictions': predictions,
    }
    return render(request, 'admin_dashboard.html', context)

@staff_member_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        try:
                username = user.username
                user.delete()
                messages.success(request, f'User {username} deleted successfully.')
                return redirect('admin-dashboard')
        except Exception as e:
                messages.error(request, f'Failed to delete user: {str(e)}')
                return redirect('admin-dashboard')

    return render(request, 'delete_user.html', {'user': user})

@staff_member_required
def edit_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        if request.method == 'POST':
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, f'User {user.username} updated successfully.')
            return redirect('admin-dashboard')
        context = {
            'user': user,
        }
        return render(request, 'edit_user.html', context)
    except User.DoesNotExist:
        messages.error(request, 'User does not exist.')
        return redirect('admin-dashboard')

@staff_member_required
def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        try:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            messages.success(request, f'User {user.username} created successfully.')
            return redirect('admin-dashboard')
        except Exception as e:
            messages.error(request, f'Failed to create user: {str(e)}')
    return render(request, 'create_user.html')
