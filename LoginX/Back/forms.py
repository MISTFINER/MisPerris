from django import forms


class AgregarUsuario(forms.Form):

   username=forms.CharField(widget=forms.TextInput(), label="Nombre de Usuario")
   password=forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
   correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
   nombre=forms.CharField(widget=forms.TextInput(),label="Nombre Real")
   apellido=forms.CharField(widget=forms.TextInput(),label="Apellido")

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(), label="Nombre de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
