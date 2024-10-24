import os
import subprocess

# Diretórios e arquivos de teste
competition_folder = r"C:/Users/Pinto & Tabita/Desktop/competição/competidor"
test_input = r"C:/Users/Pinto & Tabita/Desktop/competição/juri/test_cases/test_input.txt"
expected_output = r"C:/Users/Pinto & Tabita/Desktop/competição/juri/test_cases/expected_output.txt"

# Função para avaliar a submissão
def evaluate_submission(file_path):
    try:
        with open(test_input, 'r') as f:
            input_data = f.read()
        
        result = subprocess.run(
            [r'C:\Users\Pinto & Tabita\AppData\Local\Programs\Python\Python313\python.exe', file_path], 
            input=input_data, 
            capture_output=True, 
            text=True, 
            timeout=5
        )
        
        with open(expected_output, 'r') as f:
            expected_data = f.read().strip()
        
        if result.stdout.strip() == expected_data:
            return "Aceito"
        else:
            return "Saída Incorreta"
    except subprocess.TimeoutExpired:
        return "Tempo Excedido"
    except Exception as e:
        return f"Erro: {str(e)}"

# Armazenando resultados dos competidores
results = []

# Itera pelas pastas dos competidores
for folder in os.listdir(competition_folder):
    folder_path = os.path.join(competition_folder, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".py"):
                result = evaluate_submission(os.path.join(folder_path, file))
                results.append((folder, result))

# Gerando o arquivo HTML com a tabela de resultados
html_content = """
<html>
<head>
    <title>Resultados da Competição</title>
    <style>
        table {
            width: 50%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h2>Resultados da Competição</h2>
    <table>
        <tr>
            <th>Competidor</th>
            <th>Resultado</th>
        </tr>
"""

# Preenchendo a tabela com os resultados
for competitor, result in results:
    html_content += f"""
        <tr>
            <td>{competitor}</td>
            <td>{result}</td>
        </tr>
    """

# Finalizando o HTML
html_content += """
    </table>
</body>
</html>
"""

# Salvando o conteúdo em um arquivo HTML
with open(r"C:/Users/Pinto & Tabita/Desktop/competição/juri/resultados.html", 'w') as f:
    f.write(html_content)

print("Arquivo HTML com os resultados gerado com sucesso.")
