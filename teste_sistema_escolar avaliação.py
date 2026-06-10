import os

# Base de dados em memória
alunos = []

def calcular_media_notas(notas):
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def definir_situacao(media):
    if media >= 7.0:
        return "Aprovado"
    elif 5.0 <= media < 7.0:
        return "Recuperação"
    else:
        return "Reprovado"

def cadastrar_aluno():
    print("\n--- CADASTRO DE ALUNO ---")
    nome = input("Nome do aluno: ").strip()
    
    # Validação para idade (evita que o programa feche se digitarem letras)
    while True:
        try:
            idade = int(input("Idade do aluno: "))
            if idade <= 0:
                print("Por favor, digite uma idade válida maior que zero.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros para a idade.")
            
    turma = input("Turma do aluno: ").strip()
    
    aluno = {
        'nome': nome,
        'idade': idade,
        'turma': turma,
        'notas': []
    }
    alunos.append(aluno)
    print(f"\n Sucesso: Aluno(a) '{nome}' cadastrado com sucesso!")

def lancar_notas():
    print("\n--- LANÇAR NOTAS ---")
    if not alunos:
        print("Nenhum aluno cadastrado no sistema ainda.")
        return
    
    print("Alunos disponíveis:")
    for i, aluno in enumerate(alunos):
        print(f"[{i}] Nome: {aluno['nome']} | Turma: {aluno['turma']}")
    
    try:
        indice = int(input("\nSelecione o número (índice) do aluno: "))
        if 0 <= indice < len(alunos):
            print(f"\nLançando as 4 notas bimestrais para: {alunos[indice]['nome']}\n")
            notas = []
            
            for j in range(1, 5):
                while True:
                    try:
                        nota = float(input(f"Digite a nota {j} (0 a 10): "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("A nota deve ser um valor entre 0.0 e 10.0.")
                    except ValueError:
                        print("Formato inválido! Use números (ex: 7.5 ou 8).")
            
            alunos[indice]['notas'] = notas
            print(f"\n Notas de {alunos[indice]['nome']} atualizadas com sucesso!")
        else:
            print("Índice inválido! Esse aluno não existe na lista.")
    except ValueError:
        print("Entrada inválida. Você precisa digitar o número do índice.")

def consultar_aluno():
    print("\n--- CONSULTA INDIVIDUAL ---")
    if not alunos:
        print("Nenhum aluno cadastrado no sistema.")
        return
        
    nome_busca = input("Digite o nome exato do aluno para buscar: ").strip().lower()
    encontrado = False
    
    for aluno in alunos:
        if aluno['nome'].strip().lower() == nome_busca:
            encontrado = True
            print("\n==============================")
            print(f" FICHA DO ALUNO: {aluno['nome'].upper()}")
            print("==============================")
            print(f"Idade: {aluno['idade']} anos")
            print(f"Turma: {aluno['turma']}")
            
            if len(aluno['notas']) == 4:
                # Transforma a lista de floats em strings bonitas para exibição
                notas_formatadas = ", ".join([str(n) for n in aluno['notas']])
                print(f"Notas: [{notas_formatadas}]")
                media = calcular_media_notas(aluno['notas'])
                print(f"Média Final: {media:.2f}")
                print(f"Situação Acadêmica: {definir_situacao(media)}")
            else:
                print("Notas: Pendentes (necessário lançar as 4 notas no menu principal).")
            print("==============================")
            break
            
    if not encontrado:
        print(f"Não encontramos nenhum aluno com o nome '{nome_busca}'.")

def gerar_relatorio_geral():
    print("\n--- RELATÓRIO GERAL E ESTATÍSTICAS ---")
    total_alunos = len(alunos)
    if total_alunos == 0:
        print("Nenhum aluno cadastrado para gerar estatísticas.")
        return
        
    soma_medias_turma = 0
    alunos_com_nota = 0
    
    melhor_aluno = None
    maior_media = -1
    
    pior_aluno = None
    menor_media = 11.0
    
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    
    for aluno in alunos:
        if len(aluno['notas']) == 4:
            media = calcular_media_notas(aluno['notas'])
            soma_medias_turma += media
            alunos_com_nota += 1
            
            situacao = definir_situacao(media)
            if situacao == "Aprovado":
                aprovados += 1
            elif situacao == "Recuperação":
                recuperacao += 1
            else:
                reprovados += 1
                
            if media > maior_media:
                maior_media = media
                melhor_aluno = aluno['nome']
                
            if media < menor_media:
                menor_media = media
                pior_aluno = aluno['nome']
    
    media_geral_turma = soma_medias_turma / alunos_com_nota if alunos_com_nota > 0 else 0.0
    
    print(f"Total de alunos cadastrados: {total_alunos}")
    print(f"Média geral da escola/turma: {media_geral_turma:.2f}")
    
    if alunos_com_nota > 0:
        print(f"Destaque Positivo: {melhor_aluno} (Média: {maior_media:.2f})")
        print(f"Destaque Negativo: {pior_aluno} (Média: {menor_media:.2f})")
        print("-" * 30)
        print(f" Alunos Aprovados: {aprovados}")
        print(f" Alunos em Recuperação: {recuperacao}")
        print(f" Alunos Reprovados: {reprovados}")
    else:
        print("\nAviso: Não há alunos com as 4 notas completas para gerar o relatório de desempenho.")

def salvar_dados():
    print("\n--- SALVANDO DADOS ---")
    try:
        with open("sistema_escolar.txt", "w", encoding="utf-8") as arquivo:
            for aluno in alunos:
                if aluno['notas']:
                    notas_str = ",".join(map(str, aluno['notas']))
                else:
                    notas_str = "Sem notas"
                linha = f"{aluno['nome']};{aluno['idade']};{aluno['turma']};{notas_str}\n"
                arquivo.write(linha)
        print("Dados salvos com sucesso no arquivo 'sistema_escolar.txt'!")
    except IOError as e:
        print(f"Erro crítico ao tentar salvar o arquivo: {e}")

def carregar_dados():
    """Função humanificada para restaurar o sistema de onde parou"""
    if os.path.exists("sistema_escolar.txt"):
        try:
            with open("sistema_escolar.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    if not linha:
                        continue
                    partes = linha.split(";")
                    if len(partes) == 4:
                        nome, idade, turma, notas_str = partes
                        
                        if notas_str == "Sem notas" or not notas_str:
                            notas = []
                        else:
                            notas = [float(n) for n in notas_str.split(",")]
                            
                        alunos.append({
                            'nome': nome,
                            'idade': int(idade),
                            'turma': turma,
                            'notas': notas
                        })
            print(" Banco de dados local carregado com sucesso!")
        except Exception as e:
            print(f"Aviso: Não foi possível ler o arquivo salvo anteriormente ({e}). Iniciando sistema vazio.")

# Menu Principal do Sistema
def menu():
    # Carrega os dados automaticamente ao abrir o programa
    carregar_dados()
    
    while True:
        print("\n==============================")
        print("  SISTEMA DE GERENCIAMENTO ESCOLAR  ")
        print("==============================")
        print("1. Cadastrar Aluno")
        print("2. Lançar Notas")
        print("3. Consultar Aluno")
        print("4. Relatório Geral")
        print("5. Salvar Dados")
        print("6. Sair")
        print("==============================")
        
        opcao = input("Escolha uma opção (1-6): ").strip()
        
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            lancar_notas()
        elif opcao == "3":
            consultar_aluno()
        elif opcao == "4":
            gerar_relatorio_geral()
        elif opcao == "5":
            salvar_dados()
        elif opcao == "6":
            # Pergunta amigável antes de fechar sem salvar
            confirmar = input("\nDeseja salvar as alterações antes de sair? (S/N): ").strip().lower()
            if confirmar == 's':
                salvar_dados()
            print("\nEncerrando o sistema de notas. Até mais!")
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 6.")

# Executa o programa
if __name__ == "__main__":
    menu()