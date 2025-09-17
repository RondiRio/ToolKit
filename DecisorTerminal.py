from OpcoesMenu import OpcoesMenu

class DecisorTerminal(OpcoesMenu):
    def __init__(self):  # CORRIGIDO: era __ini__
        super().__init__("Decisor Terminal", "Decisor: termina com 'b'?")
        
    def executar(self):
        print(f"=== {self.descricao} ===")
        
        # Validação do alfabeto primeiro
        alfabeto = {'a', 'b'}
        print(f"Alfabeto aceito: Σ = {alfabeto}")
        
        cadeia = input('Digite uma cadeia: ')
        
        # PRÉ-CONDIÇÃO: Verificar se cadeia está sobre Σ
        if cadeia and not all(char in alfabeto for char in cadeia):
            invalidos = set(cadeia) - alfabeto
            print(f"ERRO: Cadeia contém caracteres inválidos: {invalidos}")
            print("Pré-condição não atendida: cadeia deve estar sobre Σ={a,b}")
            return
        
        # CASO VAZIO tratado
        if not cadeia:
            resultado = False
            print("Cadeia vazia (ε) não termina com 'b'")
            print("NAO")  # Formato conforme requisito
            return
        
        # DECISÃO: termina com 'b'?
        resultado = cadeia[-1] == 'b'
        
        print(f"A cadeia '{cadeia}' termina com 'b': {resultado}")
        print("SIM" if resultado else "NAO")  # SAÍDA conforme requisito