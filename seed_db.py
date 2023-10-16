from models import SessionLocal,Instro, Purpose, Base, engine




instroList = [('sg','case',2330),
              ['tc','rotor',2331]]

purposeList = ['Safety','Analytical Correlation','Mapping']

purposeitems = [Purpose(purpose = x) for x in purposeList]    
instroitems = [Instro(type=x[0],part = x[1], masterNumber = x[2]) for x in instroList]

with SessionLocal() as session:
    
    Base.metadata.create_all(engine) 
    
    
    session.add_all(purposeitems)
    session.add_all(instroitems)
    session.commit()
        