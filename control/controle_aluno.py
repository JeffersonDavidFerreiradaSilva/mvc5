from model.model_aluno import aluno_model
from view.pagina_cadastro_aluno import cadastro_de_aluno

class aluno_controle():
    def __init__(self):
        self.modal = aluno_model()
        self.view = cadastro_de_aluno()
    def gravar_aluno(self):
        nome,idade,peso = self.view.pegar_dados_alunos()
        self.modal.salvar_aluno()
        self.view.mostrar_messagem("ALUNO CADASTRADO COM SUCESSO!")