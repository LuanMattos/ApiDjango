# :page_facing_up: API REST com Django Rest
API Alunos
<br>
<br>
### Executar a aplicação

```bash
# Clone este repositório 
$ git clone git@github.com:LuanMattos/ApiDjango.git

# Acesse a pasta do projeto no terminal/cmd
$ cd ApiDjango

# Instale o virtual env
$ python -m venv

# Ative o venv
Windows $ venv\Scripts\activate 

#execute o banco de dados postgres:
$ docker-compose up -d

#Execute as migrações
$ python manage.py migrate

#Execute o servidor
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse http://localhost:800 
# Usuário e Senha do admin = admin (http://localhost:8000/admin)

No admin é onde você cadastra seus alunos(as)
```
<b>Parte técnica do projeto</br>
-API's básico
<br>
-Serializer e Auth Basic
<br>
-Versionamento
<br>
-Níveis e permissões de usuário
<br>
-limit no número de request's (Throttle)
<br>
-Integração de um front-end com React (BFF)
<br>
-CORS
<br>


# :art: Layout dos Endpoints
<br>




