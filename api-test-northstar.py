import requests
import mysql.connector
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from rate_limiter import RateLimiter
from rate_limiter_data import DataTracker
from logging_config import setup_logging
import logging
import json
import time



db_config = {
    'user': 'root',
    'unix_socket': '/var/run/mysqld/mysqld.sock',
    'database': 'northstar2',
    'password': 'db_root'
}


api_url = "https://api.mlsgrid.com/v2"
api_key = "21c353c022c196e275c13cff9aefd48f4e8813b5"
#api_key="afe39048e8e4fd9d448f13e5c1a9baa2521088e2"
#setup_logging('northstar.log',db_config)
setup_logging('mlsapp/mlsgrid/logs/northstar.log')
logger = logging.getLogger(__name__)
#logger.disabled=True
skip='0'


def get_last_time(): # get latest/last modification time from every table

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(buffered=True)
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    table_timestamps = {}
    #print("getting latest records!!")
    for table in tables:
        table_name = table[0]
        
        cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}' AND COLUMN_NAME = 'ModificationTimestamp';")
        column_exists = cursor.fetchone()

        if column_exists:
            
            query = f"SELECT ModificationTimestamp FROM {table_name} ORDER BY ModificationTimestamp DESC LIMIT 1;"
            cursor.execute(query)
            result = cursor.fetchone()

            if not result:
                table_timestamps[table_name] = '2020-12-30T23:59:59.99Z'
            else:
                table_timestamps[table_name] = result[0].strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z' # save the converted api compatible time format
    
    logger.info("Last Record Timestamp",table_timestamps)
    print("Last Record Timestamp",table_timestamps)
    #print("Last Record Timestamp",table_timestamps)
    
    conn.close()
    return table_timestamps

#@RateLimiter(max_calls=1, period=1)
def fetch_metadata():

    headers = {'Authorization': f'Bearer {api_key}'}
    params = {'$filter': "OriginatingSystemName eq 'northstar'"}
    metadata_url = f'{api_url}/$metadata'
    response = requests.get(metadata_url, headers=headers, params=params)
    
    if response.status_code == 200:
        try:
            bytes_size = len(response.content)
            bytes_size_gb = bytes_size / (1024 * 1024 * 1024)
            return ET.fromstring(response.content), bytes_size_gb
        except ET.ParseError as e:
            print(f"Error parsing XML: {e}")
            return None
    else:
        print(f"Error fetching metadata: {response.status_code}")
        print(f"Response content: {response.text}")
        return None


def fetch_property_expansion_data(expansion,modificationTime):  # property,office,unitypes

    api_property_url = "https://api.mlsgrid.com/v2/Property"
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {
        '$filter': "OriginatingSystemName eq 'northstar' and ModificationTimestamp gt "+modificationTime,
        '$expand': expansion,
        '$skip': skip,

    }

    try:
        propertydata_url = f'{api_property_url}'
        response = requests.get(propertydata_url, headers=headers, params=params)
        
        if response.status_code == 200:

            bytes_size = len(response.content)
            bytes_size_gb = bytes_size / (1024 * 1024 * 1024)
            logger.info(f'Data downloaded from Property total records {skip} payload size {bytes_size_gb} gb')
            return json.loads(response.text), bytes_size_gb

        else:

            logger.error(f'Error fetching propertydata:{response.status_code}')
            logger.error(f'Response content: {response.text}')

            return [],0.0
        
    except Exception as e:
        
        logger.error(f'An error occurred: {str(e)}')
        return [],None


