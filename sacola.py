#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer


class Entidade:

    @property
    def id(self):
        return id(self)


class Usuario(Entidade):
    nome = None
    senha = None

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha


class Item(Entidade):
    nome = None
    descricao = None
    valor = None
    estoque = None

    def __init__(self, nome, descricao, valor, estoque):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.estoque = estoque


class Sacola(Entidade):
    usuario = None
    itens = []

    def __init__(self, usuario, itens):
        self.usuario = usuario
        self.itens = itens.copy()


usuario = Usuario(nome='meunome', senha='meuaniversario')
itens = [
    Item(nome='', descricao='', valor=0.00, estoque=0),
    Item(nome='', descricao='', valor=0.00, estoque=0),
    Item(nome='', descricao='', valor=0.00, estoque=0),
]

sacola = Sacola(usuario=usuario, itens=itens)

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title>Sacola</title></head><body>")
        for item in sacola.itens:
            self.wfile.write(bytes(f"ID:{item.id} - NOME:{item.nome} - DESCR:{item.descricao}<br>", 'utf-8'))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
