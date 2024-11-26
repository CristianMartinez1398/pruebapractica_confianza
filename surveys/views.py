from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import User, Ask, Answer, Voting
from .serializers import UserSerializer, AskSerializer, AnswerSerializer, VotingSerializer

# CRUD para usuarios (User)
class UserListCreate(APIView):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user_list.html', {'users': users})

    def post(self, request):
        # Usamos request.POST para obtener los datos del formulario HTML
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            users = User.objects.all()
            return render(request, 'user_list.html', {'users': users, 'message': 'Usuario creado exitosamente'})
        users = User.objects.all()
        return render(request, 'user_list.html', {'users': users, 'errors': serializer.errors})


class UserDetail(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return render(request, 'user_detail.html', {'user': user})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        # Usamos request.POST para los datos del formulario HTML
        serializer = UserSerializer(user, data=request.POST, partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'user_detail.html', {'user': user, 'message': 'Usuario actualizado exitosamente'})
        return render(request, 'user_detail.html', {'user': user, 'errors': serializer.errors})

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        # Confirmar eliminación desde HTML
        if request.method == "POST":
            if Voting.objects.filter(user_id=user).exists():
                return render(request, 'user_confirm_delete.html', {'user': user, 'error': 'No se puede eliminar un usuario con votos asociados'})
            user.delete()
            users = User.objects.all()
            return render(request, 'user_list.html', {'users': users, 'message': 'Usuario eliminado exitosamente'})
        return render(request, 'user_confirm_delete.html', {'user': user})

# CRUD para preguntas (Ask)
class AskListCreate(APIView):
    def get(self, request):
        asks = Ask.objects.all()
        return render(request, 'ask_list.html', {'asks': asks})

    def post(self, request):
        # Usamos request.POST para los datos del formulario HTML
        serializer = AskSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            asks = Ask.objects.all()
            return render(request, 'ask_list.html', {'asks': asks, 'message': 'Pregunta creada exitosamente'})
        asks = Ask.objects.all()
        return render(request, 'ask_list.html', {'asks': asks, 'errors': serializer.errors})


class AskDetail(APIView):
    def get(self, request, pk):
        ask = get_object_or_404(Ask, pk=pk)
        return render(request, 'ask_detail.html', {'ask': ask})

    def post(self, request, pk):
        ask = get_object_or_404(Ask, pk=pk)
        # Usamos request.POST para los datos del formulario HTML
        serializer = AskSerializer(ask, data=request.POST, partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'ask_detail.html', {'ask': ask, 'message': 'Pregunta actualizada exitosamente'})
        return render(request, 'ask_detail.html', {'ask': ask, 'errors': serializer.errors})

    def delete(self, request, pk):
        ask = get_object_or_404(Ask, pk=pk)
        # Confirmar eliminación desde HTML
        if request.method == "POST":
            if Answer.objects.filter(ask_id=ask).exists():
                return render(request, 'ask_confirm_delete.html', {'ask': ask, 'error': 'No se puede eliminar una pregunta con respuestas asociadas'})
            ask.delete()
            asks = Ask.objects.all()
            return render(request, 'ask_list.html', {'asks': asks, 'message': 'Pregunta eliminada exitosamente'})
        return render(request, 'ask_confirm_delete.html', {'ask': ask})

# CRUD para respuestas (Answer)
class AnswerListCreate(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        return render(request, 'answer_list.html', {'answers': answers})

    def post(self, request):
        # Usamos request.POST para los datos del formulario HTML
        serializer = AnswerSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            answers = Answer.objects.all()
            return render(request, 'answer_list.html', {'answers': answers, 'message': 'Respuesta creada exitosamente'})
        answers = Answer.objects.all()
        return render(request, 'answer_list.html', {'answers': answers, 'errors': serializer.errors})


class AnswerDetail(APIView):
    def get(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        return render(request, 'answer_detail.html', {'answer': answer})

    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        # Usamos request.POST para los datos del formulario HTML
        serializer = AnswerSerializer(answer, data=request.POST, partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'answer_detail.html', {'answer': answer, 'message': 'Respuesta actualizada exitosamente'})
        return render(request, 'answer_detail.html', {'answer': answer, 'errors': serializer.errors})

    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        # Confirmar eliminación desde HTML
        if request.method == "POST":
            if Voting.objects.filter(answer_id=answer).exists():
                return render(request, 'answer_confirm_delete.html', {'answer': answer, 'error': 'No se puede eliminar una respuesta con votos asociados'})
            answer.delete()
            answers = Answer.objects.all()
            return render(request, 'answer_list.html', {'answers': answers, 'message': 'Respuesta eliminada exitosamente'})
        return render(request, 'answer_confirm_delete.html', {'answer': answer})

# CRUD para votos (Voting)
class VotingListCreate(APIView):
    def get(self, request):
        votes = Voting.objects.all()
        return render(request, 'voting_list.html', {'votes': votes})

    def post(self, request):
        # Usamos request.POST para los datos del formulario HTML
        serializer = VotingSerializer(data=request.POST)
        if serializer.is_valid():
            # Verificamos si el voto ya existe para un usuario y una respuesta
            if Voting.objects.filter(
                answer_id=serializer.validated_data['answer_id'],
                user_id=serializer.validated_data['user_id']
            ).exists():
                return render(request, 'voting_list.html', {'votes': Voting.objects.all(), 'error': 'El usuario ya votó por esta respuesta'})
            serializer.save()
            return render(request, 'voting_list.html', {'votes': Voting.objects.all(), 'message': 'Voto registrado exitosamente'})
        return render(request, 'voting_list.html', {'votes': Voting.objects.all(), 'errors': serializer.errors})

class VotingDetail(APIView):
    def delete(self, request, pk):
        vote = get_object_or_404(Voting, pk=pk)
        # Confirmar eliminación desde HTML
        if request.method == "POST":
            vote.delete()
            return render(request, 'voting_list.html', {'votes': Voting.objects.all(), 'message': 'Voto eliminado exitosamente'})
        return render(request, 'voting_confirm_delete.html', {'vote': vote})
