import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        ddl = "drop table if exists words"
        cur.execute(ddl)
        ddl = "create table words ( word TEXT not null primary key, usage_count INT default 1 not null );"
        cur.execute(ddl)
        ddl = "create unique index words_word_uindex on words (word);"
        cur.execute(ddl)


def save_words_to_database(database_path: str, words_list: list):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in words_list:
            # check to see if the word is in there
            sql = "select count(word) from words where word = '" + word + "'"
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word = '" + word + "'"
            else:
                sql = "insert into words (word) values ('" + word + "')"
                conn.execute(sql)
            #conn.close()
            print("Database save complete!")



