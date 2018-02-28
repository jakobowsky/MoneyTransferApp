import sqlite3


class Accounts:
    def __init__(self,db): # db = name of our database , in this case name of database with account numbers
        self.conn=sqlite3.connect(db) # connecting to database
        self.cur=self.conn.cursor() # creating cursor
        self.cur.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY , username text, accnr text, money INTEGER)")
        self.conn.commit()

    def insert(self,username,accnr,money):
        self.cur.execute("INSERT INTO accounts VALUES (NULL,?,?,?)",(username,accnr,money))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM accounts")
        rows = self.cur.fetchall()
        return rows

    def update(self,id,username,accnr,money):
        self.cur.execute("UPDATE accounts SET username=?, accnr=?, money=? WHERE id=?",(username,accnr,money,id))
        self.conn.commit()

    def delete(self,id):
        self.cur.execute("DELETE FROM accounts WHERE id=?",(id,))

    def deposit(self,id,money,amount):
        self.cur.execute("UPDATE accounts SET money=? WHERE id=?", (money+amount,id))
        self.conn.commit()
    def withdraw(self,id,money,amount):
        self.cur.execute("UPDATE accounts SET money=? WHERE id=?", (money-amount,id))
        self.conn.commit()

    def transfer(self,id1,money1,amount,id2,money2):
        self.withdraw(id1,money1,amount)
        self.deposit(id2,money2,amount)

    def search(self,id='',username='',accnr=''):
        self.cur.execute('SELECT * FROM accounts WHERE id=? or username=? or accnr=?',(id,username,accnr))
        rows = self.cur.fetchall()
        return rows

    def findID(self,accnr=''):
        self.cur.execute('SELECT * from accounts WHERE accnr=?',(accnr,))
        row = self.cur.fetchall()
        return row[0][0]

    def findMoney(self,accnr=''):
        self.cur.execute('SELECT money from accounts WHERE accnr=?',(accnr,))
        row = self.cur.fetchall()
        return row[0][0]

    def __del__(self):
        self.conn.close()

base=Accounts('konta.db')
#base.insert("Adam","123456789",5000)
#base.insert("Jan","9239283",1200)
#base.insert("Patryk","231456789",300)
#print(base.view())
#base.transfer(1,200,150,2,5000)
#base.update(1,"Jakob Wolitzki","123456789",90)
#base.deposit(1,100,100)
#print(base.search(1))
#print(base.view())
#base.transfer(1,5000,1000,6,8888)
#print(base.view())
#print(base.findMoney('923938'))