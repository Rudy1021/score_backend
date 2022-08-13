from flask import Flask, request, jsonify
from database import db_session, init_db
from models.score import Score
from sqlalchemy import desc
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)
init_db()


@app.route("/GetStudents", methods=["GET"])
def GetStudents():
    Students = {}
    res = Score.query.all()
    temp = []
    for x in res:
        temp.append(x.to_json())
    return jsonify(object=temp)


'''
    for user in AllScore:
        student = {'Name': user.Name,
                   'Score1_name': user.Score1_name,
                   'Score1_score': user.Score1_score,
                   'Score2_name': user.Score2_name,
                   'Score2_score': user.Score2_score,
                   'Score3_name': user.Score3_name,
                   'Score3_score': user.Score3_score,
                   'Score4_name': user.Score4_name,
                   'Score4_score': user.Score4_score,
                   'Score5_name': user.Score5_name,
                   'Score5_score': user.Score5_score}
    Students.update(student)
'''


@app.route("/GetStudent/<name>", methods=["GET"])
def GetStudent(name):
    d_query = Score.query.get(name)
    student = {'Name': d_query.Name,
               'Score1_name': d_query.Score1_name,
               'Score1_score': d_query.Score1_score,
               'Score2_name': d_query.Score2_name,
               'Score2_score': d_query.Score2_score,
               'Score3_name': d_query.Score3_name,
               'Score3_score': d_query.Score3_score,
               'Score4_name': d_query.Score4_name,
               'Score4_score': d_query.Score4_score,
               'Score5_name': d_query.Score5_name,
               'Score5_score': d_query.Score5_score}
    return jsonify(student)


@app.route("/Upload", methods=["POST"])
def UploadScore():
    uploadStudent = request.get_json()
    if 'Score4_name' in uploadStudent:
        if 'Score5_name' not in uploadStudent:
            uploadStudent['Score5_name'] = 'none'
            uploadStudent['Score5_score'] = 'none'
    else:
        uploadStudent['Score4_name'] = 'none'
        uploadStudent['Score4_score'] = 'none'
        uploadStudent['Score5_name'] = 'none'
        uploadStudent['Score5_score'] = 'none'
    StudentScore = Score(
        Name=uploadStudent['Name'],
        Score1_name=uploadStudent['Score1_name'],
        Score1_score=uploadStudent['Score1_score'],
        Score2_name=uploadStudent['Score2_name'],
        Score2_score=uploadStudent['Score2_score'],
        Score3_name=uploadStudent['Score3_name'],
        Score3_score=uploadStudent['Score3_score'],
        Score4_name=uploadStudent['Score4_name'],
        Score4_score=uploadStudent['Score4_score'],
        Score5_name=uploadStudent['Score5_name'],
        Score5_score=uploadStudent['Score5_score']
    )
    db_session.add(StudentScore)
    db_session.commit()
    return "001"


@app.route("/UpdateStudent/<name>", methods=["POST"])
def UpdateStudent(name):
    updateStudent = request.get_json()
    d_query = Score.query.get(name)
    for i in editStudent.keys():
        setattr(d_query, i, editStudent[i])
    db_session.commit()
    return '001'


@app.route("/DelStudent/<name>", methods=["POST"])
def DelStudent(name):
    d_query = Score.query.get(name)
    db_session.delete(d_query)
    db_session.commit()
    return '001'


# Run App
if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5555,
        debug=True
    )
