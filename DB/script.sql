use practica13;

CREATE TABLE ventas (
    id_orden INT NOT NULL,
    fecha_compra DATE NOT NULL,
    id_cliente INT NOT NULL,
    genero_cliente VARCHAR(10),
    edad_cliente INT,
    categoria_producto VARCHAR(50),
    nombre_producto VARCHAR(100),
    precio_producto DECIMAL(10, 2),
    cantidad_comprada INT,
    total_orden DECIMAL(10, 2),
    metodo_pago VARCHAR(50),
    region_envio VARCHAR(50),
    PRIMARY KEY (id_orden)
);