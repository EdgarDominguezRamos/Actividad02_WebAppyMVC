import config as config 

db = config.db 

'''
Metodo para seleccionar todos los registros de la tabla clientes
'''
def select_clientes():
    try:
        return db.select('clientes') 
    except Exception as e:
        print "Model select_clientes Error {}".format(e.args)
        print "Model select_clientes Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el id
'''
def select_cliente(id_cliente):
    try:
        return db.select('clientes',where='id_cliente=$id_cliente', vars=locals())[0] 
    except Exception as e:
        print "Model select_cliente Error {}".format(e.args)
        print "Model select_cliente Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando nombre_cliente, apellido_paterno, apellido_materno, telefono
'''
def insert_cliente(nombre_cliente, apellido_paterno, apellido_materno, telefono):
    try:
        return db.insert('clientes', nombre_cliente=nombre_cliente, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, telefono=telefono) 
    except Exception as e:
        print "Model insert_clientes Error {}".format(e.args)
        print "Model insert_clientes Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el id
'''
def delete_cliente(id_cliente):
    try:
        return db.delete('clientes', where='id_cliente=$id_cliente',vars=locals()) 
    except Exception as e:
        print "Model delete_clientes Error {}".format(e.args)
        print "Model delete_clientes Message {}".format(e.message)
        return None

'''
Metodo para actualizar el email, del nombre_cliente, apellido_paterno, apellido_materno, telefono
'''
def update_cliente(id_cliente, nombre_cliente, apellido_paterno, apellido_materno, telefono): 
    try:
        return db.update('clientes', nombre_cliente=nombre_cliente, apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, telefono=telefono,  
            where='id_cliente=$id_cliente',
            vars=locals())
    except Exception as e:
        print "Model update_clientes Error {}".format(e.args)
        print "Model update_clientes Message {}".format(e.message)
        return None
