from OpcoesMenu import OpcoesMenu

class VerificarAlfabeto(OpcoesMenu):
    def __init__(self):
        super().__init__("Verificador de alfabeto e cadeia", "Verificador de alfabeto e cadeia em Σ={a,b}")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        
        # Alfabeto fixo conforme requisito
        alfabeto = {'a', 'b'}
        print(f"Alfabeto definido: Σ = {alfabeto}")
        
        # REQUISITO: Verificar símbolo individual primeiro
        print("\n1) Verificação de símbolo individual:")
        simbolo = input("Digite um símbolo: ")
        
        if len(simbolo) != 1:
            print("INVÁLIDO: Digite apenas um caractere")
            return
        
        simbolo_valido = simbolo in alfabeto
        print(f"Símbolo '{simbolo}' ∈ Σ: {'VÁLIDO' if simbolo_valido else 'INVÁLIDO'}")
        
        # REQUISITO: Verificar cadeia completa
        print("\n2) Verificação de cadeia:")
        cadeia = input("Digite uma cadeia: ")
        
        if not cadeia:
            print("Cadeia vazia (ε) ∈ Σ*: VÁLIDA")
            return
        
        cadeia_valida = all(char in alfabeto for char in cadeia)
        print(f"Cadeia '{cadeia}' ∈ Σ*: {'VÁLIDA' if cadeia_valida else 'INVÁLIDA'}")
        
        if not cadeia_valida:
            invalidos = set(cadeia) - alfabeto
            print(f"Caracteres inválidos encontrados: {invalidos}")