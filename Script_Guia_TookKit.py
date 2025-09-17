from abc import ABC, abstractmethod
from typing import Dict, Callable

class MenuOption(ABC):
    """Classe abstrata para opções do menu"""
    
    def __init__(self, titulo: str, descricao: str):
        self.titulo = titulo
        self.descricao = descricao
    
    @abstractmethod
    def executar(self):
        """Executa a funcionalidade da opção"""
        pass

class VerificarAlfabeto(MenuOption):
    """AV1 - Item 1: Verificar alfabeto e cadeia"""
    
    def __init__(self):
        super().__init__("Verificar Alfabeto", "Verificar alfabeto e cadeia (Sigma={a,b})")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        cadeia = input("Digite uma cadeia: ")
        
        alfabeto = {'a', 'b'}
        valida = all(char in alfabeto for char in cadeia)
        
        print(f"Cadeia '{cadeia}' é válida no alfabeto {{a,b}}: {valida}")
        if not valida:
            invalidos = set(cadeia) - alfabeto
            print(f"Caracteres inválidos: {invalidos}")

class ClassificadorJSON(MenuOption):
    """AV1 - Item 2: Classificador T/I/N por JSON"""
    
    def __init__(self):
        super().__init__("Classificador JSON", "Classificador T/I/N por JSON")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        print("Funcionalidade: Classificar strings como Terminadas(T), Infinitas(I) ou Nulas(N)")
        print("Implementação pendente - requer estrutura JSON específica")

class DecisorTerminaBComB(MenuOption):
    """AV1 - Item 3: Decisor termina com 'b'"""
    
    def __init__(self):
        super().__init__("Decisor Termina B", "Decisor: termina com 'b'?")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        cadeia = input("Digite uma cadeia: ")
        
        if not cadeia:
            resultado = False
            print("Cadeia vazia não termina com 'b'")
        else:
            resultado = cadeia[-1] == 'b'
            print(f"A cadeia '{cadeia}' termina com 'b': {resultado}")

class AvaliadorProposicional(MenuOption):
    """AV1 - Item 4: Avaliador proposicional (P,Q,R)"""
    
    def __init__(self):
        super().__init__("Avaliador Proposicional", "Avaliador proposicional (P,Q,R)")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        print("Digite valores para as proposições:")
        
        try:
            p = input("P (True/False): ").lower() == 'true'
            q = input("Q (True/False): ").lower() == 'true'
            r = input("R (True/False): ").lower() == 'true'
            
            print(f"\nResultados:")
            print(f"P = {p}, Q = {q}, R = {r}")
            print(f"P AND Q = {p and q}")
            print(f"P OR Q = {p or q}")
            print(f"P AND Q AND R = {p and q and r}")
            print(f"NOT P = {not p}")
            
        except Exception as e:
            print(f"Erro na avaliação: {e}")

class ReconhecedorParA(MenuOption):
    """AV1 - Item 5: Reconhecedor L_par_a e a b*"""
    
    def __init__(self):
        super().__init__("Reconhecedor Par A", "Reconhecedor: L_par_a e a b*")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        cadeia = input("Digite uma cadeia: ")
        
        # Conta número de 'a's
        count_a = cadeia.count('a')
        par_a = count_a % 2 == 0
        
        # Verifica se termina com b* (zero ou mais b's no final)
        import re
        padrao_b_final = re.match(r'^a*b*$', cadeia)
        
        print(f"Número de 'a's: {count_a} (par: {par_a})")
        print(f"Cadeia aceita por L_par_a: {par_a}")
        print(f"Cadeia aceita por a*b*: {padrao_b_final is not None}")

class ProblemaInstanciaJSON(MenuOption):
    """AV2 - Item 1: Problema x instância por JSON"""
    
    def __init__(self):
        super().__init__("Problema JSON", "Problema x instância por JSON")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        print("Funcionalidade: Processar definições de problemas via JSON")
        print("Implementação pendente - requer formato JSON específico")

class DecisoresLFimB(MenuOption):
    """AV2 - Item 2: Decisores L_fim_b e L_mult3_b"""
    
    def __init__(self):
        super().__init__("Decisores L_fim_b", "Decisores: L_fim_b e L_mult3_b")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        cadeia = input("Digite uma cadeia: ")
        
        # L_fim_b: termina com 'b'
        fim_b = cadeia.endswith('b') if cadeia else False
        
        # L_mult3_b: número de 'b's é múltiplo de 3
        count_b = cadeia.count('b')
        mult3_b = count_b % 3 == 0
        
        print(f"L_fim_b (termina com 'b'): {fim_b}")
        print(f"L_mult3_b (número de 'b's múltiplo de 3): {mult3_b} (count: {count_b})")

