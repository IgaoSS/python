# pylint: disable=C0114,C0115,C0116,W0703,C0209,E0015,C0304,C0301
from sqlalchemy import Column, BIGINT, String, REAL, INT
from src.models.sqlite.settings.base import Base

class JuridicPersonTable(Base):
    __tablename__ = "pessoa_juridica"
    id = Column(BIGINT, primary_key=True)
    faturamento = Column(REAL, nullable=False)
    idade = Column(INT, nullable=False)
    nome_fantasia = Column(String, nullable=False)
    celular = Column(String, nullable=False)
    email_corporativo = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return f"pessoa_juridica [nome_fantasia={self.nome_fantasia}, email_corporativo={self.email_corporativo}, celular={self.celular}, faturamento={self.faturamento}, categoria={self.categoria}, saldo={self.saldo}]"