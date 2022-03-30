from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import func, desc
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)

# def most_frequent_answer(q, id):
#     if id == 1:
#         return Questions.query.get(q).ans1
#     elif id == 2:
#         return Questions.query.get(q).ans2
#     else:
#         return Questions.query.get(q).ans3


# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True)
#     gender = db.Column(db.Text)
#     education = db.Column(db.Text)
#     age = db.Column(db.Integer)

# class Results(db.Model):
#     __tablename__ = 'results'
#     id = db.Column(db.Integer, primary_key=True)
#     personality = db.Column(db.Text)

# class Questions(db.Model):
#     __tablename__ = 'questions'
#     question_id = db.Column(db.Integer, primary_key=True)
#     text = db.Column(db.Text)
#     ans1 = db.Column(db.Text)
#     ans2 = db.Column(db.Text)
#     ans3 = db.Column(db.Text)

# class Answers(db.Model):
#     __tablename__ = 'answers'
#     id = db.Column(db.Integer, primary_key=True)
#     q1 = db.Column(db.Integer)
#     q2 = db.Column(db.Integer)
#     q3 = db.Column(db.Integer)
#     q4 = db.Column(db.Integer)
#     q5 = db.Column(db.Integer)
#     q6 = db.Column(db.Integer)
#     q7 = db.Column(db.Integer)
#     q8 = db.Column(db.Integer)
#     q9 = db.Column(db.Integer)
#     q10 = db.Column(db.Integer)
#     q11 = db.Column(db.Integer)
#     q12 = db.Column(db.Integer)

# db.create_all()

@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template("mainbody.html")

@app.route('/grafs.html', methods=['GET', 'POST'])
def calculus():
    return render_template("grafs.html")


@app.route('/description.html', methods=['GET', 'POST'])
def biography():
    return render_template("description.html")


if __name__ == '__main__':
    app.run()