from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
    )

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class Tool(Base):
    __tablename__ = 'tool'
    id = Column(Integer, primary_key=True)
    stat_id = Column(Integer, ForeignKey('stats.id'))
    name = Column(Text)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value

class Stat(Base):
    __tablename__ = 'stats'
    id = Column(Integer, primary_key=True)
    tools = relationship(Tool, backref="session")

    def __init__(self, tools):
        _tools = []
        for t in tools:
            _tools.append(Tool(t, int(tools[t])))
        self.tools = _tools
