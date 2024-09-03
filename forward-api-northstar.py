import socket
import requests
import mysql.connector
import json
import logging
import smtplib
from datetime import datetime
from logging_config_api import setup_logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import threading
import queue


to_email = ['steve@theuptownguy.com', 'nabeelayub00718@gmail.com']
from_email = 'sell@airebrokers.com'
smtp_server = 'smtp.sendgrid.net'
smtp_port = 587  # For TLS
login = 'apikey'
password = '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'

api_db_config = {
    'user': 'root',
    'unix_socket': '/var/run/mysqld/mysqld.sock',
    'database': 'northstar2',
    'password': 'db_root'
}

setup_logging('mlsapp/mlsgrid/logs/northstar-api-forward.log')
logger = logging.getLogger(__name__)

def PostApi(raw_text):
    # print("in forward!")

    API_ENDPOINT = "http://192.168.8.100:50001/api/v1/preprocessing/"
    api_key =  "testapijson"
    url='https://api.mlsgrid.com/v2'
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",  # Assuming JSON content
    }

    data = {
        "date_timestamp": datetime.now().isoformat(),
        "url": url,
        "source_domain_name": url.split('/')[2],
        "source_full_url": url,
        "error": "error",
        "raw_text": json.dumps(raw_text, ensure_ascii=False),
        "method": "mls-direct-northstar",
        "agent_id": socket.gethostname(),
        "agent_ip": get_outbound_ip(),
        "size": f"{len(json.dumps(raw_text, ensure_ascii=False))}"
    }

    print(data)
    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=data)
        if response.status_code == 200:
            logger.info(f'Northstar data forwarded to api detail {raw_text[:250]}')
        else:
            logger.error(f'Response Error forward api Northstar: {response.text}')
            error_check(response.text)
    except requests.exceptions.ConnectTimeout as e:
        error_check(e)
    except requests.exceptions.HTTPError as e:
        error_check(e)
    except requests.exceptions.RequestException as e:
        error_check(e)
    except Exception as err:
        error_check(err)   

def error_check(err):

    subject = 'MLS System Issue Arise NorthStar'
    body = f"Error Details:\n{err}"
    send_email(subject, body, to_email, from_email, smtp_server, smtp_port, login, password)
    sys.exit(0)

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, login, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to_email)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Connect to the server and send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
    

def get_outbound_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        outbound_ip = response.json().get('origin', 'Unknown')
        return outbound_ip
    except Exception as e:
        print(f"Error fetching outbound IP: {e}")
        return 'Unknown'


def get_columns():

    connection = mysql.connector.connect(**api_db_config)
    cursor_default = connection.cursor(buffered=True)
    
    try:
        with connection.cursor() as cursor_columns:
            cursor_columns.execute(f"SHOW COLUMNS FROM Property")
            property_columns = [column[0] for column in cursor_columns.fetchall()]
    except mysql.connector.Error as e:
        logger.error(f"Error executing SHOW COLUMNS query for Property table northstar forward api: {e}")
        property_columns = []

    # Fetching columns for Office table
    try:
        with connection.cursor() as cursor_columns:
            cursor_columns.execute(f"SHOW COLUMNS FROM Office")
            office_columns = [column[0] for column in cursor_columns.fetchall()]
    except mysql.connector.Error as e:
        logger.error(f"Error executing SHOW COLUMNS query for Office table forward api: {e}")
        office_columns = []

    # Fetching columns for Member table
    try:
        with connection.cursor() as cursor_columns:
            cursor_columns.execute(f"SHOW COLUMNS FROM Member")
            member_columns = [column[0] for column in cursor_columns.fetchall()]
    except mysql.connector.Error as e:
        logger.error(f"Error executing SHOW COLUMNS query for Member table forward api northstar: {e}")
        member_columns = []

    # Fetching columns for Media table
    try:
        with connection.cursor() as cursor_columns:
            cursor_columns.execute(f"SHOW COLUMNS FROM Media")
            media_columns = [column[0] for column in cursor_columns.fetchall()]
    except mysql.connector.Error as e:
        logger.error(f"Error executing SHOW COLUMNS query for Media table forward api northstar: {e}")
        media_columns = []

    # Fetching columns for PropertyUnitTypes table
    try:
        with connection.cursor() as cursor_columns:
            cursor_columns.execute(f"SHOW COLUMNS FROM PropertyUnitTypes")
            unit_columns = [column[0] for column in cursor_columns.fetchall()]
    except mysql.connector.Error as e:
        logger.error(f"Error executing SHOW COLUMNS query for PropertyUnitTypes table forward api northstar: {e}")
        unit_columns = []

    # Fetching columns for PropertyRooms table
    try:
        with connection.cursor() as cursor_columns:
            cursor_columns.execute(f"SHOW COLUMNS FROM PropertyRooms")
            room_columns = [column[0] for column in cursor_columns.fetchall()]
    except mysql.connector.Error as e:
        logger.error(f"Error executing SHOW COLUMNS query for PropertyRooms table forward api northstar: {e}")
        room_columns = []
    
    logger.info("Arranging Property Data")
    
    cursor_default.close()
    connection.close()

    return property_columns,office_columns,member_columns,media_columns,unit_columns,room_columns


