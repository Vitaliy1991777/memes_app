from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas

async def get_meme(db: AsyncSession, meme_id: int):
    return await db.get(models.Meme, meme_id)

async def get_memes(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(models.Meme).offset(skip).limit(limit)
    )
    return result.scalars().all()

async def create_meme(db: AsyncSession, meme: schemas.MemeCreate):
    db_meme = models.Meme(text=meme.text, image_url=meme.image_url)
    db.add(db_meme)
    await db.commit()
    await db.refresh(db_meme)
    return db_meme

async def update_meme(db: AsyncSession, meme_id: int, meme: schemas.MemeCreate):
    db_meme = await get_meme(db, meme_id)
    if db_meme:
        db_meme.text = meme.text
        db_meme.image_url = meme.image_url
        await db.commit()
        await db.refresh(db_meme)
    return db_meme

async def delete_meme(db: AsyncSession, meme_id: int):
    db_meme = await get_meme(db, meme_id)
    if db_meme:
        await db.delete(db_meme)
        await db.commit()
    return db_meme
