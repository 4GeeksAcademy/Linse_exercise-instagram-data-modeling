import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String , Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    firstname= Column(String(250), nullable=False)
    lastname =  Column(String(250), nullable=False)
    email= Column(String(250), nullable=False)
    
class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
   
    user_from_id= Column (Integer, primary_key=True, nullable=False  )
    user_to_id= Column(Integer , ForeignKey('user.id')  ,nullable=False)
    user = relationship('user')




class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer ,  nullable=False)
    user = relationship('user')
    comment = relationship('comment')
    media = relationship('media')
    comment_id = Column(String, ForeignKey('user.id')  ,nullable=False)




class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.

    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(Enum ,  nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, primary_key=True, nullable=False)
    user = relationship('user')
    comment = relationship('comment')
   
    media_id = Column(String, ForeignKey('post.id')  ,nullable=False)


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.

    id = Column(Integer, primary_key=True, nullable=False)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, primary_key=True, nullable=False)
    post_id = Column(Integer, primary_key=True, nullable=False)
    user = relationship('user')
    comment = relationship('comment')
    post = relationship('post')
    post_id = Column(String, ForeignKey('post.id')  ,nullable=False)



    comment_id = Column(String, ForeignKey('user.id')  ,nullable=False)






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
