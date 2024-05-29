<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=3498db&height=120&section=header"/>
<div align="center">
  <img src="https://github.com/oficina-do-brito/gym_io/blob/main/archive/modelagem/logo.png" width="70" height="70">
</div>

<h4 align="center">A portfolio to demonstrate what I do, projects, code sales, blog etc :call_me_hand:</h4>

<p align="center">
  [Project's badges]
</p>

<p align="center">
  <a href="https://github.com/oficina-do-brito/gym_io/blob/main/archive/modelagem/nomenclatura.md">Nomenclatura de banco de Dados</a> •
  <a href="#Modelo_Conceitual">Modelo Conceitual</a> •
   <a href="https://github.com/oficina-do-brito/gym_io/blob/main/archive/modelagem/breakpoints.md">Recursos</a> •
  <a href="#">Modelo Logico</a> •
  <a href="#Tecnologias_usadas">Tecnologias Usadas</a> •
  <a href="#Rodando_aplicação">Rodando aplicação</a> •
</p>

## Modelo_Conceitual

<img src="#" />

## Tecnologias_usadas

IDE:

<img src="https://user-images.githubusercontent.com/25181517/192108891-d86b6220-e232-423a-bf5f-90903e6887c3.png" width="50" height="50">

Backend:

<img src="https://github.com/marwin1991/profile-technology-icons/assets/62091613/9bf5650b-e534-4eae-8a26-8379d076f3b4" width="50" height="50"><img src="https://user-images.githubusercontent.com/25181517/183896128-ec99105a-ec1a-4d85-b08b-1aa1620b2046.png" width="50" height="50">

Frontend:

<img src="https://user-images.githubusercontent.com/25181517/183898054-b3d693d4-dafb-4808-a509-bab54cf5de34.png" width="50" height="50">

## Rodando_aplicação

### Pré Requisitos

- Presizaremos do python 3.10 configurado em nossa maquina e precisaremos criar um virtual env para baixar e executar o projeto.
```
  pip install virtualenv
```
- Criar a venv
```
  virtualenv.exe venv
```
- ativar o ambiente virtual
```
  .\venv\Scripts\activate
```
- baixar as dependencias
```
  pip install -r requirements.txt
```

> [!IMPORTANT]
> Renomear o arquivo ".env.example" para ".env" e colocar suas variaveis de ambiente antes de executar o projeto, ou qualquer task relacionada. Caso contrario ocorrerá erros na execução. A seguir o padrão para preenchimento :

- SECRET_KEY=alguma_key_django
- DEBUG=True

Opcional para Produção
- NAME=novo_db
- HOST=127.0.0.1
- PORT=3306
- USER=username
- PASSWORD=password

### Rodando o projeto backend

- estar no mesmo diretorio quemanage.py:
```python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser```
- iniciar app:
```python manage.py runserver```

### Limpando todos containers e images usadas (cuidado)

`docker-compose down  && docker rmi $(docker images -q) && docker images`


<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=3498db&height=120&section=footer"/>