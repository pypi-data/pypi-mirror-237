import pathlib, os
data_path = pathlib.Path(__file__).parent / "data"
DATA_DIR = str(data_path)
SQLITE_PATH = str(data_path / "pgadmin4.db")


os.environ['PGADMIN_SETUP_PASSWORD'] =  'admin123'
os.environ['PGADMIN_SETUP_EMAIL'] ='admin@example.com'