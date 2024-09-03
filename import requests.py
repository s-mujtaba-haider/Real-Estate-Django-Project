import requests

# url = 'http://192.168.8.100:50001/api/v1/buyer_seller/'
# headers = {
#     'accept': 'application/json',
#     'Content-Type': 'application/json',
# }
# data = {
#     "delimiter": 10
# }

# response = requests.post(url, headers=headers, json=data)

# print(response.status_code)
# print(response.json())

from huggingface_hub import login
login(token='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')

import json
import torch
from torch import cuda, bfloat16
from accelerate import init_empty_weights, infer_auto_device_map
from transformers import AutoModelForCausalLM, AutoConfig,BitsAndBytesConfig,pipeline,AutoTokenizer

# Load the tokenizer
#access_token = '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'
access_token ='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'
model = "meta-llama/Llama-2-7b-hf"

#model= 'meta-llama/Llama-2-7b-chat-hf'
#device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'

#model_name = "meta-llama/Llama-2-13b-chat-hf"
model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
#model_name = "mistralai/Mistral-7B-Instruct-v0.2"

# Check if CUDA is available and set the device accordingly
# device = f'cuda:{torch.cuda.current_device()}' if torch.cuda.is_available() else 'cpu'
# print(device)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load the model
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
if torch.cuda.device_count() > 1:
    print("Using", torch.cuda.device_count(), "GPUs!")
    model = torch.nn.DataParallel(model)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("device is", device)
model.to(device)


# Create the pipeline for text generation
text_gen_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

