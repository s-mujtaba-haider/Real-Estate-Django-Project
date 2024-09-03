from pymongo import MongoClient
import re
import spacy

nlp = spacy.load("en_core_web_sm")
# from spacy.training import offsets_to_biluo_tags
# text = "Suite B WEST SPRINGFIELD MA 01089"
# entities = [(0, 4, "STREET_NUMBER"), (5, 14, "STREET_NAME"), (15, 26, "CITY"), (27, 29, "STATE"), (30, 35, "ZIP")]
# biluo_tags = spacy.training.offsets_to_biluo_tags(nlp.make_doc(text), entities)
# print(list(zip(text.split(), biluo_tags)))

# training_data = [
    # ("2738 Emerson Ave S Minneapolis MN 55408", {"entities": [(0, 4, "STREET_NUMBER"), (5, 18, "STREET_NAME"), (19, 30, "CITY"), (31, 33, "STATE"), (34, 39, "ZIP")]}),
    # ("3340 Colfax Ave S Minneapolis MN 55408", {"entities": [(0, 4, "STREET_NUMBER"), (5, 17, "STREET_NAME"), (18, 29, "CITY"), (30, 32, "STATE"), (33, 38, "ZIP")]}),
    # ("190 University Drive Amherst MA 01002", {"entities": [(0, 3, 'STREET_NUMBER'), (4, 20, 'STREET_NAME'), (21, 28, 'CITY'), (29, 31, 'STATE'), (32, 37, 'ZIP')]}),
    # ("22 Hartford Avenue Granby CT 06035", {"entities": [(0, 2, 'STREET_NUMBER'), (3, 18, 'STREET_NAME'),(19, 25, 'CITY'), (26, 28, 'STATE'), (29, 34, 'ZIP')]}),
    # ("136 Dwight Rd Longmeadow MA 01106", {"entities":[(0, 3, "STREET_NUMBER"), (4, 13, "STREET_NAME"), (14, 24, "CITY"), (25, 27, "STATE"), (28, 33, "ZIP")]}),
    # ("3536 1st Ave S Minneapolis MN 55408", {"entities": [(0, 4, "STREET_NUMBER"), (5, 14, "STREET_NAME"), (15, 26, "CITY"), (27, 29, "STATE"), (30, 35, "ZIP")]}),
    # ]

def clean_string(input_string):

    clean_address=[]

    for address in input_string:
        cleaned_string = re.sub('[,.]', '', address)
        cleaned_string = re.sub(r'\s+', ' ', cleaned_string)
        if '669' not in cleaned_string:
            clean_address.append(cleaned_string)
        else:
            print(cleaned_string)
    
    return clean_address

def rearrange(training_data):

    new_labels = ['STREET_NUMBER', 'STREET_NAME', 'CITY', 'STATE', 'ZIP']

    rearranged_training_data = []

    for text, annotations in training_data:
        entities = annotations['entities']
        rearranged_entities = []
        for label in new_labels:
            for entity in entities:
                if entity[2] == label:
                    rearranged_entities.append(entity)
                    break
        rearranged_training_data.append((text, {'entities': rearranged_entities}))
    
    return rearranged_training_data


def get_addresses():
    list_addr=[]
    try:
        client = MongoClient('mongodb://192.168.8.100:27020/')
        db = client['storage']  # database name
        collection = db['address']
        cursor = collection.find().limit(300)
        print(cursor[0])
        for document in cursor:
            if document['street_number'] and document['street_name'] and document['city'] and document['state'] and document['zip_code']:
                list_addr.append(document['street_number']+' '+document['street_name']+' '+document['city']+' '+document['state']+' '+document['zip_code'])
        with open('usaddress.txt','w') as file:
             file.write(str(list_addr))
             
    except Exception as e:
        print("Error connecting to MongoDB:", e)
    
    return list_addr

def label_entities(sentence):
    words = sentence.split()
    entities = []
    start = 0
    for word in words:
        end = start + len(word)
        entities.append((start, end, get_label(word,words)))
        start = end + 1  # Add 1 for the space between words
    return entities

def get_label(word,words):

    if words[0]==word: # first word
        return "STREET_NUMBER"
    elif words[-1]==word: # last word
        return "ZIP"
    elif words[-2]==word:
        return "STATE"
    elif words[-3]==word:
        return "CITY"
    else:
        return "STREET_NAME"

def reset_entities(entities):

    start_index = None
    for entity in entities:
        if entity[2] == 'STREET_NAME':
            start_index = entity[0]
            break

    # Find end index of last occurrence of STREET_NAME
    end_index = None
    for entity in reversed(entities):
        if entity[2] == 'STREET_NAME':
            end_index = entity[1]
            break

    # Update the list of entities
    updated_entities = []
    for entity in entities:
        if entity[2] != 'STREET_NAME':
            updated_entities.append(entity)

    # Append a single occurrence of STREET_NAME with the start and end indices
    updated_entities.append((start_index, end_index, 'STREET_NAME'))
    return updated_entities

def format_training_data(sentence, entities):
    training_data = {"entities": []}
    for entity in entities:
        training_data["entities"].append((entity[0], entity[1], entity[2]))
    return (sentence, training_data)

if __name__ == "__main__":
    addr=get_addresses()
    clean_addr=clean_string(addr)
    ent_addr=[]
    for address in clean_addr:
        ent= label_entities(address)
        re_ent=reset_entities(ent)
        formatted_data = format_training_data(address, re_ent)
        ent_addr.append(formatted_data)
    
    # b_tags_clear=b_tags(ent_addr)
    arrange_addr=rearrange(ent_addr)

    with open('addresses.txt','w') as file:
        file.write(str(arrange_addr))