from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from home.models import Contact, Order, GetJob, Softwares, SoftwareType
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .forms import OrderForm,UserForm
from django.contrib import messages
# Create your views here.


# HTML
def index(request):
    '''this function is for rendering the landing page'''
    # return HttpResponse('this is homepage')

    # in context we'll be sending all the sentences we need to show in the landing page for experimenting
    context: dict = {"variable": "this is me "}
    return render(request, 'home/index.html', context)


def about(request):
    '''this function is for rendering the about page'''
    return render(request, 'home/aboutus.html')


def service(request):
    '''this function is for rendering the services page'''
    return render(request, 'home/services.html')


def projects(request):
    '''this function is for rendering the projects page'''
    return render(request, 'home/projects.html')

# order related


@login_required(login_url='/login')
def orders(request,):
    '''this function is for rendering the order page and placing order'''
    form = OrderForm(request.POST)
    # softwares = Softwares.objects.all()
    # software_type = SoftwareType.objects.all()
    # sending the data
    if request.method == "POST":
        # software_type_name = request.POST.get('soft_type')
        # software_type = SoftwareType.objects.get()
        # software = request.POST.get('software')

        Order.objects.create(
            customer_name=request.user,
            soft_name=request.POST.get('softName'),
            # software=request.POST.get('software'),
            software=request.POST.get('software'),
            # soft_time=request.POST.get('soft_time'),
            soft_amount=request.POST.get('softAmount'),
            soft_desc=request.POST.get('softDesc'),
            # soft_type=software_type
        )
        messages.success(request, 'Your order has been placed')

    # form = OrderForm()

    # if request.method == 'POST':
    #     if form.is_valid():
    #         print(request.POST)
    #         # form.save()

        return redirect('/payment/')
    # rendering the orders page
    context: dict = {'form': form,}
    # context: dict = {'form': form}
    return render(request, 'home/order/orders.html', context)
    # return render(request, 'experiment.html', context)
    # else:
    # messages.error(request, 'Please login to order ')
    # if user isn't logined then redirecting the user to the home page
    # return redirect('/')


@login_required(login_url='/login')
def trackOrder(request):
    '''this is the function which we which showing all the info after placing the order '''
    return render(request,'home/order/order_track.html')

@login_required(login_url='/login')
def orderSave(request):
    '''this function is for saving the order we'll have '''

@login_required(login_url='/login')
def ord_cancel(request):
    '''this function is for canceling the order '''

    return render(request, 'home/cancelation-policy.html')

@login_required(login_url='/login')
def orderPayment(request):
    return render(request,'home/order/order_payment.html')

@login_required(login_url='/login')
def orderPaymentProcess(request):
    pass
    
    
# contact related


@login_required(login_url='/login')
def contact(request):
    '''this function is for rendering the contact page'''

    # checking the user is authencticated or not
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            contact = Contact(name=name, email=email,
                              message=message, date=datetime.today())
            # saving the data
            contact.save()
            # showing a message if the contact has been submitted successfully
            messages.success(request, 'Success,Your message has been sent!')
        return render(request, 'home/contact.html')
    else:
        # if user is not logined the showing a message , to login to contact us
        messages.error(request, 'Please login to contact us ')
        return render(request, 'home/contact.html')

# subscription related


def subscription(request):
    '''this function is for rendering the subscription page'''
    return render(request, 'home/subscription.html')


def projects(request):
    '''this function is for rendering the projects page'''
    return render(request, 'home/projects.html')

# job related

@login_required(login_url='/login')
def job(request):
    '''this function is for rendering the job page'''

    # checking the user is authenticated or not
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            UserName = request.POST.get('username')
            phoneno = request.POST.get('phoneno')
            email = request.POST.get('email')
            education = request.POST.get('education')
            qualification = request.POST.get('qualification')
            ever_worked = request.POST.get('worked_ever')
            status = request.POST.get('status')
            address = request.POST.get('address')
            jobrole = request.POST.get('jobrole')
            skills = request.POST.get('skills')
            explain = request.POST.get('describe')

            # sending the data
            jobrequest = GetJob(name=name, UserName=UserName, email=email, phone=phoneno, education=education, qualification=qualification,
                                address=address, your_skills=skills, ever_worked=ever_worked, jobrole=jobrole, status=status, describe=explain)
            # saving the data
            jobrequest.save()
            # showing a message that your application has been submitted successfully
            messages.success(request, 'Your application has been submitted')
        # showing the page
        return render(request, 'home/job.html')
    else:
        # if user is not logined the showing a message , to login to apply for a job
        messages.error(request, 'Please login to apply for a job ')
        # redirecting the user to the home page of recxo
        return redirect('/')

def ai(request):
    '''this function is for rendering the ai page'''
    return render(request, 'ai.html')

# company info related

def term_and_cond(request):
    '''this function is for rendering the terms and condition page'''
    return render(request, 'home/term&cond.html')

def priv_policy(request):
    '''this function is for rendering the terms and condition page'''
    return render(request, 'home/privacy_policy.html')

# profile related

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user, }
    messages.success(request, 'Your update has been made successfully')


    return render(request, 'home/profile.html', context)

def updateUserProfile(request,pk):
    user = request.user
    form = UserForm(instance=user)

    if request.method =='POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            redirect('user-profile',pk=user.id)
    messages.success(request, 'Your update has been made successfully')
    return render(request,'home/update-user.html',{'form':form})

# APIs
# login related

def loginUser(request):
    '''this function is for rendering the login page and authenicating the user'''

    if request.method == 'POST':
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        email = request.POST.get('loginUsername')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password, email=email)

        # conditions logging in a user
        if user is not None:
            login(request, user)
            messages.success(
                request, f'Successfully Logged In as {request.user.username}')
            return redirect('/')
        else:
            messages.error(request, 'Login Credentials didn\'t match')
            return render(request, 'home/loginrelated/loginform2.html')
            # return render(request, '/')
    return render(request, 'home/loginrelated/loginform2.html')

def logoutUser(request):
    '''this function is logging out the user'''
    # making the user logging out
    logout(request)
    return redirect('/')

def signup(request):
    '''this function is for rendering the signup page'''
    return render(request, 'home/loginrelated/signup.html')

def handleSignup(request):
    '''this function handles the signup of user'''
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['confirmpass']
        # username should be under 10 characters
        if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('/')

        # username should be alphanumeric
        if not username.isalnum():
            messages.error(
                request, 'Username should only contain letters and numbers')
            return redirect('/')

        # passwords should match
        if password != password_confirm:
            messages.error(request, 'Passwords do not match')
            return redirect('/')

        #  checks for errorneous inputs
        # create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        # saving the use
        myuser.save()
        # showing a user that you have signed up successfully
        messages.success(
            request, 'Your recxo account has been successfully created now you can login')
        return redirect('/')
    else:
        # showing error
        return HttpResponse('404 - Page not found')

def forpass(request):
    '''this function is for rendering the forgot pass page'''
    return render(request, 'home/forgotpass.html')
