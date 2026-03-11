from django.urls import path
from .import views
#-------------------------#
urlpatterns = [
 path('register' , views.Register ),
 path('login' , views.login_view),
 path('logout' , views.logout_view)

]