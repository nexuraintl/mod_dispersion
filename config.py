import os

if os.getenv("ENVIRONMENT") == "local":
    # Configuración para base de datos local
    MYSQL_CONFIG = {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME'),
    }
else:
    # Configuración para Cloud SQL en Cloud Run
    MYSQL_CONFIG = {
        'unix_socket': f"/cloudsql/{os.environ['INSTANCE_CONNECTION_NAME']}",
        'user': os.environ['DB_USER'],
        'password': os.environ['DB_PASSWORD'],
        'database': os.environ['DB_NAME'],
    }