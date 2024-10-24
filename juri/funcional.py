import os
import subprocess

competition_folder = r"C:\Users\Pinto & Tabita\Desktop\competição\competidor"
test_input = r"C:\Users\Pinto & Tabita\Desktop\competição\juri\test_cases\test_input.txt"
expected_output = r"C:\Users\Pinto & Tabita\Desktop\competição\juri\test_cases\expected_output.txt"

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
        
        print("Entrada lida:", input_data.strip())
        print("Saída do programa:", result.stdout.strip())
        print("Saída de erro do programa:", result.stderr.strip())  # Captura de erro
        if result.stdout.strip() == expected_data:
            return "Aceito"
        else:
            return "Saída Incorreta"
    except subprocess.TimeoutExpired:
        return "Tempo Excedido"
    except Exception as e:
        return f"Erro: {str(e)}"

for folder in os.listdir(competition_folder):
    folder_path = os.path.join(competition_folder, folder)
    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".py"):
                result = evaluate_submission(os.path.join(folder_path, file))
                print(f"Competidor {folder}: {result}")
                
                
