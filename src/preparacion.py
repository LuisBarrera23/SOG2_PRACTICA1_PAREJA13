import pandas as pd
import mysql.connector

# Cargar los datos del archivo CSV
df = pd.read_csv('src/ventas_tienda_online.csv')

# Verificar valores faltantes
print("Valores faltantes antes de la limpieza:\n", df.isnull().sum())

# Verificar duplicados
print("Duplicados antes de la limpieza: ", df.duplicated().sum())

# Eliminar duplicados
df = df.drop_duplicates()

# Eliminar filas con valores faltantes
df = df.dropna()

# Verificar nuevamente después de la limpieza
print("Valores faltantes después de la limpieza:\n", df.isnull().sum())
print("Duplicados después de la limpieza: ", df.duplicated().sum())

# Asegurar que los tipos de datos son correctos
df['order_id'] = df['order_id'].astype(int)
df['purchase_date'] = pd.to_datetime(df['purchase_date'])
df['customer_id'] = df['customer_id'].astype(int) 
df['customer_gender'] = df['customer_gender'].astype(str) 
df['customer_age'] = df['customer_age'].astype(int) 
df['product_category'] = df['product_category'].astype(str) 
df['product_name'] = df['product_name'].astype(str) 
df['product_price'] = df['product_price'].astype(float)
df['quantity'] = df['quantity'].astype(int)
df['order_total'] = df['order_total'].astype(float)
df['payment_method'] = df['payment_method'].astype(str) 
df['shipping_region'] = df['shipping_region'].astype(str)

# Verificar que los tipos de datos se han convertido correctamente
print(df.dtypes)

# Conectar a la base de datos MySQL en GCP
conexion = mysql.connector.connect(
    host="34.172.242.238", 
    user="root",        
    password="gerenciales13",  
    database="practica13" 
)

cursor = conexion.cursor()

# Truncar la tabla antes de insertar los nuevos datos
cursor.execute("TRUNCATE TABLE ventas")

# Preparar la consulta SQL para insertar los datos en la tabla
sql = """
INSERT INTO ventas (id_orden, fecha_compra, id_cliente, genero_cliente, edad_cliente, 
                    categoria_producto, nombre_producto, precio_producto, cantidad_comprada, 
                    total_orden, metodo_pago, region_envio) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Convertir los datos en una lista de tuplas para la inserción por lotes
data = [
    (
        row['order_id'], 
        row['purchase_date'], 
        row['customer_id'], 
        row['customer_gender'], 
        row['customer_age'], 
        row['product_category'], 
        row['product_name'], 
        row['product_price'], 
        row['quantity'], 
        row['order_total'], 
        row['payment_method'], 
        row['shipping_region']
    ) 
    for _, row in df.iterrows()
]

# Insertar todos los datos en un solo lote
cursor.executemany(sql, data)

# Confirmar los cambios en la base de datos
conexion.commit()

# Cerrar la conexión
cursor.close()
conexion.close()

print("Datos cargados exitosamente en la base de datos.")
