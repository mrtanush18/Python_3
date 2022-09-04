from abc import ABC, abstractmethod

class db(ABC):  # interface
    def name(s):
        pass

    def conn(c):
        pass

class Oracle(db):

        def name(s):
            s.db_name = input('Enter name of database: ')


        def conn(c):
            c.username = input('Enter username: ')
            c.password = input('Enter password: ')
            
        def machine(m):
            m.server_id = input('Enter server on which db is installed: ')


        def print(p):
            print(p.db_name)
            print(p.username, p.password)
            print(p.server_id)


        def call(c):
            c.name()
            c.conn()
            c.machine()
            c.print()



class mySQL(db):

        def name(s):
            s.db_name = input('Enter name of database: ')


        def conn(c):
            c.username = input('Enter username: ')
            c.password = input('Enter password: ')


        def table(t):
            t.table_n = int(input('Enter no. of tables: '))


        def print(p):
            print(p.db_name)
            print(p.username, p.password)
            print(p.table_n)


        def call(c):
            c.name()
            c.conn()
            c.table()
            c.print()



db = input('Select db: ')
className = globals()[db]
obj = className()

print(obj.call())