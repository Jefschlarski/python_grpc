class Hello:
    def __init__(self, name):
        self.name = name

    def mensagem(self):
        # Faça alguma coisa com os parâmetros
        mensagem = (f"Hello {self.name}")
        return mensagem