import ollama
import csv
import sys
import re


def consultar_ollama(prompt):
    """
    Envia um prompt para o Ollama e retorna a resposta
    """
    try:
        # Envia o prompt para o Ollama
        resposta = ollama.chat(model="gemma3:4b", messages=[
            {
                "role": "user",
                "content": prompt
            }
        ])

        # A resposta já vem como um dicionário Python
        return resposta
    except Exception as e:
        print(f"Erro ao consultar Ollama: {e}")
        sys.exit(1)


def extrair_linhas_e_gerar_csv(texto, arquivo_saida="verbos_exemplos.csv"):
    """
    Extrai verbos e exemplos e gera um único CSV
    """
    try:
        # Divide o texto em linhas
        linhas = [linha for linha in texto.split(
            '\n') if linha.strip()]  # Remove linhas vazias

        # Lista para armazenar pares [verbo, exemplo]
        pares_verbos = []

        # Encontra linhas que começam com números (ex: "1. **Be**...")
        for linha in linhas:
            # Verifica se a linha começa com um número seguido de ponto
            if re.match(r'^\d+\.', linha):
                # Extrai o nome do verbo (entre ** se estiver presente)
                verbo_match = re.search(r'\*\*(.*?)\*\*', linha)
                if verbo_match:
                    verbo = verbo_match.group(1).strip()
                else:
                    # Se não encontrar marcação **, tenta extrair o verbo após o número
                    verbo_match = re.search(r'^\d+\.\s+(.*?)\s+[\(–-]', linha)
                    verbo = verbo_match.group(1).strip(
                    ) if verbo_match else "Verbo não encontrado"

                # Extrai os exemplos (tudo após o primeiro traço ou parêntese)
                exemplo_match = re.search(r'[\(–-](.*?)$', linha)
                exemplo = exemplo_match.group(
                    1).strip() if exemplo_match else ""

                # Remove marcações ** do exemplo
                exemplo = re.sub(r'\*\*', '', exemplo)

                # Adiciona o par à lista
                pares_verbos.append([verbo, exemplo])

        # Abre o arquivo CSV para escrita
        with open(arquivo_saida, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            # Escreve os dados no CSV
            for verbo, exemplo in pares_verbos:
                escritor.writerow([verbo, exemplo])

        print(f"Arquivo CSV '{arquivo_saida}' gerado com sucesso!")

        # Exibe os pares de verbos e exemplos encontrados
        print("\nVerbos e exemplos extraídos:")
        for verbo, exemplo in pares_verbos:
            print(f"Verbo: {verbo}")
            print(f"Exemplo: {exemplo}")
            print("-" * 50)

    except Exception as e:
        print(f"Erro ao gerar CSV: {e}")
        sys.exit(1)


def main():
    # Solicita o prompt ao usuário
    prompt = input("Digite seu comando para a IA Ollama: ")

    # Chama a função para consultar o Ollama
    resposta = consultar_ollama(prompt)

    # Exibe a resposta completa (opcional, para debug)
    print("\nResposta completa do Ollama:",
          resposta.get('message').get('content'))

    # Extrai os dados e gera o CSV
    extrair_linhas_e_gerar_csv(resposta.get('message').get('content'))


if __name__ == "__main__":
    main()
