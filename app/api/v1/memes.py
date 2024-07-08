from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ... import crud, models, schemas
from ...dependencies import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.Meme])
async def read_memes(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    memes = await crud.get_memes(db, skip=skip, limit=limit)
    return memes

@router.get("/{meme_id}", response_model=schemas.Meme)
async def read_meme(meme_id: int, db: AsyncSession = Depends(get_db)):
    meme = await crud.get_meme(db, meme_id=meme_id)
    if meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return meme

@router.post("/", response_model=schemas.Meme)
async def create_meme(meme: schemas.MemeCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_meme(db=db, meme=meme)

@router.put("/{meme_id}", response_model=schemas.Meme)
async def update_meme(meme_id: int, meme: schemas.MemeCreate, db: AsyncSession = Depends(get_db)):
    return await crud.update_meme(db=db, meme_id=meme_id, meme=meme)

@router.delete("/{meme_id}", response_model=schemas.Meme)
async def delete_meme(meme_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_meme(db=db, meme_id=meme_id)
