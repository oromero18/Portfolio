from sqlalchemy import create_engine, text
# Configuración de conexión
usuario = 'root'
contraseña = '******' #Se oculta la contraseña
host = 'localhost'
base_de_datos = 'busmx_db'

# 1. Conectar al servidor MySQL sin especificar la base de datos
engine_temp = create_engine(f"mysql+mysqlconnector://{usuario}:{contraseña}@{host}/")

# 2. Crear la base de datos si no existe
with engine_temp.connect() as conexion:
    conexion.execute(text(f"CREATE DATABASE IF NOT EXISTS {base_de_datos}"))
    conexion.commit()

# 3. Conectar a la base de datos específica
engine = create_engine(f"mysql+mysqlconnector://{usuario}:{contraseña}@{host}/{base_de_datos}")

# Verificación
print("¡Conexión exitosa!")
with engine.connect() as test_con:
    test_con.execute(text("SELECT 1"))
print("Base de datos operativa")