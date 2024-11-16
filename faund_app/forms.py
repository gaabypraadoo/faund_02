from django import forms
from .models import ONG, Tutor, Pet
from localflavor.br.forms import BRStateSelect

class Ong_form(forms.ModelForm):
    estado = forms.ChoiceField(
        choices=[('', 'Selecione um estado')] + list(BRStateSelect().choices),
        label='Estado'
    )
    email_ong = forms.EmailField(label="E-mail", required=True)
    senha_ong = forms.CharField(widget=forms.PasswordInput(), label="Senha")

    class Meta:
        model = ONG
        fields = [
            'imagem_perfil', 'nome_ong', 'data_criacao', 'cidade', 'estado', 'endereco', 
            'link_doacao', 'instagram', 'historia', 'telefone', 'email_ong', 'senha_ong'
        ]
        labels = {
            'nome_ong': 'Nome da ONG',
            'data_criacao': 'Data de Criação',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'endereco': 'Endereço',
            'link_doacao': 'Link de Doação',
            'instagram': 'Instagram',
            'historia': 'História',
            'telefone': 'Telefone',
            'email_ong': 'E-mail',
            'senha_ong': 'Senha',
        }

    def clean_email_ong(self):
        email = self.cleaned_data.get('email_ong')
        if ONG.objects.filter(email_ong=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email

class Tutor_form(forms.ModelForm):
    estado = forms.ChoiceField(
        choices=[('', 'Selecione um estado')] + list(BRStateSelect().choices),
        label='Estado'
    )
    email_tutor = forms.EmailField(label="E-mail", required=True)
    senha_tutor = forms.CharField(widget=forms.PasswordInput(), label="Senha")

    class Meta:
        model = Tutor
        fields = [
            'imagem_perfil', 'nome_tutor', 'data_nascimento', 'cidade', 'estado', 
            'endereco', 'telefone', 'email_tutor', 'senha_tutor'
        ]
        labels = {
            'nome_tutor': 'Nome',
            'data_nascimento': 'Data de Nascimento',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'endereco': 'Endereço',
            'telefone': 'Telefone',
            'email_tutor': 'E-mail',
            'senha_tutor': 'Senha',
        }

    def clean_email_tutor(self):
        email = self.cleaned_data.get('email_tutor')
        if Tutor.objects.filter(email_tutor=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email
    
class Pet_form(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'imagem_perfil','nome', 'idade', 'data_ong', 'raca', 'porte', 'pelagem', 'sexo', 'tipo_pet', 'historia'
        ]
        labels = {
            'nome': 'Nome do Pet',
            'idade': 'Idade',
            'data_ong': 'Data de chegada na ONG',
            'raca': 'Raça',
            'porte': 'Porte',
            'pelagem': 'Pelagem',
            'sexo': 'Sexo',
            'tipo_pet': 'Tipo',
            'historia': 'História',
        }
