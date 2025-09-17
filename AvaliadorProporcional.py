from OpcoesMenu import OpcoesMenu

class AvaliadorProporcional(OpcoesMenu):
    def __init__(self):  # CORRIGIDO: era __ini__
        super().__init__("Avaliador Proposicional", "Avaliador proposicional básico (P,Q,R)")
        
        # Fórmulas predeterminadas
        self.formulas = {
            1: {
                "nome": "Conjunção e Disjunção",
                "formulas": ["P ∧ Q", "P ∨ Q", "P ∧ Q ∧ R"],
                "func": self.avaliar_conjuncao_disjuncao
            },
            2: {
                "nome": "Implicações",
                "formulas": ["P → Q", "(P ∧ Q) → R", "P → (Q ∨ R)"],
                "func": self.avaliar_implicacoes
            },
            3: {
                "nome": "Negações e Mistas",
                "formulas": ["¬P", "¬P ∨ Q", "¬(P ∧ Q)"],
                "func": self.avaliar_negacoes
            }
        }
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        
        # Menu com diferentes fórmulas
        print("\nEscolha o tipo de fórmulas para avaliar:")
        for key, value in self.formulas.items():
            print(f"{key}) {value['nome']}")
            for formula in value['formulas']:
                print(f"   • {formula}")
        
        while True:
            try:
                opcao = int(input("\nEscolha uma opção (1-3): "))
                if opcao in self.formulas:
                    break
                print("Opção inválida!")
            except ValueError:
                print("Digite um número válido!")
        
        # Entrada dos valores
        print(f"\nAvaliando: {self.formulas[opcao]['nome']}")
        print('Digite valores para as proposições:')
        
        try:
            p = input("P (True/False): ").lower() == 'true'  # CORRIGIDO: era "P" para todos
            q = input("Q (True/False): ").lower() == 'true'
            r = input("R (True/False): ").lower() == 'true'
            
            print(f"\nValores: P = {p}, Q = {q}, R = {r}")
            print("-" * 40)
            
            # Avaliar fórmulas da opção escolhida
            self.formulas[opcao]['func'](p, q, r)
            
            # Opção para tabela-verdade completa
            tabela = input("\nDeseja ver a tabela-verdade completa? (s/n): ").lower()
            if tabela == 's':
                self.gerar_tabela_verdade(opcao)
            
        except Exception as e:
            print(f"Erro na avaliação: {e}")
    
    def avaliar_conjuncao_disjuncao(self, p, q, r):
        print("Resultados:")
        print(f"P ∧ Q = {p and q}")
        print(f"P ∨ Q = {p or q}")
        print(f"P ∧ Q ∧ R = {p and q and r}")
    
    def avaliar_implicacoes(self, p, q, r):
        print("Resultados:")
        print(f"P → Q = {(not p) or q}")
        print(f"(P ∧ Q) → R = {not (p and q) or r}")
        print(f"P → (Q ∨ R) = {(not p) or (q or r)}")
    
    def avaliar_negacoes(self, p, q, r):
        print("Resultados:")
        print(f"¬P = {not p}")
        print(f"¬P ∨ Q = {(not p) or q}")
        print(f"¬(P ∧ Q) = {not (p and q)}")
    
    def gerar_tabela_verdade(self, opcao):
        print(f"\n{'='*60}")
        print("TABELA-VERDADE COMPLETA")
        print('='*60)
        
        valores = [True, False]
        print("P     Q     R     ", end="")
        
        for formula in self.formulas[opcao]['formulas']:
            print(f"{formula:^12}", end="")
        print()
        print("-" * 60)
        
        for p in valores:
            for q in valores:
                for r in valores:
                    print(f"{str(p):^5} {str(q):^5} {str(r):^5} ", end="")
                    
                    if opcao == 1:
                        resultados = [p and q, p or q, p and q and r]
                    elif opcao == 2:
                        resultados = [(not p) or q, not (p and q) or r, (not p) or (q or r)]
                    else:  # opcao == 3
                        resultados = [not p, (not p) or q, not (p and q)]
                    
                    for resultado in resultados:
                        print(f"{str(resultado):^12}", end="")
                    print()