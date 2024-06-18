import sqlite3
import datetime


class DBInterface:
    def __init__(self, db_path: str):
        self.con = sqlite3.connect(db_path, check_same_thread=False)
        self.cur = self.con.cursor()


DB = DBInterface('database.db')


def exist_user(user_id: int) -> bool:
    return DB.cur.execute(f"""
        SELECT 1 from users WHERE id = {user_id}
    """).fetchone() is not None


def add_user(user_id: int, username: str) -> None:
    DB.cur.execute(f"""
        INSERT INTO users(id, username, date)
        VALUES(
            "{user_id}",
            "{username}",
            "{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}"
        )
    """)
    DB.con.commit()


def get_subs(user_id: int) -> list[tuple[int, str]]:
    ids = DB.cur.execute(f"""
    SELECT event_id from subs WHERE user_id = {user_id}
    """).fetchall()

    return [(x[0], DB.cur.execute(f"""
    SELECT name from events WHERE id = {x[0]}
    """).fetchone()[0]) for x in ids]


def delete_sub(user_id: int, event_id: int) -> bool:
    if DB.cur.execute(f"""
    SELECT * from subs WHERE user_id = {user_id} AND event_id = {event_id}
    """).fetchone() is None:
        return False

    DB.cur.execute(f"""
        DELETE from subs WHERE user_id = {user_id} AND event_id = {event_id}
    """)

    DB.con.commit()
    return True


def add_sub(user_id: int, event_id: int) -> bool:
    if DB.cur.execute(f"""
    SELECT * from events WHERE id = {event_id}
    """).fetchone() is None:
        return False

    DB.cur.execute(f"""
    INSERT INTO subs(user_id, event_id)
    VALUES(
        "{user_id}",
        "{event_id}"
    )
    """)

    DB.con.commit()
    return True


def exist_sub(user_id: int, event_id: int) -> bool:
    return DB.cur.execute(f"""
    SELECT * from subs WHERE user_id = {user_id} AND event_id = {event_id}
    """).fetchone() is not None


def get_all_users() -> list[int]:
    return list(map(lambda x: x[0], DB.cur.execute("""
        SELECT id FROM users
        """).fetchall()))


def is_admin(user_id: int) -> bool:
    return bool(DB.cur.execute(f"""
    SELECT admin FROM users WHERE id = {user_id}
    """).fetchone()[0])


def make_event(name: str, desc: str) -> int:
    DB.cur.execute(f"""
    INSERT INTO events(name, description)
    VALUES(
        "{name}",
        "{desc}"
    )
    """)
    DB.con.commit()
    return DB.cur.execute(f'SELECT * FROM events WHERE name = "{name}"').fetchone()[0]

