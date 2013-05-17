import string
if auth.user_id != None:
    me = auth.user_id
else:
    me = None

def doCountry():
    countries = {"AF":"Afghanistan","AL":"Albania","DZ":"Algeria","AS":"American Samoa","AD":"Andorra","AO":"Angola","AI":"Anguilla","AQ":"Antarctica","AG":"Antigua and Barbuda","AR":"Argentina","AM":"Armenia","AW":"Aruba","AU":"Australia","AT":"Austria","AZ":"Azerbaijan","BS":"Bahamas","BH":"Bahrain","BD":"Bangladesh","BB":"Barbados","BY":"Belarus","BE":"Belgium","BZ":"Belize","BJ":"Benin","BM":"Bermuda","BT":"Bhutan","BO":"Bolivia","BA":"Bosnia and Herzegovina","BW":"Botswana","BV":"Bouvet Island","BR":"Brazil","BQ":"British Antarctic Territory","IO":"British Indian Ocean Territory","VG":"British Virgin Islands","BN":"Brunei","BG":"Bulgaria","BF":"Burkina Faso","BI":"Burundi","KH":"Cambodia","CM":"Cameroon","CA":"Canada","CT":"Canton and Enderbury Islands","CV":"Cape Verde","KY":"Cayman Islands","CF":"Central African Republic","TD":"Chad","CL":"Chile","CN":"China","CX":"Christmas Island","CC":"Cocos [Keeling] Islands","CO":"Colombia","KM":"Comoros","CG":"Congo - Brazzaville","CD":"Congo - Kinshasa","CK":"Cook Islands","CR":"Costa Rica","HR":"Croatia","CU":"Cuba","CY":"Cyprus","CZ":"Czech Republic","CI":"C\u00f4te d\u2019Ivoire","DK":"Denmark","DJ":"Djibouti","DM":"Dominica","DO":"Dominican Republic","NQ":"Dronning Maud Land","DD":"East Germany","EC":"Ecuador","EG":"Egypt","SV":"El Salvador","GQ":"Equatorial Guinea","ER":"Eritrea","EE":"Estonia","ET":"Ethiopia","FK":"Falkland Islands","FO":"Faroe Islands","FJ":"Fiji","FI":"Finland","FR":"France","GF":"French Guiana","PF":"French Polynesia","TF":"French Southern Territories","FQ":"French Southern and Antarctic Territories","GA":"Gabon","GM":"Gambia","GE":"Georgia","DE":"Germany","GH":"Ghana","GI":"Gibraltar","GR":"Greece","GL":"Greenland","GD":"Grenada","GP":"Guadeloupe","GU":"Guam","GT":"Guatemala","GG":"Guernsey","GN":"Guinea","GW":"Guinea-Bissau","GY":"Guyana","HT":"Haiti","HM":"Heard Island and McDonald Islands","HN":"Honduras","HK":"Hong Kong SAR China","HU":"Hungary","IS":"Iceland","IN":"India","ID":"Indonesia","IR":"Iran","IQ":"Iraq","IE":"Ireland","IM":"Isle of Man","IL":"Israel","IT":"Italy","JM":"Jamaica","JP":"Japan","JE":"Jersey","JT":"Johnston Island","JO":"Jordan","KZ":"Kazakhstan","KE":"Kenya","KI":"Kiribati","KW":"Kuwait","KG":"Kyrgyzstan","LA":"Laos","LV":"Latvia","LB":"Lebanon","LS":"Lesotho","LR":"Liberia","LY":"Libya","LI":"Liechtenstein","LT":"Lithuania","LU":"Luxembourg","MO":"Macau SAR China","MK":"Macedonia","MG":"Madagascar","MW":"Malawi","MY":"Malaysia","MV":"Maldives","ML":"Mali","MT":"Malta","MH":"Marshall Islands","MQ":"Martinique","MR":"Mauritania","MU":"Mauritius","YT":"Mayotte","FX":"Metropolitan France","MX":"Mexico","FM":"Micronesia","MI":"Midway Islands","MD":"Moldova","MC":"Monaco","MN":"Mongolia","ME":"Montenegro","MS":"Montserrat","MA":"Morocco","MZ":"Mozambique","MM":"Myanmar [Burma]","NA":"Namibia","NR":"Nauru","NP":"Nepal","NL":"Netherlands","AN":"Netherlands Antilles","NT":"Neutral Zone","NC":"New Caledonia","NZ":"New Zealand","NI":"Nicaragua","NE":"Niger","NG":"Nigeria","NU":"Niue","NF":"Norfolk Island","KP":"North Korea","VD":"North Vietnam","MP":"Northern Mariana Islands","NO":"Norway","OM":"Oman","PC":"Pacific Islands Trust Territory","PK":"Pakistan","PW":"Palau","PS":"Palestinian Territories","PA":"Panama","PZ":"Panama Canal Zone","PG":"Papua New Guinea","PY":"Paraguay","YD":"People's Democratic Republic of Yemen","PE":"Peru","PH":"Philippines","PN":"Pitcairn Islands","PL":"Poland","PT":"Portugal","PR":"Puerto Rico","QA":"Qatar","RO":"Romania","RU":"Russia","RW":"Rwanda","RE":"R\u00e9union","BL":"Saint Barth\u00e9lemy","SH":"Saint Helena","KN":"Saint Kitts and Nevis","LC":"Saint Lucia","MF":"Saint Martin","PM":"Saint Pierre and Miquelon","VC":"Saint Vincent and the Grenadines","WS":"Samoa","SM":"San Marino","SA":"Saudi Arabia","SN":"Senegal","RS":"Serbia","CS":"Serbia and Montenegro","SC":"Seychelles","SL":"Sierra Leone","SG":"Singapore","SK":"Slovakia","SI":"Slovenia","SB":"Solomon Islands","SO":"Somalia","ZA":"South Africa","GS":"South Georgia and the South Sandwich Islands","KR":"South Korea","ES":"Spain","LK":"Sri Lanka","SD":"Sudan","SR":"Suriname","SJ":"Svalbard and Jan Mayen","SZ":"Swaziland","SE":"Sweden","CH":"Switzerland","SY":"Syria","ST":"S\u00e3o Tom\u00e9 and Pr\u00edncipe","TW":"Taiwan","TJ":"Tajikistan","TZ":"Tanzania","TH":"Thailand","TL":"Timor-Leste","TG":"Togo","TK":"Tokelau","TO":"Tonga","TT":"Trinidad and Tobago","TN":"Tunisia","TR":"Turkey","TM":"Turkmenistan","TC":"Turks and Caicos Islands","TV":"Tuvalu","UM":"U.S. Minor Outlying Islands","PU":"U.S. Miscellaneous Pacific Islands","VI":"U.S. Virgin Islands","UG":"Uganda","UA":"Ukraine","SU":"Union of Soviet Socialist Republics","AE":"United Arab Emirates","GB":"United Kingdom","US":"United States","ZZ":"Unknown or Invalid Region","UY":"Uruguay","UZ":"Uzbekistan","VU":"Vanuatu","VA":"Vatican City","VE":"Venezuela","VN":"Vietnam","WK":"Wake Island","WF":"Wallis and Futuna","EH":"Western Sahara","YE":"Yemen","ZM":"Zambia","ZW":"Zimbabwe","AX":"\u00c5land Islands"}
    l = []
    for v in countries.values():
        l.append(v)
    return sorted(l)

