import os
import subprocess
from datetime import datetime

def DownloadClip(jeux):
    date_du_jour = datetime.today().strftime("%Y-%m-%d")
    predefined_folder_path = os.path.abspath(f"CLIP/{jeux}")
    folder_name = os.path.join(predefined_folder_path, f"CLIP_{date_du_jour}")

    # Création du dossier CLIP/jeux/CLIP_{date}
    os.makedirs(folder_name, exist_ok=True)

    # Changer le répertoire de travail vers le dossier CLIP/jeux/CLIP_{date}
    os.chdir(folder_name)

    with open('urls_list.txt', 'r') as file:
        urls_list = file.readlines()

    clip_number = 1  # Initialisation du numéro du clip
    
    # Itérer sur les URLs pour télécharger chaque clip avec un numéro croissant
    for url in urls_list:
        url = url.strip()
        output_filename = f"clip_{clip_number}.mp4"  # Nom du fichier avec le numéro du clip
        command = f"twitch-dl download -q 1080 {url} -o {output_filename}"
        subprocess.run(command, shell=True)
        clip_number += 1  # Incrémentation du numéro du clip pour le prochain
        
    os.chdir('YOUR PATH')


