import pandas as pd
import mysql.connector

# Cargar los datos del archivo CSV
df = pd.read_csv('src/ventas_tienda_online.csv')

# Verificar valores faltantes
print("Valores faltantes:\n", df.isnull().sum())

# Verificar duplicados
print("Duplicados: ", df.duplicated().sum())

# Conectar a la base de datos MySQL en GCP
conexion = mysql.connector.connect(
    host="34.133.24.88", 
    user="root",        
    password="gerenciales13",  
    database="practica13" 
)

cursor = conexion.cursor()

# Preparar la consulta SQL para insertar los datos en la tabla
sql = """
INSERT INTO ventas (id_orden, fecha_compra, id_cliente, genero_cliente, edad_cliente, 
                    categoria_producto, nombre_producto, precio_producto, cantidad_comprada, 
                    total_orden, metodo_pago, region_envio) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for _, row in df.iterrows():
    cursor.execute(sql, (
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
    ))


# Confirmar los cambios en la base de datos
conexion.commit()

# Cerrar la conexión
cursor.close()
conexion.close()

print("Datos cargados exitosamente en la base de datos.")