data={
    "properties": [
        {
            "abovegradefinishedarea": 1215.0,
            "accessibilityfeatures": "None",
            "basement": "Full",
            "basementyn": 1,
            "bathroomsfull": 2,
            "bathroomstotalinteger": 2,
            "bedroomstotal": 3,
            "belowgradefinishedarea": 390.0,
            "buyeragencycompensation": "2.70",
            "buyeragencycompensationtype": "%",
            "buyeragentkey": "NST107452",
            "buyeragentmlsid": "NST502046851",
            "buyerfinancing": "Cash",
            "buyerofficekey": "NST49277",
            "buyerofficemlsid": "NST49277",
            "buyerofficename": "Realty Group LLC",
            "city": "Minneapolis",
            "closedate": "2022-09-23",
            "closeprice": 224900.0,
            "colistagentfullname": "John Newhall",
            "colistagentkey": "NST96198",
            "transactionbrokercompensation": "0.0000",
            "transactionbrokercompensationtype": "%",
            "watersource": "City Water/Connected",
            "yearbuilt": 1909,
            "zoningdescription": "Residential-Single Family",
            "room": [
                {
                    "nst_roomsortorder": "2",
                    "roomdimensions": "13x11",
                    "roomkey": "NST107516287",
                    "roomlevel": "Main",
                    "roomtype": "Dining Room",
                    "listingid": "NST6252617"
                },
                {
                    "nst_roomsortorder": "3",
                    "roomdimensions": "9x18",
                    "roomkey": "NST107516288",
                    "roomlevel": "Lower",
                    "roomtype": "Family Room",
                    "listingid": "NST6252617"
                },
                {
                    "nst_roomsortorder": "9",
                    "roomdimensions": "9x18",
                    "roomkey": "NST107516289",
                    "roomlevel": "Lower",
                    "roomtype": "Family Room",
                    "listingid": "NST6252617"
                },
                {
                    "nst_roomsortorder": "5",
                    "roomdimensions": "9x13",
                    "roomkey": "NST107516290",
                    "roomlevel": "Main",
                    "roomtype": "Bedroom 1",
                    "listingid": "NST6252617"
                },
                {
                    "nst_roomsortorder": "4",
                    "roomdimensions": "9x10",
                    "roomkey": "NST107516291",
                    "roomlevel": "Main",
                    "roomtype": "Kitchen",
                    "listingid": "NST6252617"
                },
                {
                    "nst_roomsortorder": "1",
                    "roomdimensions": "14x13",
                    "roomkey": "NST107516292",
                    "roomlevel": "Main",
                    "roomtype": "Living Room",
                    "listingid": "NST6252617"
                },
                {
                    "nst_roomsortorder": "6",
                    "roomdimensions": "10x12",
                    "roomkey": "NST107516293",
                    "roomlevel": "Main",
                    "roomtype": "Bedroom 2",
                    "listingid": "NST6252617"
                },
                {
                    "nst_roomsortorder": "7",
                    "roomkey": "NST107516294",
                    "roomlevel": "Upper",
                    "roomtype": "Bedroom 3",
                    "listingid": "NST6252617"
                }
            ]
        },
        {
            "abovegradefinishedarea": 1315.0,
            "accessibilityfeatures": "None",
            "basement": "Finished",
            "basementyn": 1,
            "belowgradefinishedarea": 800.0,
            "buyeragencycompensation": "2.70",
            "buyeragencycompensationtype": "%",
            "buyeragentkey": "NST57259",
            "buyeragentmlsid": "NST496503609",
            "buyerfinancing": "Conventional",
            "buyerofficekey": "NST16638",
            "buyerofficemlsid": "NST5116",
            "buyerofficename": "Coldwell Banker Realty",
            "carportspaces": 3.0,
            "city": "Minneapolis",
            "closedate": "2023-12-14",
            "closeprice": 450000.0,
            "concessionsamount": 5000,
            "constructionmaterials": "Block, Vinyl Siding",
            "contingency": "None",
            "countyorparish": "Hennepin",
            "cumulativedaysonmarket": 49,
            "daysonmarket": 49,
            "directions": "Hennepin Ave to 33rd St So. East to Colfax and then South to house",
            "foundationarea": 1015.0,
            "heating": "Boiler",
            "highschooldistrict": "Minneapolis",
            "internetaddressdisplayyn": 1,
            "internetautomatedvaluationdisplayyn": 1,
            "internetconsumercommentyn": 1,
            "internetentirelistingdisplayyn": 1,
            "latitude": 44.9417,
            "levels": "One and One Half",
            "listagentfullname": "Hizzle\u00ae @ SP Real Estate",
            "listagentkey": "NST107452",
            "listagentmlsid": "NST502046851",
            "listagentofficephone": "612-888-5888",
            "listingagreement": "Exclusive Right To Sell",
            "listingcontractdate": "2023-10-11",
            "listingid": "NST6446482",
            "listingkey": "NST7294978",
            "listingterms": "Conventional Rehab, Conventional, Trade, FHA, FHA Rehab 203k, Cash",
            "listofficekey": "NST49277",
            "listofficemlsid": "NST49277",
            "listofficename": "Realty Group LLC",
            "listprice": 450000.0,
            "livingarea": 2115.0,
            "longitude": -93.2924,
            "lotfeatures": "Tree Coverage - Light",
            "lotsizearea": 0.12,
            "lotsizedimensions": "40 X 129",
            "lotsizeunits": "Acres",
            "mapcoordinate": "120-C1",
            "mapcoordinatesource": "King's Street Atlas",
            "mlgcanuse": "IDX, VOW, BO",
            "mlgcanview": 1,
            "modificationtimestamp": "2024-03-06T21:32:03+00:00",
            "nst_abovegradesqfttotal": "1315.0000",
            "nst_agentowner": "Yes",
            "nst_ageofproperty": "115",
            "nst_assessmentpending": "No",
            "nst_assumablemortgage": "Not Assumable",
            "nst_belowgradesqfttotal": "1015.0000",
            "nst_bonusyn": "No",
            "nst_constructionmaterialsdesc": "Timber/Post & Beam,Brick",
            "nst_dpresource": "Y",
            "nst_expenses": "0.0000",
            "nst_foreclosurestatus": "No",
            "nst_foundationdimensions": "1015",
            "nst_fractionalownershipyn": "No",
            "nst_fuel": "Natural Gas",
            "nst_garagedimensions": "0",
            "nst_garagedoorheight": "0",
            "nst_garagedoorwidth": "0",
            "nst_garagesquarefeet": "0",
            "nst_incomemiscann": "0.0000",
            "nst_incomemiscmon": "0.0000",
            "nst_internetoptions": "Cable,DSL,Fiber Optic,Satellite",
            "nst_lastupdatedate": "2024-03-06",
            "nst_lenderowned": "No",
            "nst_mainlevelfinishedarea": "1015.0000",
            "nst_neighborhoodnumber": "South Uptown",
            "nst_officeboard": "SPAAR",
            "nst_owneroccupied": "No",
            "nst_potentialshortsale": "No",
            "nst_presentuse": "Yearly",
            "nst_proposedtitledate": "2023-12-14",
            "nst_rangenum": "Two",
            "nst_refrigeratornum": "Two",
            "nst_rentallicenseyn": "No",
            "nst_schooldistrictnumber": "1",
            "nst_schooldistrictphone": "612-668-0000",
            "nst_sqfttotal": "2330.00",
            "nst_taxwithassessments": "3941.0000",
            "numberofunitstotal": 2,
            "occupanttype": "Owner",
            "offmarketdate": "2023-11-29",
            "originalentrytimestamp": "2023-10-11T17:03:43+00:00",
            "originallistprice": 450000.0,
            "originatingsystemmodificationtimestamp": "2024-03-06T21:30:38+00:00",
            "originatingsystemname": "northstar",
            "ownerpays": "None",
            "parcelnumber": "0402824140173",
            "parkingfeatures": "Carport, Guest Parking, Parking Lot",
            "photoschangetimestamp": "2024-03-06T21:32:03+00:00",
            "photoscount": 39,
            "postalcity": "Minneapolis",
            "postalcode": "55408",
            "privateremarks": "House was converted into a legal duplex with permits. Almost everything is new! \n\nSome photos virtually altered. All measurements approximate.",
            "propertysubtype": "Duplex Up and Down",
            "propertytype": "Residential Income",
            "publicremarks": "Discover 3340 Colfax Ave S, where historic charm meets modern convenience. This converted duplex, upgraded in September 2023, presents a golden investment opportunity. Recent enhancements encompass a new roof, electrical, plumbing, and luxurious interiors in both units, ensuring immediate occupancy & rental income.\n\nThe main-floor apartment boasts a fully revamped kitchen, bathroom, and energy-efficient LED lighting. Meanwhile, the garden-level apartment dazzles with a fresh kitchen, remodeled bathroom, and in-unit laundry. Privacy and serenity are guaranteed with a new staircase and sound/fire barrier between units.\n\nEmbrace versatility, whether you prefer owner occupancy with rental income or leasing both units for a savvy investment. With parking for 2-3 cars and a coveted Uptown location, this property is a rare treasure. Seize the chance to own this income-generating gem in Minneapolis' most sought-after neighborhoods!\n\nSome photos virtually altered. All measurements approximate.",
            "publicsurveyrange": "24",
            "publicsurveysection": "04",
            "publicsurveytownship": "28",
            "purchasecontractdate": "2023-12-04",
            "roadfrontagetype": "City Street",
            "roadresponsibility": "Public Maintained Road",
            "roof": "Age 8 Years or Less, Architecural Shingle",
            "sewer": "City Sewer/Connected",
            "sourcesystemname": "RMLS",
            "standardstatus": "Closed",
            "stateorprovince": "MN",
            "streetdirsuffix": "S",
            "streetname": "Colfax",
            "streetnumber": "3340",
            "streetnumbernumeric": 3340,
            "streetsuffix": "Avenue",
            "subagencycompensation": "0.00",
            "subagencycompensationtype": "%",
            "subdivisionname": "Remingtons 2nd Add",
            "taxannualamount": 3941.0,
            "taxlegaldescription": "LOT 004 BLOCK 045 REMINGTONS 2ND ADDN TO MPLS",
            "taxyear": 2023,
            "tenantpays": "Cable TV, Electricity",
            "topography": "Level",
            "transactionbrokercompensation": "0.0000",
            "transactionbrokercompensationtype": "%",
            "watersource": "City Water/Connected",
            "yearbuilt": 1909,
            "zoningdescription": "Residential-Multi-Family",
            'agent': [{'agent_uuid': '28fe1e0c-a11c-4895-8096-0ba0d6f1e8d1', 'personal_details': {'full_name': 'Caryn E Gerber'}, 'contact_info': {'email': '', 'phone': {'phone1': '2185910564'}}, 'address_linked': ['03dc5de1-a436-44d5-beeb-3123823d6a6d', 'e7742115-90c8-49ef-9e94-b5eef2e0560a'], 'roles': {'role': 'Buyer'}, 'source_url': 'mysql-database[ecrv_db]', 'source_domain': 'ecrv_db', 'created_at': '2024-05-26 10:09:03.027346', 'last_modified': '2024-05-26 10:09:03.027348', 'party_id': '10457'}, {'agent_uuid': '371216cd-5a13-4490-b53d-d853852bd4bb', 'personal_details': {'full_name': 'Kelly Roewkamp'}, 'contact_info': {'email': '', 'phone': {'phone1': '5076967967'}}, 'address_linked': ['3854e2ae-afa0-446d-931e-fe53ec8c020b', '7fd6e87e-4962-48e6-bf78-33d759948849'], 'roles': {'role': 'Buyer'}, 'source_url': 'mysql-database[ecrv_db]', 'source_domain': 'ecrv_db', 'created_at': '2024-05-26 10:09:03.605757', 'last_modified': '2024-05-26 10:09:03.605758', 'party_id': '10458'}, {'agent_uuid': '6ddf6a87-1ac3-4bf6-ac2a-1cb8692dbc00', 'personal_details': {'full_name': 'Christopher A Nordine'}, 'contact_info': {'email': '', 'phone': {'phone1': '5075136820'}}, 'address_linked': ['e86d2716-b7a7-4a26-a511-ee1916389097', '4958fe9d-1653-4065-a83a-af148d933373'], 'roles': {'role': 'Seller'}, 'source_url': 'mysql-database[ecrv_db]', 'source_domain': 'ecrv_db', 'created_at': '2024-05-26 10:09:03.957306', 'last_modified': '2024-05-26 10:09:03.957307', 'party_id': '10459'}, {'agent_uuid': '48a7a70d-55e5-44ad-a93e-cf0b824ef4bf', 'personal_details': {'full_name': 'Heather Nordine'}, 'contact_info': {'email': '', 'phone': {'phone1': '5075136820'}}, 'address_linked': ['faa796e5-488a-46d1-a20e-a699bf9ad6e2', '1409110b-385f-40dc-aea2-f65bba9d71da'], 'roles': {'role': 'Seller'}, 'source_url': 'mysql-database[ecrv_db]', 'source_domain': 'ecrv_db', 'created_at': '2024-05-26 10:09:04.300594', 'last_modified': '2024-05-26 10:09:04.300596', 'party_id': '10460'}, {'agent_uuid': 'c965867e-7760-494d-a518-8a959a5f7fb9', 'personal_details': {'full_name': 'Trevor D Pugleasa'}, 'contact_info': {'email': '', 'phone': {'phone1': '7632808508'}}, 'address_linked': ['e5bb58f3-e7c2-4530-8aa7-f2e64995a422', '4903553f-8d44-4925-aaea-b6e5022abb2b'], 'roles': {'role': 'Buyer'}, 'source_url': 'mysql-database[ecrv_db]', 'source_domain': 'ecrv_db', 'created_at': '2024-05-26 10:09:05.053654', 'last_modified': '2024-05-26 10:09:05.053655', 'party_id': '10461'}, {'agent_uuid': '6a9acafc-97d2-49d2-bd60-3aa000b2fc2c', 'personal_details': {'full_name': 'Cherie A Bridges'}, 'contact_info': {'email': '', 'phone': {'phone1': '2183914204'}}, 'address_linked': ['24ff88bc-9668-4f90-a803-f4da9e073aff', 'd87630b7-ae19-46b0-a8ac-b538a463a832'], 'roles': {'role': 'Seller'}, 'source_url': 'mysql-database[ecrv_db]', 'source_domain': 'ecrv_db', 'created_at': '2024-05-26 10:09:05.534675', 'last_modified': '2024-05-26 10:09:05.534676', 'party_id': '10462'}, {'agent_uuid': 'eefec6f0-74b0-44dd-94f5-9a3ad199375c', 'personal_details': {'full_name': 'Megan M. Pugleasa'}, 'contact_info': {'email': '', 'phone': {'phone1': '7632808508'}}, 'address_linked': ['bc79c662-5496-4365-85ba-9652c31803b4', 'c5b97729-750d-440e-ae1b-26777acb0d51'], 'roles': {'role': 'Buyer'}, 'source_url': 'mysql-database[ecrv_db]', 'source_domain': 'ecrv_db', 'created_at': '2024-05-26 10:09:05.877735', 'last_modified': '2024-05-26 10:09:05.877737', 'party_id': '10463'}, {'agent_uuid': 'ec2f72fb-a296-4d06-abdb-db035184583d', 'personal_details': {'full_name': 'The Trust Agreement of Wallace and Barbara Smida'}, 'contact_info': {'email': '', 'phone': {'phone1': '7632227107'}}, 'address_linked': ['ebe58035-0ae2-48bd-90e6-f17a04befa54', 'ae737231-7253-4840-8154-b7bff8beed86'], 'roles': {'role': 'Seller'}, 'source_url': 'mysql-database[ecrv_db]', 'source_domain': 'ecrv_db', 'created_at': '2024-05-26 10:09:06.340895', 'last_modified': '2024-05-26 10:09:06.340897', 'party_id': '10464'}, {'agent_uuid': 'fc6afe71-7acf-415b-9316-292957f3dbd2', 'personal_details': {'full_name': 'Jerome Edwin Schultz'}, 'contact_info': {'email': '', 'phone': {'phone1': '6519554325'}}, 'address_linked': ['837ff598-9454-40eb-a146-598f36012e4e', '4b4591b7-c8f5-43e2-bd75-6096c37e2d84'], 'roles': {'role': 'Buyer'}, 'source_url': 'mysql-database[ecrv_db]', 'source_domain': 'ecrv_db', 'created_at': '2024-05-26 10:09:06.970911', 'last_modified': '2024-05-26 10:09:06.970913', 'party_id': '10465'}, {'agent_uuid': 'da46cd06-6516-4544-ac5d-ee4841469200', 'personal_details': {'full_name': 'Henry David Woeltge'}, 'contact_info': {'email': '', 'phone': {'phone1': '6514295075'}}, 'address_linked': ['7a6d9836-7649-415f-9a66-be6c7c1bd55d', '3dbc51e1-79f1-447c-b954-c646c1c4aa6c'], 'roles': {'role': 'Seller'}, 'source_url': 'mysql-database[ecrv_db]', 'source_domain': 'ecrv_db', 'created_at': '2024-05-26 10:09:07.350304', 'last_modified': '2024-05-26 10:09:07.350305', 'party_id': '10466'}],
            "room": [
                {
                    "nst_roomsortorder": "1",
                    "roomdimensions": "10.8x11.6",
                    "roomkey": "NST112646655",
                    "roomlevel": "Main",
                    "roomtype": "Family Room",
                    "listingid": "NST6446482"
                },
                {
                    "nst_roomsortorder": "2",
                    "roomdimensions": "9.4x11.6",
                    "roomkey": "NST112646656",
                    "roomlevel": "Main",
                    "roomtype": "Dining Room",
                    "listingid": "NST6446482"
                },
                {
                    "nst_roomsortorder": "3",
                    "roomdimensions": "13.3x20",
                    "roomkey": "NST112646657",
                    "roomlevel": "Main",
                    "roomtype": "Family Room",
                    "listingid": "NST6446482"
                },
                {
                    "nst_roomsortorder": "4",
                    "roomdimensions": "9.4x13.1",
                    "roomkey": "NST112646658",
                    "roomlevel": "Upper",
                    "roomtype": "Bedroom 1",
                    "listingid": "NST6446482"
                },
                {
                    "nst_roomsortorder": "5",
                    "roomdimensions": "10.1x12",
                    "roomkey": "NST112646659",
                    "roomlevel": "Upper",
                    "roomtype": "Bedroom 2",
                    "listingid": "NST6446482"
                },
                {
                    "nst_roomsortorder": "6",
                    "roomdimensions": "12x16.4",
                    "roomkey": "NST112646660",
                    "roomlevel": "Upper",
                    "roomtype": "Bedroom 3",
                    "listingid": "NST6446482"
                },
                {
                    "nst_roomsortorder": "7",
                    "roomdimensions": "11.5x20.6",
                    "roomkey": "NST112646661",
                    "roomlevel": "Lower",
                    "roomtype": "Bedroom 4",
                    "listingid": "NST6446482"
                }
            ]
        }
    ]
}

