import mysql

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'rain'")

#That statement retrieved all the rows of the Dictionary table where the value of the column Expression was rain. The string inside cursor.execute() is SQL code that Python sends to the database. That kind of language is understood by the database.



"SELECT * FROM Dictionary WHERE Expression  LIKE 'r%'" #Get all rows where the value of the column Expression starts with r:


"SELECT * FROM Dictionary WHERE Expression  LIKE 'rain%'" #Get all rows where the value of the column Expression starts with rain:


"SELECT * FROM Dictionary WHERE length(Expression) < 4" #All rows where the length of the value of the column Expression is less than four characters:


"SELECT * FROM Dictionary WHERE length(Expression) = 4" #All rows where the length of the value of the column Expression is four characters:


"SELECT * FROM Dictionary WHERE length(Expression) > 1 AND length(Expression) < 4" #All rows where the length of the value of the column Expression is greater than 1 but less than 4 characters:


"SELECT Definition FROM Dictionary WHERE Expression  LIKE 'r%'" #All rows of column Definition where the value of the column Expression starts with r:
