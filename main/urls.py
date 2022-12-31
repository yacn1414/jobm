from django.urls import path
from main import views

urlpatterns= [
    path('',views.main),
    path('signup',views.registeration),
    path('auth/',views.auth,name="information"),
    path('account/',views.account),
    path('login',views.log_in),
    path('authlogin',views.authlogin,name="auth"),
    path('add',views.add),
    path('adda',views.adda),
    path('procces',views.procces)

]