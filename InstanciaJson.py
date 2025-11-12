from OpcoesMenu import OpcoesMenu
import json

class InstanciaJSON(OpcoesMenu):
    def __init__(self):
        super().__init__("Problema x Instância por JSON", "Carrega e analisa problemas e instâncias via JSON")
        
        # Base de dados de problemas com suas instâncias
        self.problemas_db = {
            "problemas": [
                {
                    "id": 1,
                    "nome": "Ordenação",
                    "descricao": "Ordenar uma lista de elementos",
                    "entrada": "Lista de números",
                    "saida": "Lista ordenada",
                    "instancias": [
                        {
                            "id": 1,
                            "entrada": [5, 2, 8, 1, 9],
                            "saida_esperada": [1, 2, 5, 8, 9],
                            "tamanho": 5
                        },
                        {
                            "id": 2,
                            "entrada": [3, 3, 1],
                            "saida_esperada": [1, 3, 3],
                            "tamanho": 3
                        },
                        {
                            "id": 3,
                            "entrada": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                            "saida_esperada": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                            "tamanho": 10
                        }
                    ]
                },
                {
                    "id": 2,
                    "nome": "Busca em Lista",
                    "descricao": "Encontrar um elemento em uma lista",
                    "entrada": "Lista e elemento alvo",
                    "saida": "Índice do elemento ou -1 se não encontrado",
                    "instancias": [
                        {
                            "id": 1,
                            "lista": [10, 20, 30, 40, 50],
                            "alvo": 30,
                            "saida_esperada": 2
                        },
                        {
                            "id": 2,
                            "lista": [1, 2, 3, 4, 5],
                            "alvo": 10,
                            "saida_esperada": -1
                        },
                        {
                            "id": 3,
                            "lista": [100],
                            "alvo": 100,
                            "saida_esperada": 0
                        }
                    ]
                },
                {
                    "id": 3,
                    "nome": "Verificador de Palíndromo",
                    "descricao": "Verificar se uma string é palíndromo",
                    "entrada": "String",
                    "saida": "True ou False",
                    "instancias": [
                        {
                            "id": 1,
                            "entrada": "arara",
                            "saida_esperada": True
                        },
                        {
                            "id": 2,
                            "entrada": "python",
                            "saida_esperada": False
                        },
                        {
                            "id": 3,
                            "entrada": "aba",
                            "saida_esperada": True
                        }
                    ]
                },
                {
                    "id": 4,
                    "nome": "Soma de Lista",
                    "descricao": "Calcular a soma de todos os elementos de uma lista",
                    "entrada": "Lista de números",
                    "saida": "Soma total",
                    "instancias": [
                        {
                            "id": 1,
                            "entrada": [1, 2, 3, 4, 5],
                            "saida_esperada": 15
                        },
                        {
                            "id": 2,
                            "entrada": [10, -5, 3],
                            "saida_esperada": 8
                        },
                        {
                            "id": 3,
                            "entrada": [],
                            "saida_esperada": 0
                        }
                    ]
                }
            ]
        }
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        print("Este módulo demonstra a diferença entre PROBLEMA e INSTÂNCIA")
        print("Um PROBLEMA é uma questão geral, uma INSTÂNCIA é um caso específico")
        print("=" * 70)
        
        # Menu de problemas
        print("\nProblemas disponíveis:")
        for problema in self.problemas_db["problemas"]:
            print(f"{problema['id']}) {problema['nome']}")
            print(f"   Descrição: {problema['descricao']}")
            print(f"   Entrada: {problema['entrada']}")
            print(f"   Saída: {problema['saida']}")
            print()
        
        # Escolha do problema
        while True:
            try:
                escolha = int(input("Escolha um problema (1-4): "))
                if 1 <= escolha <= 4:
                    break
                print("Opção inválida!")
            except ValueError:
                print("Digite um número válido!")
        
        problema_escolhido = self.problemas_db["problemas"][escolha - 1]
        
        print("\n" + "=" * 70)
        print(f"PROBLEMA SELECIONADO: {problema_escolhido['nome']}")
        print("=" * 70)
        print(f"Descrição: {problema_escolhido['descricao']}")
        print(f"\nInstâncias disponíveis: {len(problema_escolhido['instancias'])}")
        print("-" * 70)
        
        # Exibir instâncias
        for instancia in problema_escolhido['instancias']:
            print(f"\nInstância #{instancia['id']}:")
            
            # Exibir de acordo com o tipo de problema
            if escolha == 1:  # Ordenação
                print(f"  Entrada: {instancia['entrada']}")
                print(f"  Tamanho: {instancia['tamanho']} elementos")
                print(f"  Saída esperada: {instancia['saida_esperada']}")
            elif escolha == 2:  # Busca
                print(f"  Lista: {instancia['lista']}")
                print(f"  Elemento alvo: {instancia['alvo']}")
                print(f"  Saída esperada: {instancia['saida_esperada']}")
            elif escolha == 3:  # Palíndromo
                print(f"  Entrada: '{instancia['entrada']}'")
                print(f"  Saída esperada: {instancia['saida_esperada']}")
            elif escolha == 4:  # Soma
                print(f"  Entrada: {instancia['entrada']}")
                print(f"  Saída esperada: {instancia['saida_esperada']}")
        
        # Opção para resolver uma instância
        print("\n" + "=" * 70)
        resolver = input("Deseja resolver uma instância? (s/n): ").lower()
        
        if resolver == 's':
            self.resolver_instancia(problema_escolhido, escolha)
    
    def resolver_instancia(self, problema, tipo_problema):
        print("\n" + "=" * 70)
        print("RESOLVER INSTÂNCIA")
        print("=" * 70)
        
        while True:
            try:
                num_instancia = int(input(f"Escolha uma instância (1-{len(problema['instancias'])}): "))
                if 1 <= num_instancia <= len(problema['instancias']):
                    break
                print("Instância inválida!")
            except ValueError:
                print("Digite um número válido!")
        
        instancia = problema['instancias'][num_instancia - 1]
        
        print(f"\nResolvendo Instância #{instancia['id']}...")
        print("-" * 70)
        
        # Resolver de acordo com o tipo
        if tipo_problema == 1:  # Ordenação
            entrada = instancia['entrada']
            resultado = sorted(entrada)
            print(f"Entrada: {entrada}")
            print(f"Resultado: {resultado}")
            print(f"Esperado: {instancia['saida_esperada']}")
            correto = resultado == instancia['saida_esperada']
            
        elif tipo_problema == 2:  # Busca
            lista = instancia['lista']
            alvo = instancia['alvo']
            try:
                resultado = lista.index(alvo)
            except ValueError:
                resultado = -1
            print(f"Lista: {lista}")
            print(f"Buscando: {alvo}")
            print(f"Resultado: {resultado}")
            print(f"Esperado: {instancia['saida_esperada']}")
            correto = resultado == instancia['saida_esperada']
            
        elif tipo_problema == 3:  # Palíndromo
            entrada = instancia['entrada']
            resultado = entrada == entrada[::-1]
            print(f"Entrada: '{entrada}'")
            print(f"É palíndromo? {resultado}")
            print(f"Esperado: {instancia['saida_esperada']}")
            correto = resultado == instancia['saida_esperada']
            
        elif tipo_problema == 4:  # Soma
            entrada = instancia['entrada']
            resultado = sum(entrada)
            print(f"Entrada: {entrada}")
            print(f"Soma: {resultado}")
            print(f"Esperado: {instancia['saida_esperada']}")
            correto = resultado == instancia['saida_esperada']
        
        print("-" * 70)
        if correto:
            print("✓ CORRETO! A solução está correta.")
        else:
            print("✗ INCORRETO! A solução não corresponde ao esperado.")
        
        print("\n💡 Nota: Este é um exemplo de como um PROBLEMA geral")
        print("   pode ter múltiplas INSTÂNCIAS específicas.")