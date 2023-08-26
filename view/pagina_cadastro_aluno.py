class cadastro_de_aluno:
    @staticmethod
    
    def pegar_dados_alunos(): 
        nome = input("DIGITE O NOME DO ALUNO: ")
        idade = int(input("DIGITE A IDADE DO ALUNO: "))
        peso = float(input("DIGITE O PESO DO ALUNO: "))
        return nome, idade, peso
    @staticmethod
    
    def mostrar_messagem(menssagem):
        print(menssagem)