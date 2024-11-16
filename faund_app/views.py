from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import Ong_form, Tutor_form, Pet_form
from .models import ONG, Tutor, Pet
from localflavor.br.br_states import STATE_CHOICES
from django.contrib import messages
from django.contrib.auth.models import Group

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

def pagina_cadastro(request):
    return render(request, 'pagina_cadastro.html')

def cadastro_ong(request):
    if request.method == 'POST':
        ong_form = Ong_form(request.POST, request.FILES)
        telefone = request.POST.get('telefone')
        # print('Cadastro ONG')
        
        if ong_form.is_valid():
            print('AAA')
            if len(telefone) > 30:
                ong_form.add_error('telefone', "O número de telefone deve ter no máximo 15 caracteres.")
                return render(request, 'cadastro_ong.html', {'ong_form': ong_form})

            usuario = User.objects.create_user(
                username=ong_form.cleaned_data['email_ong'],
                email=ong_form.cleaned_data['email_ong']
            )
            usuario.set_password(ong_form.cleaned_data['senha_ong'])
            usuario.save()

            ong = ong_form.save(commit=False)
            ong.user = usuario
            ong.telefone = telefone
            ong.save()

            from django.contrib.auth.models import Group
            grupo_ong, criado = Group.objects.get_or_create(name='ONG')
            usuario.groups.add(grupo_ong)

            auth_login(request, usuario)

            print('perfil ong')
            return redirect('ong') 
        # , ong_id=ong.id)
        else:
            for field, errors in ong_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, 'cadastro_ong.html', {'ong_form': ong_form})
    else:
        ong_form = Ong_form()
    
    return render(request, 'cadastro_ong.html', {'ong_form': ong_form})

@login_required
def ong(request):
    ong = get_object_or_404(ONG, user=request.user)
    return render(request, 'ong.html', {'ong': ong})
    # ong = request.user
    # # if request.method == 'POST':
    # form = Ong_form(request.POST, request.FILES, instance=ong)
    # form.save()
    # return render(request, 'ong.html')
    # #     print('perfil ong')
    # #     form = Ong_form(request.POST, request.FILES, instance=ong)
    # #     if form.is_valid():
    # #         form.save()
    # #     return render(request, 'ong.html')
    # # else:
    # #     form = Ong_form(instance=ong)
    
    # # return render(request, 'cadastro_ong.html', {'form': form})

@login_required
def cadastro_pet(request):
    print("Iniciando o cadastro do pet")

    if request.method == 'POST':
        pet_form = Pet_form(request.POST, request.FILES)

        if pet_form.is_valid():
            if hasattr(request.user, 'ong'):
                pet = pet_form.save(commit=False)
                pet.ong = request.user.ong  # Associa automaticamente a ONG
                pet.save()

                messages.success(request, "Pet cadastrado com sucesso!")
                return redirect('pets_cadastrados')
            else:
                messages.error(request, "Usuário não possui uma ONG associada.")
                return redirect('erro')
        else:
            print("Erros no formulário:", pet_form.errors)
            for field, errors in pet_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        pet_form = Pet_form()

    return render(request, 'cadastro_pet.html', {'pet_form': pet_form})

@login_required
def pet(request):
    pet = get_object_or_404(Pet)
    ong = pet.ong  # Acessando a ONG do pet
    telefone_whatsapp = f"55{ong.telefone.replace(' ', '').replace('-', '')}"  # Formatação do número de telefone da ONG

    return render(request, 'perfil_pet.html', {'pet': pet, 'ong': ong, 'telefone_whatsapp': telefone_whatsapp})

