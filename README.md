# ApiPython

Como Usar o projeto:

Crie uma venv com o comando -> python -m venv nome_da_venv,
após isso, ative-a -> nome_da_venv/Scripts/activate

Instale os requirements dentro do ambiente virtual com o seguinte comando -> pip install -r requirements.txt

O meu banco de dados local está no database, o ideal é que você crie um banco de dados mysql na sua maquina local editando em DATABASES que está nas configurações da api.

Exemplo: 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '', #nome do banco de dados
        'USER': '', #usuario do banco de dados
        'PASSWORD': '', #senha do usuario do banco de dados
        'HOST': '', #host do banco de dadoos
        'PORT': '', #porta do banco de dados
    }
}

Sobre o projeto em si:

1 - Foi feito com Python/django/ninjaRestAPI
2 - Crie seu super usuário para acesso no admin
3 - Não foi dado deploy ou posto em um mysql na nuvem por questão de tempo e por estar aprendendo a lidar agora com essas situações
4 - Para acessar o admin entre com /admin
5 - Para acessar a api entre com /docs
