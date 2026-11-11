from src.database.db_conexion import obtener_conexion, inicializar_base_de_datos

def probar_conexion():
    conexion = None
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT 1")
        resultado = cursor.fetchone()
        
        if resultado and resultado[0] == 1:
            print("Conexión a la base de datos exitosa.")
            
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        print("Intentando inicializar la base de datos...")
        inicializar_base_de_datos()
    finally:
        if conexion:
            conexion.close()

if __name__ == "__main__":
    probar_conexion()