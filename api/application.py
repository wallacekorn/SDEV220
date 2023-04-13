# -*- coding: utf-8 -*-
"""
Created: Wed Apr 12 15:06:28 2023
Author: David Amon
Class: SDEV220 Spring 2023

Program Name: application.py
Program Description: CRUD API for Books
"""
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# db configuration selection.  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# instance of SQLAlchemy stored in a variable
db = SQLAlchemy(app) 

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publisher = db.Column(db.String(50))
 
    def __repr__(self): # representation when trying to print Book object in a list
        return f"{self.book_name} by {self.author}. Published by {self.publisher}."

@app.route('/') # creates an endpoint
def index():
    return 'Hello World! (Arbitrary Landing Page?)'

@app.route('/books') # creates an endpoint to store books
def get_books():
    books = Book.query.all() # stores all books objects into a variable
    output = []
    for book in books: # loop iterates over the query and adds all entries to output
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {"books" : output} # returns the formatted query list

@app.route('/books', methods=['POST']) # endpoint for POST on /books -- CREATE
def add_book():
    book = Book(book_name=request.json['book_name'], 
                  author=request.json['author'],
                  publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return{'id': book.id}

@app.route('/books/<id>', methods=['GET']) # endpoint for GET on /books -- READ
def get_book(id):
    book = Book.query.get_or_404(id) # this either GET's or returns 404 if not found
    return {"book_name": book.book_name, "author": book.author, 'publisher': book.publisher}

@app.route('/books/<id>', methods=['PUT']) # endpoint for PUT on /books -- UPDATE
def update_book(id):
    book = Book.query.get_or_404(id)
    book.book_name = request.json['book_name']
    book.author = request.json['author']
    book.publisher = request.json['publisher']
    db.session.commit()
    return{'message': "Book updated Successfully"}

@app.route('/books/<id>', methods=['DELETE']) # endpoint for DELETE on /books -- DELETE
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "Nothing found to delete"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Item found and deleted"}