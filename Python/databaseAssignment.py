# import sqlite 3 and open connection
import sqlite3
conn = sqlite3.connect('test.db')
# adding table fileList if not exist
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')
# tuple of file names
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
# for loop that analyzes tuple of file names and pulls those that
# end in .txt into one-element tuples. Adds to tbl_fileList and prints
# one-elemnt tuples that end with .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_fileList (col_files) VALUES (?)", (x,))
            print(x)


conn.close









