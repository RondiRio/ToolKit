from OpcoesMenu import OpcoesMenu

class ReconheceParA(OpcoesMenu):
    def __init__(self):
        super().__init__('Reconhece Par A')
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        cadeia = input("Digite uma cadeia: ")
        
        acha_a = cadeia.count('a')
        
        par_a = acha_a % 2 ==0
        
        # Verificando se termina com b
        
        import re
        padrao_b_final = re.match(r'^a*b*$', cadeia)
        print(f"Número de a's: {acha_a} (par: {par_a})")
        print(f"Cadeia aceita por L_Par_a: {par_a}")
        print(f"Cadeia aceita por a*b* : {padrao_b_final is not None} ")
        