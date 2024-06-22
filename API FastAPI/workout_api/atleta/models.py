from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Datetime, String, Float, ForeignKey
from datetime import datetime

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'
    pk_id: Mapped[int] = mapped_column(Integer, primary_Key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(Datetime, nullable=False) #cria relacionamento de atleta com categoria
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.pk_id'))
    centros_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta')
    centros_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centros_treinamento.pk_id'))