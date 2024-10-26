from fastapi import FastAPI, Depends, Request, Form, status, HTTPException
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    autores = db.query(models.Autor).all()
    livros = db.query(models.Livro).filter(models.Livro.emprestimo_disponivel == True).all()
    bibliotecas = db.query(models.Biblioteca).all()
    emprestimos = db.query(models.Emprestimo).all()
    return templates.TemplateResponse("base.html", {
        "request": request,
        "autores": autores,
        "livros": livros,
        "bibliotecas": bibliotecas,
        "emprestimos": emprestimos
    })

# Autor CRUD
@app.post("/add_autor")
def add_autor(nome: str = Form(...), db: Session = Depends(get_db)):
    new_autor = models.Autor(nome=nome)
    db.add(new_autor)
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)

@app.get("/autores")
def get_autores(db: Session = Depends(get_db)):
    return db.query(models.Autor).all()

@app.put("/update_autor/{autor_id}")
def update_autor(autor_id: int, nome: str = Form(...), db: Session = Depends(get_db)):
    autor = db.query(models.Autor).filter(models.Autor.id == autor_id).first()
    if not autor:
        raise HTTPException(status_code=404, detail="Autor not found")
    autor.nome = nome
    db.commit()
    return {"message": "Autor updated successfully"}

@app.delete("/delete_autor/{autor_id}")
def delete_autor(autor_id: int, db: Session = Depends(get_db)):
    autor = db.query(models.Autor).filter(models.Autor.id == autor_id).first()
    if not autor:
        raise HTTPException(status_code=404, detail="Autor not found")
    db.delete(autor)
    db.commit()
    return {"message": "Autor deleted successfully"}

# Livro CRUD
@app.post("/add_livro")
def add_livro(titulo: str = Form(...), codigo: str = Form(...), autor_id: int = Form(...), db: Session = Depends(get_db)):
    new_livro = models.Livro(titulo=titulo, codigo=codigo, autor_id=autor_id)
    db.add(new_livro)
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)

@app.get("/livros")
def get_livros(db: Session = Depends(get_db)):
    return db.query(models.Livro).all()

@app.put("/update_livro/{livro_id}")
def update_livro(livro_id: int, titulo: str = Form(...), codigo: str = Form(...), autor_id: int = Form(...), db: Session = Depends(get_db)):
    livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro not found")
    livro.titulo = titulo
    livro.codigo = codigo
    livro.autor_id = autor_id
    db.commit()
    return {"message": "Livro updated successfully"}

@app.delete("/delete_livro/{livro_id}")
def delete_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    if not livro:
        raise HTTPException(status_code=404, detail="Livro not found")
    db.delete(livro)
    db.commit()
    return {"message": "Livro deleted successfully"}

# Biblioteca CRUD
@app.post("/add_biblioteca")
def add_biblioteca(nome: str = Form(...), db: Session = Depends(get_db)):
    new_biblioteca = models.Biblioteca(nome=nome)
    db.add(new_biblioteca)
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)

@app.get("/bibliotecas")
def get_bibliotecas(db: Session = Depends(get_db)):
    return db.query(models.Biblioteca).all()

@app.put("/update_biblioteca/{biblioteca_id}")
def update_biblioteca(biblioteca_id: int, nome: str = Form(...), db: Session = Depends(get_db)):
    biblioteca = db.query(models.Biblioteca).filter(models.Biblioteca.id == biblioteca_id).first()
    if not biblioteca:
        raise HTTPException(status_code=404, detail="Biblioteca not found")
    biblioteca.nome = nome
    db.commit()
    return {"message": "Biblioteca updated successfully"}

@app.delete("/delete_biblioteca/{biblioteca_id}")
def delete_biblioteca(biblioteca_id: int, db: Session = Depends(get_db)):
    biblioteca = db.query(models.Biblioteca).filter(models.Biblioteca.id == biblioteca_id).first()
    if not biblioteca:
        raise HTTPException(status_code=404, detail="Biblioteca not found")
    db.delete(biblioteca)
    db.commit()
    return {"message": "Biblioteca deleted successfully"}

# Emprestimo CRUD
@app.post("/add_emprestimo")
def add_emprestimo(livro_id: int = Form(...), cliente: str = Form(...), data_emprestimo: str = Form(...), db: Session = Depends(get_db)):
    new_emprestimo = models.Emprestimo(livro_id=livro_id, cliente=cliente, data_emprestimo=data_emprestimo)
    db.add(new_emprestimo)
    # Atualizar a disponibilidade do livro
    livro = db.query(models.Livro).filter(models.Livro.id == livro_id).first()
    livro.emprestimo_disponivel = False
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)

@app.get("/emprestimos")
def get_emprestimos(db: Session = Depends(get_db)):
    return db.query(models.Emprestimo).all()

@app.put("/update_emprestimo/{emprestimo_id}")
def update_emprestimo(emprestimo_id: int, livro_id: int = Form(...), cliente: str = Form(...), data_emprestimo: str = Form(...), data_devolucao: str = Form(None), db: Session = Depends(get_db)):
    emprestimo = db.query(models.Emprestimo).filter(models.Emprestimo.id == emprestimo_id).first()
    if not emprestimo:
        raise HTTPException(status_code=404, detail="Emprestimo not found")
    emprestimo.livro_id = livro_id
    emprestimo.cliente = cliente
    emprestimo.data_emprestimo = data_emprestimo
    emprestimo.data_devolucao = data_devolucao
    db.commit()
    return {"message": "Emprestimo updated successfully"}

@app.delete("/delete_emprestimo/{emprestimo_id}")
def delete_emprestimo(emprestimo_id: int, db: Session = Depends(get_db)):
    emprestimo = db.query(models.Emprestimo).filter(models.Emprestimo.id == emprestimo_id).first()
    if not emprestimo:
        raise HTTPException(status_code=404, detail="Emprestimo not found")
    # Atualizar a disponibilidade do livro
    livro = db.query(models.Livro).filter(models.Livro.id == emprestimo.livro_id).first()
    livro.emprestimo_disponivel = True
    db.delete(emprestimo)
    db.commit()
    return {"message": "Emprestimo deleted successfully"}