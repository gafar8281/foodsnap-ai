import pandas as pd
from database import engine
import csv
from io import StringIO



def psql_insert_copy(table, conn, keys, data_iter):
    """
    Execute SQL statement inserting data

    Parameters
    ----------
    table : name of SQL table.
    conn : sqlalchemy connection engine.
    keys : list of str
        Column names
    data_iter : Iterable that iterates the values to be inserted
    """
    # gets a DBAPI connection that can provide a cursor
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        writer = csv.writer(s_buf)
        writer.writerows(data_iter)
        s_buf.seek(0)

        columns = ', '.join(['"{}"'.format(k) for k in keys])
        if table.schema:
            table_name = '{}.{}'.format(table.schema, table.name)
        else:
            table_name = table.name

        sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(
            table_name, columns)
        cur.copy_expert(sql=sql, file=s_buf)

df = pd.read_csv(r'C:\Users\GAFAR\Desktop\ai-project\web_scrap\cal_data.csv')

df.to_sql(
    name= 'nutrition_data_project',
    con= engine,
    if_exists= 'append',
    index= False,
    method= psql_insert_copy
)

print("DATA SAVED INTO TABLE SUCCESSFULLY !!!")

# FASTEST METHOD TO STORE LARGE DATASET INTO DB.