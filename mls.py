import requests
import mysql.connector
import xml.etree.ElementTree as ET


# Database configuration
db_config = {
    'user': 'root',
    'unix_socket': '/var/run/mysqld/mysqld.sock',
    'database': 'northstar2',
    'password': 'db_root'
}


# API Setup
api_url = "https://api.mlsgrid.com/v2"
#api_key = "afe39048e8e4fd9d448f13e5c1a9baa2521088e2"
api_key = "21c353c022c196e275c13cff9aefd48f4e8813b5"

# Function to fetch and parse metadata as XML
def fetch_metadata():
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {'$filter': "OriginatingSystemName eq 'northstar'"}
    metadata_url = f'{api_url}/$metadata'
    response = requests.get(metadata_url, headers=headers, params=params)
    print(f'Requesting metadata: {response.url}')
    if response.status_code == 200:
        print(f"API Response: {response.text}")
        try:
            return ET.fromstring(response.content)
        except ET.ParseError as e:
            print(f"Error parsing XML: {e}")
            return None
    else:
        print(f"Error fetching metadata: {response.status_code}")
        print(f"Response content: {response.text}")
        return None

# Function to map MLS Grid data types to MySQL data types
def map_data_types(mls_type, max_length):
    if mls_type in ['Edm.String', 'Collection(Edm.String)']:
        return 'TEXT' if max_length is None or int(max_length) > 40 else f'VARCHAR({max_length})'
    mapping = {
        'Edm.Int16': 'SMALLINT',
        'Edm.Int32': 'INT',
        'Edm.Boolean': 'BOOLEAN',
        'Edm.DateTimeOffset': 'DATETIME',
        'Edm.Decimal': 'DECIMAL(18,4)',
        'Edm.Int64': 'BIGINT',
        'Edm.Date': 'DATE',
    }
    return mapping.get(mls_type, 'TEXT')
# Function to find the primary key from metadata
def find_primary_key(entity_type):
    key = entity_type.find(".//{http://docs.oasis-open.org/odata/ns/edm}Key")
    if key is not None:
        return key.find("{http://docs.oasis-open.org/odata/ns/edm}PropertyRef").get('Name')
    return None

# Function to generate CREATE TABLE statement from metadata
def generate_create_table_statement(resource_name, properties, primary_key):
    field_statements = []
    primary_key_type = None
    primary_key_max_length = None

    for prop in properties:
        name = prop['Name']
        mls_type = prop['Type']
        max_length = prop.get('MaxLength')
        mysql_type = map_data_types(mls_type, max_length)
        field_statements.append(f"{name} {mysql_type}")

        if name == primary_key:
            primary_key_type = mysql_type
            primary_key_max_length = max_length

    # Handle primary key for TEXT or BLOB fields
    if primary_key_type in ['TEXT', 'BLOB']:
        key_length = min(int(primary_key_max_length), 255) if primary_key_max_length else 255
        key_statement = f"PRIMARY KEY({primary_key}({key_length}))"
    else:
        key_statement = f"PRIMARY KEY({primary_key})"

    fields_sql = ',\n'.join(field_statements + [key_statement])
    return f"CREATE TABLE IF NOT EXISTS {resource_name} (\n{fields_sql}\n) ROW_FORMAT=DYNAMIC;"

# Function to create table in MySQL
def create_table_in_mysql(create_statement):
    
    try:
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        cursor.execute(create_statement)
        cnx.commit()
        print(f"Executed create statement: {create_statement}")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()

# Main function to process metadata
def main():
    metadata_xml = fetch_metadata()
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
            print(properties,"______________-----")
            primary_key = find_primary_key(entity_type)
            create_statement = generate_create_table_statement(resource_name, properties, primary_key)
            create_table_in_mysql(create_statement)

if __name__ == "__main__":
    main()
