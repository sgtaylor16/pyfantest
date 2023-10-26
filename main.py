
from graphene import ObjectType, String, Int, Float, Field,List, Schema

from fastapi import FastAPI, Depends, HTTPException
from starlette_graphene3 import GraphQLApp, make_graphiql_handler, make_playground_handler
from models import Instro
from crud import getAllInstros, getInstroByMN

from starlette.applications import Starlette
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from database import SessionLocal

app = FastAPI(title="ContactQL",description='GraphQL Contact APIs',version='0.1')

#Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
  

#Graphene setup
class InstroQL(ObjectType):
    type = String()
    dataRange = String()
    part = String()
    masterNumber = Int()
    unit = String()
    r = Float()
    theta= Float()
    z = Float()

    
    
class Query(ObjectType):
    instros = List(InstroQL)
    instro = Field(InstroQL,masterNumber=Int(required=True))
    
    def resolve_instros(parent,info):
        return getAllInstros()
        
    def resolve_instro(parent,info,masterNumber):
        return getInstroByMN(masterNumber)
    

app = Starlette()

schema = Schema(query=Query)

app.mount("/", GraphQLApp(schema, on_get=make_graphiql_handler()))
    







