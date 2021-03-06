from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

bill_legislators = db.Table('bill_legislator',
								db.Column('bill_id', db.Integer, db.ForeignKey('bill.id')),
								db.Column('legislator_id', db.Integer, db.ForeignKey('legislator.legislator_id')))

class Bill(db.Model):
	__tablename__ = "bill"
	id = db.Column(db.Integer, primary_key=True)
	bill_id = db.Column(db.String, unique=True)
	leg_session = db.Column(db.String(10))
	type = db.Column(db.String(32))
	number = db.Column(db.Integer)
	aye_or_nay = db.Column(db.String(64))
	text = db.Column(db.Text(10000000))
	authors = db.relationship("legislator", backref="author")
	sponsors = db.relationship("legislator", backref="sponsor")



class Legislator(db.Model):
	__tablename__ = "legislator"
	legislator_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128))
	filer_id = db.Column(db.Integer)
	bio = db.Column(db.String(100000))
	party = db.Column(db.String(128))
	district = db.Column(db.Integer)
	# contributors = db.ForeignKey()
	# bills = db.ForeignKey()
	contributions = db.relationship('Legislator', backref='legislator', lazy='dynamic')


class Contributor(db.Model):
	__tablename__ = "contributor"
	contributor_id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(16))
	name = db.Column(db.String(256))
	zipcode = db.Column(db.String(32))
	contributions = db.relationship('Contribution', backref='contributor', lazy='dynamic')

class Contribution(db.Model):
	__tablename__ = "contribution"
	contribution_id = db.Column(db.Integer, primary_key=True)
	amount = db.Column(db.Integer)
	date_contributed = db.Column(db.Date)
	contributor_id = db.Column(db.Integer, db.ForeignKey('contributor.id'))
	legislator_id = db.Column(db.Integer, db.ForeignKey('legislator.id'))