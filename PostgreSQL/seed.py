import psycopg2
from faker import Faker
from psycopg2 import sql

# Connecting to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password='mysecretpassword',
    host="localhost",
    port="5432",
)


# Creating a cursor
cur = conn.cursor()

# Initializing the random data generator
fake = Faker()

# Filling the users table
for _ in range(10):  # fill in 10 users
    fullname = fake.name()
    email = fake.email()
    cur.execute(
        sql.SQL("INSERT INTO users (fullname, email) VALUES (%s, %s)"),
        (fullname, email),
    )

# Filling the status table
statuses = ["new", "in progress", "completed"]
for status in statuses:
    cur.execute(sql.SQL("INSERT INTO status (name) VALUES (%s)"), (status,))

# Filling the tasks table
for _ in range(20):  # fill in 20 tasks
    title = fake.text(max_nb_chars=50)  # random task title
    description = fake.text()  # random task description
    status_id = fake.random_int(min=1, max=len(statuses))  # random status
    user_id = fake.random_int(min=1, max=10)  # random user
    cur.execute(
        sql.SQL(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)"
        ),
        (title, description, status_id, user_id),
    )

# Saving changes to the database
conn.commit()

# Closing the cursor and connecting to the database
cur.close()
conn.close()
