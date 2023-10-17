# projet_FogComputing
Ce projet met en œuvre une architecture maître , esclave pour distribuer une tâche d'analyse d'image entre un serveur et trois clients, permettant de diviser, traiter et fusionner une image en utilisant un algorithme de détection de contours.

language utilisé : python 
biblothéques : threading  , socket , Pillow ,os , opencv

Description :
Initialisation de la communication :

Le serveur "Mariem" établit la communication avec les clients "Eya", "Oumayma" et "Manar".
Division de l'image :

Le serveur "Mariem" divise l'image en trois parties distinctes.
Chaque partie est envoyée aux clients respectifs : "Eya", "Oumayma" et "Manar".
Traitement de la partie de l'image par chaque client :

Chaque client (Eya, Oumayma, Manar) reçoit sa partie spécifique de l'image.
Chaque client applique un traitement de détection de contours à sa partie de l'image.
Envoi des parties traitées au serveur :

Chaque client envoie sa partie d'image traitée au serveur "Mariem".
Fusion des parties d'image :

Le serveur "Mariem" reçoit les parties traitées de l'image de chaque client.
Le serveur combine les parties traitées pour former l'image complète.
Traitement ultérieur de l'image complète :

Après avoir reçu et assemblé les parties traitées, le serveur peut appliquer d'autres traitements à l'image complète, si nécessaire.
Renvoi du résultat final :

Le serveur "Mariem" peut ensuite renvoyer l'image traitée et assemblée aux clients ou à d'autres parties prenantes, en fonction des exigences du système.


Les captures : serveur Mariem (https://github.com/mariemmarrekchi/projet_FogComputing/blob/master/capture1.png)
