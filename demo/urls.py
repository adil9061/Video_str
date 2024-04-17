from django.urls import path
from demo import views

urlpatterns = [
    
    path('register/', views.SignUp.as_view(), name='register'),

    path('', views.Login.as_view(), name='login'),

    path('home/', views.Home.as_view(), name='home'),

    path('create_video/', views.CreateVideo.as_view(), name='create_video'),

    path('edit_video/<video_id>/', views.EditVideo.as_view(), name='edit_video'),

    path('delete_video/<video_id>/', views.DeleteVideo.as_view(), name='delete_video'),

    path('videos/', views.VideoList.as_view(), name='video_list'),

    path('logout/', views.Logout.as_view(), name='logout'),

]

