import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(15), nullable=False)
    apellido = Column(String(15), nullable=False)
    email = Column(String(20), unique=True, nullable=False)
    password =  Column(String(10), nullable=False)
    favoritos= relationship('Favoritos', back_populates="usuario", cascade="all, delete-orphan")
    

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(20),unique=True, nullable=False)
    clima = Column(String(50), nullable=False)
    residentes = Column(String(50), nullable=False)
    url = Column(String(50),unique=True, nullable=False)
    personajes = relationship('Personaje', back_populates='planeta_origen')
    favoritos= relationship('Favoritos')


class Personaje(Base):
    __tablename__ ='personaje'
    id = Column(Integer, primary_key=True)
    nombre= Column(String(50), nullable=False)
    especie= Column(String(50), nullable=False)
    genero= Column(String(50), nullable=False)
    planeta_origen_id= Column (Integer, ForeignKey(Planeta.id))
    planeta_origen = relationship('Planeta', back_populates='personajes')


class Favoritos(Base):
    __tablename__='favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id= Column(Integer, ForeignKey('usuario.id'), nullable=False)
    tipo= Column(String(50), nullable=False)
    elemento_id= Column(Integer, nullable=False)
    usuario= relationship('Usuario', back_populates='favoritos')
    planetas = relationship('Planeta', back_populates='favoritos')




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