# prompt = (
#    'Hi! you are the helpful assistantm extract the only value which is being asked in the question donot give whole data\n' 'Provided data: '+str(data)
# )
question="who is the last owner of 3340 Colfax Avenue South, Minneapolis, MN 55408?"
prompt=f"""[INST] <<SYS>>
'Hi! you are the helpful assistant. extract the only correct value carefully, give answer user friendly,  which is being asked in the question donot give whole data\n' 'Provided data from api: '{str(data)}<</SYS>>

{question} [/INST]""" 
# Generate text
sequences = text_gen_pipeline(
    prompt,
    num_return_sequences=1,
    do_sample=True,
    max_new_tokens=4096,
)

# Print the generated text
print(sequences[0]['generated_text'])

# property_address = "3340 Colfax Ave S"
# context = """
# {
#     "abovegradefinishedarea": 1215.0,
#     "bathroomsfull": 2,
#     "bathroomstotalinteger": 2,
#     "bedroomstotal": 3,
#     "yearbuilt": 1909,
#     "city": "Minneapolis",
#     "closedate": "2022-09-23",
# }
# """

# # Construct the input prompt with question and context
# input_prompt = f"question: In which year was {property_address} built? context: {context}"

# # Tokenize the input text
# input_ids = tokenizer.encode(input_prompt, return_tensors="pt", truncation=True, max_length=8192)  # Move input tensor to device

# # Generate the output
# output_ids = model.generate(input_ids, max_new_tokens=50, num_return_sequences=1)

# # Decode the output
# output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# print(output_text)
