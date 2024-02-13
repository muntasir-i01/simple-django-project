from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Registered')
                return redirect('register')
                
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save();
                print('user created')              
            
        
        else:
            print('Password not matching...')   
            return redirect('register')
        return redirect('/')          
                    
            
       
   
       

    else:
        
        return render(request, 'register.html')  #when call the register.html that means you are sending a get request
