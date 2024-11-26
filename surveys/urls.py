from django.urls import path
from .views import UserListCreate, UserDetail, AskListCreate, AskDetail, AnswerListCreate, AnswerDetail, VotingListCreate, VotingDetail

urlpatterns = [
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('asks/', AskListCreate.as_view(), name='ask-list-create'),
    path('asks/<int:pk>/', AskDetail.as_view(), name='ask-detail'),
    path('answers/', AnswerListCreate.as_view(), name='answer-list-create'),
    path('answers/<int:pk>/', AnswerDetail.as_view(), name='answer-detail'),
    path('votes/', VotingListCreate.as_view(), name='voting-list-create'),
    path('votes/<int:pk>/', VotingDetail.as_view(), name='voting-detail'),
   
]

