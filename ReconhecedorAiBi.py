from OpcoesMenu import OpcoesMenu
import time

class ReconhecedorAiBi(OpcoesMenu):
    def __init__(self):
        super().__init__("Reconhecedor a^i b^i", "Reconhecedor que pode não terminar (linguagem a^i b^i)")
        
    def executar(self):
        print(f"=== {self.descricao} ===")
        print("Este reconhecedor verifica a linguagem L = {a^i b^i | i ≥ 0}")
        print("Exemplos válidos: ε (vazio), ab, aabb, aaabbb, aaaabbbb, ...")
        print("Exemplos inválidos: a, b, aab, abb, ba, abab, ...")
        print("=" * 70)
        
        # Validação do alfabeto
        alfabeto = {'a', 'b'}
        print(f"Alfabeto aceito: Σ = {alfabeto}")
        
        # Opção de limite de tempo
        print("\n⚠️  AVISO: Este reconhecedor pode não terminar para cadeias grandes!")
        print("Recomendamos usar cadeias de até 1000 caracteres.")
        
        usar_timeout = input("\nDeseja usar timeout de segurança? (s/n): ").lower()
        
        if usar_timeout == 's':
            try:
                timeout = int(input("Digite o timeout em segundos (recomendado: 5): "))
            except ValueError:
                timeout = 5
                print(f"Valor inválido. Usando timeout padrão: {timeout}s")
        else:
            timeout = None
            print("⚠️  Executando SEM timeout - pressione Ctrl+C para cancelar se travar")
        
        cadeia = input("\nDigite uma cadeia: ")
        
        # Verificar se cadeia está sobre o alfabeto
        if cadeia and not all(char in alfabeto for char in cadeia):
            invalidos = set(cadeia) - alfabeto
            print(f"\nERRO: Cadeia contém caracteres inválidos: {invalidos}")
            print(f"A cadeia deve conter apenas caracteres de Σ = {alfabeto}")
            return
        
        print("\n" + "=" * 70)
        print("PROCESSANDO...")
        print("=" * 70)
        
        try:
            if timeout:
                # Execução com timeout simulado (para demonstração)
                print(f"⏱️  Timeout configurado: {timeout} segundos")
                inicio = time.time()
                resultado = self.reconhecer_aibi(cadeia)
                tempo_decorrido = time.time() - inicio
                
                if tempo_decorrido > timeout:
                    print(f"\n⏰ TIMEOUT! Execução excedeu {timeout} segundos")
                    print("O reconhecedor pode não ter terminado.")
                    return
            else:
                resultado = self.reconhecer_aibi(cadeia)
            
            # Exibir resultado
            self.exibir_resultado(cadeia, resultado)
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Execução interrompida pelo usuário!")
            print("Este é um exemplo de programa que pode não terminar.")
        except Exception as e:
            print(f"\nErro durante execução: {e}")
    
    def reconhecer_aibi(self, cadeia):
        """
        Reconhece a linguagem L = {a^i b^i | i ≥ 0}
        
        Esta é uma linguagem livre de contexto (não regular)
        Algoritmo:
        1. Cadeia vazia é aceita (i=0)
        2. Conta número de a's consecutivos no início
        3. Conta número de b's consecutivos após os a's
        4. Verifica se não sobrou nada e se #a's == #b's
        """
        
        # Caso vazio (ε)
        if not cadeia:
            return {
                "aceita": True,
                "i": 0,
                "motivo": "Cadeia vazia (ε) pertence à linguagem (i=0)"
            }
        
        # Contar a's no início
        count_a = 0
        pos = 0
        
        while pos < len(cadeia) and cadeia[pos] == 'a':
            count_a += 1
            pos += 1
        
        # Contar b's após os a's
        count_b = 0
        while pos < len(cadeia) and cadeia[pos] == 'b':
            count_b += 1
            pos += 1
        
        # Verificar se consumiu toda a cadeia
        consumiu_tudo = pos == len(cadeia)
        
        # Verificar se número de a's == número de b's
        igual_quantidade = count_a == count_b
        
        # Verificar se tem pelo menos um 'a' e um 'b' (i > 0)
        tem_ambos = count_a > 0 and count_b > 0
        
        # Aceita se: consumiu tudo, quantidades iguais, e não está vazia
        aceita = consumiu_tudo and igual_quantidade and tem_ambos
        
        # Preparar análise detalhada
        analise = {
            "aceita": aceita,
            "i": count_a if aceita else None,
            "count_a": count_a,
            "count_b": count_b,
            "consumiu_tudo": consumiu_tudo,
            "igual_quantidade": igual_quantidade,
            "formato": f"a^{count_a} b^{count_b}"
        }
        
        # Determinar motivo
        if aceita:
            analise["motivo"] = f"Cadeia no formato a^{count_a}b^{count_b} (i={count_a})"
        elif not consumiu_tudo:
            sobrou = cadeia[pos:]
            analise["motivo"] = f"Formato inválido: sobrou '{sobrou}' após processar"
        elif not igual_quantidade:
            analise["motivo"] = f"Quantidade diferente: {count_a} a's e {count_b} b's"
        elif count_a == 0 or count_b == 0:
            analise["motivo"] = "Falta 'a's ou 'b's na cadeia"
        else:
            analise["motivo"] = "Formato inválido"
        
        return analise
    
    def exibir_resultado(self, cadeia, resultado):
        print("\n" + "=" * 70)
        print("RESULTADO DA ANÁLISE")
        print("=" * 70)
        print(f"Cadeia analisada: '{cadeia}'")
        print(f"Tamanho: {len(cadeia)} caracteres")
        print("-" * 70)
        
        if "formato" in resultado:
            print(f"Formato detectado: {resultado['formato']}")
        
        if "count_a" in resultado:
            print(f"Quantidade de 'a's: {resultado['count_a']}")
        if "count_b" in resultado:
            print(f"Quantidade de 'b's: {resultado['count_b']}")
        
        print("-" * 70)
        print(f"Consumiu toda a cadeia: {'SIM' if resultado.get('consumiu_tudo', False) else 'NÃO'}")
        print(f"Quantidades iguais: {'SIM' if resultado.get('igual_quantidade', False) else 'NÃO'}")
        print("-" * 70)
        
        if resultado['aceita']:
            print("✓ ACEITA")
            print(f"  A cadeia pertence à linguagem L = {{a^i b^i | i ≥ 0}}")
            if resultado['i'] is not None:
                print(f"  Valor de i: {resultado['i']}")
        else:
            print("✗ REJEITA")
            print(f"  A cadeia NÃO pertence à linguagem")
        
        print(f"\nMotivo: {resultado['motivo']}")
        print("=" * 70)
        
        # Nota educacional
        print("\n💡 NOTA IMPORTANTE:")
        print("   A linguagem L = {a^i b^i | i ≥ 0} é uma linguagem LIVRE DE CONTEXTO,")
        print("   mas NÃO é REGULAR. Ela não pode ser reconhecida por um autômato finito.")
        print("   É necessário uma máquina de Turing ou autômato com pilha.")
        print("   ")
        print("   Para cadeias muito grandes, o reconhecimento pode demorar ou não terminar,")
        print("   ilustrando o problema da DECIDIBILIDADE em computação.")