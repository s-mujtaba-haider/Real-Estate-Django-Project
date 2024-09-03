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
from accelerate import Accelerator
from transformers import AutoModelForCausalLM,BitsAndBytesConfig,pipeline,AutoTokenizer

url = 'http://192.168.8.100:50001/api/v1/buyer_seller/'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    "delimiter": 10
}

response = requests.post(url, headers=headers, json=data)
owner=response.json()

# Load the tokenizer
#access_token = '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'
access_token ='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'
#model = "meta-llama/Llama-2-7b-hf"

model_name='meta-llama/Llama-2-70b-chat-hf'
#device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'

#model_name = "meta-llama/Llama-2-13b-chat-hf"
#model_name = "meta-llama/Meta-Llama-3-8B-Instruct"


# Check if CUDA is available and set the device accordingly
# device = f'cuda:{torch.cuda.current_device()}' if torch.cuda.is_available() else 'cpu'
# print(device)


# Define the quantization configuration
bnb_config = BitsAndBytesConfig(
    load_in_8bit=True,  # Enable 8-bit quantization
    load_in_4bit=False,  # Disable 4-bit quantization (optional)
    llm_int8_threshold=6.0,  # Threshold for mixed precision
)


tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name,torch_dtype=torch.float16, device_map='auto' )


text_gen_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map='auto' 
)

