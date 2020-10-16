from django.urls import path
from . import views  # by using simple "." we import all things from the same directory we're currently in.

urlpatterns = [
    path('',views.all_blogs, name='all_blogs'),
 ]