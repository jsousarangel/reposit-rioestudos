import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd 
from mysql.connector import Error

# 1) Cursos (ids gerados: 1, 2, 3)
cursos = [
    # (nome_curso, carga_horaria, turno)
    ('Informática',    800,  'Manhã'),
    ('Administração',  1000, 'Noite'),
    ('Enfermagem',     1200, 'Tarde'),
]

# 2) Alunos (ids gerados: 1 a 10) — o último campo é o id_curso (FK)
# 1 = Informática, 2 = Administração, 3 = Enfermagem
alunos = [
    # (nome, cpf, data_nascimento, email, telefone, data_matricula, id_curso)
    ('Ana Souza',      '11122233344', '2005-03-14', 'ana@email.com',     '21999990001', '2026-02-01', 1),  # id 1
    ('Bruno Lima',     '22233344455', '2004-07-22', 'bruno@email.com',   '21999990002', '2026-02-01', 1),  # id 2
    ('Carla Mendes',   '33344455566', '2003-11-05', 'carla@email.com',   '21999990003', '2026-02-03', 2),  # id 3
    ('Diego Ferreira', '44455566677', '2006-01-30', 'diego@email.com',   '21999990004', '2026-02-05', 3),  # id 4
    ('Joana Ribeiro',  '55566677788', '2005-04-21', 'joana@email.com',   '21999990005', '2026-02-07', 1),  # id 5
    ('Lucas Martins',  '66677788899', '2004-09-10', 'lucas@email.com',   '21999990006', '2026-02-07', 1),  # id 6
    ('Mariana Costa',  '77788899900', '2003-12-02', 'mariana@email.com', '21999990007', '2026-02-10', 3),  # id 7
    ('Pedro Alves',    '88899900011', '2006-06-18', 'pedro@email.com',   '21999990008', '2026-02-10', 2),  # id 8
    ('Rafaela Nunes',  '99900011122', '2005-08-25', 'rafaela@email.com', '21999990009', '2026-02-12', 3),  # id 9
    ('Thiago Rocha',   '10120230344', '2004-02-14', 'thiago@email.com',  '21999990010', '2026-02-12', 1),  # id 10
]

# 3) Disciplinas (ids gerados: 1 a 6) — o último campo é o id_curso (FK)
disciplinas = [
    # (nome_disciplina, carga_horaria, id_curso)
    ('Lógica de Programação', 80, 1),  # id 1
    ('Banco de Dados',        60, 1),  # id 2
    ('Gestão Financeira',     60, 2),  # id 3
    ('Marketing',             40, 2),  # id 4
    ('Anatomia',              80, 3),  # id 5
    ('Farmacologia',          60, 3),  # id 6
]

# 4) Notas — cada aluno recebe nota nas disciplinas do seu curso
notas = [
    # (id_aluno, id_disciplina, nota, data_avaliacao)
    # Informática (alunos 1, 2, 5, 6, 10 | disciplinas 1 e 2)
    (1, 1, 8.5, '2026-06-30'), (1, 2, 9.0, '2026-06-30'),
    (2, 1, 7.0, '2026-06-30'), (2, 2, 6.5, '2026-06-30'),
    (5, 1, 9.5, '2026-06-30'), (5, 2, 8.0, '2026-06-30'),
    (6, 1, 6.0, '2026-06-30'), (6, 2, 7.5, '2026-06-30'),
    (10, 1, 8.0, '2026-06-30'), (10, 2, 8.5, '2026-06-30'),
    # Administração (alunos 3, 8 | disciplinas 3 e 4)
    (3, 3, 7.5, '2026-06-30'), (3, 4, 8.0, '2026-06-30'),
    (8, 3, 6.5, '2026-06-30'), (8, 4, 9.0, '2026-06-30'),
    # Enfermagem (alunos 4, 7, 9 | disciplinas 5 e 6)
    (4, 5, 9.0, '2026-06-30'), (4, 6, 8.5, '2026-06-30'),
    (7, 5, 7.0, '2026-06-30'), (7, 6, 6.0, '2026-06-30'),
    (9, 5, 8.5, '2026-06-30'), (9, 6, 9.5, '2026-06-30'),
]

try:
    conexao = mysql.connector.connect(
        host = 'localhost',
        user='root',
        password='',
        database= 'escola',
    if conexao.is_connected():
        print('conectado com sucesso!')
        cursor = conexao.cursor()
    
except error as e:
    print(f'erro ao conectar ou executar: {e}')
finally:
    if 'cursor' in locals():
        try:
            cursor.close():
        except Exception:
            pass
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print('conexão encerrada')

)