from django.urls import path
from . import apis

urlpatterns = [
    path('ask/', apis.ask_question, name='ask_question'),
    path('question/<int:pk>/', apis.question_detail, name='question_detail'),
    path('answer/<int:pk>/like/', apis.like_answer, name='like_answer'),
]