@auth.requires_login()
def index():
    table = SQLFORM.grid(db.habitaciones, fields=[db.habitaciones.codigo_habitacion, db.habitaciones.tipo, db.habitaciones.costo_por_noche, db.habitaciones.disponible])
    return dict(table=table)