data={
  "data": [
    {
      "common_property_data": {
        "sale_price": "224900.0",
        "year_built": "1909",
        "lot_size": "5227",
        "city": "Minneapolis",
        "state": "MN",
        "zip_code": "55408",
        "county": "Hennepin"
      },
      "unique_property_data": [
        {
          "source_url": "https://gis-hennepin.hub.arcgis.com/datasets/county-parcels/",
          "source_domain": "https://gis-hennepin.hub.arcgis.com/datasets/",
          "address_uuid": "8c21db1c-d15b-4d53-98d2-45ec46a354b8",
          "internal_property_id": "05219229-b1f9-4b8d-98dc-0b4edee54ec4",
          "property_id": "402824140173",
          "property_type": "RESIDENTIAL",
          "estimated_taxes": {
            "total_tax": "4168.56"
          },
          "high_school": "1",
          "property_sub_type": "RESIDENTIAL",
          "created_at": "2024-05-18 19:12:41.379472"
        },
        {
          "address_uuid": "01fc15b2-14e7-445d-a759-c8290377da0c",
          "bedroom_count": "0",
          "square_footage": {
            "finished": "2115",
            "total": 2115
          },
          "property_type": "Single Family Residence",
          "listing_id": "1419628595645064817",
          "list_office_information": "Listing Courtesy of Realty Group LLC",
          "list_price": "450000",
          "close_price": "450000",
          "parking_total": "3",
          "property_condition": "Closed",
          "subdivision_name": "CARAG",
          "unit_style": "Single Family Residence",
          "utilities": "['Air Conditioning', 'Basement', 'Carport Parking', 'Laundry', 'Parking Included', 'Parking Lot']",
          "waterfront": "False",
          "source_url": "https://www.compass.com/homes-for-sale/7425/status=coming-soon,active,contract-out,contract-signed,contingencies-dropped,sold/sold-date=any-time/start=19681/",
          "source_domain": "www.compass.com",
          "last_modified": "2024-04-20 15:12:48.434704",
          "created_at": "2024-04-20 15:12:48.434705",
          "pageLink": "/listing/3340-colfax-avenue-south-minneapolis-mn-55408/1419628595645064817/",
          "internal_property_id": "4987b629-d83f-4551-9976-43b998736b7d",
          "external_property_id": "63821633830314770"
        },
        {
          "address_uuid": "5b1b4439-7dcb-4142-8943-e27516f219cc",
          "bedroom_count": "3",
          "bathrooms": "1.0",
          "square_footage": {
            "finished": "1215"
          },
          "property_type": "6",
          "pool": "False",
          "close_price": "436898.43",
          "property_condition": "Sold",
          "source_url": "https://www.redfin.com/stingray/api/home/details/aboveTheFold?accessLevel=1&propertyId=51292165",
          "source_domain": "www.redfin.com",
          "last_modified": "2024-04-20 19:13:01.183408",
          "created_at": "2024-04-20 19:13:01.183447",
          "pageLink": "www.redfin.com/MN/Minneapolis/3340-Colfax-Ave-S-55408/home/51292165",
          "internal_property_id": "110cad97-5fa0-4ef7-9d6e-1dc495c0cf81",
          "external_property_id": 51292165
        },
        {
          "internal_property_id": "2c74aef0-f2ec-4723-aeed-5aef8db1096b",
          "address_uuid": "23ec4a7e-0888-41a3-9adf-711efafade25",
          "property_type": "Residential - Residential Homestead",
          "estimated_taxes": {
            "total_tax": "$0.00"
          },
          "new_construction": "No",
          "parcel_number": "04-028-24-14-0173",
          "property_sub_type": "Residential / Single family home",
          "source_url": "mysql-database[ecrv_db]",
          "source_domain": "ecrv_db",
          "last_modified": "2024-05-28 12:43:43.095185",
          "created_at": "2024-05-28 12:43:43.095169",
          "external_property_id": "1470771",
          "property_id": "0402824140173",
          "land_value": "139000.0",
          "acres": "0.12"
        }
      ],
      "transaction_data": [
        {
          "property_id": "402824140173",
          "internal_property_uuid": "05219229-b1f9-4b8d-98dc-0b4edee54ec4",
          "transaction_uuid": "40e3b09a-c7a0-4126-9497-484a7ec59ee2",
          "transaction_id_source": [
            {
              "property_id": "402824140173"
            }
          ],
          "amount": "224900.0",
          "parties_involved": [
            {
              "name": "NICOLAUS G BAUMAN",
              "type": "owner"
            },
            {
              "name": "NICOLAUS G BAUMAN",
              "type": "taxpayer"
            }
          ],
          "dates": {
            "start_date": "202209"
          },
          "linked_properties": [
            "402824140173"
          ],
          "source_url": "https://gis-hennepin.hub.arcgis.com/datasets/county-parcels/",
          "source_domain": "https://gis-hennepin.hub.arcgis.com/datasets/",
          "created_at": "2024-05-18 19:12:41.379497",
          "last_modified": "2024-05-18 19:12:41.379499",
          "address_linked": "8c21db1c-d15b-4d53-98d2-45ec46a354b8"
        },
        {
          "transaction_uuid": "098064b8-0bfb-4579-9398-90ab8bacf07e",
          "amount": "450000",
          "dates": {},
          "linked_properties": [
            "4987b629-d83f-4551-9976-43b998736b7d"
          ],
          "linked_media": [
            "c6546473-ebde-4563-a1e4-35397539293c"
          ],
          "source_url": "https://www.compass.com/homes-for-sale/7425/status=coming-soon,active,contract-out,contract-signed,contingencies-dropped,sold/sold-date=any-time/start=19681/",
          "source_domain": "www.compass.com",
          "created_at": "2024-04-20 15:12:48.434738",
          "last_modified": "2024-04-20 15:12:48.434739",
          "address_linked": "01fc15b2-14e7-445d-a759-c8290377da0c"
        },
        {
          "transaction_uuid": "20b1b1ae-41b8-4760-a4f2-88bb329f0f80",
          "transaction_type": "Last Sold Price",
          "amount": "450000",
          "dates": {
            "end_date": "DEC 14, 2023"
          },
          "linked_properties": [
            "110cad97-5fa0-4ef7-9d6e-1dc495c0cf81"
          ],
          "linked_media": [
            "08eb193d-6f09-4bca-be24-9ce1d0dc10ac"
          ],
          "source_url": "https://www.redfin.com/stingray/api/home/details/aboveTheFold?accessLevel=1&propertyId=51292165",
          "source_domain": "www.redfin.com",
          "created_at": "2024-04-20 19:13:01.183473",
          "last_modified": "2024-04-20 19:13:01.183475",
          "address_linked": "5b1b4439-7dcb-4142-8943-e27516f219cc"
        },
        {
          "transaction_uuid": "c691711c-f7f0-42d0-ad9b-5c9336189b1e",
          "transaction_type": "New Mortgage",
          "amount": "$224,900.00",
          "parties_involved": [
            {
              "person_id": "2547725",
              "role": "Buyer"
            }
          ],
          "dates": {
            "contract_date": "09/23/2022"
          },
          "source_url": "mysql-database[ecrv_db]",
          "source_domain": "ecrv_db",
          "created_at": "2024-05-28 12:43:43.095224",
          "last_modified": "2024-05-28 12:43:43.095225",
          "address_linked": "23ec4a7e-0888-41a3-9adf-711efafade25"
        }
      ],
      "people_data": [
        {
          "agent_uuid": "18422d94-f9d4-41e0-9814-6a3045d71d0f",
          "personal_details": {
            "full_name": "3340 Colfax LLC"
          },
          "contact_info": {
            "phone": {
              "phone1": "6122639999"
            }
          },
          "address_linked": [
            "23ec4a7e-0888-41a3-9adf-711efafade25",
            "36486bd1-d3a8-41e1-8847-132028fdbc76"
          ],
          "source_url": "mysql-database[ecrv_db]",
          "source_domain": "ecrv_db",
          "created_at": "2024-05-28 12:43:43.095220",
          "last_modified": "2024-05-28 12:43:43.095221",
          "party_id": "2547725",
          "first_name": "",
          "role": "Buyer",
          "transaction_dates": [
            {
              "start_date": "202209"
            },
            {
              "end_date": "DEC 14, 2023"
            },
            {
              "contract_date": "09/23/2022"
            }
          ],
          "associated_property_id": [
            "402824140173",
            "",
            "",
            "0402824140173"
          ]
        }
      ]
    }
  ]
}
# data={
#     "properties": [
#         {
#             "abovegradefinishedarea": 1215.0,
#             "accessibilityfeatures": "None",
#             "basement": "Full",
#             "basementyn": 1,
#             "bathroomsfull": 2,
#             "bathroomstotalinteger": 2,
#             "bedroomstotal": 3,
#             "belowgradefinishedarea": 390.0,
#             "buyeragencycompensation": "2.70",
#             "buyeragencycompensationtype": "%",
#             "buyeragentkey": "NST107452",
#             "buyeragentmlsid": "NST502046851",
#             "buyerfinancing": "Cash",
#             "buyerofficekey": "NST49277",
#             "buyerofficemlsid": "NST49277",
#             "buyerofficename": "Realty Group LLC",
#             "city": "Minneapolis",
#             "closedate": "2022-09-23",
#             "closeprice": 224900.0,
#             "colistagentfullname": "John Newhall",
#             "colistagentkey": "NST96198",
#             "transactionbrokercompensation": "0.0000",
#             "transactionbrokercompensationtype": "%",
#             "watersource": "City Water/Connected",
#             "yearbuilt": 1909,
#             "zoningdescription": "Residential-Single Family",
#             "room": [
#                 {
#                     "nst_roomsortorder": "2",
#                     "roomdimensions": "13x11",
#                     "roomkey": "NST107516287",
#                     "roomlevel": "Main",
#                     "roomtype": "Dining Room",
#                     "listingid": "NST6252617"
#                 },
#                 {
#                     "nst_roomsortorder": "3",
#                     "roomdimensions": "9x18",
#                     "roomkey": "NST107516288",
#                     "roomlevel": "Lower",
#                     "roomtype": "Family Room",
#                     "listingid": "NST6252617"
#                 },
#                 {
#                     "nst_roomsortorder": "9",
#                     "roomdimensions": "9x18",
#                     "roomkey": "NST107516289",
#                     "roomlevel": "Lower",
#                     "roomtype": "Family Room",
#                     "listingid": "NST6252617"
#                 },
#                 {
#                     "nst_roomsortorder": "5",
#                     "roomdimensions": "9x13",
#                     "roomkey": "NST107516290",
#                     "roomlevel": "Main",
#                     "roomtype": "Bedroom 1",
#                     "listingid": "NST6252617"
#                 },
#                 {
#                     "nst_roomsortorder": "4",
#                     "roomdimensions": "9x10",
#                     "roomkey": "NST107516291",
#                     "roomlevel": "Main",
#                     "roomtype": "Kitchen",
#                     "listingid": "NST6252617"
#                 },
#                 {
#                     "nst_roomsortorder": "1",
#                     "roomdimensions": "14x13",
#                     "roomkey": "NST107516292",
#                     "roomlevel": "Main",
#                     "roomtype": "Living Room",
#                     "listingid": "NST6252617"
#                 },
#                 {
#                     "nst_roomsortorder": "6",
#                     "roomdimensions": "10x12",
#                     "roomkey": "NST107516293",
#                     "roomlevel": "Main",
#                     "roomtype": "Bedroom 2",
#                     "listingid": "NST6252617"
#                 },
#                 {
#                     "nst_roomsortorder": "7",
#                     "roomkey": "NST107516294",
#                     "roomlevel": "Upper",
#                     "roomtype": "Bedroom 3",
#                     "listingid": "NST6252617"
#                 }
#             ]
#         },
#         {
#             "abovegradefinishedarea": 1315.0,
#             "accessibilityfeatures": "None",
#             "basement": "Finished",
#             "basementyn": 1,
#             "belowgradefinishedarea": 800.0,
#             "buyeragencycompensation": "2.70",
#             "buyeragencycompensationtype": "%",
#             "buyeragentkey": "NST57259",
#             "buyeragentmlsid": "NST496503609",
#             "buyerfinancing": "Conventional",
#             "buyerofficekey": "NST16638",
#             "buyerofficemlsid": "NST5116",
#             "buyerofficename": "Coldwell Banker Realty",
#             "carportspaces": 3.0,
#             "city": "Minneapolis",
#             "closedate": "2023-12-14",
#             "closeprice": 450000.0,
#             "concessionsamount": 5000,
#             "constructionmaterials": "Block, Vinyl Siding",
#             "contingency": "None",
#             "countyorparish": "Hennepin",
#             "cumulativedaysonmarket": 49,
#             "daysonmarket": 49,
#             "directions": "Hennepin Ave to 33rd St So. East to Colfax and then South to house",
#             "foundationarea": 1015.0,
#             "heating": "Boiler",
#             "highschooldistrict": "Minneapolis",
#             "internetaddressdisplayyn": 1,
#             "internetautomatedvaluationdisplayyn": 1,
#             "internetconsumercommentyn": 1,
#             "internetentirelistingdisplayyn": 1,
#             "latitude": 44.9417,
#             "levels": "One and One Half",
#             "listagentfullname": "Hizzle\u00ae @ SP Real Estate",
#             "listagentkey": "NST107452",
#             "listagentmlsid": "NST502046851",
#             "listagentofficephone": "612-888-5888",
#             "listingagreement": "Exclusive Right To Sell",
#             "listingcontractdate": "2023-10-11",
#             "listingid": "NST6446482",
#             "listingkey": "NST7294978",
#             "listingterms": "Conventional Rehab, Conventional, Trade, FHA, FHA Rehab 203k, Cash",
#             "listofficekey": "NST49277",
#             "listofficemlsid": "NST49277",
#             "listofficename": "Realty Group LLC",
#             "listprice": 450000.0,
#             "livingarea": 2115.0,
#             "longitude": -93.2924,
#             "lotfeatures": "Tree Coverage - Light",
#             "lotsizearea": 0.12,
#             "lotsizedimensions": "40 X 129",
#             "lotsizeunits": "Acres",
#             "mapcoordinate": "120-C1",
#             "mapcoordinatesource": "King's Street Atlas",
#             "mlgcanuse": "IDX, VOW, BO",
#             "mlgcanview": 1,
#             "modificationtimestamp": "2024-03-06T21:32:03+00:00",
#             "nst_abovegradesqfttotal": "1315.0000",
#             "nst_agentowner": "Yes",
#             "nst_ageofproperty": "115",
#             "nst_assessmentpending": "No",
#             "nst_assumablemortgage": "Not Assumable",
#             "nst_belowgradesqfttotal": "1015.0000",
#             "nst_bonusyn": "No",
#             "nst_constructionmaterialsdesc": "Timber/Post & Beam,Brick",
#             "nst_dpresource": "Y",
#             "nst_expenses": "0.0000",
#             "nst_foreclosurestatus": "No",
#             "nst_foundationdimensions": "1015",
#             "nst_fractionalownershipyn": "No",
#             "nst_fuel": "Natural Gas",
#             "nst_garagedimensions": "0",
#             "nst_garagedoorheight": "0",
#             "nst_garagedoorwidth": "0",
#             "nst_garagesquarefeet": "0",
#             "nst_incomemiscann": "0.0000",
#             "nst_incomemiscmon": "0.0000",
#             "nst_internetoptions": "Cable,DSL,Fiber Optic,Satellite",
#             "nst_lastupdatedate": "2024-03-06",
#             "nst_lenderowned": "No",
#             "nst_mainlevelfinishedarea": "1015.0000",
#             "nst_neighborhoodnumber": "South Uptown",
#             "nst_officeboard": "SPAAR",
#             "nst_owneroccupied": "No",
#             "nst_potentialshortsale": "No",
#             "nst_presentuse": "Yearly",
#             "nst_proposedtitledate": "2023-12-14",
#             "nst_rangenum": "Two",
#             "nst_refrigeratornum": "Two",
#             "nst_rentallicenseyn": "No",
#             "nst_schooldistrictnumber": "1",
#             "nst_schooldistrictphone": "612-668-0000",
#             "nst_sqfttotal": "2330.00",
#             "nst_taxwithassessments": "3941.0000",
#             "numberofunitstotal": 2,
#             "occupanttype": "Owner",
#             "offmarketdate": "2023-11-29",
#             "originalentrytimestamp": "2023-10-11T17:03:43+00:00",
#             "originallistprice": 450000.0,
#             "originatingsystemmodificationtimestamp": "2024-03-06T21:30:38+00:00",
#             "originatingsystemname": "northstar",
#             "ownerpays": "None",
#             "parcelnumber": "0402824140173",
#             "parkingfeatures": "Carport, Guest Parking, Parking Lot",
#             "photoschangetimestamp": "2024-03-06T21:32:03+00:00",
#             "photoscount": 39,
#             "postalcity": "Minneapolis",
#             "postalcode": "55408",
#             "privateremarks": "House was converted into a legal duplex with permits. Almost everything is new! \n\nSome photos virtually altered. All measurements approximate.",
#             "propertysubtype": "Duplex Up and Down",
#             "propertytype": "Residential Income",
#             "publicremarks": "Discover 3340 Colfax Ave S, where historic charm meets modern convenience. This converted duplex, upgraded in September 2023, presents a golden investment opportunity. Recent enhancements encompass a new roof, electrical, plumbing, and luxurious interiors in both units, ensuring immediate occupancy & rental income.\n\nThe main-floor apartment boasts a fully revamped kitchen, bathroom, and energy-efficient LED lighting. Meanwhile, the garden-level apartment dazzles with a fresh kitchen, remodeled bathroom, and in-unit laundry. Privacy and serenity are guaranteed with a new staircase and sound/fire barrier between units.\n\nEmbrace versatility, whether you prefer owner occupancy with rental income or leasing both units for a savvy investment. With parking for 2-3 cars and a coveted Uptown location, this property is a rare treasure. Seize the chance to own this income-generating gem in Minneapolis' most sought-after neighborhoods!\n\nSome photos virtually altered. All measurements approximate.",
#             "publicsurveyrange": "24",
#             "publicsurveysection": "04",
#             "publicsurveytownship": "28",
#             "purchasecontractdate": "2023-12-04",
#             "roadfrontagetype": "City Street",
#             "roadresponsibility": "Public Maintained Road",
#             "roof": "Age 8 Years or Less, Architecural Shingle",
#             "sewer": "City Sewer/Connected",
#             "sourcesystemname": "RMLS",
#             "standardstatus": "Closed",
#             "stateorprovince": "MN",
#             "streetdirsuffix": "S",
#             "streetname": "Colfax",
#             "streetnumber": "3340",
#             "streetnumbernumeric": 3340,
#             "streetsuffix": "Avenue",
#             "subagencycompensation": "0.00",
#             "subagencycompensationtype": "%",
#             "subdivisionname": "Remingtons 2nd Add",
#             "taxannualamount": 3941.0,
#             "taxlegaldescription": "LOT 004 BLOCK 045 REMINGTONS 2ND ADDN TO MPLS",
#             "taxyear": 2023,
#             "tenantpays": "Cable TV, Electricity",
#             "topography": "Level",
#             "transactionbrokercompensation": "0.0000",
#             "transactionbrokercompensationtype": "%",
#             "watersource": "City Water/Connected",
#             "yearbuilt": 1909,
#             "zoningdescription": "Residential-Multi-Family",
#             "room": [
#                 {
#                     "nst_roomsortorder": "1",
#                     "roomdimensions": "10.8x11.6",
#                     "roomkey": "NST112646655",
#                     "roomlevel": "Main",
#                     "roomtype": "Family Room",
#                     "listingid": "NST6446482"
#                 },
#                 {
#                     "nst_roomsortorder": "2",
#                     "roomdimensions": "9.4x11.6",
#                     "roomkey": "NST112646656",
#                     "roomlevel": "Main",
#                     "roomtype": "Dining Room",
#                     "listingid": "NST6446482"
#                 },
#                 {
#                     "nst_roomsortorder": "3",
#                     "roomdimensions": "13.3x20",
#                     "roomkey": "NST112646657",
#                     "roomlevel": "Main",
#                     "roomtype": "Family Room",
#                     "listingid": "NST6446482"
#                 },
#                 {
#                     "nst_roomsortorder": "4",
#                     "roomdimensions": "9.4x13.1",
#                     "roomkey": "NST112646658",
#                     "roomlevel": "Upper",
#                     "roomtype": "Bedroom 1",
#                     "listingid": "NST6446482"
#                 },
#                 {
#                     "nst_roomsortorder": "5",
#                     "roomdimensions": "10.1x12",
#                     "roomkey": "NST112646659",
#                     "roomlevel": "Upper",
#                     "roomtype": "Bedroom 2",
#                     "listingid": "NST6446482"
#                 },
#                 {
#                     "nst_roomsortorder": "6",
#                     "roomdimensions": "12x16.4",
#                     "roomkey": "NST112646660",
#                     "roomlevel": "Upper",
#                     "roomtype": "Bedroom 3",
#                     "listingid": "NST6446482"
#                 },
#                 {
#                     "nst_roomsortorder": "7",
#                     "roomdimensions": "11.5x20.6",
#                     "roomkey": "NST112646661",
#                     "roomlevel": "Lower",
#                     "roomtype": "Bedroom 4",
#                     "listingid": "NST6446482"
#                 }
#             ]
#         }
#     ]
# }

# prompt = (
#    'Hi! you are the helpful assistantm extract the only value which is being asked in the question donot give whole data\n' 'Provided data: '+str(data)
# )
question="who is the last owner of 3340 Colfax Ave S, Minneapolis, MN 55408?"
prompt=f"""[INST] <<SYS>>
'Hi! you are the helpful assistant. extract the only correct value carefully, give answer in  user friendly way to customers,  which is being asked in the question donot give whole data\n' 'Provided data from api: '{str(data)}<</SYS>>

{question} [/INST]""" 
# Generate text
sequences = text_gen_pipeline(
    prompt,
    num_return_sequences=1,
    do_sample=True,
    temperature=3,
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
