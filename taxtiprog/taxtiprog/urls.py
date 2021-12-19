from taxtiapp.views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view()),
    path('car.html', cars.as_view()),
    path('user.html', users.as_view()),
    path('page_registr.html', registration.as_view()),
    path('2.html', login.as_view()),
    path('admin.html', admin_castom.as_view()),
    path('page_payback.html', Page_payback.as_view()),
]
