from django.urls import path
from . import views
app_name='allifmainapp'
urlpatterns = [

path('', views.allifmaalmaindashboard, name="allifmaalmaindashboard"),
path('for-testing-only', views.fortestingonly, name="fortestingonly"),

]  
