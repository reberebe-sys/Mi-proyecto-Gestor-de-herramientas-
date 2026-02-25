from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List, Optional
import datetime

# Configuración de Base de Datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./herramientas.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelos de DB
class ToolModel(Base):
    __tablename__ = "tools"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    current_uses = Column(Integer, default=0)
    max_uses = Column(Integer)

class UsageLog(Base):
    __tablename__ = "usage_logs"
    id = Column(Integer, primary_key=True, index=True)
    tool_id = Column(Integer, ForeignKey("tools.id"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    action = Column(String) # 'USE', 'CREATE', 'MAINTENANCE'

Base.metadata.create_all(bind=engine)

# Esquemas Pydantic
class ToolBase(BaseModel):
    name: str
    location: str
    max_uses: int

class ToolCreate(ToolBase):
    pass

class Tool(ToolBase):
    id: int
    current_uses: int
    class Config:
        orm_mode = True

app = FastAPI(title="Gestor de Herramientas v2.0")

# Dependencia DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/tools", response_model=List[Tool])
def get_tools(db: Session = Depends(get_db)):
    return db.query(ToolModel).all()

@app.post("/api/tools", response_model=Tool)
def create_tool(tool: ToolCreate, db: Session = Depends(get_db)):
    db_tool = ToolModel(**tool.dict())
    db.add(db_tool)
    db.commit()
    db.refresh(db_tool)
    
    # Log creation
    log = UsageLog(tool_id=db_tool.id, action="CREATE")
    db.add(log)
    db.commit()
    
    return db_tool

@app.put("/api/tools/{tool_id}/use")
def use_tool(tool_id: int, db: Session = Depends(get_db)):
    db_tool = db.query(ToolModel).filter(ToolModel.id == tool_id).first()
    if not db_tool:
        raise HTTPException(status_code=404, detail="No encontrada")
    
    if db_tool.current_uses < db_tool.max_uses:
        db_tool.current_uses += 1
        log = UsageLog(tool_id=tool_id, action="USE")
        db.add(log)
        db.commit()
        db.refresh(db_tool)
        return db_tool
    
    raise HTTPException(status_code=400, detail="Vida útil agotada")

@app.put("/api/tools/{tool_id}/maintenance")
def maintenance_tool(tool_id: int, db: Session = Depends(get_db)):
    db_tool = db.query(ToolModel).filter(ToolModel.id == tool_id).first()
    if not db_tool:
        raise HTTPException(status_code=404, detail="No encontrada")
    
    db_tool.current_uses = 0
    log = UsageLog(tool_id=tool_id, action="MAINTENANCE")
    db.add(log)
    db.commit()
    db.refresh(db_tool)
    return db_tool

@app.delete("/api/tools/{tool_id}")
def delete_tool(tool_id: int, db: Session = Depends(get_db)):
    db_tool = db.query(ToolModel).filter(ToolModel.id == tool_id).first()
    if db_tool:
        db.delete(db_tool)
        db.commit()
    return {"message": "Eliminada"}

@app.get("/api/tools/{tool_id}/history")
def get_history(tool_id: int, db: Session = Depends(get_db)):
    return db.query(UsageLog).filter(UsageLog.tool_id == tool_id).order_by(UsageLog.timestamp.desc()).limit(10).all()

# Servir estáticos
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
