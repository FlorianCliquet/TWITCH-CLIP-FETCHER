import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def RecupClipURL(jeux):
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Chemin du dossier CLIP/jeux/CLIP_{date}
    dossier_clips_date = os.path.abspath(f"CLIP/{jeux}/CLIP_{current_date}")

    # Création du dossier CLIP/jeux/CLIP_{date}
    if not os.path.exists(dossier_clips_date):
        os.makedirs(dossier_clips_date)
        print(f"Dossier créé : {dossier_clips_date}")

    webdriver_path = '/home/florian/Documents/Logiciel/chrome driver/chromedriver_linux64/chromedriver'
    chrome_binary = '/usr/bin/google-chrome'

    service = Service(webdriver_path)
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_binary
    driver = webdriver.Chrome(service=service, options=options)

    url = f"https://www.twitch.tv/directory/category/{jeux}/clips?lang=fr&range=24hr"
    driver.get(url)

    wait = WebDriverWait(driver, 10)  
    clip_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a[data-a-target='preview-card-image-link']")))

    urls_list = []
    streamer_names = []  # Liste pour stocker les noms des streamers

    for link in clip_links:
        clip_url = link.get_attribute("href")
        if clip_url:
            urls_list.append(clip_url)
            # Extraction du nom du streamer à partir de l'URL du clip
            streamer_name = clip_url.split('/')[3]  # Récupère le nom du streamer à partir de l'URL
            streamer_names.append(streamer_name)
        else:
            print("L'élément n'a pas d'attribut href")

    if urls_list:
        print("Liste d'URLs des clips :")
        for url in urls_list:
            print(url)

        with open(os.path.join(dossier_clips_date, 'urls_list.txt'), 'w') as file:
            for url in urls_list:
                file.write(url + '\n')
        print("Les URLs des clips ont été enregistrées dans 'urls_list.txt'.")

        # Enregistrement des noms des streamers dans un fichier texte
        with open(os.path.join(dossier_clips_date, 'streamer_names.txt'), 'w') as stream_file:
            for name in streamer_names:
                stream_file.write(f"{name}\n")
        print("Les noms des streamers ont été enregistrés dans 'streamer_names.txt'.")
    else:
        print("Aucune URL de clip trouvée.")

    driver.quit()


