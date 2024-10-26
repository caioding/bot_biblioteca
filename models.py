from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Autor(Base):
    __tablename__ = "autor"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    livros = relationship("Livro", back_populates="autor")

class Livro(Base):
    __tablename__ = "livro"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    codigo = Column(String(20), nullable=False)
    emprestimo_disponivel = Column(Boolean, default=True, nullable=False)
    autor_id = Column(Integer, ForeignKey("autor.id"))

    autor = relationship("Autor", back_populates="livros")
    emprestimos = relationship("Emprestimo", back_populates="livro")

class Biblioteca(Base):
    __tablename__ = "biblioteca"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

class Emprestimo(Base):
    __tablename__ = "emprestimo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    livro_id = Column(Integer, ForeignKey("livro.id"))
    cliente = Column(String(100), nullable=False)
    data_emprestimo = Column(Date, nullable=False)
    data_devolucao = Column(Date)

    livro = relationship("Livro", back_populates="emprestimos")