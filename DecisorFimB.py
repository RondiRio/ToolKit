from OpcoesMenu import OpcoesMenu

class DecisorFimB(OpcoesMenu):
    def __init__(self):
        super().__init__('Decisores cadeia com fim b e/ou cadeia com fim multiplos de 3 sendo b')
        
    def executar(self):
        print(f'=== {self.descricao} ===')
        cadeia = input('digite uma cadeia: ')
        
        termina_com_b = cadeia.endswith('b') if cadeia else False
        
        conta_b = cadeia.count('b')
        conta_mult3_b = conta_mult3_b % 3 == 0
        
        print(f'L_fim_b (terminado com b): {termina_com_b}' )
        print(f"L_mult3_b (quantudade de b's multiplos de 3): {conta_mult3_b} (conta: {conta_b})")