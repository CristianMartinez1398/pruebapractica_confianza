from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    name = models.CharField(max_length=80, unique=False, null=False)
    id_number = models.CharField(max_length=15, unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, unique=False, null=False)  
    updated_at = models.DateTimeField( auto_now=True, unique=False, null=False)
    
    def __str__(self):
        return self.name

#Preguntas 
class Ask(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    description = models.TextField( max_length=150, unique=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, unique=False, null=False)  
    updated_at = models.DateTimeField( auto_now=True, unique=False, null=False)
       
    def __str__(self):
        return self.description

    
#Respuestas    
class Answer(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    description = models.CharField(max_length=150, unique=False, null=False)    
    ask_id = models.ForeignKey(Ask, on_delete=models.CASCADE, related_name="answers", unique=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, unique=False, null=False)  
    updated_at = models.DateTimeField( auto_now=True, unique=False, null=False)
    
    def __str__(self):
        return self.description

    
#Votos
class Voting(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    answer_id = models.ForeignKey(Answer, on_delete=models.CASCADE, unique=False, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, unique=False, null=False)  
    updated_at = models.DateTimeField( auto_now=True, unique=False, null=False) 
    
    class Meta:
        unique_together = ('answer_id', 'user_id') 
        
    def __str__(self):
        return f"Voto de {self.user_id.name} a {self.answer_id.description}"
      