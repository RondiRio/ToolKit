from OpcoesMenu import OpcoesMenu

class DecisorTerminal(OpcoesMenu):
    def __init__(self):
        super().__ini__("Decisor, termina B ou termina b?")
        
    def executar(self):
        print(f"=== {self.descricao} ===")
        cadeia = input('Digite uma cadeia:')
        
        if not cadeia:
            resultado = False
            print("Cadeia vazia, não termina com b")
        else:
            if cadeia[-1] == 'B':
                resultado = cadeia[-1] == 'b'
                print(f"A cadeia {cadeia} termina com B: {resultado}, cadeia inválida")
                quit
            else:
                resultado = cadeia[-1] == 'b'
                print(f"A cadeia {cadeia} termina com b: {resultado}")