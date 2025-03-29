import os
import re
import shutil
from collections import defaultdict

def get_base_name(filename):
    # Elimină extensia .html
    name = filename.replace('.html', '')
    
    # Extrage numele de bază eliminând extensia domeniului
    # Ex: site.com.html -> site
    parts = name.split('.')
    if len(parts) > 1:
        return parts[0]
    return name

def create_directory(base_path, dirname):
    # Creează un director dacă nu există
    dir_path = os.path.join(base_path, dirname)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

def organize_files():
    # Directorul curent
    current_dir = os.getcwd()
    
    # Dicționar pentru gruparea fișierelor
    file_groups = defaultdict(list)
    
    # Parcurge recursiv toate directoarele pentru a găsi fișiere HTML
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith('.html'):
                base_name = get_base_name(file)
                # Adaugă calea completă și numele de bază
                file_groups[base_name].append(os.path.join(root, file))
    
    # Creează directorul principal pentru fișierele organizate
    organized_dir = create_directory(current_dir, 'organized_files')
    
    # Mută fișierele în directoarele corespunzătoare
    for base_name, file_paths in file_groups.items():
        if len(file_paths) > 0:  # Creează director doar dacă există fișiere
            # Creează un subdirector pentru acest grup de fișiere
            group_dir = create_directory(organized_dir, base_name)
            
            # Mută fiecare fișier în noul director
            for file_path in file_paths:
                # Obține numele original al fișierului
                original_filename = os.path.basename(file_path)
                # Calea destinație pentru fișier
                dest_path = os.path.join(group_dir, original_filename)
                
                try:
                    # Copiază fișierul în noul director
                    shutil.copy2(file_path, dest_path)
                    print(f"Fișierul {original_filename} a fost copiat în {group_dir}")
                except Exception as e:
                    print(f"Eroare la copierea fișierului {original_filename}: {str(e)}")

if __name__ == "__main__":
    organize_files() 
