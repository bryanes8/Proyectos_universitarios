use Proyecto1_201800526

create table Tipo_Tarjeta(
id_Tipo_Tarjeta int primary key not null,
Tipo varchar(160) not null                     --Master, visa
);
create table Autorizacion(
id_Autorizacion int primary key not null,
Descripcion varchar(160) not null       
);
create table Cargo(
id_Cargo int primary key not null,
Descripcion varchar(160) not null       --Alta/Baja
);
create table Categorias(
id_Categorias int primary key not null,
Abreviatura varchar(160) not null,       
Descripcion varchar(160) not null,       
Codigo varchar(160) not null,       
);
create table Rango_Usuarios(
id_Rango_Usuarios int primary key not null,
Descripcion varchar(160) not null       --1-10 personas, etc
);
create table Tipo_Suscripcion(
id_Tipo_Suscripcion int primary key not null,
Descripcion varchar(160) not null       
);
create table Tasa_Cambio(
id_Tasa_Cambio int primary key not null,
Precio_Dolar float not null,
Precio_Quetzal float not null,       
);
create table Especificacion_Modulo(
id_Especificacion_Modulo int primary key not null,
Descripcion varchar(160) null       
);
create table Estado(
id_Estado int primary key not null,
Estado varchar(160) not null       --Activo/Inactivo
);
create table Clasificacion(
id_Clasificacion int primary key not null,
Clasificacion varchar(160) not null       --boquitas, lácteos etc
);
create table Presentacion(
id_Presentacion int primary key not null,
Presentacion varchar(160) not null       --unidad, litro, etc
);
create table Correo(
id_Correo int primary key not null,
Cuerpo varchar(160) not null                 --Validación, etc
);
create table Tarjeta_Credito(
id_Tarjeta_Credito int primary key not null,
Numero_Tarjeta int not null,
Nombre varchar(160) not null,
Fecha_vencimiento date not null,
Codigo_verificacion int not null,
id_Tipo_Tarjeta int not null,
foreign key (id_Tipo_Tarjeta) references Tipo_Tarjeta (id_Tipo_Tarjeta) 
);
create table Cambio_Tarjeta(
id_Cambio_Tarjeta int primary key not null,
Numero_Tarjeta int null,
Nombre varchar(160) null,
Fecha_vencimiento date null,
Codigo_verificacion int null,
id_Tipo_Tarjeta int null,
foreign key (id_Tipo_Tarjeta) references Tipo_Tarjeta (id_Tipo_Tarjeta)
);

