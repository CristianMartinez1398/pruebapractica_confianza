from rest_framework import serializers
from .models import User, Ask, Answer, Voting

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ask 
        fields = '__all__'    
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer 
        fields = '__all__'    
        
class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting 
        fields = '__all__'                 