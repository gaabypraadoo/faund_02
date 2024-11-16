# models.py
from django.db import models
from django.contrib.auth.models import User


class ONG(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem_perfil = models.ImageField(upload_to='imagens_perfil/', blank=True, null=True)
    nome_ong = models.CharField(max_length=200)
    data_criacao = models.DateField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    endereco = models.CharField(max_length=300)
    link_doacao = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    historia = models.TextField()
    telefone = models.CharField(max_length=30)
    email_ong = models.EmailField(unique=True)

    def __str__(self):
        return self.nome_ong

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagem_perfil = models.ImageField(upload_to='imagens_perfil/', blank=True, null=True)
    nome_tutor = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    endereco = models.CharField(max_length=300)
    telefone = models.CharField(max_length=30)
    email_tutor = models.EmailField(unique=True)

    def __str__(self):
        return self.nome_tutor

class Pet(models.Model):
    imagem_perfil = models.ImageField(upload_to='imagens_perfil/', blank=True, null=True)
    nome = models.CharField(max_length=200)
    ong = models.ForeignKey(ONG, related_name='animais', on_delete=models.CASCADE)
    idade = models.CharField(max_length=200)
    data_ong = models.DateField()
    raca = models.CharField(max_length=100)
    porte = models.CharField(max_length=100)
    pelagem = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    tipo_pet = models.CharField(max_length=50)
    historia = models.TextField()

    TIPO_CHOICES = [
        ('todos', 'Todos'),
        ('gato', 'Gato'),
        ('cachorro', 'Cachorro'),
        # Outros tipos de pets
    ]

    def __str__(self):
        return self.nome
    
# class Mensagem(models.Model):
#     remetente = models.ForeignKey(User, related_name='mensagens_enviadas', on_delete=models.CASCADE)
#     destinatario = models.ForeignKey(User, related_name='mensagens_recebidas', on_delete=models.CASCADE)
#     conteudo = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"De {self.remetente} para {self.destinatario}: {self.conteudo[:20]}"

# from django.db import models
# import sqlite3 
# import bcrypt
# # Create your models here.

# class Database:
#     def __init__(self, db_faund='faund.db'):
#         try:
#             self.conn = sqlite3.connect(db_faund)
#             self.cursor = self.conn.cursor()
#             self.create_tables()
#         except sqlite3.Error as e:
#             print(f"Não foi possível conectar com o banco de dados: {e}")

#     def create_tables(self): #table for ongs
#         self.cursor.execute('''
#             CREATE TABLE IF NOT EXISTS ongs(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 ong_nome TEXT NOT NULL,
#                 data_criacao DATE NOT NULL,
#                 cidade TEXT NOT NULL,
#                 estado TEXT NOT NULL,
#                 endereco TEXT NOT NULL,
#                 quant_pets INTEGER NOT NULL,
#                 link_doacao TEXT NOT NULL,
#                 instagram TEXT NOT NULL,
#                 historia TEXT NOT NULL,
#                 telefone INTEGER NOT NULL,
#                 email_ong_id INTEGER NOT NULL,
#                 senha_ong TEXT NOT NULL
#             )           
#     ''')
#         #table for tutor
#         self.cursor.execute('''
#             CREATE TABLE IF NOT EXISTS tutor(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 tutor_nome TEXT NOT NULL,
#                 data_nascimento DATE NOT NULL,
#                 cidade TEXT NOT NULL,
#                 estado TEXT NOT NULL,
#                 endereco TEXT NOT NULL,
#                 telefone INTEGER NOT NULL,
#                 email_tutor_id INTEGER NOT NULL,
#                 senha_tutor TEXT NOT NULL
#             )                         
#     ''')
#         #table for pets
#         self.cursor.execute('''
#             CREATE TABLE IF NOT EXISTS pets(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 email_ong_id INTEGER NOT NULL,
#                 nome_pet TEXT NOT NULL,
#                 idade INTEGER NOT NULL,
#                 data_ong DATE NOT NULL,
#                 raca TEXT NOT NULL,
#                 porte TEXT NOT NULL,
#                 pelagem TEXT NOT NULL,
#                 sexo TEXT NOT NULL,
#                 historia TEXT NOT NULL
#             )
#     ''')
#         self.conn.commit()

#     def add_ong(self, ong_nome, data_criacao, cidade, estado, endereco, quant_pets, link_doacao, instagram, historia, telefone, email_ong_id, senha_ong):
#         hashed_password = bcrypt.hashpw(senha_ong.encode('utf-8'), bcrypt.gensalt())
#         self.cursor.execute('''
#             INSERT INTO ongs (ong_nome, data_criacao, cidade, estado, endereco, quant_pets, link_doacao, instagram, historia, telefone, email_ong_id, senha_ong)         
#             VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        
#         ''',(ong_nome, data_criacao, cidade, estado, endereco, quant_pets, link_doacao, instagram, historia, telefone, email_ong_id, hashed_password))
#         self.conn.commit()

#     def add_tutor(self, tutor_nome, data_nascimento, cidade, estado, endereco, telefone, email_tutor, senha_tutor):
#         hashed_password = bcrypt.hashpw(senha_tutor.encode('utf-8'), bcrypt.gensalt())
#         self.cursor.execute('''
#             INSERT INTO tutor(tutor_nome, data_nascimento, cidade, estado, endereco, telefone, email_tutor, senha_tutor)
#             VALUES (?,?,?,?,?,?,?,?)
#         ''', (tutor_nome, data_nascimento, cidade, estado, endereco, telefone, email_tutor, hashed_password))
#         self.conn.commit()

#     def add_pet(self, email_ong_id, nome_pet, idade, data_ong, raca, porte, pelagem, sexo, historia):
#         self.cursor.execute('''
#             INSERT INTO pets (email_ong_id, nome_pet, idade, data_ong, raca, porte, pelagem, sexo, historia)
#             VALUES (?,?,?,?,?,?,?,?,?)
#         ''', (email_ong_id, nome_pet, idade, data_ong, raca, porte, pelagem, sexo, historia))
#         self.conn.commit()

#     def close(self):
#         self.conn.close()