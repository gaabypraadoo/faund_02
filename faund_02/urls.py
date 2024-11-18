"""
URL configuration for faund_02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from faund_app import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('cadastro/', views.pagina_cadastro, name='pagina_cadastro'),
    path('cadastro/cadastro_ong/', views.cadastro_ong, name='cadastro_ong'),  # Alterado para incluir 'cadastro/'
    path('cadastro/cadastro_tutor/', views.cadastro_tutor, name='cadastro_tutor'),  # Alterado para incluir 'cadastro/'
    path('login/', views.login, name='login'),
    path('cadastro_pet/', views.cadastro_pet, name='cadastro_pet'),
    path('ong/', views.ong, name='ong'),
    path('tutor/', views.tutor, name='tutor'),
    path('adocao/', views.pagina_adocao, name='pagina_adocao'),
    path('lista_ong/', views.lista_ong, name='lista_ong'),
    path('perfil_pet/<int:pet_id>/', views.pet, name='perfil_pet'),
    path('pets_cadastrados/', views.pets_cadastrados, name='pets_cadastrados'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pet_adotado/', views.pet_adotado, name='pet_adotado'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
