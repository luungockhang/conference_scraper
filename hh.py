# Created by 22810019
# Reviewed by 22880068
# May 29 2024 - Refactored and created async function to run with the program
# Lets DB import csv file

import pypyodbc as odbc
import pandas as pd


# Edit your database server info here
DRIVER = 'SQL Server'
SERVER_NAME = 'LAPTOP-FBH7ER7I\\CSDL_PRAC_SERVER'
DATABASE_NAME = 'JJ'

# Get connection string
def connection_string(driver,server_name,database_name):
    conn_string = f'''
        DRIVER={{{driver}}};
        SERVER={server_name};
        DATABASE={database_name};
        Trusted_Connection=yes;
'''
    return conn_string




async def import_to_db():
    # import dataset from csv
    df = pd.read_csv('final_output.csv')

    
    #--Data clean up--
    # Remove rows contain NaN values
    df.dropna(inplace=True)

    # Remove duplicate records
    df.drop_duplicates(inplace=True)

    # Clean string data
    df['Conference'] = df['Conference'].str.strip().str.lower()
    df['City,Country'] = df['City,Country'].str.strip().str.lower()
    df['Deadline'] = df['Deadline'].str.strip().str.lower()
    df['Date'] = df['Date'].str.strip().str.lower()
    df['Website'] = df['Website'].str.strip().str.lower()
    df['Description'] = df['Description'].str.strip().str.lower()

    # specify columns we want to import
    columns = ['Conference','City, Country','Deadline', 'Date', 'Website', 'Description']
    df_data = df[columns].astype(str)
    records = df_data.values.tolist()


    # Create database connection instance
    try:
        conn = odbc.connect(connection_string(DRIVER,SERVER_NAME,DATABASE_NAME))
    except odbc.DatabaseError as e:
        print('Database error:')
        print(str(e.value[1]))
    except odbc.Error as e:
        print('Connection Error:')
        print(str(e.value[1]))
        
    # Create a cursor connection

    sql_insert = '''
        INSERT INTO Conferences ( Conference,CityCountry, Deadline, Date, Website, Description)
        VALUES (?,?,?,?,?,?)
    '''

    try:
        cursor = conn.cursor()
        cursor.execute('TRUNCATE TABLE Conferences')
        cursor.executemany(sql_insert,records)
        cursor.commit()
    except Exception as e:
        cursor.rollback()
        print('Error while importing to database. Argument: {0}'.format(e.args[1]))
    finally:
        print('Imported csv to database')
        cursor.close()
        conn.close()