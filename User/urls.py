from django.urls import path,include
from User import views

app_name = 'User'


urlpatterns = [
        path('signup/', views.SignupView.as_view(),name='signup'),
        path('login/', views.loginview, name='login'),
        path('logout/', views.logOut, name='logout'),
]
