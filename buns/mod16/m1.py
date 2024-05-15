import random
import sqlite3


CREATE_TABLES = """
drop table if exists actors;
create table actors (
    act_id integer primary key autoincrement,
    act_first_name varchar(50) not null,
    act_last_name varchar(50) not null,
    act_gender varchar(1) not null
);

drop table if exists movie;
create table movie (
    mov_id integer primary key autoincrement,
    mov_title varchar(50) not null
);

drop table if exists director;
create table director (
    dir_id integer primary key autoincrement,
    dir_first_name varchar(50) not null,
    dir_last_name varchar(50) not null
);

drop table if exists movie_cast;
create table movie_cast (
    act_id integer not null,
    mov_id integer not null,
    role_ varchar(50) not null,
    foreign key (act_id) references actors(act_id) on delete cascade,
    foreign key (mov_id) references movie(mov_id) on delete cascade
);

drop table if exists oscar_awarded;
create table oscar_awarded (
    award_id integer primary key autoincrement,
    mov_id integer not null,
    foreign key (mov_id) references movie(mov_id) on delete cascade
);

drop table if exists movie_direction;
create table movie_direction (
    dir_id integer not null,
    mov_id integer not null,
    foreign key (dir_id) references director(dir_id) on delete cascade,
    foreign key (mov_id) references movie(mov_id) on delete cascade
);
"""

with sqlite3.connect("m1.db") as conn:
    cursor = conn.cursor()
    cursor.executescript(CREATE_TABLES)
    conn.commit()