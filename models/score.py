from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
import datetime
import uuid


class Score(Base):
    __tablename__ = 'student'
    Name = Column(String(50), nullable=False, primary_key=True)
    Score1_name = Column(String(50), nullable=False)
    Score1_score = Column(String(50), nullable=False)
    Score2_name = Column(String(50), nullable=False)
    Score2_score = Column(String(50), nullable=False)
    Score3_name = Column(String(50), nullable=False)
    Score3_score = Column(String(50), nullable=False)
    Score4_name = Column(String(50), nullable=True)
    Score4_score = Column(String(50), nullable=True)
    Score5_name = Column(String(50), nullable=True)
    Score5_score = Column(String(50), nullable=True)

    def __init__(self, Name, Score1_name, Score1_score,
                 Score2_name, Score2_score,
                 Score3_name, Score3_score,
                 Score4_name, Score4_score,
                 Score5_name, Score5_score):
        self.Name = Name
        self.Score1_name = Score1_name
        self.Score1_score = Score1_score
        self.Score2_name = Score2_name
        self.Score2_score = Score2_score
        self.Score3_name = Score3_name
        self.Score3_score = Score3_score
        self.Score4_name = Score4_name
        self.Score4_score = Score4_score
        self.Score5_name = Score5_name
        self.Score5_score = Score5_score

    def to_json(self):
        return {
            'Name': self.Name,
            'Score1_name': self.Score1_name,
            'Score1_score': self.Score1_score,
            'Score2_name': self.Score2_name,
            'Score2_score': self.Score2_score,
            'Score3_name': self.Score3_name,
            'Score3_score': self.Score3_score,
            'Score4_name': self.Score4_name,
            'Score4_score': self.Score4_score,
            'Score5_name': self.Score5_name,
            'Score5_score': self.Score5_score
        }
