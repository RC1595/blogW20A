from flask import Flask
import mariadb
import dbcreds

conn = None
cursor = None

def option_select():
    database_connect()
    cursor = conn.cursor()
    option = input()
    if (option == "1"):
        print("begin your post")
        content = input()
        cursor.execute("INSERT INTO blog_post(content) VALUES (?)", [content])
        conn.commit()
    else:
        cursor.execute("SELECT username, content FROM blog_post")


def database_connect():
    try:
        conn=mariadb.connect(user = dbcreds.user,
                            password = dbcreds.password,
                            host = dbcreds.host,
                            port = dbcreds.port,
                            database = dbcreds.database)
        print("connection success")
    
    except:
        print("you did a very bad thing and should feel shame!")
    return conn
    

def user_name():
    try:
        database_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM blog_post WHERE username=?", [username,])                
        if (cursor.rowcount ==1 and username == [username,]):
            print(cursor.rowcount)
            print("Welcome!")
        else:
            print("username does not exist. Please try again.")
    except mariadb.DatabaseError:
        print("Something went wrong with the database")
    except mariadb.OperationalError:
        print("Operational error on the connection")
    except mariadb.ProgrammingError:
        print("bad query")
    except mariadb.IntegrityError:
        print("Bad query intercepted")
    
    

try:
    print("Please enter your username to continue: ")
    username = input()
    user_name()
    print("Make a selection from the following options")
    print("Press 1 to write a new post")
    print("press 2 to see all other posts")
    option_select()
except:
    print('nope')    
    
finally:
    if(cursor != None):
        cursor.close()
    else:
        print("There is no cursor")    
    if (conn != None):
        conn.rollback()
        conn.close()
    else:
        print("The connection is not open, there is nothing to close")    




