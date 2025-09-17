from OpcoesMenu import OpcoesMenu
import re

class ReconheceParA(OpcoesMenu):
    def __init__(self):
        super().__init__('Reconhecedor L_par_a e a*b*', 'Reconhecedor de duas linguagens por menu')
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        
        # MENU para escolher linguagem (requisito)
        print("Escolha a linguagem para reconhecimento:")
        print("1) L_par_a = {w ∈ {a,b}* | w contém número par de a's}")
        print("2) L = {w | w = a*b*} (zero ou mais a's seguidos de zero ou mais b's)")
        
        while True:
            try:
                opcao = int(input("Escolha uma opção (1-2): "))
                if opcao in [1, 2]:
                    break
                print("Opção inválida!")
            except ValueError:
                print("Digite um número válido!")
        
        cadeia = input("Digite uma cadeia: ")
        
        # VALIDAÇÃO do alfabeto antes da decisão (requisito)
        alfabeto = {'a', 'b'}
        if cadeia and not all(char in alfabeto for char in cadeia):
            invalidos = set(cadeia) - alfabeto
            print(f"ERRO: Cadeia contém caracteres inválidos: {invalidos}")
            print(f"Alfabeto aceito: Σ = {alfabeto}")
            print("REJEITA")
            return
        
        if opcao == 1:
            self.reconhecer_l_par_a(cadeia)
        else:
            self.reconhecer_a_estrela_b_estrela(cadeia)
    
    def reconhecer_l_par_a(self, cadeia):
        print(f"\nReconhecendo L_par_a para cadeia: '{cadeia}'")
        
        # Contar número de a's
        count_a = cadeia.count('a')
        par_a = count_a % 2 == 0
        
        print(f"Número de a's encontrados: {count_a}")
        print(f"Número par de a's: {par_a}")
        
        # SAÍDA conforme requisito
        resultado = "ACEITA" if par_a else "REJEITA"
        print(f"Resultado: {resultado}")
    
    def reconhecer_a_estrela_b_estrela(self, cadeia):
        print(f"\\nReconhecendo a*b* para cadeia: '{cadeia}'")
        
        # Verificar se está no formato a*b* usando regex
        padrao = re.match(r'^a*b*$', cadeia)
        aceita = padrao is not None
        
        # Análise detalhada
        if aceita:
            count_a = len(cadeia) - len(cadeia.lstrip('a'))
            count_b = len(cadeia) - count_a
            print(f"Formato válido: a^{count_a}b^{count_b}")
        else:
            print("Formato inválido: não segue o padrão a*b*")
        
        # SAÍDA conforme requisito
        resultado = "ACEITA" if aceita else "REJEITA"
        print(f"Resultado: {resultado}")