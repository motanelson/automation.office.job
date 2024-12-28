import os
import time
import shutil

# Configuração das pastas
WORK_DIR = os.path.join(os.getcwd(), "work")
DONE_DIR = os.path.join(os.getcwd(), "dones")

# Criar os diretórios se não existirem
os.makedirs(WORK_DIR, exist_ok=True)
os.makedirs(DONE_DIR, exist_ok=True)

def process_file(file_name):
    """
    Função para processar um ficheiro. Atualmente, apenas imprime o nome do ficheiro.
    """
    print(f"Processing file: {file_name}")

def main():
    print("Starting file processor...")
    processed_files = set()  # Para rastrear os arquivos já processados

    while True:
        try:
            # Listar arquivos na pasta `work`
            files = [f for f in os.listdir(WORK_DIR) if os.path.isfile(os.path.join(WORK_DIR, f))]

            # Filtrar novos arquivos
            new_files = [f for f in files if f not in processed_files]

            for file_name in new_files:
                # Caminho completo do arquivo
                src_path = os.path.join(WORK_DIR, file_name)
                dest_path = os.path.join(DONE_DIR, file_name)

                # Processar o arquivo
                process_file(file_name)

                # Mover o arquivo para a pasta `dones`
                shutil.move(src_path, dest_path)

                # Marcar como processado
                processed_files.add(file_name)

            # Esperar 35 segundos antes de verificar novamente
            time.sleep(35)

        except KeyboardInterrupt:
            print("\nStopping file processor...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

