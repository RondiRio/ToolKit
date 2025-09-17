from OpcoesMenu import OpcoesMenu
class VerificarAlfabeto(OpcoesMenu):
    def __init__(self):
        super().__init__("Verifiacar alfabeto e cadeia (sigma={a,b})")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        alfabeto = input("Digite um alfabeto")
        cadeia = input("digite uma cadeia:")
        
        valida = all(char in alfabeto for char in cadeia)
        print(f"Cadeia '{cadeia}' é valida no alfabeto {alfabeto}: {valida}")
        
        if not valida:
            invalidos = set(cadeia) - alfabeto
            print(f"Caracteres inválidos: {invalidos} no alfabeto {alfabeto}")
        