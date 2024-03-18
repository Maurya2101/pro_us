from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from .models import User, Item, Booking, Invoice
from .forms import CustomerRegistrationForm, ServiceproviderRegistrationForm, ProfileForm
# Note: Ensure to import any other required models or forms.

# User Registration for Customers
class CustomerRegisterView(CreateView):
    template_name = 'user/customer_register.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Upon successful form validation, send a welcome email.
        valid = super().form_valid(form)
        self.send_welcome_email(form.cleaned_data.get('email'))
        return valid

    def send_welcome_email(self, email):
        subject = 'Welcome to Our Service'
        message = 'Thank you for registering with us. We are glad to have you on board!'
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

# User Registration for Service Providers
class ServiceproviderRegisterView(CreateView):
    template_name = 'user/serviceprovider_register.html'
    form_class = ServiceproviderRegistrationForm
    success_url = reverse_lazy('login')

# User Login View
class UserLoginView(LoginView):
    template_name = 'user/login.html'
    
    def get_success_url(self):
        # Redirect users based on their role after login.
        if self.request.user.is_customer:
            return reverse_lazy('customer-dashboard')
        elif self.request.user.is_serviceprovider:
            return reverse_lazy('serviceprovider-dashboard')
        else:
            return reverse_lazy('home')

# Customer Dashboard View
class CustomerDashboardView(LoginRequiredMixin, ListView):
    model = Item  # Assuming you want to list items or services
    template_name = 'user/customer_dashboard.html'
    context_object_name = 'items'
    
    def get_queryset(self):
        # Customize the queryset as per your requirements, e.g., filter available items.
        return Item.objects.filter(available=True)

# Service Provider Dashboard View
class ServiceproviderDashboardView(LoginRequiredMixin, ListView):
    template_name = 'user/serviceprovider_dashboard.html'
    # Implement specific logic for service provider dashboard

# Profile Update View
class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'user/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        # Users can only edit their own profile
        return self.request.user

# Static Pages
def home(request):
    # Display home page with a list of items/services.
    items = Item.objects.all()
    return render(request, 'user/home.html', {'items': items})

def about_us(request):
    return render(request, 'user/aboutus.html')

def contact(request):
    return render(request, 'user/contact.html')

# Booking and Invoice
def book_now(request, item_id):
    if request.method == "POST" and request.user.is_authenticated:
        item = Item.objects.get(id=item_id)
        booking = Booking.objects.create(user=request.user, item=item, bdate=timezone.now())
        Invoice.objects.create(booking=booking, amount=item.price, status="Pending")
        return redirect('show_invoice', invoice_id=booking.invoice.id)
    else:
        return redirect('login')

def show_invoice(request, invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    item = invoice.booking.item
    return render(request, 'user/invoice.html', {'invoice': invoice,'item': item})






# from django.shortcuts import render,redirect
# from django.views.generic.edit import CreateView
# from .models import User
# from .forms import userRegistrationForm, ServiceproviderRegistrationForm
# #import settings.py
# from django.conf import settings
# #send_mail is built-in function in django
# from django.core.mail import send_mail
# from django.http import HttpRequest, HttpResponse
# from .models import User, Item, Booking, Invoice
# from.forms import userRegistrationForm
# from django.contrib.auth.views import LoginView
# from django.views.generic import ListView
# from service.models import Service
# from django.views.generic import UpdateView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import ProfileForm
# from django.utils import timezone

# # from django.contrib.auth.decorators import login_required
# # from django.utils.decorators import method_decorator

# # Create your views here.
# class userRegisterView(CreateView):
#     template_name = 'user/user_register.html'
#     model = User
#     form_class = userRegistrationForm
#     success_url = '/login/'
    
    
#     def form_valid(self, form):
#         email = form.cleaned_data.get('email')
#         #print("email....",email)
#         if sendMail(email):
#             print("Mail sent successfully")
#             return super().form_valid(form)
#         else:
#             return super().form_valid(form)


# class ServiceproviderRegisterView(CreateView):
#     template_name = 'user/serviceprovider_register.html'
#     model = User
#     form_class = ServiceproviderRegistrationForm
#     success_url = '/login/'    
    

# def sendMail(to):
#     subject = 'Welcome to Urban Service'
#     message = 'Hope you are enjoying your Django Tutorials'
#     #recepientList = ["samir.vithlani83955@gmail.com"]
#     recepientList = [to]
#     EMAIL_FROM = settings.EMAIL_HOST_USER
#     send_mail(subject,message, EMAIL_FROM, recepientList)
#     #attach file
#     #html
#     return True


# class UserLoginView(LoginView): 
#     template_name = 'user/login.html'
#     model = User
    
    
#     def get_redirect_url(self):
#         if self.request.user.is_authenticated:
#             if self.request.user.is_user:
#                 return '/user/user-dashboard/'
#             else:
#                 return '/user/serviceprovider-dashboard/'
            

# class userDashboardView(ListView):
    
#     def get(self, request, *args, **kwargs):
#         #logic to get all the projects
#         print("userDashboardView")
#         services = Service.objects.all() #select * from project
#         print(".............................................",services)
       
#         return render(request, 'user/user_dashboard.html',{"services": services})
    
    
#     template_name = 'user/user_dashboard.html'

# class ServiceproviderDashboardView(ListView):
#     def get(self, request, *args, **kwargs):
#         #logic to get all the projects
#         return render(request, 'user/serviceprovider_dashboard.html')
    
#     template_name = 'user/serviceprovider_dashboard.html'    
    
# def home(request):
#     return render(request, 'user/home.html')

# def aboutus(request):
#     return render(request, 'user/aboutus.html')

# def contact(request):
#     return render(request, 'user/contact.html')

def submit(request):
    return render(request, 'user/submit.html')


def terms(request):
    return render(request, 'user/terms.html')

def payment(request):
    return render(request, 'user/payment.html')


# def show_invoice(request, invoice_id):
#     invoice = Invoice.objects.get(id=invoice_id)
#     return render(request, 'invoice.html', {'invoice': invoice})
# # def invoice(request):
# #     return render(request, 'user/invoice.html')
# # class InvoiceDetailView(DetailView):
# #     model = Item
# #     context_object_name = "item"
# #     template_name = "user/invoice.html"

# def home(request):
#     items = Item.objects.all()  # Querying all items
#     return render(request, 'user/home.html', {'items': items})


# class ProfileView(LoginRequiredMixin, UpdateView):
#     model = User
#     form_class = ProfileForm
#     template_name = 'user/profile.html'
#     success_url = reverse_lazy('profile')

#     def get_object(self):
#         return self.request.user  # Assuming User model is used for profile


# def book_now(request, item_id):
#     if request.method == "POST":
#         # Assuming the user is authenticated and user details are accessible
#         user = request.user.user
#         item = Item.objects.get(id=item_id)
        
#         booking = Booking.objects.create(user=user, item=item, booking_date=timezone.now())
        
#         # Create an invoice for the booking with the item's price
#         invoice = Invoice.objects.create(booking=booking, amount=item.price, status="Pending")
        
#         # Redirect to an invoice page
#         return redirect('show_invoice', invoice_id=invoice.id)