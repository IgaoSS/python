# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0301
from sqlalchemy import Column, String, BIGINT, REAL, INT
from src.models.sqlite.settings.base import Base

class NaturalPersonTable(Base):
    __tablename__ = "pessoa_fisica"
    id = Column(BIGINT, primary_key=True)
    renda_mensal = Column(REAL, nullable=False)
    idade = Column(INT, nullable=False)
    nome_completo = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return f"pessoa_fisica [nome_completo={self.nome_completo}, celular={self.celular}, categoria={self.categoria}, renda_mensal={self.renda_mensal}, saldo={self.saldo}]"