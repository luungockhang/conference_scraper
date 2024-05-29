import pypyodbc as odbc
import pandas as pd

"""
Step 1: Importing data set from CSV
"""

df = pd.read_csv('final_output.csv') 



"""
Step 2.2: Specify columns we want to import
"""

columns = ['Conference','City,Country','Deadline', 'Date', 'Website', 'Description'] # 
df_data = df[columns].astype(str)
records = df_data.values.tolist()

"""
Step 3.1 Create SQL Server Connection String
"""

DRIVER = 'SQL Server'
SERVER_NAME = 'DESKTOP-TVR6JU9\\MSSQLSERVER6'
DATABASE_NAME = 'JJ'

def connection_string(driver,server_name,database_name):
    conn_string = f'''
        DRIVER={{{driver}}};
        SERVER={server_name};
        DATABASE={database_name};
        Trusted_Connection=yes;
'''
    return conn_string

"""
Step 3.2 Create database connection instance
"""

try:
    conn = odbc.connect(connection_string(DRIVER,SERVER_NAME,DATABASE_NAME))
except odbc.DatabaseError as e:
    print('Database error:')
    print(str(e.value[1]))
except odbc.Error as e:
    print('Connection Error:')
    print(str(e.value[1]))

"""
Step 3.3 Create a cursor connection
"""

sql_insert = '''
    INSERT INTO Conferences ( Conference,CityCountry, Deadline, Date, Website, Description)
    VALUES (?,?,?,?,?,?)
'''


try:
    cursor = conn.cursor()
    cursor.executemany(sql_insert,records)
    cursor.commit()
except Exception as e:
    cursor.rollback()
    print(e.args[1])
finally:
    print('Task is complete')
    cursor.close()
    conn.close()