def get_data(escaped_property_id,property_columns,office_columns,member_columns,media_columns,unit_columns,room_columns):

    connection = mysql.connector.connect(**api_db_config)
    cursor_default = connection.cursor(buffered=True)
    logger.info(f'Getting Properties against id including office,member {escaped_property_id}')
    cursor_default.execute(f"""
        SELECT *
        FROM Property
        LEFT JOIN Office ON Property.BuyerOfficeKey = Office.OfficeKey
        LEFT JOIN Member AS BuyerAgentMember ON Property.BuyerAgentKey = BuyerAgentMember.MemberKey
        LEFT JOIN Member AS ListAgentMember ON Property.ListAgentKey = ListAgentMember.MemberKey
        WHERE Property.ListingId = '{escaped_property_id}';
    """)

    # Fetch the results
    default_data = cursor_default.fetchall()
    logger.info(f'Getting Media Property Unittypes PropertyRooms Data against {escaped_property_id}')
    try:
        with connection.cursor() as cursor_default:
            # Execute the query for the 'Media' table
            cursor_default.execute(f"""
                SELECT *
                FROM Media
                WHERE Media.ListingId = '{escaped_property_id}';
            """)
            media_data = cursor_default.fetchall()

            # Execute the query for the 'PropertyUnitTypes' table
            cursor_default.execute(f"""
                SELECT *
                FROM PropertyUnitTypes
                WHERE PropertyUnitTypes.ListingId = '{escaped_property_id}';
            """)
            unit_data = cursor_default.fetchall()

            # Execute the query for the 'PropertyRooms' table
            cursor_default.execute(f"""
                SELECT *
                FROM PropertyRooms
                WHERE PropertyRooms.ListingId = '{escaped_property_id}';
            """)
            rooms_data = cursor_default.fetchall()

    except mysql.connector.Error as e:
        logger.error(f"Error executing queries: {e}")
        error_check(e)
        media_data = []
        unit_data = []
        rooms_data = []

    
    # Combine all columns
    columns = property_columns + office_columns + member_columns + media_columns + unit_columns + room_columns

    # Initialize a list to store the final JSON response
    json_response_default = []

    # Process the default_data results 
    for row in default_data:
        row_dict = {}
        for idx, column_name in enumerate(columns):
            row_dict[column_name] = row[idx] if idx < len(row) else None
        json_response_default.append(row_dict)

    # Process the media_data results 
    media_data_list = []
    for i in range(len(media_data)):
        my_dict = {}
        for j in range(len(media_data[i])):
            my_dict[media_columns[j]] = media_data[i][j]
        media_data_list.append(my_dict)

    # Process the rooms_data results 
    rooms_data_list = []
    for i in range(len(rooms_data)):
        my_dict = {}
        for j in range(len(rooms_data[i])):
            my_dict[room_columns[j]] = rooms_data[i][j]
        rooms_data_list.append(my_dict)

    # Process the unit_data results
    unit_data_list = []
    for i in range(len(unit_data)):
        my_dict = {}
        for j in range(len(unit_data[i])):
            my_dict[unit_columns[j]] = unit_data[i][j]
        unit_data_list.append(my_dict)

    # Combine processed data into a final JSON structure
    row_dict = {'media': media_data_list, 'rooms': rooms_data_list, 'unittypes': unit_data_list}
    json_response_default.append(row_dict)
   
    cursor_default.close()
    connection.close()

    return json_response_default


def get_property(batch_size,offset):

    connection = mysql.connector.connect(**api_db_config)
    cursor = connection.cursor(buffered=True)

    try:
        query = f"""
            SELECT ListingId
            FROM Property
            ORDER BY ModificationTimestamp DESC
            LIMIT %s OFFSET %s
        """
        cursor.execute(query, (batch_size, offset))
    
        results = cursor.fetchall()
        properties = [result[0] for result in results]

    except mysql.connector.Error as e:
        logger.error(f"Error fetching properties: {e}")
        properties = None
    finally:
        cursor.close()
        connection.close()

    cursor.close()
    connection.close()

    return properties


def worker_thread(q,property_columns, office_columns, member_columns, media_columns, unit_columns, room_columns):

    while True:
        try:
            property_id = q.get(timeout=1)  # Timeout to periodically check the stop_event
        except queue.Empty:
            continue

        if property_id is None:
            break
        try:
            # Process the property data
            property_info = get_data(property_id, property_columns, office_columns, member_columns, media_columns, unit_columns, room_columns)
            # Post the data or perform other processing
            json_text = PostApi(str(property_info))  # Assuming PostApi is your function to post data
        except Exception as e:
            # Handle exceptions if any
            print(f"Error processing property {property_id}: {e}")
        finally:
            # Mark the task as done
            q.task_done()

def main():

    property_columns,office_columns,member_columns,media_columns,unit_columns,room_columns = get_columns()
    batch_size=10000
    offset=0

    while True:

        properties = get_property(batch_size,offset)

        if not properties:
            break;
        
        # Create a queue to hold property IDs
        q = queue.Queue()

        # Start worker threads
        num_worker_threads = 15

        threads = []
        for _ in range(num_worker_threads):
            t = threading.Thread(target=worker_thread, args=(q,property_columns, office_columns, member_columns, media_columns, unit_columns, room_columns))
            t.start()
            threads.append(t)

        for prop in properties:
            q.put(prop)

        # Wait for all tasks to be processed
        q.join()

        for _ in range(num_worker_threads):
            q.put(None)
        for t in threads:
            t.join()
        
        offset += batch_size

        with open('batch_file.txt','w') as file: 
            file.write(str(offset))

if __name__ == "__main__":
    main()

# ps aux | grep forward-api-northstar
# kill -9 pid (the first digit numbers)