class ReconhecedorAiBi(MenuOption):
    """AV2 - Item 3: Reconhecedor a^i b^i"""
    
    def __init__(self):
        super().__init__("Reconhecedor a^i b^i", "Reconhecedor que pode não terminar (a^ib^i)")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        cadeia = input("Digite uma cadeia: ")
        
        # Verifica se está no formato a^n b^n
        import re
        if re.match(r'^a*b*$', cadeia):
            # Conta a's e b's
            primeira_parte = cadeia.lstrip('b')  # Remove b's do início (não deve haver)
            count_a = len(cadeia) - len(cadeia.lstrip('a'))
            count_b = len(cadeia) - len(cadeia.rstrip('b'))
            
            # Verifica se não há mistura
            if cadeia == 'a' * count_a + 'b' * count_b:
                aceita = count_a == count_b
                print(f"Formato válido: a^{count_a} b^{count_b}")
                print(f"Aceita pela linguagem a^i b^i: {aceita}")
            else:
                print("Formato inválido: a's e b's misturados")
        else:
            print("Formato inválido: contém caracteres não permitidos")

class DetectorLoop(MenuOption):
    """AV2 - Item 4: Detector ingênuo de loop"""
    
    def __init__(self):
        super().__init__("Detector Loop", "Detector ingênuo de loop")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        print("Simulando detecção de loop em sequência de estados...")
        
        estados_visitados = set()
        estado_atual = 0
        max_iteracoes = 10
        
        for i in range(max_iteracoes):
            print(f"Iteração {i}: Estado {estado_atual}")
            
            if estado_atual in estados_visitados:
                print(f"🔄 LOOP detectado! Estado {estado_atual} já foi visitado")
                break
                
            estados_visitados.add(estado_atual)
            estado_atual = (estado_atual + 1) % 3  # Simula transição cíclica

class SimuladorAFD(MenuOption):
    """AV2 - Item 5: Simulador AFD simples"""
    
    def __init__(self):
        super().__init__("Simulador AFD", "Simulador AFD simples (termina com 'b')")
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        cadeia = input("Digite uma cadeia: ")
        
        # AFD simples: aceita cadeias que terminam com 'b'
        # Estados: 0 (inicial), 1 (aceita)
        estado = 0
        
        print("Simulando AFD...")
        print(f"Estado inicial: {estado}")
        
        for i, char in enumerate(cadeia):
            if char == 'b':
                estado = 1
            elif char == 'a':
                estado = 0
            else:
                print(f"Caractere inválido '{char}' na posição {i}")
                return
                
            print(f"Lendo '{char}' → Estado {estado}")
        
        aceita = estado == 1
        print(f"\nEstado final: {estado}")
        print(f"Cadeia aceita: {aceita}")

class ToolkitMenu:
    """Classe principal do menu do toolkit"""
    
    def __init__(self):
        self.opcoes: Dict[int, MenuOption] = {
            1: VerificarAlfabeto(),
            2: ClassificadorJSON(),
            3: DecisorTerminaBComB(),
            4: AvaliadorProposicional(),
            5: ReconhecedorParA(),
            6: ProblemaInstanciaJSON(),
            7: DecisoresLFimB(),
            8: ReconhecedorAiBi(),
            9: DetectorLoop(),
            10: SimuladorAFD()
        }
    
    def exibir_menu(self):
        """Exibe o menu principal"""
        print("=" * 50)
        print("Projeto Toolkit (versão OOP)")
        print("=" * 50)
        print("---- AV1 ----")
        print("1) Verificar alfabeto e cadeia (Sigma={a,b})")
        print("2) Classificador T/I/N por JSON")
        print("3) Decisor: termina com 'b'?")
        print("4) Avaliador proposicional (P,Q,R)")
        print("5) Reconhecedor: L_par_a e a b*")
        print("---- AV2 ----")
        print("6) Problema x instância por JSON")
        print("7) Decisores: L_fim_b e L_mult3_b")
        print("8) Reconhecedor que pode não terminar (a^ib^i)")
        print("9) Detector ingênuo de loop")
        print("10) Simulador AFD simples (termina com 'b')")
        print("0) Sair")
        print("=" * 50)
    
    def ler_opcao(self) -> int:
        """Lê uma opção válida do menu"""
        while True:
            try:
                opcao = int(input("Escolha uma opção (0-10): "))
                if 0 <= opcao <= 10:
                    return opcao
                else:
                    print("❌ Opção inválida! Digite um número entre 0 e 10.")
            except ValueError:
                print("❌ Por favor, digite um número válido.")
    
    def executar_opcao(self, opcao: int):
        """Executa a opção escolhida"""
        if opcao in self.opcoes:
            print()
            self.opcoes[opcao].executar()
            print()
            input("Pressione Enter para continuar...")
    
    def executar(self):
        """Loop principal do programa"""
        while True:
            self.exibir_menu()
            opcao = self.ler_opcao()
            
            if opcao == 0:
                print("\n👋 Encerrando o programa...")
                break
            
            self.executar_opcao(opcao)
            print()

def main():
    """Função principal"""
    toolkit = ToolkitMenu()
    toolkit.executar()

if __name__ == "__main__":
    main()