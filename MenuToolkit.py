from VerificarAlfabeto import VerificarAlfabeto
from classificador import classificador
from DecisorTerminal import DecisorTerminal
from AvaliadorProporcional import AvaliadorProporcional
from ReconheceParA import ReconheceParA
from InstanciaJson import InstanciaJSON
from DecisorFimB import DecisorFimB
from ReconhecedorAiBi import ReconhecedorAiBi
from OpcoesMenu import OpcoesMenu

class MenuToolkit:
    def __init__(self):
        
        self.opcoes: dict[int, OpcoesMenu] ={
            1: VerificarAlfabeto,
            2: classificador,
            3: DecisorTerminal,#termina b com b
            4: AvaliadorProporcional,
            5: ReconheceParA, #identifica se tem A A
            6: InstanciaJSON,
            7: DecisorFimB,
            8: ReconhecedorAiBi,
            # 9: DetectaLoop(),
            # 10: SimuladorAF()
        }

    def exibi_menu(self):
        pass

def main():
    """Função principal"""
    toolkit = MenuToolkit()
    toolkit.executar

if __name__ == "__main__":
    main()