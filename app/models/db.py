import psycopg2
from psycopg2.extras import RealDictCursor
import os


class Database():
  def __init__(self):
    try:
      self.connection = psycopg2.connect(url = 'postgres://spzzqfyvfsrcyp:8be1b4979cb14615fdf020b1b15de2410836f50388b9c514ea367fa6f11f2093@ec2-54-227-246-152.compute-1.amazonaws.com:5432/d27hcrnfoaph58')
      self.cursor = self.connection.cursor()
      self.connection.autocommit()=True

    except psycopg2.DatabaseError as e:
      print ('failed to connect to DB')


  def create_db_tables(self):
    queries = (

        """
            CREATE TABLE IF not EXISTS  users(
              user_id serial primary key,
              username varchar(10) not null unique,
              password varchar(20) not null,
              isAdmin boolean default false,
              email Text,
              firstname varchar(20),
              lastname varchar(20),
              phonenumber varchar(10),
              registered timestampTZ default NOW()
            );
            """,

        """
            CREATE TABLE IF not EXISTS red_flags(
              flag_id serial primary key,
              location varchar(100) not null,
              description varchar(1000) not null,
              image varchar(100),
              video varchar(100),
              flag_type varchar(15) not null default 'red_flag',
              status varchar(20) not null default 'none',
              createdOn timestampTZ default NOW(),
              createdby INTEGER REFERENCES users(user_id) ON DELETE CASCADE
            );
            """,
            """
            CREATE TABLE IF not EXISTS interventions(
              flag_id serial primary key,
              location varchar(100) not null,
              description varchar(1000) not null,
              image varchar(100),
              video varchar(100),
              flag_type varchar(15) not null default 'intervention',
              status varchar(20) not null default 'none',
              createdOn timestampTZ default NOW(),
              createdby INTEGER REFERENCES users(user_id) ON DELETE CASCADE
            );
            """

    )
    for query in queries:
      self.cursor.execute(query)
      self.connection.commit()

  def fetch_one(self,query):
    self.dict_cursor = self.connection.cursor(cursor_factory = RealDictCursor)
    self.dict_cursor.execute(query)
    res = self.dict_cursor.fetchone()
    if res:
      return res
    return None

  def drop_tables(self):
    query = "DROP TABLE IF EXISTS users,red_flags,interventions"
    self.cursor.execute(query)
    self.connection.commit()

  def fetch_all(self, query):
    try:
      self.dict_cur = self.connection.cursor(cursor_factory=RealDictCursor)
      self.dict_cur.execute(query)
      results = self.dict_cur.fetchall()
      if results:
        return results
    except (Exception, psycopg2.DatabaseError) as e:
      return None
	

  if __name__ == '__main__':
    db = Database()
