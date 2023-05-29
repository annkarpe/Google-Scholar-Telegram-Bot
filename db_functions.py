import sqlite3

def create_table():
    with sqlite3.connect('users_queries.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS user_records (
                user_id INTEGER,
                user_query TEXT,
                PRIMARY KEY (user_id, user_query)
            )''')
    conn.commit()


def run_query(query, params=()):
    with sqlite3.connect('users_queries.db') as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, params)
        conn.commit()
    return result


def insert_query(user_id, user_query):
    query = "INSERT OR IGNORE INTO user_records (user_id, user_query) VALUES(?, ?);"
    run_query(query, (user_id, user_query))


def remove_record(user_id, user_query):
    query = "DELETE FROM user_records WHERE user_id = ? AND user_query = ?;"
    run_query(query, (user_id, user_query))


def remove_all_records():
    query = "DELETE FROM user_records;"
    run_query(query)


def print_records():
    query = "SELECT * FROM user_records;"
    result = run_query(query).fetchall()
    print(result)