from django.urls import path
from .views import UserListCreate, UserDetail, AskListCreate, AskDetail, AnswerListCreate, AnswerDetail, VotingListCreate, VotingDetail

urlpatterns = [
    path('api/users/', UserListCreate.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('api/asks/', AskListCreate.as_view(), name='ask-list-create'),
    path('api/asks/<int:pk>/', AskDetail.as_view(), name='ask-detail'),
    path('api/answers/', AnswerListCreate.as_view(), name='answer-list-create'),
    path('api/answers/<int:pk>/', AnswerDetail.as_view(), name='answer-detail'),
    path('api/votes/', VotingListCreate.as_view(), name='voting-list-create'),
    path('api/votes/<int:pk>/', VotingDetail.as_view(), name='voting-detail'),
    # Si tienes otras rutas de administración o vistas adicionales, añádelas aquí
]

