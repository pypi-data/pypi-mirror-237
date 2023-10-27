# Biblioteca para trabalhar com o Rabbit
- Ao instanciar a classe do Rabbit já deve ser passado os parametros de conexão e de reconexão se assim desejar.
- Nesta biblioteca pode ser encontrado os metodos:
    - getMessages
        - Pegar as mensagens de uma fila e passa a mesma para a função de callback passada para a função getMessages, exemplo:
        ````
            class example():
                def process_message(self, channel, method, properties, body):
                    pass
                def example(self):
                    self.queue.getMessages('name_queue', 'name_exchange', self.process_message, 1)
        ````
        - Parametros:
            - queue: str
                - Nome da fila que ficará escutando para ler as mensagens.
            - exchange: str
                - Nome da exchange que a fila está vinculada.
            - message_handler: typing.Callable
                - Função de processamento da mensagem recebida, serve para fazer o processamento da mensagem que está entrando na fila.
            - limit_get_messages: int
                - Quantidade de mensagens que deseja pegar por vez do rabbit, por padrão se nao informada será atribuido 1.
    - postMessage
        - Enviar uma mensagem para uma fila do rabbit.
        - Parametros:
            - queue: str
                - Nome da fila que será colocado a mensagem.
            - exchange: str
                - Nome da exchange que a fila está vinculada.
            - message: str
                - Conteúdo da mensagem que será colocado na fila.
    - close_connection
        - Realizar o fechamento da conexão com o rabbit.
# Requerimentos(DEV):
- Para poder iniciar é preciso ter instalado as dependências abaixo:
    - [Python](https://www.python.org/)
    - [Pip](https://pip.pypa.io/)
    - [Poetry](https://poetry.eustace.io/)
    - [Git](https://git-scm.com/)
    - [poethepoet](https://github.com/nat-n/poethepoet)
# Como montar a biblioteca e fazer uploud para o pypi.org
- Video de auxlilio pode ser encontrado [aqui](https://youtu.be/YpTuuGBggcE?t=828)
- O arquivo de LICENCE é necessário para dizer de quem é esta biblioteca, alterar de acordo com as regras e necessidade.
- Necessário instalar o setuptools, já está sendo instalado pelo poetry
######
    pip install setuptools
- Criar/editar o arquivo setup.py e configura-lo de acordo com a necessidade
- Rodar o comando abaixo para ele realizar o empacotamento da nossa biblioteca de acordo com o que está configurado no setup.py:
######
    python3 setup.py sdist
- Necessário instalar o twine para  poder fazer uploud desta biblioteca para fazer uploud para o pypi:
######
    pip install twine
- Necessário ter uma conta no pypi criado para poder fazer uploud
- Rodar o comando abaixo para fazer o uploud de tudo que tem na pasta dist que foi criada pelo processo de geração da nossa biblioteca:
######
    twine upload dist/*

# Testes
- Todos os testes foram desenvolvidos com o pytest, para executar os mesmos pode ser executado o comando ```poetry run coverage run -m pytest``` ou se caso tenha instalado o [poethepoet](https://github.com/nat-n/poethepoet) pode ser executado ```poe cove_tests```