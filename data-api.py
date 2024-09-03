import os
from openai import OpenAI
import requests


# url = 'http://192.168.8.100:50001/api/v1/buyer_seller/'

# headers = {
#     'accept': 'application/json',
#     'Content-Type': 'application/json'
# }

# data = {
#     "delimiter": 10
# }

# response = requests.post(url, headers=headers, json=data)
# owner=response.json()


client= OpenAI(api_key='sk-proj-mJEtMzqGc55mKy8uxeE7T3BlbkFJLUSsZ3ow3Uafwz8HNOcp')
#os.environ.get("OPENAI_API_KEY")

# response = client.chat.completions.create(
#         model="gpt-3.5-turbo-0125",
#         # response_format={ "type": "json_object" },
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant designed to output"},
#             {"role": "user", "content": "extract the address and output only address not extra information from following sentence -> in which year 3340 Colfax Ave S, Minneapolis, MN 55408 was built \n"}
#         ]
#     )

# address=response.choices[0].message.content # cleaning address from user input

# url = "http://192.168.38.100:8000/api/data/address/property" # now sending address to our api that have property
# payload = {
#     "address": address
# }
# response = requests.post(url, json=payload)

# # Checking the response
# if response.status_code == 200:
#     print("Request successfull!")
#     data=response.json()
# else:
#     print("Request failed with status code:", response.status_code)
#     print("Response:", response.text)

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
response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        # response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to give property information from the api response"},
            {"role": "user", "content": " what is the listing price of  3340 Colfax Ave S, Minneapolis, MN 55408 ? \n"+str(data)}
        ]
    )

print(response.choices[0].message.content)