import subprocess
import time
import os

# Fonction pour démarrer un processus dans un nouveau terminal
def start_process_in_new_terminal(command):
    # Utilise 'start' pour ouvrir une nouvelle fenêtre de terminal
    subprocess.Popen(f'start cmd /k {command}', shell=True)

# Démarrer Zookeeper dans un nouveau terminal
start_process_in_new_terminal("C:\\kafka\\bin\\windows\\zookeeper-server-start.bat C:\\kafka\\config\\zookeeper.properties")

# Attendre que Zookeeper démarre complètement avant de lancer Kafka
time.sleep(10)

# Démarrer Kafka dans un autre terminal
start_process_in_new_terminal("C:\\kafka\\bin\\windows\\kafka-server-start.bat C:\\kafka\\config\\server.properties")

# Afficher un message indiquant que les processus sont en cours
print("Zookeeper et Kafka sont en cours d'exécution dans des terminaux séparés.")
