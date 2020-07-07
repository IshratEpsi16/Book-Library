
import sqlite3
#connecting the db
def connect():      
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)") # here id will automatic assign 1,2... numbers
    
    conn.commit()
    conn.close()

#Add Entry
def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn)) 
    conn.commit()
    conn.close()
#View All
def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book") 
    rows=cur.fetchall()
    conn.close()
    return rows

#Search
def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?" ,(title,author,year,isbn)) 
    rows=cur.fetchall()
    conn.close()
    return rows

#delete
def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=? ",(id,)) 
    #rows=cur.fetchall()
    conn.commit()
    conn.close()
    #return rows
#update
def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=? ",(title,author,year,isbn,id)) 
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()

#insert("The ice","Jon Snow",2008,12233345)
#delete(2)
#update(2,"The moon",'Stark',1998,23456)
#print(view())

#print(search(author="Jon Snow"))



