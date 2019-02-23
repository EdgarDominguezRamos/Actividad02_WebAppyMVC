import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() 
    
    def POST(self):
        formulario= web.input() 
        nombre_cliente= formulario['nombre_cliente'] 
        apellido_paterno= formulario['apellido_paterno'] 
        apellido_materno= formulario['apellido_materno'] 
        telefono= formulario['telefono'] 
        config.model_clientes.insert_cliente(nombre_cliente, apellido_paterno, apellido_materno, telefono) 
        raise web.seeother('/') 
