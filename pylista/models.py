from pylista.db import Base


class List(Base):
    __tablename__ = "lists"


class Note(Base):
    __tablename__ = "notes"
