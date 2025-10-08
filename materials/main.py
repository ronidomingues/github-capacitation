from datetime import datetime

def main():
    mensagem = [
        "🚀 Ação Python executada com sucesso!",
        f"🕒 Horário da execução: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
        "✅ Arquivo gerado automaticamente pela Action!",
    ]

    # Nome do arquivo de saída
    arquivo_saida = "resultado.txt"

    # Grava as mensagens no arquivo
    with open(arquivo_saida, "w", encoding="utf-8") as f:
        f.write("\n".join(mensagem))

    print("📄 Arquivo 'resultado.txt' criado com sucesso!")

if __name__ == "__main__":
    main()