import mysql.connector

def application(env, start_response):
    db_foobar = {
        'user': 'abrah926',
        'password': 'Micasa#1758926',
        'host': 'localhost',
        'database': 'foobar'
    }

    try:
        cnx = mysql.connector.connect(**db_foobar)
        cursor = cnx.cursor()
        cursor.execute('SELECT DATABASE();')
        result = cursor.fetchone()
        message = f"Connected to database: {result[0]}"
    except mysql.connector.Error as err:
        message = f'Error connecting to MySQL: {err}'
    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

    # Properly use `final_message` for response
    final_message = message + " | Running LAMP stack with Python & Nginx, yeah buddy!"
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [final_message.encode('utf-8')]
