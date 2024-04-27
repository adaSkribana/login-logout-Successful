from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import View, FormView  
from django.urls import reverse_lazy
from django.contrib.auth import login

from django.contrib.auth.forms import AuthenticationForm 

class MiVista(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        return render(request, 'mi_template.html', {'user': request.user})

    def post(self, request):  # Manejar solicitudes POST
        # Lógica para manejar solicitudes POST aquí si es necesario
        pass

class OtraVista(PermissionRequiredMixin, View):
    permission_required = 'permisos_app.puede_ver_algo'

    def get(self, request):
        return render(request, 'otra_template.html', {'user': request.user})

    def handle_no_permission(self):
        return redirect('acceso_denegado')

def acceso_denegado(request):
    return render(request, 'acceso_denegado.html', {})

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('mi_vista')  # Redirigir a 'mi_vista' después de iniciar sesión

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)