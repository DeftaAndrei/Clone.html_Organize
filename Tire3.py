import os
import shutil
from collections import defaultdict

def get_category_info(filename):
    category_keywords = {
        'Magazine_si_Ecommerce': ['store', 'shop', 'cameliastore'],
        'Sanatate_si_Frumusete': ['bellederma', 'hycare', 'etawalin', 'herbal', 'milk', 'proapremium'],
        'Consultanta_si_Business': ['consultants', 'majesty', 'adeptohomes', 'renewconsultants'],
        'Tehnologie': ['tech', 'okcis', 'coade', 'fieldtech'],
        'Transport_si_Taxi': ['taxi', 'viptaxi', 'automotive', 'renaut'],
        'Restaurante_si_Vinarii': ['winebar', 'deli', 'dianessidewalk', 'frankies', 'lagusto'],
        'Imobiliare_si_Credite': ['mortgages', 'homes', 'adeptohomes', 'estate'],
        'Turism_si_Calatorii': ['eastbourne', 'london', 'broadwell'],
        'Organizatii': ['council', 'neighborhoods', 'masjid'],
        'Servicii_Online': ['online', 'site', 'info', 'icu']
    }
    
    filename_lower = filename.lower()
    
    for category, keywords in category_keywords.items():
        if any(keyword.lower() in filename_lower for keyword in keywords):
            return category
            
    return 'Altele'

def organize_by_category():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    x3_dir = os.path.join(script_dir, 'X3')
 
    if not os.path.exists(x3_dir):
        os.makedirs(x3_dir)
    
    category_groups = defaultdict(list)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(current_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(current_dir, filename)
            category = get_category_info(filename)
            category_groups[category].append((file_path, filename))
    
    output_dir = os.path.join(x3_dir, 'categorii')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for category, files in category_groups.items():
        category_dir = os.path.join(output_dir, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
        
        for file_path, filename in files:
            dest_path = os.path.join(category_dir, filename)
            try:
                shutil.copy2(file_path, dest_path)
                print(f"[{category}] Fișierul {filename} a fost copiat în {category_dir}")
            except Exception as e:
                print(f"Eroare la copierea fișierului {filename}: {str(e)}")
        
        with open(os.path.join(category_dir, '_info_categorie.txt'), 'w', encoding='utf-8') as f:
            f.write(f"Categorie: {category}\n")
            f.write(f"Număr de site-uri: {len(files)}\n")
            f.write("\nSite-uri în această categorie:\n")
            for _, filename in files:
                f.write(f"- {filename}\n")

if __name__ == "__main__":
    organize_by_category()
