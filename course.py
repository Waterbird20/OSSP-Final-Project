#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Database URL : https://rpyy83l3r1.execute-api.ap-northeast-2.amazonaws.com/dev

Created on Fri Apr 29 13:33:24 2022
@author: hsherlcok
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from flask import Flask
from flask import request
from flask import jsonify
from werkzeug.serving import WSGIRequestHandler
import json

USER = ""
PW = ""
URL = ".ap-northeast-2.rds.amazonaws.com"
PORT = "5432"
DB = "postgres"

# This line is for solving flask's CORS error
# You need 'pip install flask_cors' to use flask_cors
from flask_cors import CORS
from werkzeug.serving import WSGIRequestHandler
import json

WSGIRequestHandler.protocol_version = "HTTP/1.1"

app = Flask(__name__)

# This line is for solving flask's CORS error
CORS(app)

engine = create_engine("postgresql://{}:{}@{}:{}/{}".format(USER, PW, URL, PORT, DB))
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class course(Base):
    __tablename__ = 'courses'
    course_id = Column(String(50), primary_key=True)
    course_name = Column(String(50), unique=True)
    professor = Column(String(50), unique=True)
    tutor = Column(String(50), unique=True)
    tutee = Column(String(200), unique=True)

    def __init__(self, course_id=None, course_name=None, professor=None, tutor=None, tutee=None):
        self.course_id = course_id
        self.course_name = course_name
        self.professor = professor
        self.tutor = tutor
        self.tutee = tutee

    def __repr__(self):
        return f'<course {self.course_id!r}>'


# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

WSGIRequestHandler.protocol_version = "HTTP/1.1"

#app = Flask(__name__)


@app.route("/addcourse", methods=['POST'])
def add_Course():
    content = request.get_json(silent=True)
    course_id = content["id"]
    course_name = content["name"]
    professor = content["professor"]
    tutor = content["tutor"]
    tutee = content["tutee"]

    if db_session.query(course).filter_by(course_id=course_id).first() is None:
        c = course(course_id=course_id, course_name=course_name, professor=professor,tutor=tutor,tutee=tutee)
        db_session.add(c)
        db_session.commit()
        return jsonify(success=True)
    else:
        return jsonify(success=False)


@app.route("/getcourse", methods=['POST'])
def get_Course():
    content = request.get_json(silent=True)
    course_id = content["id"]
    output = {}
    check = False
    result = db_session.query(course).all()

    for i in result:
        if i.course_id == course_id:
            check = True
            output["course_id"] = i.course_id
            output["course_name"] = i.course_name
            output["professor"] = i.professor
            output["tutee"] = i.tutee
            output["tutor"] = i.tutor
            break

    if(check):
        return jsonify(output)
    else:
        return jsonify(success=check)


@app.route("/getallcourse", methods=['GET'])
def get_Allcourse():
    output = {}
    result = db_session.query(course).all()

    for i in result:
        check = True
        temp = {}
        course_id = i.course_id
        temp["id"] = i.course_id
        temp["name"] = i.course_name
        temp["professor"] = i.professor
        temp["tutee"] = i.tutee
        temp["tutor"] = i.tutor
        if course_id in output:
            continue
        else:
            output[course_id] = temp

    if(check):
        return jsonify(output)
    else:
        return jsonify(success=check)



@app.route("/addtutee", methods=['POST'])
def add_tutee():
    content = request.get_json(silent=True)
    course_id = content["id"]
    newtutee = content["tutee"]
    check = False

    result = db_session.query(course).all()

    for i in result:
        if i.course_id == course_id:
            currentTutee = StrToArray(i.tutee)
            if newtutee in currentTutee:
                break
            elif len(currentTutee) > 5:
                break
            else:
                check = True
                currentTutee.append(newtutee)
                i.tutee = str(currentTutee)
                db_session.commit()
                break
    return jsonify(success = check)

def StrToArray(Str):
    temp = Str.strip("{""}"" ")
    Arr = temp.split(",")
    return Arr

@app.route("/test", methods=['GET'])
def test():
    return jsonify(success=True)

@app.route("/delete", methods=['POST'])
def delete_all():
    result = db_session.query(course).all()

    for i in result:
        db_session.delete(i)
        db_session.commit()

    check= True

    return jsonify(success = check)



if __name__ == "__main__":
    app.run(host='localhost', port=8888)