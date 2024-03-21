import os
from datetime import date
from moviepy.editor import VideoFileClip, concatenate_videoclips
from Scripts.DownloadClip import DownloadClip

def extract_number(filename):
    # Extraction des chiffres du nom de fichier
    return int(''.join(filter(str.isdigit, filename)))

def MontageClip(jeux):
    date_du_jour = date.today().strftime("%Y-%m-%d")

    # Chemin du dossier CLIP/jeux/CLIP_{date}
    dossier_videos = os.path.abspath(f"CLIP/{jeux}/CLIP_{date_du_jour}")

    # Chemin du dossier VIDEO_FINALE/jeux/date
    chemin_dossier_final = os.path.abspath(f"VIDEO_FINALE/{jeux}/{date_du_jour}")

    # Création du dossier CLIP/jeux/CLIP_{date}
    if not os.path.exists(dossier_videos):
        os.makedirs(dossier_videos)
        print(f"Dossier créé : {dossier_videos}")

    liste_videos = []

    # Liste des vidéos téléchargées
    for video in os.listdir(dossier_videos):
        if video.endswith(".mp4"):  
            video_path = os.path.join(dossier_videos, video)
            clip = VideoFileClip(video_path)
            liste_videos.append(clip)

    # Trier les clips par les chiffres dans leur nom
    liste_videos.sort(key=lambda x: extract_number(x.filename))

    final_clip = concatenate_videoclips(liste_videos)

    # Création du dossier VIDEO_FINALE/jeux/date
    if not os.path.exists(chemin_dossier_final):
        os.makedirs(chemin_dossier_final)
        print(f"Dossier créé : {chemin_dossier_final}")
    
    # Chemin complet pour la vidéo finale
    titre_video = f"video_finale_.mp4"
    chemin_complet_video = os.path.join(chemin_dossier_final, titre_video)

    # Écriture de la vidéo finale
    final_clip.write_videofile(chemin_complet_video, codec='libx264', fps=24)


