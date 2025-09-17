from OpcoesMenu import OpcoesMenu

class AvaliadorProporcional(OpcoesMenu):
    def __ini__(self):
        super().__ini__("Avaliador proporcional (P,Q,R)")
        print('Digite valores para as proposições')
        
        try:
            p = input("P (TRUE/FALSE): ").lower() == 'true'
            q = input("P (TRUE/FALSE): ").lower() == 'true'
            r = input("P (TRUE/FALSE): ").lower() == 'true'
            
            print(f"\nResultados:")
            print(f'P = {p}, Q = {q}, R = {r}')
            print(f"P and Q = {p and q}")
            print(f"P or Q = {p  or q}")
            print(f"P and Q and R = {p and q and r}")
            print(f"Not P = {not p}")
            
        except Exception as e:
            print(f"Erro na avaliação:{e}")
    