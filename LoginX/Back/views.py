from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import AgregarUsuario, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
#@login_required(login_url='login')
def gestionarUsuario(request):
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        #Limpiar cada vez que se entre a la vista
        data=form.cleaned_data
        #Creamos el objeto usuario
        usuario=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
        #Luego lo guardamos
        usuario.save()
        #Registramos en la base de datos
        regDB=Usuario(user=usuario,nombre=data.get("nombre"),apellido=data.get("apellido"))
        #Lo guardamos en la base de datos
        regDB.save()
    form=AgregarUsuario()
    usuarios=Usuario.objects.all()
    return render(request,"gestionarUsuario.html",{'usuarios':usuarios,'form':form})
def ingresar(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request, user)
            return redirect('user_logged')
    return render(request,"login.html",{'form':form})

def user_logged(request):
    return render(request,"user_logged.html")

def password_reset(request):
    return redirect('password_reset_done')
def password_reset_done(request):
    return render(request,"password_reset_done.html")

def index(request):
     return render(request, "index.html")

@login_required(login_url='login')
def salir(request):
    logout(request)
    return redirect('index')

def listing(request):
    usuario_list = Usuario.objects.all()
    paginator = Paginator(usuario_list,5)
    page = request.GET.get('page')
    usuarios = paginator.get_page(page)
    return render(request,'listing.html',{'usuarios':usuarios})

#def email(request):
#    subject = 'Thank you for registering to our site'
#    message = ' it  means a world to us '
#    email_from = settings.EMAIL_HOST_USER
#    print(settings.EMAIL_HOST_USER)
#    recipient_list = ['receiver@gmail.com',]
#    send_mail( subject, message, email_from, recipient_list )
#    print("Paso por aqui1")
#    return redirect('password_reset')
