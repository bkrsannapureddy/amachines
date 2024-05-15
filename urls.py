"""
URL configuration for amachines1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from amachines.views import signup,dashboard,create_question_bank,create_question,SubjectListView





urlpatterns = [
    path('api/signup/', signup, name='signup'),
    path('api/dashboard/', dashboard, name='dashboard'),
    path('api/create-question-bank/', create_question_bank, name='create_question_bank'),
    path('api/create-question/', create_question, name='create_question'),
    path('api/subjects/', SubjectListView.as_view(), name='subject_list'),
    
    # Add other URL patterns as needed
]
