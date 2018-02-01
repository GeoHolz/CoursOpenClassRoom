# -*-coding:Utf-8 -*

import socket
import select
import pickle

class Server:
    """Class serveur"""
    MSG_LEN = 1024

    connectedClients = []

    def __init__(self, map):
        self.host = 'localhost'
        self.port = 20123
        self.map = map

    def start(self):
        self.mainConnection = socket.socket()
        self.mainConnection.bind((self.host, self.port))
        self.mainConnection.listen(5)
        print("Le serveur ecoute sur {0}:{1}...".format(self.host, self.port))
        
    def waitForClient(self):
        """ Attends que les clients se connectent 
        et retourne le nombre de client connectes
        """
        while True:
            # Attends que les clients se connectent(50ms)
            incomingConnections, wlist, xlist = select.select([self.mainConnection], [], [], 0.05)
            for iConnection in incomingConnections:
                conn, info = iConnection.accept()
                self.connectedClients.append(conn)
                print("Client {0} connecte".format(info))
                self.sendString(conn, "Bienvenue numero {0}".format(len(self.connectedClients)))
                self.sendStringAll("{0} clients connectes".format(len(self.connectedClients)))

            # Si le nombre de client est >= 2 alors on propose de commencer la partie grace a la touche C
            if (len(self.connectedClients) >=2):
                toReadClient = []
                try:
                    toReadClient, wlist, xlist = select.select(self.connectedClients, [], [], 0.05)
                except select.error:
                    pass
                else:
                    #Lecture des commandes envoyés par les clients
                    for client in toReadClient:
                        msg = client.recv(self.MSG_LEN).decode().rstrip()
                        if msg == "c":
                            print(">>>> START <<<<<")
                            self.sendStringAll("START")
                            return

    def sendObject(self, conn, obj):
        conn.send(pickle.dumps(obj))

    def sendObjectAll(self, obj):
        for conn in self.connectedClients:
            conn.send(pickle.dumps(obj))

    def sendString(self, conn, msg):
        """Envoie un message à un client"""
        conn.send(msg.ljust(self.MSG_LEN).encode())

    def sendStringAll(self, msg):
        for conn in self.connectedClients:
            conn.send(msg.ljust(self.MSG_LEN).encode())

    def __repr__(self, **kwargs):
        return "<Server listening on {0}>".format(self.port)
    def close(self):
        self.mainConnection.close()