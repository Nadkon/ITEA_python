import psycopg2
import psycopg2.extras

dbname = "python_pro"
user = "nadinekononykhina"
password = "1234"
host = "localhost"
port = "5432"


def get_connection():
    return psycopg2.connect(
        dbname = dbname,
        user = user,
        password = password,
        host = host,
        port = port,
        cursor_factory = psycopg2.extras.DictCursor
    )

def search_by_name(name: str):
      with get_connection() as connection:
          with connection.cursor() as cursor:

              query = """
                select
                  *
                from "user" u
                join address a on u.address_id = a.id
                join city c on a.city_id = c.id
                join country c2 on c2.id = c.country_id
                WHERE u.name ilike "%%" || %a || "%%"
              """

              cursor.execute(query, (name, ))
              result = cursor.fetchall()
              return(result)

print(search_by_name('N'))

'''
with get_connection() as connection:
    with connection.cursor() as cursor:

        query = """
          select
            u.name, surname, phone, email, street, a.postal_code, c.name as city, c2.name as country
          from "user" u
          join address a on u.address_id = a.id
          join city c on a.city_id = c.id
          join country c2 on c2.id = c.country_id
          WHERE c.name = 'Kyiv'
                """
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
'''