def cadastro_tutor(request):
    if request.method == 'POST':
        tutor_form = Tutor_form(request.POST, request.FILES)
        telefone = request.POST.get('telefone')
        print('Cadastro Tutor')
        
        if tutor_form.is_valid():
            if len(telefone) > 30:
                tutor_form.add_error('telefone', "O número de telefone deve ter no máximo 15 caracteres.")
                return render(request, 'cadastro_tutor.html', {'tutor_form': tutor_form})

            usuario = User.objects.create_user(
                username=tutor_form.cleaned_data['email_tutor'],
                email=tutor_form.cleaned_data['email_tutor']
            )
            usuario.set_password(tutor_form.cleaned_data['senha_tutor'])
            usuario.save()

            tutor = tutor_form.save(commit=False)
            tutor.user = usuario
            # tutor.nome_tutor = "Tutor"
            tutor.telefone = telefone
            tutor.save()

            from django.contrib.auth.models import Group
            grupo_tutor, criado = Group.objects.get_or_create(name='Tutor')
            usuario.groups.add(grupo_tutor)

            auth_login(request, usuario)

            print('perfil tutor')
            return redirect('tutor')
        # , tutor_id=tutor.id)
        else:
            for field, errors in tutor_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, 'cadastro_tutor.html', {'tutor_form': tutor_form})
    else:
        tutor_form = Tutor_form()
    
    return render(request, 'cadastro_tutor.html', {'tutor_form': tutor_form})

@login_required
def tutor(request):
    tutor = get_object_or_404(Tutor, user=request.user)
    return render(request, 'tutor.html', {'tutor': tutor})
    # tutor = request.user
    # if request.method == 'POST':
    #     form = Tutor_form(request.POST, request.FILES, instance=tutor)
    #     if form.is_valid():
    #         form.save()
    #         print('perfil tutor')
    #         return redirect('tutor')
    # else:
    #     form = Tutor_form(instance=tutor)
    
    # return render(request, 'cadastro_tutor.html', {'form': form})

def login(request):
    if request.method == 'POST':
        print("login")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)

                # Redireciona com base no perfil do usuário
                if hasattr(user, 'ong'):
                    print("ong")
                    return redirect('ong')
                elif hasattr(user, 'tutor'):
                    print("tutor")
                    return redirect('tutor')
                else:
                    return redirect('pagina_inicial')
            else:
                messages.error(request, 'E-mail ou senha incorretos.')
        else:
            messages.error(request, 'Por favor, preencha todos os campos corretamente.')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def redirecionar_apos_login(request):
    user = request.user
    if hasattr(user, 'ong') and user.ong:
        return redirect('ong', ong_id=user.ong.id)
    elif hasattr(user, 'tutor') and user.tutor:
        return redirect('tutor', tutor_id=user.tutor.id)
    else:
        return redirect('pagina_inicial')

@login_required
def pagina_adocao(request):
    tutor_form = Tutor_form(request.GET or None)  # Para manter os filtros após submissão
    tipo_pet = request.GET.get('tipo_pet', '')
    estado = request.GET.get('estado', '')

    # Selecionar pets apenas se algum filtro for ativado 
    if not estado and not tipo_pet:
        pets = []
    else:
        pets = Pet.objects.all()

    # Filtrar pets conforme o estado e tipo selecionados
    if estado:
        pets = pets.filter(ong__estado=estado)
    if tipo_pet:
        pets = pets.filter(tipo_pet=tipo_pet)

    context = {
        'tutor_form': tutor_form,
        'pets': pets,
        'tipo_pet': tipo_pet,
        'estado': estado,
    }
    return render(request, 'pagina_adocao.html', context)

@login_required
def lista_ong(request):
    ongs = ONG.objects.all() 
    return render(request, 'lista_ong.html', {'ongs': ongs})

@login_required
def pets_cadastrados(request):
    print("lista de pets cadastrados")
    if request.user.is_authenticated and hasattr(request.user, 'ong'):
        # Filtra os pets que pertencem à ONG do usuário logado
        ong = request.user.ong
        pets = Pet.objects.filter(ong=ong)
    else:
        pets = []
    return render(request, 'pets_cadastrados.html', {'pets': pets})    

# @login_required
# def ong(request):
#     ong = request.user  
#     return render(request, 'ong.html', {'ong': ong})

# @login_required
# def tutor(request):
#     tutor = request.user  
#     return render(request, 'tutor.html', {'tutor': tutor})