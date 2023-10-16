from pydantic import BaseModel

class InstroBase(BaseModel):
    id: int
    type: str
    dataRange: str | None = None
    part: str
    masterNumber:int
    unit: str | None = None
    r: float | None = None
    theta: float | None = None
    z: float | None = None
    
    class Config:
        orm_mode = True
    
class PurposeBase(BaseModel):
    id: int
    purpose: str

    orm_mode = True 
    
class IntroPurposeBase(BaseModel):
    id: int
    
    orm_mode = True

    