use Practica2_201800526

create table Tiendas(
id_Tiendas int primary key not null,
Municipio varchar(160) null,
Departamento varchar(160) null,
Direccion varchar(160) null,
Encargado varchar(160) null,
Telefono int not null
);
create table Empleados(
CUI int primary key not null,
Nombre varchar(160) not null,
Apellido varchar(160) not null,
Telefono int not null,
Puesto varchar(160) not null,
Fecha_inicio date not null,
Fecha_fin date null,
Hora_inicio time not null,
Hora_fin time null,
id_Tiendas int not null,
Jefe varchar(160) null,
Password varchar(160) not null,
foreign key (id_Tiendas) references Tiendas(id_Tiendas)
);
create table Producto(
id_Producto int primary key not null,
Categoria  varchar(160) not null,
Existencias  int not null,
Marca varchar(160) not null,
Precio  float not null,
tamanio  float not null, --Se refiere a libras
Fecha_vencimiento date not null,
id_Tiendas int not null,
foreign key (id_Tiendas) references Tiendas(id_Tiendas)
);
