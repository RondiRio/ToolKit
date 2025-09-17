from OpcoesMenu import OpcoesMenu
import json
class classificador(OpcoesMenu):
    def __init__(self):
        super().__init__("Classificador JSON T/I/N", "Classificador de problemas T/I/N por JSON")
        
        # Lista embutida de problemas em formato JSON
        self.problemas_json = {
            "problemas": [
                {
                    "id": 1,
                    "nome": "Ordenação por bubble sort",
                    "descricao": "Ordenar lista de n elementos usando bubble sort",
                    "classificacao_correta": "T"
                },
                {
                    "id": 2,
                    "nome": "Problema da parada",
                    "descricao": "Determinar se um programa qualquer para com uma entrada",
                    "classificacao_correta": "N"
                },
                {
                    "id": 3,
                    "nome": "Caixeiro viajante",
                    "descricao": "Encontrar menor rota visitando todas as cidades",
                    "classificacao_correta": "I"
                },
                {
                    "id": 4,
                    "nome": "Busca linear",
                    "descricao": "Encontrar elemento em lista não ordenada",
                    "classificacao_correta": "T"
                },
                {
                    "id": 5,
                    "nome": "Problema da equivalência de CFGs",
                    "descricao": "Determinar se duas gramáticas livres de contexto são equivalentes",
                    "classificacao_correta": "N"
                },
                {
                    "id": 6,
                    "nome": "Coloração de grafos (k cores)",
                    "descricao": "Colorir grafo com k cores sem vértices adjacentes da mesma cor",
                    "classificacao_correta": "I"
                }
            ]
        }
    
    def executar(self):
        print(f"=== {self.descricao} ===")
        print("Legenda:")
        print("T = Tratável (Complexidade polinomial)")
        print("I = Intratável (Complexidade exponencial)")
        print("N = Não computável (Indecidível)")
        print("-" * 50)
        
        acertos = 0
        total = len(self.problemas_json["problemas"])
        
        for problema in self.problemas_json["problemas"]:
            print(f"\nProblema {problema['id']}: {problema['nome']}")
            print(f"Descrição: {problema['descricao']}")
            
            while True:
                resposta = input("Classificação (T/I/N): ").upper()
                if resposta in ['T', 'I', 'N']:
                    break
                print("Digite apenas T, I ou N")
            
            correto = resposta == problema['classificacao_correta']
            if correto:
                print("CORRETO!")
                acertos += 1
            else:
                print(f"INCORRETO! Resposta correta: {problema['classificacao_correta']}")
        
        # Resumo final
        print("\n" + "="*50)
        print("RESUMO FINAL")
        print("="*50)
        print(f"Total de questões: {total}")
        print(f"Acertos: {acertos}")
        print(f"Erros: {total - acertos}")
        print(f"Percentual de acerto: {(acertos/total)*100:.1f}%")
        
        if acertos == total:
            print("PARABÉNS! Você acertou todas!")
        elif acertos >= total * 0.7:
            print("Bom desempenho!")
        else:
            print("Continue estudando complexidade computacional!")