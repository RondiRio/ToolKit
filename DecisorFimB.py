# from OpcoesMenu import OpcoesMenu

# class DecisorFimB(OpcoesMenu):
#     def __init__(self):
#         super().__init__('Decisores cadeia com fim b e/ou cadeia com fim multiplos de 3 sendo b')
        
#     def executar(self):
#         print(f'=== {self.descricao} ===')
#         cadeia = input('digite uma cadeia: ')
        
#         termina_com_b = cadeia.endswith('b') if cadeia else False
        
#         conta_b = cadeia.count('b')
#         conta_mult3_b = conta_mult3_b % 3 == 0
        
#         print(f'L_fim_b (terminado com b): {termina_com_b}' )
#         print(f"L_mult3_b (quantudade de b's multiplos de 3): {conta_mult3_b} (conta: {conta_b})")

from OpcoesMenu import OpcoesMenu

class DecisorFimB(OpcoesMenu):
    def __init__(self):
        super().__init__('Decisores L_fim_b e L_mult3_b', 'Decisores: cadeia termina com b E/OU quantidade de b\'s é múltiplo de 3')
        
    def executar(self):
        print(f'=== {self.descricao} ===')
        print('Este decisor verifica duas condições:')
        print('  L_fim_b: A cadeia termina com "b"')
        print('  L_mult3_b: A quantidade de "b"s é múltiplo de 3')
        print('-' * 60)
        
        # Validação do alfabeto
        alfabeto = {'a', 'b'}
        print(f'Alfabeto aceito: Σ = {alfabeto}')
        
        cadeia = input('\nDigite uma cadeia: ')
        
        # Verificar se cadeia está sobre o alfabeto
        if cadeia and not all(char in alfabeto for char in cadeia):
            invalidos = set(cadeia) - alfabeto
            print(f'ERRO: Cadeia contém caracteres inválidos: {invalidos}')
            print(f'A cadeia deve conter apenas caracteres de Σ = {alfabeto}')
            return
        
        # L_fim_b: Termina com 'b'
        termina_com_b = cadeia.endswith('b') if cadeia else False
        
        # L_mult3_b: Quantidade de 'b's é múltiplo de 3
        conta_b = cadeia.count('b')
        mult3_b = conta_b % 3 == 0
        
        # Exibição dos resultados
        print('\n' + '=' * 60)
        print('RESULTADOS:')
        print('=' * 60)
        print(f'Cadeia analisada: "{cadeia}"')
        print(f'Quantidade de "b"s: {conta_b}')
        print('-' * 60)
        print(f'L_fim_b (termina com "b"): {"SIM" if termina_com_b else "NÃO"}')
        print(f'L_mult3_b (quantidade de "b"s é múltiplo de 3): {"SIM" if mult3_b else "NÃO"}')
        print('=' * 60)
        
        # Análise combinada
        print('\nAnálise combinada (L_fim_b OU L_mult3_b):')
        aceita_alguma = termina_com_b or mult3_b
        print(f'Aceita por pelo menos uma linguagem: {"SIM" if aceita_alguma else "NÃO"}')
        
        if termina_com_b and mult3_b:
            print('✓ A cadeia é aceita por AMBAS as linguagens!')
        elif termina_com_b:
            print('✓ A cadeia é aceita apenas por L_fim_b')
        elif mult3_b:
            print('✓ A cadeia é aceita apenas por L_mult3_b')
        else:
            print('✗ A cadeia NÃO é aceita por nenhuma das linguagens')