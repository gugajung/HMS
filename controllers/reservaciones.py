@auth.requires_login()
def nueva():
    wId = None
    if len(request.args) == 1:
        wId = request.args[0]
    db.reservaciones.cliente.default = wId
    form = SQLFORM(db.reservaciones)
    if form.validate():
        habId = form.vars["habitacion"]
        if habId != None:
            habitacionDisponible = db(db.habitaciones.id == habId).select().first().disponible
            if habitacionDisponible:
                if form.vars["fecha_salida"] == None:
                    response.flash = "Seleccione una fecha de salida."          
                else:
                    if form.vars["fecha_salida"] <= form.vars["fecha_entrada"]:
                        response.flash = "La fecha de salida no puede ser antes de la fecha de entrada."
                    else:
                        allRoomBookings = db(db.reservaciones.habitacion == form.vars["habitacion"]).select()
                        noDisponibleFlag = False
                        for row in allRoomBookings:
                            if (row.fecha_entrada < form.vars["fecha_entrada"] < row.fecha_salida) or (row.fecha_entrada < form.vars["fecha_salida"] < row.fecha_salida):
                                noDisponibleFlag = True
                                break
                        if noDisponibleFlag:
                            response.flash = "La habicación seleccionada ya está ocupada en el rango de fecha seleccionado."
                        else:
                            db.reservaciones.insert(**dict(form.vars))        
                            response.flash = 'Reservación realizada con éxito!'
            else:
                response.flash = 'La habitación seleccionada no está disponible para reservar.'
                #form.errors
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    return dict(form=form)

@auth.requires_login()
def administrar():
    db.reservaciones.cliente.represent = lambda value, row: db(db.clientes.id == value).select().first().codigo_cliente
    db.reservaciones.habitacion.represent = lambda value, row: db(db.habitaciones.id == value).select().first().codigo_habitacion
    table = SQLFORM.grid(db.reservaciones, create=False, fields=[db.reservaciones.cliente, db.reservaciones.habitacion, 
        db.reservaciones.fecha_entrada, db.reservaciones.fecha_salida])
    return  dict(table=table)

@auth.requires_login()
def selhab():
    script = SCRIPT("""
                    $('document').ready(function(){
                        $('#mycombo').change(function(){
                            $('#myform').submit();
                        });
                    });
                    """)
    form = SQLFORM.factory(Field("habitacion",label="Seleccione habitación",requires=IS_IN_DB(db(db.habitaciones.id>0),'habitaciones.id','habitaciones.codigo_habitacion',error_message="Seleccione una habitación de la lista")))
    submit = form.element('input',_type='submit') 
    form.attributes['_id'] = 'myform'
    submit['_style'] = 'display:none;' 
    form.element('select').attributes['_id'] = 'mycombo'
    
    if form.accepts(request.vars, keepvalues=True):
        a = form.vars.habitacion
        redirect(URL('calendario', args=a))
    return dict(script=script,form=form)


@auth.requires_login()
def calendario():
    if len(request.args) != 1:
        redirect(URL('selhab'))
    wId = request.args[0]
    roomName = db(db.habitaciones.id == wId).select().first().codigo_habitacion
    rows = db(db.reservaciones.habitacion == wId).select()
    return dict(rows=rows, roomName = roomName)


@auth.requires_login()
def buscarCliente():
    #form, table = crud.search(db.clientes, fields = ['id','nombre', 'apellido_paterno', 'apellido_materno', 'rfc', 'email'], queries=["contains"], query_labels=dict(contains='Contiene'))
    db.clientes.id.represent = lambda value, row: A('RESERVAR', _href=URL('nueva', args = value))
    db.clientes.id.label = "Acción"
    form = SQLFORM.grid(db.clientes,fields=[db.clientes.id, db.clientes.nombre, db.clientes.apellido_paterno, db.clientes.apellido_materno, db.clientes.rfc, db.clientes.email],
                        deletable=False, editable=False, details=False, csv = False,create=False,)
    return dict(form=form)


@auth.requires_login()
def buscarReservacion():
    db.reservaciones.id.represent = lambda value, row: A('REALIZAR COBRO', _href=URL('cobrar', args = value))
    db.reservaciones.id.label = "Acción"
    db.reservaciones.cliente.represent = lambda value, row: db(db.clientes.id == value).select().first().codigo_cliente
    db.reservaciones.habitacion.represent = lambda value, row: db(db.habitaciones.id == value).select().first().codigo_habitacion
    form = SQLFORM.grid(db.reservaciones,
                        deletable=False, editable=False, details=False, csv = False,create=False,)
    return dict(form=form)


@auth.requires_login()
def cobrar():
    if len(request.args) != 1:
        redirect(URL('buscarReservacion'))
    wId = request.args[0]
    start = db(db.reservaciones.id == wId).select().first().fecha_entrada
    end = db(db.reservaciones.id == wId).select().first().fecha_salida
    totalTime = end - start
    daysTime = totalTime.days if totalTime.days != 0 else 1
    idHabitacion = db(db.reservaciones.id == wId).select().first().habitacion
    costoHabitacion = db(db.habitaciones.id == idHabitacion).select().first().costo_por_noche
    subtotal = costoHabitacion * daysTime
    listaServiciosExtra = db(db.reservaciones.id == wId).select().first().servicios_extra
    costoServicios = 0
    

    idCliente = db(db.reservaciones.id == wId).select().first().cliente
    porcentajeDescuento = db(db.clientes.id == idCliente).select().first().porcentaje_descuento

    if len(listaServiciosExtra) == 0:
        if porcentajeDescuento == 0:
            total = subtotal
        else:
            aDescontar = float(subtotal) * (float(porcentajeDescuento) / 100)
            total = subtotal - aDescontar
    else:
        for servicio in listaServiciosExtra:
            sExtra = db(db.servicios_extra.id == servicio).select().first().cargo_extra
            costoServicios += sExtra
        if porcentajeDescuento == 0:
            total = subtotal + costoServicios
        else:
            aDescontar = float(subtotal) * (float(porcentajeDescuento) / 100)
            total = (subtotal + costoServicios) - aDescontar

    db.cobros.cliente.default = db(db.reservaciones.id == wId).select().first().cliente
    db.cobros.cliente.writable = False
    db.cobros.cliente.represent = lambda value, row: db(db.clientes.id == value).select().first().codigo_cliente
    db.cobros.habitacion.default = db(db.reservaciones.id == wId).select().first().habitacion
    db.cobros.habitacion.represent = lambda value, row: db(db.habitaciones.id == value).select().first().codigo_habitacion
    db.cobros.habitacion.writable = False
    db.cobros.total_noches.label = "Total de noches"
    db.cobros.total_noches.writable = False
    db.cobros.total_noches.default = daysTime
    db.cobros.costo_servicios_extra.writable = False
    db.cobros.costo_servicios_extra.default = costoServicios
    db.cobros.subtotal_noches.writable = False
    db.cobros.subtotal_noches.default = subtotal
    db.cobros.descuento.writable = False
    db.cobros.descuento.comment = "%"
    db.cobros.descuento.default = porcentajeDescuento
    db.cobros.total.writable = False
    db.cobros.total.default = total

    if porcentajeDescuento != 0:
        db.cobros.total.comment = "[Descuento aplicado]"

    form = SQLFORM(db.cobros, submit_button = 'Registrar pago')
    if form.process().accepted:
        response.flash = 'Pago registrado con éxito!'
        db(db.reservaciones.id == wId).delete()
        redirect(URL('buscarReservacion'))
    elif form.errors:
        response.flash = 'El formulario tiene errores'
    return dict(form=form)