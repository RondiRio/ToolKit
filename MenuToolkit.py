from VerificarAlfabeto import VerificarAlfabeto
from classificador import classificador
from DecisorTerminal import DecisorTerminal
from AvaliadorProporcional import AvaliadorProporcional
from ReconheceParA import ReconheceParA
from InstanciaJson import InstanciaJSON
from DecisorFimB import DecisorFimB
from ReconhecedorAiBi import ReconhecedorAiBi

class MenuToolkit:
    def __init__(self):
        # Instanciando as classes (CORRIGIDO)
        self.opcoes = {
            1: VerificarAlfabeto(),
            2: classificador(),
            3: DecisorTerminal(),
            4: AvaliadorProporcional(),
            5: ReconheceParA(),
            6: InstanciaJSON(),
            7: DecisorFimB(),
            8: ReconhecedorAiBi(),
        }

    def exibir_menu(self):
        print("=" * 60)
        print("PROJETO TOOLKIT")
        print("=" * 60)
        print("-" * 60)
        
        for num, opcao in self.opcoes.items():
            # Emoji para status
            if num <= 5:  # Itens obrigatórios AV1
                status = "V" if num != 6 else "F"
                print(f"{status} {num}) {opcao.titulo}")
                print(f"    {opcao.descricao}")
        
        print("-" * 60)
        print("Parte da AV2 - Não desenvolvido")
        print("-" * 60)
        
        for num in [6, 7, 8]:
            if num in self.opcoes:
                print(f" {num}) {self.opcoes[num].titulo}")
                print(f"    {self.opcoes[num].descricao}")
        
        print("-" * 60)
        print("0) 🚪 Sair")
        print("=" * 60)

    def ler_opcao(self):
        while True:
            try:
                opcao = int(input("Escolha uma opção (0-8): "))
                if 0 <= opcao <= 8:
                    return opcao
                else:
                    print("Opção inválida! Digite um número entre 0 e 8.")
            except ValueError:
                print("Por favor, digite um número válido.")

    def executar_opcao(self, opcao: int):
        if opcao in self.opcoes:
            print()
            try:
                self.opcoes[opcao].executar()
            except Exception as e:
                print(f"Erro ao executar: {e}")
            print()
            input("Pressione Enter para continuar...")

    def executar(self): 
        """Loop principal do programa"""
        while True:
            self.exibir_menu()
            opcao = self.ler_opcao()
            
            if opcao == 0:
                print("\\ THE END...")
                break
            
            self.executar_opcao(opcao)

def main():
    """Função principal"""
    toolkit = MenuToolkit()
    toolkit.executar()  # CORRIGIDO

if __name__ == "__main__":
    main()