from googleapiclient.discovery import build
from datetime import datetime
def upload(category):
    # Remplacez 'YOUR_API_KEY' par votre clé d'API YouTube
    api_key = 'YOUR API KEY'
    date = datetime.today().strftime("%Y-%m-%d")


    # Créer une instance de l'API YouTube
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Définir les métadonnées de la vidéo
    request = youtube.videos().insert(
        part='snippet',
        body={
            'snippet': {
                'title': 'Titre de votre vidéo',
                'description': 'Description de votre vidéo',
                # Autres métadonnées comme les tags, la catégorie, etc.
            }
        },
        media_body='path_to/'+str(category)+'/'+str(date)+'/video_finale_.mp4'
    )

    # Exécuter la requête pour uploader la vidéo
    response = request.execute()
    print(response)
