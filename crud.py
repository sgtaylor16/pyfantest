from sqlalchemy import select
from models import SessionLocal, Instro


def getAllInstros():
    with SessionLocal() as session:
        myselection = select(Instro)
        return session.scalars(myselection).all()
    
def getInstroByMN(mn:int):
    with SessionLocal() as session:
        myselection = select(Instro).where(Instro.masterNumber == mn)
        return session.scalar(myselection)