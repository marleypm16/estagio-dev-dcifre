from db import engine
from empresa_model import Base


Base.metadata.create_all(bind=engine)