def fetch_lookup_data(modificationTime):

    api_lookup_url = "https://api.mlsgrid.com/v2/Lookup"
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {
        '$filter': "OriginatingSystemName eq 'northstar' and ModificationTimestamp gt "+modificationTime,
        '$skip':skip,
    }

    try:
        lookupdata_url = f'{api_lookup_url}'
        response = requests.get(lookupdata_url, headers=headers, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            bytes_size = len(response.content)
            bytes_size_gb = bytes_size / (1024 * 1024 * 1024)
            logger.info(f'Data downloaded from Lookup total records payload size {bytes_size_gb} gb')
            return json.loads(response.text), bytes_size_gb
        else:
            # Handle the case where the request was not successful
            logger.error(f"Error fetching lookup data: {response.status_code}")
            logger.error(f"Response content: {response.text}")
            return [],0.0
    except Exception as e:
        # Handle any exceptions that might occur during the request
        logger.error(f"An error occurred on Lookup: {str(e)}")
        return [],0.0


def fetch_office_data(modificationTime):
    api_office_url = "https://api.mlsgrid.com/v2/Office"
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {
        '$filter': "OriginatingSystemName eq 'northstar' and ModificationTimestamp gt "+modificationTime,
        '$skip': skip,
    }
    try:
        officedata_url = f'{api_office_url}'
        response = requests.get(officedata_url, headers=headers, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            bytes_size = len(response.content)
            bytes_size_gb = bytes_size / (1024 * 1024 * 1024)
            logger.info(f'Data downloaded from Office total records payload size {bytes_size_gb} gb')
            return json.loads(response.text), bytes_size_gb
        else:
            # Handle the case where the request was not successful
            logger.error(f"Error fetching office data: {response.status_code}")
            logger.error(f"Response content: {response.text}")
            return [],0.0
    except Exception as e:
        # Handle specific exceptions related to requests (e.g., connection errors)
        logger.error(f"An error occured on Office: {str(e)}")
        return [],0.0



def fetch_member_data(modificationTime):
    api_member_url = "https://api.mlsgrid.com/v2/Member"
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {
        '$filter': "OriginatingSystemName eq 'northstar' and ModificationTimestamp gt "+modificationTime,
        '$skip':skip,
    }
    
    try:
        memberdata_url = f'{api_member_url}'
        response = requests.get(memberdata_url, headers=headers, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            bytes_size = len(response.content)
            bytes_size_gb = bytes_size / (1024 * 1024 * 1024)
            logger.info(f'Data downloaded from Member total records payload size {bytes_size_gb} gb')
            return json.loads(response.text), bytes_size_gb
        else:
            # Handle the case where the request was not successful
            logger.error(f"Error fetching member data: {response.status_code}")
            logger.error(f"Response content: {response.text}")
            return [],0.0

    except Exception as e:
        # Handle any exceptions that might occur during the request
        logger.error(f"An error occurred on fetching Member: {str(e)}")
        return [],0.0



def fetch_openhouse_data(modificationTime):
    api_openhouse_url = "https://api.mlsgrid.com/v2/OpenHouse"
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {
        '$filter': "OriginatingSystemName eq 'northstar' and ModificationTimestamp gt "+modificationTime,
        '$skip':skip,
    }
    try:
        openhousedata_url = f'{api_openhouse_url}'
        response = requests.get(openhousedata_url, headers=headers, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            bytes_size = len(response.content)
            bytes_size_gb = bytes_size / (1024 * 1024 * 1024)
            logger.info(f'Data downloaded from OpenHouse total records payload size {bytes_size_gb} gb')
            return json.loads(response.text), bytes_size_gb
        else:
            # Handle the case where the request was not successful
            print(f"Error fetching open house data: {response.status_code}")
            print(f"Response content: {response.text}")
            return [],0.0
    except Exception as e:
        # Handle any exceptions that might occur during the request
        print(f"An error occurred on open house: {str(e)}")
        return [],0.0

    

def convert_to_mysql_datetime(data_entry):
    converted_entry = {}
    
    for key, value in data_entry.items():
        if isinstance(value, str):
            try:
                dt_object = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
                mysql_datetime_str = dt_object.strftime("%Y-%m-%d %H:%M:%S.%f")
                converted_entry[key] = mysql_datetime_str
            except ValueError:
                converted_entry[key] = value
        elif isinstance(value, list):
                converted_entry[key]=', '.join(map(str, value))
        else:
            converted_entry[key] = value
    
    return converted_entry

def insert_data_property(resource_name,property_data,properties,expand,table_name):

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    keys_to_check = [item['Name'] for item in properties]

    if resource_name in table_name:

        index = table_name.index(resource_name)
        insert_data=[]

        for ind in range(len(property_data['value'])):
            if expand[index] in property_data['value'][ind]:
                insert_data=property_data['value'][ind][expand[index]]
    
            for i in range(len(insert_data)):
                current_dict = {}
                list3 = []
                for key in keys_to_check:
                    if key in insert_data[i]:
                        current_dict[key] = insert_data[i][key]
                current_dict['ListingId'] = property_data['value'][ind]['ListingId']
                list3.append(current_dict)      

                for data_entry in list3:
                    data_entry=convert_to_mysql_datetime(data_entry)
                    columns = ', '.join([f"`{col}`" for col in data_entry.keys()])
                    placeholders = ', '.join(['%s' for _ in data_entry.values()])

                    update_col = ', '.join([f"`{col}` = %s" for col in data_entry.keys()])
                    insert_command = f"INSERT INTO {resource_name} ({columns}) VALUES ({placeholders}) ON DUPLICATE KEY UPDATE {update_col}"
                    logger.info(f"Query is {insert_command}")

                    try:
                        values = tuple(list(data_entry.values()) * 2) 
                        #logger.info(f"values: {values}")
                        cursor.execute(insert_command, values)
                        # process_and_send_to_queue(data_entry, channel)
                        logger.info(f"Data inserted or updated on {resource_name} last record {str(data_entry)[:250]}")
                        #print("Data inserted or updated successfully")
                    except Exception as err:
                        logger.error(f"Error inserting data on {resource_name}: {err}")
                        #logger.error(f"Query is -: {insert_command}")
                       
                        #print(f"error while insertion{err}")
                
    elif resource_name.lower() =='property':
        
        list3=[]
        for i in range(len(property_data['value'])):
            current_dict = {}            
            for key in keys_to_check:
                if key in property_data['value'][i] and key not in expand:
                    current_dict[key] = property_data['value'][i][key]
            
            list3.append(current_dict)
        
            
        for data_entry in list3:
            data_entry=convert_to_mysql_datetime(data_entry)
            data_entry_values = []

            for value in data_entry.values():
                if isinstance(value, list):
                    value_str = ', '.join(map(str, value))
                else:
                    value_str = value
                data_entry_values.append(value_str)

            columns = ', '.join([f"`{col}`" for col in data_entry.keys()])
            values = ', '.join(['%s' for _ in data_entry_values])
            update_col = ', '.join([f"`{col}` = %s" for col in data_entry.keys()])
            insert_command = f"INSERT INTO Property ({columns}) VALUES ({values}) ON DUPLICATE KEY UPDATE {update_col}"
            try:
                values = tuple(list(data_entry.values()) * 2)
                #logger.error(f"Values: {values}")
                cursor.execute(insert_command, values)
                logger.info(f"Data inserted or updated on {resource_name} last timestamp {str(data_entry)[:250]}")
                #print("Data inserted or updated successfully")
            except mysql.connector.Error as err:
                logger.error(f"Error inserting data on {resource_name}: {err}")
                #logger.error(f"Query: {insert_command}")
                
                       
    conn.commit()
    conn.close()


def insert_data_lookup_member_office_openhouse(resource_name,property_data,properties):

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    list3=[]
    keys_to_check = [item['Name'] for item in properties]

    for i in range(len(property_data['value'])):
        current_dict = {}            
        for key in keys_to_check:
            if key in property_data['value'][i]:
                current_dict[key] = property_data['value'][i][key]
        
        list3.append(current_dict)
    
         
    for data_entry in list3:
       data_entry=convert_to_mysql_datetime(data_entry)
       columns = ', '.join([f"`{col.strip()}`" for col in data_entry.keys()])
       values = ', '.join(['%s' for _ in data_entry.values()])
       update_col = ', '.join([f"`{col}` = %s" for col in data_entry.keys()])
       insert_command = f"INSERT INTO {resource_name} ({columns}) VALUES ({values}) ON DUPLICATE KEY UPDATE {update_col}"
       
       try:
            values = tuple(list(data_entry.values()) * 2)
            cursor.execute(insert_command, values)
            logger.info(f"Data inserted or updated on {resource_name} last record {data_entry}")
            #print("Data inserted or updated successfully")
       except mysql.connector.Error as err:
            logger.error(f"Error inserting data on {resource_name}: {err}")
            #print(f"Error inserting data  {err}")
            
               
    conn.commit()
    conn.close()

def prepare_metadata (*args):
    
    metadata_xml=args[4]
    if metadata_xml is not None:
        for entity_type in metadata_xml.findall(".//{http://docs.oasis-open.org/odata/ns/edm}EntityType"):
            resource_name = entity_type.get('Name')
            properties = [
                {
                    'Name': prop.get('Name'),
                    'Type': prop.get('Type'),
                    'MaxLength': prop.get('MaxLength')
                }
                for prop in entity_type.findall("{http://docs.oasis-open.org/odata/ns/edm}Property")
            ]

            if resource_name.lower() == 'lookup':
                if args[0] is not None:
                    insert_data_lookup_member_office_openhouse(resource_name,args[0],properties)
            elif resource_name.lower() == 'member':
                if args[1] is not None:
                    insert_data_lookup_member_office_openhouse(resource_name,args[1],properties)
            elif resource_name.lower() == 'office':
                if args[2] is not None:
                    insert_data_lookup_member_office_openhouse(resource_name,args[2],properties)
            elif resource_name.lower() == 'openhouse':
                if args[3] is not None:
                    insert_data_lookup_member_office_openhouse(resource_name,args[3],properties)


# def process_and_send_to_queue(data, channel):

#     channel.basic_publish(
#         exchange='',
#         routing_key='data_queue_northstar_download',
#         body=json.dumps(data)
#     )

def main():

    rate_rps = RateLimiter(max_requests=2, per_time_unit=1)
    rate_hourly = RateLimiter(max_requests=7200, per_time_unit=3600)
    rate_daily = RateLimiter(max_requests=40000, per_time_unit=86400)
    data_tracker = DataTracker(max_data_size_per_hour=3.98) 
    data_size=0.0

    if rate_rps.allow_request() and rate_hourly.allow_request() and rate_daily.allow_request():
        if data_tracker.check_data_usage():
            metadata_xml,res_size = fetch_metadata()
            data_tracker.update_data_usage(res_size)
        else:
            logger.error('You have downloaded maximum data in an hour')
            return
    else:
        logger.error('Rate Limit near to exceed')
        return
        
    # last_time=get_last_time()
    last_time='2020-12-30T23:59:59.99Z'
    global skip
    expand=[]
    table_name=[]

    for nav_type in metadata_xml.findall(".//{http://docs.oasis-open.org/odata/ns/edm}NavigationProperty"):
        
        if nav_type.get('Name') not in expand:
            expand.append(nav_type.get('Name'))
            last_table=nav_type.get('Type')
            second_part = last_table.split('(')[1]
            result = second_part.rstrip(')')
            last_word = result.split('.')[-1]
            table_name.append(last_word)
           
    
    exp_str = ",".join(expand)
    
    
    while True:

        if rate_rps.allow_request() and rate_hourly.allow_request() and rate_daily.allow_request():            
            if data_tracker.check_data_usage():
                property_data,res_size = fetch_property_expansion_data(exp_str,last_time['Property'])
                #process_and_send_to_queue(property_data, channel)

                data_tracker.update_data_usage(res_size)
                
                if '@odata.nextLink' in property_data:
                    parsed_url = urlparse(property_data['@odata.nextLink'])
                    query_params = parse_qs(parsed_url.query)
                    skip_value = query_params.get('$skip', [None])[0]
                    skip=skip_value
                    
                    if metadata_xml is not None:
                        for entity_type in metadata_xml.findall(".//{http://docs.oasis-open.org/odata/ns/edm}EntityType"):
                            resource_name = entity_type.get('Name')
                            properties = [
                                {
                                    'Name': prop.get('Name'),
                                    'Type': prop.get('Type'),
                                    'MaxLength': prop.get('MaxLength')
                                }
                                for prop in entity_type.findall("{http://docs.oasis-open.org/odata/ns/edm}Property")
                            ]
                            
                            insert_data_property(resource_name,property_data,properties,expand,table_name)
                else:
                    if metadata_xml is not None:
                        for entity_type in metadata_xml.findall(".//{http://docs.oasis-open.org/odata/ns/edm}EntityType"):
                            resource_name = entity_type.get('Name')
                            properties = [
                                {
                                    'Name': prop.get('Name'),
                                    'Type': prop.get('Type'),
                                    'MaxLength': prop.get('MaxLength')
                                }
                                for prop in entity_type.findall("{http://docs.oasis-open.org/odata/ns/edm}Property")
                            ]
                            
                        insert_data_property(resource_name,property_data,properties,expand,table_name)
                    break;

                time.sleep(1)
            else:
                logger.error("You have downloaded maximum data in a hour")
                logger.error("data size",data_size)
                break;
        else:
            logger.warning("Near to exceeding limit in property")
            break;
    
    skip='0'
    while True:

        if rate_rps.allow_request() and rate_hourly.allow_request() and rate_daily.allow_request():
            
            if data_tracker.check_data_usage():

                lookup,res_size = fetch_lookup_data(last_time['Lookup'])
                data_tracker.update_data_usage(res_size)
                #process_and_send_to_queue(lookup, channel)
                if '@odata.nextLink' in lookup:  # to check next link of page available

                    parsed_url = urlparse(lookup['@odata.nextLink'])
                    query_params = parse_qs(parsed_url.query)
                    skip_value = query_params.get('$skip', [None])[0]
                    skip=skip_value
                    prepare_metadata(lookup,None,None,None,metadata_xml)
                    
                else:
                    if lookup:
                        prepare_metadata(lookup,None,None,None,metadata_xml)
                    break;
            else:

                logger.error("You have downloaded maximum data in a hour")
        else:
            logger.info("Near to exceed Rate Limit!!")
    
   
    skip='0'
    while True:

        if rate_rps.allow_request() and rate_hourly.allow_request() and rate_daily.allow_request():
            
            if data_tracker.check_data_usage():
                member,res_size = fetch_member_data(last_time['Member'])
                #process_and_send_to_queue(member, channel)
                data_tracker.update_data_usage(res_size)
                
                if '@odata.nextLink' in member:  # to check next link of page available
                    parsed_url = urlparse(member['@odata.nextLink'])
                    query_params = parse_qs(parsed_url.query)
                    skip_value = query_params.get('$skip', [None])[0]
                    skip=skip_value
                    prepare_metadata(None,member,None,None,metadata_xml)
                else:

                    if member:
                        prepare_metadata(None,member,None,None,metadata_xml)
                    break;
                
                time.sleep(1)

            else:
                logger.error("You have download maximum data in an hour")
        else:
            logger.warning("Near to exceed Rate Limit!!")

    skip='0'
    while True:

        if rate_rps.allow_request() and rate_hourly.allow_request() and rate_daily.allow_request():
            
            if data_tracker.check_data_usage():

                office,res_size = fetch_office_data(last_time['Office'])
                #process_and_send_to_queue(office, channel)
                data_tracker.update_data_usage(res_size)

                if '@odata.nextLink' in office:  # to check next link of page available
                    parsed_url = urlparse(office['@odata.nextLink'])
                    query_params = parse_qs(parsed_url.query)
                    skip_value = query_params.get('$skip', [None])[0]
                    skip=skip_value
                    prepare_metadata(None,None,office,None,metadata_xml)
                else:
                    if office:
                        prepare_metadata(None,None,office,None,metadata_xml)
                    break;
                
                time.sleep(1)

            else:
                logger.error("You have download Maximum Data in an hour!!")

        else:
            logger.warning("Near to exceed Rate Limit!!")

    skip='0'
    
    while True:
       
        if rate_rps.allow_request() and rate_hourly.allow_request() and rate_daily.allow_request():
            
            if data_tracker.check_data_usage():

                openhouse,res_size = fetch_openhouse_data(last_time['OpenHouse'])
                #process_and_send_to_queue(openhouse, channel)
                data_tracker.update_data_usage(res_size)

                if '@odata.nextLink' in openhouse:  # to check next link of page available

                    parsed_url = urlparse(openhouse['@odata.nextLink'])
                    query_params = parse_qs(parsed_url.query)
                    skip_value = query_params.get('$skip', [None])[0]
                    skip=skip_value
                    prepare_metadata(None,None,None,openhouse,metadata_xml)
                else:
                    if openhouse:
                        prepare_metadata(None,None,None,openhouse,metadata_xml)
                    break;
                
                time.sleep(1)

            else:
                logger.error("You have download Maximum Data in an hour!!")

        else:
            logger.warning("Near to exceed Rate Limit!!")
    
    
        
if __name__ == "__main__":
    main()


#logger.disabled=False