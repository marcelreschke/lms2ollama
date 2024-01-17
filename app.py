import os
from pathlib import Path

def create_modelfiles(base_path):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.gguf'):
                model_name = Path(file).stem
                modelfile_path = Path(root) / f"{model_name}.Modelfile"
                with modelfile_path.open('w') as modelfile:
                    modelfile.write(f"FROM ./{file}")
                    print(f"Created {modelfile_path}")

if __name__ == "__main__":
    models_folder = Path.home() / ".cache/lm-studio/models"
    if models_folder.exists():
        create_modelfiles(models_folder)
    else:
        print(f"The directory {models_folder} does not exist.")
