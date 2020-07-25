from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.hashers import make_password, check_password

from django.views import View

from .models import Customer,LogFile

class Index(View):
    def get(self,request):
        customer_id = request.session.get('customer')
        if customer_id:
            customer = Customer.objects.get(id=customer_id)
            return render(request, 'index.html',{'customer' : customer})
        else:
            return render(request, 'index.html')


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        f_name = request.POST.get('fname')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        passport = request.POST.get('passport')
        email = request.POST.get('email')
        image = request.POST.get('image')
        password = request.POST.get('password')

        # print(type(f_name),type(dob),type(phone),type(passport),type(email),type(passport))
        # print((f_name),(dob),(phone),(passport),(email),(passport))
        customer = Customer(full_name = f_name,
                            dob = dob,
                            phone = phone,
                            passport = passport,
                            email = email,
                            image = image,
                            password = password)

        values = {
            'full_name': f_name,
            'dob': dob,
            'phone': phone,
            'passport' : passport,
            'email': email,
            'image':image
        }

        error_message = self.validateCustomer(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('index')

        else:
            data = {
                'error': error_message,
                'value': values
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.full_name:
            error_message = 'First name required'
        elif len(customer.full_name) < 4:
            error_message = 'First name must have atleast four characters'
        elif not customer.dob:
            error_message = 'Last name required'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must have atleast ten characters'
        elif not customer.passport:
            error_message = 'Passport Number required'
        elif not customer.password:
            error_message = 'Password required'
        elif len(customer.password) < 6:
            error_message = 'Password must have atleast six characters'
        elif not customer.email:
            error_message = 'Email required'
        elif customer.isExists():
            error_message = 'Email already exists'

        return error_message


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        # get customer by email
        try:
            customer = Customer.objects.get(phone=phone)
        except:
            customer = False

        # error_message = None

        if customer:
            if check_password(password, customer.password):

                request.session['customer'] = customer.id
                LogFile.objects.create(customer=customer)
                return redirect('index')
            else:
                error_message = 'Incorrect email or password'
        else:
            error_message = 'Incorrect email or password'

        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')