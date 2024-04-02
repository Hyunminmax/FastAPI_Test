# models.py - 데이터베이스 테이블 컬럼 정의와 같다.
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database   import Base

# User(테이블)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    items = relationship("Item", back_populates='owner') # reverse_accessor => _set 이것은 장고용.

# Item(테이블)
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    # owner =  다른 테이블에서 유저를 부를 때 보편적으로 쓰는 말.
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates = 'items')