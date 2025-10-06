import os
from datetime import datetime

# Caminho da pasta onde os arquivos de presença devem estar localizados;
BASE_PATH = os.path.dirname(os.path.abspath(__file__)) # Determinando como base dos PATHs a seguir o diretório do script "generate_presence_list.py";
FILES_PATH = os.path.join(BASE_PATH, "..", "presences") # Caminho para a pasta "../presences";
OUTPUT_FILE = os.path.join(BASE_PATH, "..", "materials", "presence_list.tex") # Caminho para o arquivo de saída "../materials/presence_list.tex";

# Coletando todos os arquivos .txt no caminho fornecido;
files = [file for file in os.listdir(FILES_PATH) if file.endswith('.txt')]

# Gerando o conteúdo do arquivo LaTeX "presence_list.tex";
content = []
content.append("\\begin{tabularx}{\\textwidth}{|>{\\centering\\arraybackslash}X|>{\\centering\\arraybackslash}X|}")
content.append("\\hline")
content.append("\\textbf{Nome} & \\textbf{Presente em} \\\\")
content.append("\\hline")

for name in sorted(files):
    path = os.path.join(FILES_PATH, name)
    person_name = os.path.splitext(name)[0]

    # Obtendo a data de criação do arquivo;
    timestamp = os.path.getctime(path)
    create_date = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y ás %H:%M:%S')
    content.append(f"   {person_name} & {create_date} \\\\")
    content.append("\\hline")
content.append("\\end{tabularx}")

# Garantindo que a pasta materials exista;
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

# Escrevendo o conteúdo no arquivo de saída;
with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
    file.write('\n'.join(content))
