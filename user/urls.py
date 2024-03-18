from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views 
from .views import payment,terms,submit

urlpatterns = [
    # User and Service Provider Registration
    path('customer-register/', views.CustomerRegisterView.as_view(), name='customer-register'),
    path('serviceprovider-register/', views.ServiceproviderRegisterView.as_view(), name='serviceprovider-register'),

    # User Login and Logout
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # Dashboard Views
    path('customer-dashboard/', views.CustomerDashboardView.as_view(), name='customer-dashboard'),
    path('serviceprovider-dashboard/', views.ServiceproviderDashboardView.as_view(), name='serviceprovider-dashboard'),

    # Profile Update
    path('profile/', views.ProfileView.as_view(), name='profile'),

    # Static Pages
    path('home/', views.home, name='home'),
    path('aboutus/', views.about_us, name='aboutus'),
    path('contact/', views.contact, name='contact'),

    # Service Booking and Invoices
    path('book-now/<int:item_id>/', views.book_now, name='book_now'),
    path('invoice/<int:invoice_id>/', views.show_invoice, name='show_invoice'),

    # Other paths...
    path('submit/',submit, name='submit'),
    path('terms/',terms, name='terms'),
    path('payment/',payment, name='payment'),
]



# from django.contrib import admin
# from django.urls import path, include
# from . import views 
# from django.contrib.auth.views import LoginView,LogoutView
# from .views import payment,terms,submit,home,aboutus,contact,ProfileView


# urlpatterns = [
    
#     path("customer-register/",views.CustomerRegisterView.as_view(),name="customer-register"),
#     path("login/",views.UserLoginView.as_view(),name="login"),
#     path("customer-dashboard/",views.CustomerDashboardView.as_view(),name="customer-dashboard"),
#     #path("serviceprovider-register/",views.ServiceproviderRegisterView.as_view(),name="serviceprovider-register"),
#     path("serviceprovider-dashboard/",views.ServiceproviderDashboardView.as_view(),name="serviceprovider-dashboard"),
#     path("logout/",LogoutView.as_view(next_page = "/user/login"),name="logout"),
#     path('home/',home, name='home'),
#     path('aboutus/',aboutus, name='aboutus'),
#     path('contact/',contact, name='contact'),
        # path('submit/',submit, name='submit'),
        # path('terms/',terms, name='terms'),
        # path('payment/',payment, name='payment'),
#     path('invoice/<int:invoice_id>/', views.show_invoice, name='show_invoice'),
#     path('profile/', ProfileView.as_view(), name='profile'),
#     path('book-now/<int:item_id>/', views.book_now, name='book_now'),
    
# ]