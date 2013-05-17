# -*- coding: utf-8 -*-


response.logo = A(B('',SPAN("HMS"),),XML('&trade;&nbsp;'), _class="brand",_href="/init")
response.title = "HMS"
response.subtitle = "Hotel Management Simplified"

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Ismael Seratos <iaserrat@me.com>'
response.meta.description = 'Hotel Management System'
response.meta.keywords = ''
response.meta.generator = ''

## your http://google.com/analytics id
response.google_analytics_id = None

T.force("es-es")


def loadMenu():
  response.menu = [
      (T('Clientes'), False, None, [
          (T('Crear nuevo cliente'), False, URL('clientes', 'crearCliente'), []),
          (T('Administrar clientes'), False, URL('clientes', 'index'), []),
        ])
  ]

  response.menu += [
      (T('Habitaciones'), False, URL('habitaciones', 'index'), [

        ])
  ]

  response.menu += [
      (T('Servicios'), False, None, [
          (T('Administrar servicios'), False, URL('servicios', 'index'), []),
          #(T('Asignar un servicio'), False, URL('servicios', 'asignar'), []),
        ])
  ]

  response.menu += [
      (T('Reservaciones'), False, None, [
          (T('Nueva reservación'), False, URL('reservaciones', 'buscarCliente'), []),
          (T('Administrar reservaciones'), False, URL('reservaciones', 'administrar'), []),
          (T('Ver reservaciones'), False, URL('reservaciones', 'selhab'), []),
        ])
  ]

  response.menu += [
      (T('Totales'), False, None, [
        (T('Realizar cobro'), False, URL('reservaciones', 'buscarReservacion'), []),
        ])
  ]

  #response.menu += [
  #    (T('Configuración'), False, URL('default', 'index'), [
  #        (T('Crear nuevo cliente'), False, URL('default', 'index'), []),
  #        (T('Actualizar un cliente'), False, URL('default', 'index'), []),
  #        (T('Buscar un cliente'), False, URL('default', 'index'), []),
  #        (T('Eliminar un cliente'), False, URL('default', 'index'), [])
  #
  #      ])
  #]



if me != None:
  loadMenu()