import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, id_cliente): 
        clientes = config.model_clientes.select_cliente(id_cliente) 
        return config.render.update(clientes) 
    
    def POST(self, id_cliente, nombre_cliente, apellido_paterno, apellido_materno, telefono):
        formulario= web.input() 
        id_cliente=formulario['id_cliente'] 
        nombre_cliente= formulario['nombre_cliente'] 
        apellido_paterno= formulario['apellido_paterno'] 
        apellido_materno= formulario['apellido_materno'] 
        telefono= formulario['telefono'] 
        config.model_clientes.update_cliente(id_cliente, nombre_cliente, apellido_paterno, apellido_materno, telefono) 
        raise web.seeother('/') 
