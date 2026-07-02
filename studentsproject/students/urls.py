from django.urls import path
from students.views import home,signup,user_login,user_logout,add_student,view_student

urlpatterns = [

    path('', home, name='home'),
    path('signup/',signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('add_student/',add_student,name='add_student'),
    path('view_student/',view_student,name='view_student')
]
