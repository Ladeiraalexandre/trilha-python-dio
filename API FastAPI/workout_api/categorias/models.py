from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Datetime, String, Float
from datetime import datetime

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'
    pk_id: Mapped[int] = mapped_column(Integer, primary_Key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')