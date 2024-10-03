from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .authentication import get_tokens_for_user
from rest_framework_simplejwt.tokens import RefreshToken

class UserLoginAPIView(APIView):
    def post(self, request):
        # Autenticación de usuario
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            tokens = get_tokens_for_user(user)
            return Response({'token': tokens, 'user': UserSerializer(user).data})
        return Response({'error': 'Credenciales inválidas'}, status=400)

class PayPalExecuteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        payment_id = request.data.get("paymentID")
        payer_id = request.data.get("payerID")

        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.execute({"payer_id": payer_id}):
            return Response({'mensaje': 'Pago completado con éxito'}, status=200)
        else:
            return Response({'error': 'Error en el procesamiento del pago'}, status=400)

def index(request):
    return render(request, 'core/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    return render(request, 'core/login.html')

def carrito(request):
    return render(request, 'core/carrito.html')

@login_required
def modificar_perfil(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        user = request.user
        user.username = username

        if password and password == confirm_password:
            user.set_password(password)
            update_session_auth_hash(request, user) 

        user.save()
        messages.success(request, 'Perfil actualizado exitosamente.')
        return redirect('modificar_perfil')

    return render(request, 'core/moduser.html', {'user': request.user})
