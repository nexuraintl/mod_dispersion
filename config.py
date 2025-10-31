import os

if os.getenv("ENVIRONMENT") == "local":
    # Configuración para base de datos local
    MYSQL_CONFIG = {
        'host': os.getenv('DB_HOST', '127.0.0.1'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'root'),
        'database': os.getenv('DB_NAME', 'Root1234!'),
    }
else:
    # Configuración para Cloud SQL en Cloud Run
    MYSQL_CONFIG = {
        'unix_socket': f"/cloudsql/{os.environ['INSTANCE_CONNECTION_NAME']}",
        'user': os.environ['DB_USER'],
        'password': os.environ['DB_PASSWORD'],
        'database': os.environ['DB_NAME'],
    }