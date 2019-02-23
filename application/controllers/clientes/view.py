import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, id_cliente):  
        clientes = config.model_clientes.select_nombre(id_cliente) 
        return config.render.view(clientes) 
