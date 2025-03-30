import os
import shutil
from collections import defaultdict

def get_country_info(filename):
   
    country_mapping = {
        'de': 'Germania',
        'uk': 'Marea_Britanie',
        'es': 'Spania',
        'in': 'India',
        'mx': 'Mexic',
        'com': 'International',
        'us': 'Statele_Unite',
        'co.uk': 'Marea_Britanie',
        'com.mx': 'Mexic',
        'online': 'International'
    }
    
   
    name = filename.replace('.html', '')
    

    parts = name.split('.')
    
    if len(parts) >= 2:
        compound_tld = '.'.join(parts[-2:])
        if compound_tld in country_mapping:
            return country_mapping[compound_tld]
    

    if len(parts) > 1:
        tld = parts[-1]
        if tld in country_mapping:
            return country_mapping[tld]
    
    return 'Altele' 

def organize_by_country():
    """Organizează fișierele HTML în directoare bazate pe țară."""
  
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tier2_dir = os.path.join(script_dir, 'Tier2')
    

    if not os.path.exists(tier2_dir):
        os.makedirs(tier2_dir)
   
    country_groups = defaultdict(list)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(current_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(current_dir, filename)
            country = get_country_info(filename)
            country_groups[country].append((file_path, filename))
    
    
    output_dir = os.path.join(tier2_dir, 'tari')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    

    for country, files in country_groups.items():
        country_dir = os.path.join(output_dir, country)
        if not os.path.exists(country_dir):
            os.makedirs(country_dir)
        

        for file_path, filename in files:
            dest_path = os.path.join(country_dir, filename)
            try:
                shutil.copy2(file_path, dest_path)
                print(f"[{country}] Fișierul {filename} a fost copiat în {country_dir}")
            except Exception as e:
                print(f"Eroare la copierea fișierului {filename}: {str(e)}")
        
     
        with open(os.path.join(country_dir, '_info_tara.txt'), 'w', encoding='utf-8') as f:
            f.write(f"Țară: {country}\n")
            f.write(f"Număr de site-uri: {len(files)}\n")
            f.write("\nSite-uri în această țară:\n")
            for _, filename in files:
                f.write(f"- {filename}\n")

if __name__ == "__main__":
    organize_by_country()