db.define_table("clientes",
    Field("nombre", requires = IS_NOT_EMPTY(error_message="No puede estár vacío.")),
    Field("apellido_paterno", requires = IS_NOT_EMPTY(error_message="No puede estár vacío.")),
    Field("apellido_materno", requires = IS_NOT_EMPTY(error_message="No puede estár vacío.")),
    Field("rfc", requires = IS_NOT_EMPTY(error_message="No puede estár vacío.")),
    Field("calle", requires = IS_NOT_EMPTY(error_message="No puede estár vacío.")),
    Field("numero", "integer"),
    Field("colonia", requires = IS_NOT_EMPTY(error_message="No puede estár vacío.")),
    Field("municipio", requires = IS_NOT_EMPTY(error_message="No puede estár vacío.")),
    Field("estado", requires = IS_NOT_EMPTY(error_message="No puede estár vacío.")),
    Field("pais"),
    Field("telefono_fijo", "integer", requires = IS_NOT_EMPTY(error_message="No puede estár vacío.")),
    Field("telefono_celular", "integer", requires = IS_NOT_EMPTY(error_message="No puede estár vacío.")),
    Field("email", requires = IS_NOT_EMPTY(error_message="No puede estár vacío.")),
    Field("cliente_frecuente", "boolean"),
    Field("porcentaje_descuento", "integer"),
    Field("codigo_cliente"),
    Field("web_password"))

