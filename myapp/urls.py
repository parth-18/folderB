from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('form1',views.form1,name='form1'),
    path('form2',views.form2,name='form2'),
    path('loginUser',views.loginUser,name='loginUser'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
    path('all/<str:id>',views.all,name='all'),
    path('explore/<str:id>',views.explore,name='explore'),
    path('profile/<str:id>',views.profile,name='profile'),
    path('hire/<str:id>',views.hire,name='hire'),
    path('sub/<str:id>',views.sub,name='sub'),
]
