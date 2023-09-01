from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mysite.models import formulario
from django.core.mail import send_mail


from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.http import HttpResponseForbidden
from rest_framework.response import Response
# - Homepage



def send_user_data_email(user_data):
    subject = 'Nuevo usuario registrado'
    message = f'Se ha registrado un nuevo usuario con los siguientes datos:\n\n{user_data}'
    
    print(message)
    from_email = 'notificaciondepaginaweb@gmail.com'
    recipient_list = ['notificaciondepaginaweb@gmail.com','maximobatallan@gmail.com']
    send_mail(subject, message, from_email, recipient_list)


@csrf_exempt






def my_csrf_failure_view(request, reason=""):
    return HttpResponseForbidden('CSRF verification failed. Reason: {}'.format(reason))

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def save_formulario(request):
    

    nombre = request.POST.get('nombre')

    telefono = request.POST.get('telefono')
    email = request.POST.get('email')
    texto = request.POST.get('texto')

    formulario1 = formulario(nombre=nombre, telefono=telefono, mail=email, texto=texto)
    formulario1.save()
    user_data = f"nombre: {nombre} telefono: {telefono} texto: {texto}"
    send_user_data_email(user_data)
    
    
    
    return render(request, 'formulario.html')