db.define_table("habitaciones",
    Field("codigo_habitacion"),
    Field("tipo"),
    Field("costo_por_noche", "double"),
    Field("disponible", "boolean"),
    )

db.define_table("servicios_extra",
    Field("codigo_servicio"),
    Field("descripcion"),
    Field("cargo_extra", "double"))

db.define_table("reservaciones",
    Field("cliente"),
    Field("habitacion"),
    Field("fecha_entrada", "date"),
    Field("fecha_salida", "date"),
    Field("servicios_extra", 'list:reference servicios_extra')
    )

db.define_table("cobros",
    Field("cliente"),
    Field("habitacion"),
    Field("total_noches"),
    Field("costo_servicios_extra"),
    Field("subtotal_noches"),
    Field("descuento"),
    Field("total")
    )


# Validators
db.habitaciones.codigo_habitacion.requires = IS_NOT_IN_DB(db, "habitaciones.codigo_habitacion", error_message = "El código seleccionado ya se está usando o está vacío.")
db.habitaciones.tipo.requires = IS_IN_SET(["Sencilla", "Doble", "Suite"], error_message="Seleccione un valor válido.")
db.habitaciones.costo_por_noche.requires = IS_NOT_EMPTY(error_message="Por favor ingrese un costo por noche.")
db.habitaciones.disponible.default = True

db.servicios_extra.codigo_servicio.requires = IS_NOT_IN_DB(db, "servicios_extra.codigo_servicio", error_message =  "El código seleccionado ya se está usando o está vacío.")
db.servicios_extra.descripcion.requires = IS_NOT_EMPTY(error_message = "Por favor ingrese una descripción.")
db.servicios_extra.cargo_extra.requires = IS_NOT_EMPTY(error_message = "Por favor ingrese una cantidad válida.")

db.clientes.codigo_cliente.requires = IS_NOT_IN_DB(db, "clientes.codigo_cliente", error_message = "El código seleccionado ya se está usando o está vacío.")
db.clientes.pais.requires = IS_IN_SET(doCountry())
db.clientes.porcentaje_descuento.requires=IS_INT_IN_RANGE(0, 100)
db.clientes.porcentaje_descuento.default = 0
db.clientes.porcentaje_descuento.comment = "%"

db.reservaciones.cliente.requires = IS_IN_DB(db, 'clientes.id', '%(codigo_cliente)s', error_message="Seleccione un cliente válido.")
db.reservaciones.habitacion.requires = IS_IN_DB(db, 'habitaciones.id', '%(codigo_habitacion)s')
db.reservaciones.fecha_entrada.default = request.now
#db.reservaciones.fecha_salida.requires = IS_NOT_EMPTY(error_message="Debe especificar una fecha de salida estimada.")
db.reservaciones.servicios_extra.requires = IS_IN_DB(db, 'servicios_extra.id', '%(codigo_servicio)s', multiple = True)