create table Tamano_Empresa(
id_Tamano_Empresa int primary key not null,
Descripcion  varchar(160) not null
);
create table Tipo_Empresa(
id_Tipo_Empresa int primary key not null,
Descripcion  varchar(160) not null    -- #1-10,…, #41-50, >50
);
create table Rol_Contacto(
id_Rol_Contacto int primary key not null,
Tipo  varchar(160) not null    --Comercial, gerencial, administrador
);
create table Contacto_Comercial(
DPI_Contacto_Comercial int primary key not null,
Nombre varchar(160) not null,
Numero_Celular int not null,     
Telefono_Oficina int not null,   
Extension int not null, 
Correo_Electronico varchar(160) not null,
Direccion varchar(160) not null,
id_Rol_Contacto  int not null,
foreign key (id_Rol_Contacto) references Rol_Contacto(id_Rol_Contacto) 
);
create table Proveedor(
id_Proveedor int primary key not null,
NIT varchar(160) not null,
Nombre varchar(160) not null,
Direccion varchar(160) not null,
Numero_telefono int not null,
Limite_credito int not null,
Nombre_contacto varchar(160) not null,
Correo_electronico varchar(160) not null,
id_Cargo int not null,
foreign key (id_Cargo) references Cargo (id_Cargo)
);
create table Productos(
id_Productos int primary key not null,
Codigo_producto varchar(160) not null,
Codigo_barras varchar(160) not null,
Nombre_producto varchar(160) not null,
Descripcion varchar(160) not null,
id_Estado int not null,
id_Presentacion int not null,
id_Clasificacion int not null,
foreign key (id_Estado) references Estado (id_Estado),
foreign key (id_Presentacion) references Presentacion (id_Presentacion),
foreign key (id_Clasificacion) references Clasificacion (id_Clasificacion)
);
create table Pago_Clientes(
id_Pago_Clientes int primary key not null,
Pago_Mensual float not null,
id_Tarjeta_Credito int not null,
id_Cambio_Tarjeta int null,
foreign key (id_Tarjeta_Credito) references Tarjeta_Credito (id_Tarjeta_Credito),
foreign key (id_Cambio_Tarjeta) references Cambio_Tarjeta (id_Cambio_Tarjeta)
);
create table Precio(
id_Precio int primary key not null,
Precio float not null,
id_Tasa_Cambio int not null,
foreign key (id_Tasa_Cambio) references Tasa_Cambio (id_Tasa_Cambio)
);
create table Periodicidad(
id_Periodicidad int primary key not null,
id_Precio int not null,
id_Tipo_Suscripcion int not null,
id_Tamano_Empresa int not null,
id_Tasa_Cambio int not null,
foreign key (id_Precio) references Precio (id_Precio),
foreign key (id_Tipo_Suscripcion) references Tipo_Suscripcion (id_Tipo_Suscripcion),
foreign key (id_Tamano_Empresa) references Tamano_Empresa(id_Tamano_Empresa),
foreign key (id_Tasa_Cambio) references Tasa_Cambio (id_Tasa_Cambio)
);
create table Tienda_Modulos(
id_Tienda_Modulos int primary key not null,
Agregar_Modulo varchar(160) not null,
Eliminar_Modulo varchar(160) not null,
id_Pago_Clientes int not null,
id_Precio int not null,
foreign key (id_Pago_Clientes) references Pago_Clientes (id_Pago_Clientes), 
foreign key (id_Precio) references Precio (id_Precio)
);
create table Lista_Precio(
id_Lista_Precio int primary key not null,
Fecha_inicio date not null,
Fecha_final date null,
id_Pago_Clientes int not null,
id_Rango_Usuarios int not null,
foreign key (id_Pago_Clientes) references Pago_Clientes (id_Pago_Clientes),
foreign key (id_Rango_Usuarios) references Rango_Usuarios (id_Rango_Usuarios)
);
create table Gestion_Clientes(
id_Gestion_Clientes int primary key not null,
NIT int not null,
Nombre varchar(160) not null,
Direccion varchar(160) not null,
Numero_telefonico int not null,
Nombre_contacto varchar(160) not null,
Correo_electronico varchar(160) not null,
Limite_credito int not null,
Cantidad_dias varchar(160) not null,
id_Cargo int not null,
foreign key (id_Cargo) references Cargo (id_Cargo)
);
create table Empresa(
id_Empresa int primary key not null,
Nombre  varchar(160) not null
);
create table EmpresaDatos(
id_EmpresaDatos int primary key not null,
id_Proveedor int not null,
id_Productos int not null,
id_Gestion_Clientes int not null,
id_Tamano_Empresa int not null,  
id_Tipo_Empresa int not null, 
id_Empresa int not null,
foreign key (id_Proveedor) references Proveedor(id_Proveedor),
foreign key (id_Productos) references Productos(id_Productos),
foreign key (id_Gestion_Clientes) references Gestion_Clientes(id_Gestion_Clientes),
foreign key (id_Tipo_Empresa) references Tipo_Empresa(id_Tipo_Empresa),
foreign key (id_Tamano_Empresa) references Tamano_Empresa(id_Tamano_Empresa),
foreign key (id_Empresa) references Empresa(id_Empresa)
);
create table Cliente_PYME(
id_Cliente_PYME int primary key not null,
NIT int not null,
Nombre_empresa varchar(160) not null,
id_Tarjeta_Credito int not null,
DPI_Contacto_Comercial int not null,
id_Empresa int not null,
foreign key (id_Tarjeta_Credito) references Tarjeta_Credito (id_Tarjeta_Credito),
foreign key (DPI_Contacto_Comercial) references Contacto_Comercial (DPI_Contacto_Comercial),
foreign key (id_Empresa) references Empresa(id_Empresa)
);
create table Usuario(
id_Usuario int primary key not null,
Nombre varchar(160) not null,
Correo_electronico varchar(160) not null,
Puesto varchar(160) not null,
Celular int not null,
);
create table ERP_SaaS(
id_ERP_SaaS int primary key not null,
Usuario_correo varchar(160) not null,
Contraseña_automatica varchar(160) not null,
id_Usuario int not null,
foreign key (id_Usuario) references Usuario (id_Usuario)
);
create table Creacion_Modulos(
id_Creacion_Modulos int primary key not null,
Codigo varchar(160) not null,
Nombre varchar(160) not null,
Abreviatura varchar(160) not null,
Descripcion varchar(160) not null,
id_Especificacion_Modulo int not null,
foreign key (id_Especificacion_Modulo) references Especificacion_Modulo(id_Especificacion_Modulo) 
);
create table Usuarios_Contratados(
id_Usuarios_Contratados int primary key not null,
Descripcion varchar(160) not null,
Nuevo_rango varchar(160) not null,
Nueva_tarifa int not null,
id_Precio int not null,
id_Rango_Usuarios int not null,
foreign key (id_Precio) references Precio (id_Precio),
foreign key (id_Rango_Usuarios) references Rango_Usuarios(id_Rango_Usuarios) 
);
create table Datos_Suscripcion(
id_Datos_Suscripcion int primary key not null,
Usuarios_uso int not null,
Usuarios_cantidad int not null,
Id_Usuarios_Contratados int not null,
id_Tipo_Suscripcion int not null,
id_Rango_Usuarios int not null,
foreign key (id_Usuarios_Contratados) references Usuarios_Contratados(id_Usuarios_Contratados),
foreign key (id_Tipo_Suscripcion) references Tipo_Suscripcion(id_Tipo_Suscripcion),
foreign key (id_Rango_Usuarios) references Rango_Usuarios(id_Rango_Usuarios) 
);
create table Nueva_Periodicidad(
id_Nueva_Periodicidad int primary key not null,
Descripcion varchar(160) not null,
Fecha_inicio date not null,  --Cobro
id_Precio int not null,
foreign key (id_Precio) references Precio (id_Precio),
);
create table Cambio_Suscripcion(
id_Cambio_Suscripcion int primary key not null,
Descripcion varchar(160) not null,
id_Rango_Usuarios int not null,
id_Tipo_Suscripcion int not null,
id_Nueva_Periodicidad int not null,
foreign key (id_Rango_Usuarios) references Rango_Usuarios (id_Rango_Usuarios), 
foreign key (id_Tipo_Suscripcion) references Tipo_Suscripcion(id_Tipo_Suscripcion),
foreign key (id_Nueva_Periodicidad) references Nueva_Periodicidad(id_Nueva_Periodicidad), 
);
create table Administrador_Sistema(
id_Administrador_Sistema int primary key not null,
Habilitar varchar(160) not null,
Deshabilitar varchar(160) not null,
Eliminar_Usuario varchar(160) null,
id_Cliente_PYME int not null,
id_Creacion_Modulos int null,
id_Correo int null,
id_Usuario int not null,
id_Datos_Suscripcion int not null,
id_Cambio_Suscripcion int not null,
foreign key (id_Cliente_PYME) references Cliente_PYME(id_Cliente_PYME),  
foreign key (id_Creacion_Modulos) references Creacion_Modulos (id_Creacion_Modulos),
foreign key (id_Correo) references Correo (id_Correo),  
foreign key (id_Usuario) references Usuario (id_Usuario),
foreign key (id_Datos_Suscripcion) references Datos_Suscripcion(id_Datos_Suscripcion),
foreign key (id_Cambio_Suscripcion) references Cambio_Suscripcion(id_Cambio_Suscripcion)
);
create table Administrador_Servicio(
id_Administrador_Servicio int primary key not null,
Usuario_Admin varchar(160) not null,
Password varchar(160) not null,
id_Correo int not null,
id_Usuario int not null,
foreign key (id_Correo) references Correo(id_Correo),
foreign key (id_Usuario) references Usuario (id_Usuario) 
);
create table Administrador_Contacto(
id_Administrador_Contacto int primary key not null,
Usuario_Admin varchar(160) not null,
Nueva_Password varchar(160) not null,
id_Correo int not null,
id_Administrador_Servicio int not null,
id_Autorizacion int null,
id_Usuario int not null,
foreign key (id_Correo) references Correo(id_Correo),
foreign key (id_Administrador_Servicio) references Administrador_Servicio(id_Administrador_Servicio),
foreign key (id_Autorizacion) references Autorizacion(id_Autorizacion),
foreign key (id_Usuario) references Usuario(id_Usuario),
);
create table Usuarios(
id_Usuarios int primary key not null,
Nombre varchar(160) not null,
id_Administrador_Sistema int not null,
id_Administrador_Servicio int not null,
id_Usuario int not null,
foreign key (id_Administrador_Sistema) references Administrador_Sistema (id_Administrador_Sistema), 
foreign key (id_Administrador_Servicio) references Administrador_Servicio (id_Administrador_Servicio), 
foreign key (id_Usuario) references Usuario (id_Usuario)
);

