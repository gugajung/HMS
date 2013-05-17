import string
import random

@auth.requires_login()
def index():
    db.clientes.nombre.label = "Nombre (s)"
    db.clientes.rfc.label = "RFC"
    db.clientes.codigo_cliente.label = "Código de cliente"
    db.clientes.codigo_cliente.default = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(8))
    db.clientes.codigo_cliente.writable = False
    db.clientes.web_password.writable = False
    db.clientes.web_password.default = ''.join(random.choice(string.digits) for x in range(8))
    grid = SQLFORM.grid(db.clientes, create = False, csv=True, fields=[db.clientes.nombre, db.clientes.apellido_paterno, db.clientes.apellido_materno, db.clientes.rfc,
        db.clientes.email, db.clientes.codigo_cliente])
    return dict(grid=grid)

@auth.requires_login()
def crearCliente():
    db.clientes.nombre.label = "Nombre (s)"
    db.clientes.codigo_cliente.default = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(8))
    db.clientes.codigo_cliente.writable = False
    db.clientes.web_password.writable = False
    db.clientes.web_password.default = ''.join(random.choice(string.digits) for x in range(8))
    form = SQLFORM(db.clientes)
    if form.process().accepted:
        response.flash = 'Cliente guardado con éxito!'
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    return dict(form=form)