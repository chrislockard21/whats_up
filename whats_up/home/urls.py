from django.urls import path
from .views import Index, Registration, Sucess, Login, Logout

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', Registration.as_view(), name='register'),
    path('sucess/', Sucess.as_view(), name='sucess'),
]
