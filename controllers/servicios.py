@auth.requires_login()
def index():
    db.servicios_extra.codigo_servicio.label = "Código de servicio"
    db.servicios_extra.descripcion.label = "Descripción"
    table = SQLFORM.grid(db.servicios_extra, fields=[db.servicios_extra.codigo_servicio, db.servicios_extra.descripcion, db.servicios_extra.cargo_extra])
    return dict(table=table)

@auth.requires_login()
def asignar():
    return dict()