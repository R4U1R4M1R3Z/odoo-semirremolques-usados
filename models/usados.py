# -*- coding:utf-8 -*-
from odoo import api, fields, models


class usados(models.Model):
    _name = 'usados'
    _description = 'Modulo para el control de semirremolques'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']

    name = fields.Char(string='Matricula',tracking=True)
    num_bastidor = fields.Char(string='Número de bastidor',tracking=True)
    marca_bastidor = fields.Char(string='Marca de bastidor',tracking=True)
    num_furgon = fields.Char(string='Número de furgón',tracking=True)
    marca_furgon = fields.Char(string='Marca de furgón',tracking=True)
    anyo_fabricacion = fields.Date(string='Fecha de fabricación')
    seguro_check = fields.Boolean(string='Seguro')
    fecha_seguro = fields.Date(string='Fecha vigencia del seguro',tracking=True)
    fecha_ITV = fields.Date(string='Fecha vigencia de ITV',tracking=True)
    ubicacion = fields.Selection(
        string='Ubicación',
        selection=[('Campa 1', 'Campa 1'),
                   ('Campa 2', 'Campa 2'),
                   ('Campa 3', 'Campa 3'),
                   ('Campa de tierra', 'Campa de tierra'),
                   ('Patio de banderas', 'Patio de banderas'),
                   ('Alberic', 'Alberic'),
                   ('otros', 'Otros')]
    )
    ubicacion_otros = fields.Char(string='Ubicación otros:')
    
    
    lateral_derecho = fields.Binary(
        string='Lateral derecho',
    )
    lateral_izquierdo = fields.Binary(
        string='Lateral izquierdo',
    )
    portapale_derecho = fields.Binary(
        string='Portapalé derecho',
    )
    portapale_izquierdo = fields.Binary(
        string='Portapalé izquierdo',
    )
    centroruedas_izquierdo = fields.Binary(
        string='Centro ruedas izquierdo',
    )
    centroruedas_derecho = fields.Binary(
        string='Centro ruedas derecha',
    )
    trasera = fields.Binary(
        string='Trasera',
    )
    esquina1 = fields.Binary(
        string='Esquina 1',
    )
    esquina2 = fields.Binary(
        string='Esquina 2',
    )
    esquina3 = fields.Binary(
        string='Esquina 3',
    )
    esquina4 = fields.Binary(
        string='Esquina 4',
    )
    frontal = fields.Binary(
        string='Frontal',
    )

    interior = fields.Binary(
        string='Interior',
    )

    otros1 = fields.Binary(
        string='Otros 1',
    )

    otros2 = fields.Binary(
        string='Otros 2',
    )

    otros3 = fields.Binary(
        string='Otros 3',
    )


    state = fields.Selection(selection=[
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('vendido', 'Vendido'),
        ('alquilado', 'Alquilado'),
        ('obsoleto', 'Obsoleto'),
        ('cedido', 'Cedido'),
    ], default='disponible', string='Estados', copy=False)
    situacion = fields.Text(string='Situacion')

    # Caracteristicas del furgon
    ATP = fields.Selection(
        string='ATP',
        selection=[('Frigorifico', 'Frigorifico'), ('Isotermo', 'Isotermo')]
    )
    documentacion_atp = fields.Boolean(string='Documentación ATP')
    fecha_ATP = fields.Date(string='Fecha vigencia ATP',tracking=True)
    termografo = fields.Boolean(string='Termógrafo')
    documentacion_termografo = fields.Boolean(string='Documentación termógrafo')
    fecha_termografo = fields.Date(string='Fecha vigencia documentación termógrafo')
    modelo = fields.Selection(
        string='Modelo',
        selection=[('Monotemperatura', 'Monotemperatura'),
                    ('Multitemperatura', 'Multitemperatura')]
    )
    zocalo = fields.Selection(
        string='Zocalo',
        selection=[('Aluminio', 'Aluminio'),
                   ('Poliester', 'Poliester')]
    )
    cierre = fields.Selection(
        string='Cierre',
        selection=[('2 cierres', '2 cierres'),
                   ('4 cierres', '4 cierres')]
    )
    tipo_carga = fields.Selection(
        string='Tipo de carga',
        selection=[('Estándar', 'Estándar'),
                   ('Carne colgada', 'Carne colgada'),
                   ('Carga a doble altura','Carga a doble altura')]
    )
    acabado_piso = fields.Selection(
        string='Acabado del piso',
        selection=[('Aluminio', 'Aluminio'),
                   ('Poliester', 'Poliester')]
    )
    altura_interior = fields.Selection(
        string='Altura interior',
        selection=[('2600', '2600'),
                   ('2650', '2650'),
                   ('2700','2700'),
                   ('2750','2750')]
    )
    anchura_interior = fields.Selection(
        string='Anchura interior',
        selection=[('2470', '2470'),
                   ('2500','2500')]
    )
    observaciones_furgon = fields.Text(string='Observaciones')
    
    # caracteristicas del chasis

    marca_ejes = fields.Char(string='Marca ejes')
    eje_direccional = fields.Boolean(string='Eje direccional')
    eje_elevable = fields.Boolean(string='Eje elevable')
    eje_elevable_ubi = fields.Char(
        string='Ejes que llevan ejes elevables',
    )
    rueda_repuesto = fields.Boolean(string='Rueda de repuesto')
    
    cantidad_neumaticos = fields.Char(
        string='Cantidad neumaticos',
    )
    tamanyo_neumaticos = fields.Selection(
        string='Tamaño de neumáticos',
        selection=[('385/55/22,5', '385/55/22,5'),
                   ('385/65/22,5','385/65/22,5')]
    )
    
    modelo1 = fields.Char(string='Modelo')
    estado1 = fields.Char(string='Estado')
    profundidad1 = fields.Char(string='Profundidad')
    modelo2 = fields.Char(string='Modelo')
    estado2 = fields.Char(string='Estado')
    profundidad2 = fields.Char(string='Profundidad')
    modelo3 = fields.Char(string='Modelo')
    estado3 = fields.Char(string='Estado')
    profundidad3 = fields.Char(string='Profundidad')
    modelo4 = fields.Char(string='Modelo')
    estado4 = fields.Char(string='Estado')
    profundidad4 = fields.Char(string='Profundidad')
    modelo5 = fields.Char(string='Modelo')
    estado5 = fields.Char(string='Estado')
    profundidad5 = fields.Char(string='Profundidad')
    modelo6 = fields.Char(string='Modelo')
    estado6 = fields.Char(string='Estado')
    profundidad6 = fields.Char(string='Profundidad')
    modelo_rueda_repuesto = fields.Char(string='Modelo')
    estado_rueda_repuesto = fields.Char(string='Estado')
    profundidad_rueda_repuesto = fields.Char(string='Profundidad')
    
    
    tipo_freno = fields.Selection(
        string='Tipo de freno',
        selection=[('Disco', 'Disco'), ('Tambor', 'Tambor')]
    )
    tipo_freno_1 = fields.Selection(
        string='Tipo',
        selection=[('B0', 'B0'), ('B120', 'B120')]
    )

    observaciones_chasis = fields.Text(string='Observaciones')
    

    lr_Horizontal_laterales = fields.Boolean(string='Líneas de retención de carga horizontal en laterales')
    lr_Horizontal_laterales_cantidad = fields.Char(string='Cantidad de líneas de retención de carga horizontal en laterales')

    lr_Horizontal_laterales_embutidas = fields.Boolean(string='Embutidas')
    lr_Horizontal_laterales_embutidas_cantidad = fields.Char(string='Cantidad')

    lr_techo = fields.Boolean(string='Líneas de retención de carga en el techo')
    lr_techo_cantidad = fields.Char(string='Cantidad de líneas de retención de carga en el techo')

    barra_horizontal = fields.Boolean(string='Barra horizontal')
    barra_horizontal_cantidad = fields.Char(string='Cantidad de barras horizontales')

    barra_vertical_puntataco = fields.Boolean(string='Barra vertical punta-taco')
    barra_vertical_puntataco_cantidad = fields.Char(string='Cantidad de barras verticales punta-taco')

    barra_vertical_tacotaco = fields.Boolean(string='Barra vertical taco-taco')
    barra_vertical_tacotaco_cantidad = fields.Char(string='Cantidad de barras verticales taco-taco')

    lona = fields.Boolean(string='Lona')
    longitud_lona = fields.Char(string='Longitud')
    rotulacion = fields.Boolean(string='Rotulación')
    banda_laterales = fields.Boolean(string='Banda de protección de aluminio de 200 en laterales')
    banda_laterales_cantidad = fields.Char(string='Cantidad de bandas de protección de aluminio de 200 en laterales')

    banda_techo = fields.Boolean(string='Banda de protección de aluminio de 200 en techo')
    banda_techo_cantidad = fields.Char(string='Cantidad de bandas de protección de aluminio de 200 en techo')

    desague = fields.Boolean(string='Desagüe')
    posicion_desague = fields.Char(string='Posición')
    canal_desague = fields.Char(string='Canal')
    colector = fields.Boolean(string='Colector')

    tipo_colector = fields.Selection(
        string='Tipo de colector',
        selection=[('Colector de poliéster ', 'Colector de poliéster '),
                ('Colector metálico ', 'Colector metálico '),
                ('Colector de lona', 'Colector de lona')]
    )



    plataforma = fields.Boolean(string='Plataforma elevadora')


    # accesorios chasis  

    portapale_cerrado = fields.Boolean(string='Portapalé cerrado')
    portapale_abierto = fields.Boolean(string='Portapalé abierto')
    anticiclista = fields.Boolean(string='Anticiclista')
    escalera_trasera = fields.Boolean(string='Escalera trasera')
    portadocumentos = fields.Boolean(string='Portadocumentos')
    cajones = fields.Boolean(string='Cajones y depósito de agua')
    posicion_cajones = fields.Char(string='Posición')
    tabique = fields.Boolean(string='Tabique')
    tipo_tabique = fields.Selection(string='Tipo tabique', selection=[('Rijido desplazable', 'Rijido desplazable'), ('Colchoneta', 'Colchoneta')])
    soporte_Rueda = fields.Boolean(string='Soporte rueda')
    tipo_Soporte = fields.Selection(string='Tipo de soporte rueda', selection=[('Jaula portaruedas doble', 'Jaula portaruedas doble'), ('Soporte de rueda tipo cesta', 'Soporte de rueda tipo cesta'),])

    observaciones_accesorios = fields.Text(string='Observaciones accesorios')

    # equipo de frio

    
    marca_Equipo_frio = fields.Selection(
        string='Marca equipo de frio',
        selection=[('Thermo King', 'Thermo King'), ('Carrier', 'Carrier'),('Otros', 'Otros')]
    )
    
    
    modelo_Equipo_frio = fields.Char(string='Modelo')
    horas_equipo = fields.Char(string='Horas del equipo')
    horas_equipo_diesel = fields.Char(string='Horas de equipo diesel')
    
    tipo_equipo = fields.Selection(string='Tipo de equipo', selection=[('Eléctrico y diesel ', 'Eléctrico y diesel'), ('Diesel', 'Diesel')])
    modelo_termografo = fields.Char(string='Modelo termógrafo ')
    observaciones_equipoFrio = fields.Text(
        string='observaciones equipo frio',
    )
    
    # datos de compra
    compradoa_id = fields.Many2one(
        string='Comprado a',
        comodel_name='res.partner',
        ondelete='restrict',
        tracking=True
    )
    fecha_Entrada = fields.Date(string='Fecha de entrada',tracking=True)
    precio_compra = fields.Float(string='Precio de compra',tracking=True)

    #datos de venta

    vendidoa_id = fields.Many2one(
        string='Vendido a',
        comodel_name='res.partner',
        ondelete='restrict',
        tracking=True
    )
    fecha_salida = fields.Date(string='Fecha de salida',tracking=True)
    precio_venta = fields.Float(string='Precio de venta',tracking=True)
    fcha_reservado = fields.Date(string='Fecha reservado',tracking=True)
    fcha_venta = fields.Date(string='Fecha venta',tracking=True)

    registro = 0
    
    accion_com = fields.Selection(
        string='Tipo de operación',
        selection=[('Venta', 'Venta'),
                   ('Renting', 'Renting'),
                   ('Ceder', 'Ceder')],tracking=True
    )

    mensualidades = fields.Char(string='Mensualidades',tracking=True)
    fecha_inicio_renting = fields.Date(
        string='Fecha inicio del renting',
        default=fields.Date.context_today,tracking=True
    )
    fecha_fin_renting = fields.Date(
        string='Fecha fin del renting',tracking=True
    ) 
    quota_renting = fields.Float(
        string='Precio quota',tracking=True
    )
    
    cedidoa_id = fields.Many2one(
        string='Cedido a',
        comodel_name='res.partner',
        ondelete='restrict',tracking=True
    )    
    
    
    
    
    
    coste_reparacion = fields.Float(
        string='Coste de reparación',tracking=True
    )
    informacion_reparacion = fields.Text(string='Información sobre la reparación')
    informe_reparacion = fields.Binary(string='Informe de reparación')
    informe_reparacion_filename = fields.Char(string='Informe de reparación')    


    #documentacion

    cambio_nombre = fields.Binary(string='Cambio de nombre')
    cambio_nombre_filename = fields.Char(string='Cambio de nombre')
    entrada = fields.Binary(string='Entrada')
    entrada_filename = fields.Char(string='Entrada')
    ATP_documentacion = fields.Binary(string='ATP')
    ATP_filename = fields.Char(string='ATP')
    entrada_devolucion = fields.Binary(string='Entrada usado')
    entrada_devolucion_filename = fields.Char(string='Entrada usado')
    ficha_tecnica = fields.Binary(string='Ficha técnica')
    ficha_tecnica_filename = fields.Char(string='Ficha técnica')
    permiso_circulacion = fields.Binary(string='Permiso de circulación')
    permiso_circulacion_filename = fields.Char(string='Permiso de circulación')
    contrato = fields.Binary(string='Contrato')
    contrato_filename = fields.Char(string='Contrato')
    factura = fields.Binary(string='Factura')
    factura_filename = fields.Char(string='Factura')
    seguro = fields.Binary(string='Seguro')
    seguro_filename = fields.Char(string='Seguro')
    

    def reservar(self):
        self.state = 'reservado'
        self.fcha_reservado = fields.Datetime.now()

    def obsoleto(self):
        self.state = 'obsoleto'

    def vender(self):
        self.state = 'vendido'
        self.fcha_reservado = fields.Datetime.now()

    def cancelar(self):
        self.state = 'disponible'

    def ceder(self):
        self.state = 'cedido'




    _sql_constraints = [ ('unique_furgon', 'unique(num_furgon)', 'Este número de furgón ya existe en la base de datos!\nPor favor, introduce otro número de furgón diferente')	]
    _sql_constraints = [ ('unique_chasis', 'unique(num_bastidor)', 'Este número de bastidor ya existe en la base de datos!\nPor favor, introduce otro número de bastidor diferente')	]
    _sql_constraints = [ ('unique_chasis', 'unique(name)', 'Este número de matricula ya existe en la base de datos!\nPor favor, introduce otro número de matricula diferente')	]






    
    
    
    
    
    
    
    
    
