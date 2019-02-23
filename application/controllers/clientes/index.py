import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        clientes = config.model_clientes.select_clientes().list() 
        return config.render.index(clientes) 
