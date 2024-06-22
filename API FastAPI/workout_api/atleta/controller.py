from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError

from workout_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from workout_api.atleta.models import AtletaModel
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

async def get_categoria(db_session, nome: str):
    return (await db_session.execute(
        select(CategoriaModel).filter_by(nome=nome))
    ).scalars().first()

async def get_centro_treinamento(db_session, nome: str):
    return (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=nome))
    ).scalars().first()

async def get_atleta_by_id(db_session, id: UUID4):
    return (await db_session.execute(
        select(AtletaModel).filter_by(id=id))
    ).scalars().first()

@router.post(
    '/', 
    summary='Criar um novo atleta.',
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut
)
async def post(
    db_session: DatabaseDependency, 
    atleta_in: AtletaIn = Body(...)
):
    categoria = await get_categoria(db_session, atleta_in.categoria.nome)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f'A categoria {atleta_in.categoria.nome} não foi encontrada.'
        )
    
    centro_treinamento = await get_centro_treinamento(db_session, atleta_in.centro_treinamento.nome)
    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f'O centro de treinamento {atleta_in.centro_treinamento.nome} não foi encontrado.'
        )
    
    atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.dict())
    atleta_model = AtletaModel(**atleta_out.dict(exclude={'categoria', 'centro_treinamento'}))
    atleta_model.categoria_id = categoria.pk_id
    atleta_model.centro_treinamento_id = centro_treinamento.pk_id
    
    try:
        db_session.add(atleta_model)
        await db_session.commit()
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail='Ocorreu um erro ao inserir os dados no banco'
        )

    return atleta_out


@router.get(
    '/', 
    summary='Consultar todos os Atletas',
    status_code=status.HTTP_200_OK,
    response_model=list[AtletaOut],
)
async def query(db_session: DatabaseDependency) -> list[AtletaOut]:
    atletas = (await db_session.execute(select(AtletaModel))).scalars().all()
    return [AtletaOut.from_orm(atleta) for atleta in atletas]


@router.get(
    '/{id}', 
    summary='Consulta um Atleta pelo id',
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def get(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta = await get_atleta_by_id(db_session, id)
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Atleta não encontrado no id: {id}'
        )
    
    return AtletaOut.from_orm(atleta)


@router.patch(
    '/{id}', 
    summary='Editar um Atleta pelo id',
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def patch(id: UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta = await get_atleta_by_id(db_session, id)
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Atleta não encontrado no id: {id}'
        )
    
    for key, value in atleta_up.dict(exclude_unset=True).items():
        setattr(atleta, key, value)

    await db_session.commit()
    await db_session.refresh(atleta)

    return AtletaOut.from_orm(atleta)


@router.delete(
    '/{id}', 
    summary='Deletar um Atleta pelo id',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete(id: UUID4, db_session: DatabaseDependency) -> None:
    atleta = await get_atleta_by_id(db_session, id)
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Atleta não encontrado no id: {id}'
        )
    
    await db_session.delete(atleta)
    await db_session.commit()
