import os
from pathlib import Path
import sys

def create_modelfiles(base_path):
    overwrite_all = False
    skip_all = False
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.gguf'):
                model_name = Path(file).stem
                modelfile_path = Path(root) / f"{model_name}.Modelfile"
                if modelfile_path.exists() and not overwrite_all and not skip_all:
                    print(f"{modelfile_path} already exists.")
                    choice = input("Overwrite (o), Skip (s), Overwrite all (oa), Skip all (sa): ").lower()
                    if choice == 'o':
                        pass
                    elif choice == 's':
                        continue
                    elif choice == 'oa':
                        overwrite_all = True
                    elif choice == 'sa':
                        skip_all = True
                        continue
                    else:
                        print("Invalid input. Exiting.")
                        sys.exit(1)
                if not skip_all:
                    with modelfile_path.open('w') as modelfile:
                        modelfile.write(f"FROM ./{file}")
                        print(f"Created {modelfile_path}")

if __name__ == "__main__":
    models_folder = Path.home() / ".cache/lm-studio/models"
    if models_folder.exists():
        create_modelfiles(models_folder)
    else:
        print(f"The directory {models_folder} does not exist.")
