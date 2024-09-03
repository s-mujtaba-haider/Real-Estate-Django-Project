from pymongo import MongoClient
import spacy
from spacy.training import Example
import ast
import requests

nlp = spacy.load("en_core_web_sm")

try:
    client = MongoClient('mongodb://192.168.8.100:27020/')
    db = client['storage']  # database name
    collection = db['address']
except Exception as e:
    print("Error connecting to MongoDB:", e)

def load_addresses():

    with open('addresses.txt','r') as file:
        addr_str= file.read()
    
    addr_list = ast.literal_eval(addr_str)

    return addr_list


def train_model(training_data):
    nlp = spacy.blank("en") 
    ner = nlp.add_pipe("ner")
    new_labels = ['STREET_NUMBER','STREET_NAME','CITY', 'STATE', 'ZIP']
    for label in new_labels:
        ner.add_label(label)
    
    optimizer = nlp.begin_training()
    for text, annotations in training_data:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], sgd=optimizer)
    
    return nlp

# Extract entities from user query
def extract_entities(user_query, nlp):
    doc = nlp(user_query)
    entities = {}
    for ent in doc.ents:
        entities[ent.label_] = ent.text
    return entities

def build_mongo_query(entities):
    print(entities)
    entity_to_field_mapping = {
    "STREET_NUMBER": "street_number",
    "STREET_NAME": "street_name",
    "CITY": "city",
    "STATE": "state",
    "ZIP": "zip_code"
    }
    query = {}

    for entity, value in entities.items():
        if entity in entity_to_field_mapping:
                field = entity_to_field_mapping[entity]
                if entity=='STREET_NAME':
                    query[field] = ' '+value
                else:
                    query[field] = value
    return query


def handle_user_query(extract_ent):
    mongo_query = build_mongo_query(extract_ent)
    results = collection.find(mongo_query)
    return list(results)


if __name__ == "__main__":
    
    training_data = load_addresses()
    trained_nlp = train_model(training_data)
    user_query = " in which year 3340 Colfax Ave S, Minneapolis, MN 55408 built?"
    extracted_entities = extract_entities(user_query, trained_nlp)
    address_results = handle_user_query(extracted_entities)
    #properties=get_properties(address_results)
    #print(properties)

    # for result in properties:
    #     print(result)