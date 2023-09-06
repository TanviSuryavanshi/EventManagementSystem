import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=' ',
    database='event_management_system'
)

print(mydb)


def EventDetails():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=' ',
        database='event_management_system'
    )
    cursor = conn.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS event (event_name VARCHAR(100), event_id VARCHAR(100) PRIMARY KEY, event_date VARCHAR(100), event_time VARCHAR(100), event_duration VARCHAR(100))')

    cursor.execute('SELECT * FROM event')
    event_details = cursor.fetchall()

    event_names = []
    event_ids = []
    event_dates = []
    event_times = []
    event_durations = []

    conn.close()

    for i in event_details:
        event_names.append(i[0])
        event_ids.append(i[1])
        event_dates.append(i[2])
        event_times.append(i[3])
        event_durations.append(i[4])

    return event_names, event_ids, event_dates, event_times, event_durations, event_details


def TicketDetails():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=' ',
        database='event_management_system'
    )
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS ticket (customer_name VARCHAR(100), ticket_id VARCHAR(100) PRIMARY KEY, event_name VARCHAR(100), event_id VARCHAR(100), event_date VARCHAR(100), event_time VARCHAR(100), duration VARCHAR(100))")

    cursor.execute('SELECT * FROM ticket')
    ticket_details = cursor.fetchall()

    customer_names = []
    ticket_ids = []
    event_names = []
    event_ids = []
    event_dates = []
    event_times = []
    event_durations = []

    conn.close()

    for i in ticket_details:
        customer_names.append(i[0])
        ticket_ids.append(i[1])
        event_names.append(i[2])
        event_ids.append(i[3])

        event_dates.append(i[4])
        event_times.append(i[5])
        event_durations.append(i[6])

    return customer_names, ticket_ids, event_names, event_ids, event_dates, event_times, event_durations, ticket_details


def BookTicket(customer_name, ticket_id, event_name):
    event_names, event_ids, event_dates, event_times, event_durations = EventDetails()[:5]

    event_index = event_names.index(event_name)
    event_id = event_ids[event_index]
    event_date = event_dates[event_index]
    event_time = event_times[event_index]
    event_duration = event_durations[event_index]

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=' ',
            database='event_management_system'
        )
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO ticket (customer_name, ticket_id, event_name, event_id, event_date, event_time, duration) VALUES (%s, %s, %s, %s, %s, %s, %s)',
            (customer_name, ticket_id, event_name, event_id, event_date, event_time, event_duration))
        conn.commit()
        conn.close()
        return 'Success'
    except mysql.connector.Error as e:
        return e
    finally:
        conn.close()


def CreateNewEvent(event_name, event_id, event_date, event_time, event_duration):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=' ',
            database='event_management_system'
        )
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO event (event_name, event_id, event_date, event_time, event_duration) VALUES (%s, %s, %s, %s, %s)',
            (event_name, event_id, event_date, event_time, event_duration))
        conn.commit()
        conn.close()
        return 'Success'
    except mysql.connector.Error as e:
        return e
    finally:
        conn.close()


def DeleteTicket(ticket_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=' ',
            database='event_management_system'
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ticket WHERE ticket_id = %s", (ticket_id,))
        conn.commit()
        conn.close()
        return 'Success'
    except mysql.connector.Error as e:
        return e
    finally:
        conn.close()
