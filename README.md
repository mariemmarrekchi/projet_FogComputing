# Projet Fog Computing

Ce projet met en œuvre une architecture maître-serveur pour distribuer une tâche d'analyse d'image entre un serveur et trois clients, permettant de diviser, traiter et fusionner une image en utilisant un algorithme de détection de contours.

## Langage Utilisé
- Python

## Bibliothèques
- Threading
- Socket
- Pillow
- OpenCV
- OS

## Description

### Initialisation de la Communication

Le serveur "Mariem" établit la communication avec les clients "Eya", "Oumayma" et "Manar.

### Division de l'Image

Le serveur "Mariem" divise l'image en trois parties distinctes.
Chaque partie est envoyée aux clients respectifs : "Eya", "Oumayma" et "Manar.

### Traitement de la Partie de l'Image par Chaque Client

Chaque client (Eya, Oumayma, Manar) reçoit sa partie spécifique de l'image.
Chaque client applique un traitement de détection de contours à sa partie de l'image.

### Envoi des Parties Traitées au Serveur

Chaque client envoie sa partie d'image traitée au serveur "Mariem".

### Fusion des Parties de l'Image

Le serveur "Mariem" reçoit les parties traitées de l'image de chaque client.
Le serveur combine les parties traitées pour former l'image complète.

### Traitement Ultérieur de l'Image Complète

Après avoir reçu et assemblé les parties traitées, le serveur peut appliquer d'autres traitements à l'image complète, si nécessaire.

### Renvoi du Résultat Final

Le serveur "Mariem" peut ensuite renvoyer l'image traitée et assemblée aux clients ou à d'autres parties prenantes, en fonction des exigences du système.

## Captures d'Écran

### Serveur Mariem
![01](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/capture1.png)
![02](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/capture2.png)
![03](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/capture3.png)
![04](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/capture4.png)

### Client Eya
Client :
![05](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/image1.png)

Traitement :
![06](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/image2.png)

Serveur :
![07](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/image3.png)

### Client Oumayma
Client :
![08](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/oumayma3.png)

Traitement :
![09](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/oumayma.png)

Serveur :
![10](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/oumayma2.png)

### Client Manar
Client :
![11](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/imagemanara1.png)

Traitement :
![13](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/imagemanar3.png)

Serveur :
![12](https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/imagemanar2.png)
