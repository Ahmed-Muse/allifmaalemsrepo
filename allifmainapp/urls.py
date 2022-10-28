from django.urls import path
from . import views
app_name='allifmainapp'
urlpatterns = [

path('', views.allifmaalmaindashboard, name="allifmaalmaindashboard"),
path('for-testing-only', views.fortestingonly, name="fortestingonly"),
path('nameregistpage_testing_only', views.nameregistpage_testing_only, name="nameregistpage_testing_only"),

]  
