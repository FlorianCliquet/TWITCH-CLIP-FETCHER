------------------------------------------------------------------------------ # Twitch Clip Fetcher[FR]---------------------------------------------------------------------------------------

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Aperçu

Twitch Clip Fetcher est un projet Python conçu pour automatiser le processus de recherche, de téléchargement et de montage de clips Twitch en fonction de catégories définies par l'utilisateur. Ce projet utilise Selenium pour le scraping web, MoviePy pour le montage vidéo et Twitch-dl pour le téléchargement des clips. Avec Twitch Clip Fetcher, les utilisateurs peuvent facilement rassembler des clips de leurs catégories Twitch préférées, les compiler dans une seule vidéo et télécharger la vidéo modifiée sur YouTube.

## Fonctionnalités

- **Récupération des URLs de clips** : Récupération automatique des URLs de clips Twitch en fonction des catégories spécifiées.
- **Téléchargement des clips** : Téléchargement des clips Twitch directement sur votre machine locale.
- **Compilation vidéo** : Combinaison des clips téléchargés en un seul fichier vidéo.
- **Upload sur YouTube** : Téléchargement de la vidéo compilée sur YouTube en utilisant l'API YouTube Data.

## Structure du dossier

```
Twitch-Clip-Fetcher/
│
├── main.py
│
├── Scripts/
│   ├── upload.py
│   ├── RecupClipURL.py
│   ├── MontageClip.py
│   ├── DownloadClip.py
│   └── CreateurVideo.py
│
├── Autres/
│   ├── [Autres fichiers et dossiers]
│   └── ...
│
└── README.md
```

## Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/FlorianCliquet/Twitch-Clip-Fetcher.git
```

2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

1. Naviguez vers le répertoire `Twitch-Clip-Fetcher`.

2. Modifiez le fichier `main.py` pour spécifier vos catégories Twitch et vos clés d'API.

3. Exécutez le script principal :

```bash
python main.py
```

4. Suivez les instructions pour récupérer, télécharger, éditer et télécharger les clips Twitch.

## Configuration

### Clés d'API

- Remplacez `'YOUR_API_KEY'` dans `upload.py` par votre clé d'API YouTube Data.

### Pilote Web

- Définissez les variables `webdriver_path` et `chrome_binary` dans `RecupClipURL.py` sur les chemins appropriés pour votre pilote Chrome WebDriver et votre binaire Chrome.

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

- Merci à [Twitch](https://www.twitch.tv/) pour fournir une plateforme incroyable pour les créateurs de contenu.
- Un grand merci aux développeurs de Selenium, MoviePy et Twitch-dl pour leurs contributions inestimables.

------------------------------------------------------------------------------ # Twitch Clip Fetcher[EN]---------------------------------------------------------------------------------------

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

Twitch Clip Fetcher is a Python project designed to automate the process of fetching, downloading, and editing Twitch clips based on user-defined categories. This project utilizes Selenium for web scraping, MoviePy for video editing, and Twitch-dl for downloading clips. With Twitch Clip Fetcher, users can easily gather clips from their favorite Twitch categories, compile them into a single video, and upload the edited video to YouTube.

## Features

- **Clip URL Retrieval**: Automatically fetch Twitch clips URLs based on specified categories.
- **Clip Downloading**: Download Twitch clips directly to your local machine.
- **Video Compilation**: Combine downloaded clips into a single video file.
- **YouTube Upload**: Upload the compiled video to YouTube using the YouTube Data API.

## Folder Structure

```
Twitch-Clip-Fetcher/
│
├── main.py
│
├── Scripts/
│   ├── upload.py
│   ├── RecupClipURL.py
│   ├── MontageClip.py
│   ├── DownloadClip.py
│   └── CreateurVideo.py
│
├── Autres/
│   ├── [Other files and folders]
│   └── ...
│
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/FlorianCliquet/Twitch-Clip-Fetcher.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Navigate to the `Twitch-Clip-Fetcher` directory.

2. Modify the `main.py` file to specify your Twitch categories and API keys.

3. Run the main script:

```bash
python main.py
```

4. Follow the prompts to fetch, download, edit, and upload Twitch clips.

## Configuration

### API Keys

- Replace `'YOUR_API_KEY'` in `upload.py` with your YouTube Data API key.

### Webdriver

- Set the `webdriver_path` and `chrome_binary` variables in `RecupClipURL.py` to the appropriate paths for your Chrome WebDriver and Chrome binary.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Twitch](https://www.twitch.tv/) for providing an amazing platform for content creators.
- Special thanks to the developers of Selenium, MoviePy, and Twitch-dl for their invaluable contributions.
