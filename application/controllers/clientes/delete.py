import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, id_cliente): 
        clientes = config.model_clientes.select_cliente(id_cliente) 
        return config.render.delete(clientes) 
    
    def POST(self, id_cliente):
        formulario = web.input() 
        id_cliente = formulario['id_cliente'] 
        config.model_clientes.delete_cliente(id_cliente) 
        raise web.seeother('/') 
