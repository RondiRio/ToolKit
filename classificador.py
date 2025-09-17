from OpcoesMenu import OpcoesMenu

class classificador(OpcoesMenu):
    def __ini__(self):
        super().__ini__("Classificador JSON T/I/N")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        print("Aqui, classificamos strings como T = Terminadas, I = Infinitas ou N = Nulas")
        print('ainda não implementamos')
    