import usaddress
from transformers import T5Tokenizer, T5ForConditionalGeneration
import requests


# print("Response Body:", response.json())

# model_name = 't5-large'
# tokenizer = T5Tokenizer.from_pretrained(model_name)
# model = T5ForConditionalGeneration.from_pretrained(model_name)

# # Prepare the input text for summarization
# property_address = "3340 Colfax Ave S"
# # check=f"question: What is the close date at {property_address} "
# # input_text = f"question: What is the close date at {property_address} context: {data}"

# # context = ""
# # for prop in data["properties"]:
# #     for key, value in prop.items():
# #         context += f"{key}: {value}\n"
# question = f"In which year 3340 Colfax Ave S, Minneapolis, MN 55408 built?"
# # Construct the input text
# input_text = f"question: {question } context: {str(response.json)}"


# input_text = f"question: {question} context: {data}"

#print("***********QUESTION*************:",check)
# Tokenize the input text
# input_ids = tokenizer.encode(input_text, return_tensors="pt")

# # Generate the output
# output_ids = model.generate(input_ids, max_length=50)

# # Decode the output
# output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
# print("*********************Response**********************:",output_text)




# input_text = "summarize: "+output_text+" "+question
# input_ids = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=512)
# # tokenizer = T5Tokenizer.from_pretrained(model_name)
# # model = T5ForConditionalGeneration.from_pretrained(model_name)

# # Generate the output
# output_ids = model.generate(input_ids, max_length=50)

# # Decode the output
# output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
# print("*********************Response**********************:",output_text)

#print("Extracted addresses:", addresses)

def extract_address(text):
    parsed_address = usaddress.parse(text)
    address_parts = []
    capturing = False

    for component, label in parsed_address:
        if label == 'AddressNumber':
            capturing = True
        if capturing:
            address_parts.append(component)
        if label == 'ZipCode':
            break

    full_address = ' '.join(address_parts)
    return full_address


def get_details(address):

    url = "http://192.168.38.100:8000/api/data/address/property"
    payload = {
        "address": address
    }

    response = requests.post(url, json=payload)

    if response.status_code==200:
        return response.json()
    else:
        print("error",response)


def get_answers(addr,user_input,property_data):
    model_name = "t5-11b"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

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
            "colistagentmlsid": "NST502040885",
            "constructionmaterials": "Brick/Stone",
            "contingency": "None",
            "cooling": "None",
            "countyorparish": "Hennepin",
            "cumulativedaysonmarket": 14,
            "daysonmarket": 14,
            "directions": "Hennepin Ave to 33rd St So. East to Colfax and then South to house",
            "dualvariablecompensationyn": 1,
            "electric": "Circuit Breakers, 100 Amp Service",
            "fireplacefeatures": "Living Room",
            "foundationarea": 1015.0,
            "garagespaces": 2.0,
            "heating": "Boiler, Hot Water",
            "highschooldistrict": "Minneapolis",
            "internetaddressdisplayyn": 1,
            "internetautomatedvaluationdisplayyn": 1,
            "internetentirelistingdisplayyn": 1,
            "latitude": 44.9417,
            "levels": "One and One Half",
            "listagentfullname": "Stephanie S Gruver",
            "listagentkey": "NST78361",
            "listagentmlsid": "NST502031846",
            "listagentofficephone": "612-581-5842",
            "listingagreement": "Exclusive Right To Sell",
            "listingcontractdate": "2022-08-26",
            "listingid": "NST6252617",
            "listingkey": "NST7142101",
            "listingterms": "Cash",
            "listofficekey": "NST19238",
            "listofficemlsid": "NST40490",
            "listofficename": "RE/MAX Results",
            "listprice": 224900.0,
            "livingarea": 1605.0,
            "lockboxtype": "Combo",
            "longitude": -93.2923,
            "lotfeatures": "Tree Coverage - Medium",
            "lotsizearea": 0.12,
            "lotsizedimensions": "40x128",
            "lotsizesquarefeet": 5227.2,
            "lotsizeunits": "Acres",
            "mapcoordinate": "120-C1",
            "mapcoordinatesource": "King's Street Atlas",
            "mlgcanuse": "IDX, VOW, BO",
            "mlgcanview": 1,
            "modificationtimestamp": "2023-09-24T07:49:04+00:00",
            "nst_abovegradesqfttotal": "1215.0000",
            "nst_agentowner": "No",
            "nst_ageofproperty": "114",
            "nst_amenitiesunit": "Hardwood Floors,Porch",
            "nst_assessmentpending": "Unknown",
            "nst_assumablemortgage": "Not Assumable",
            "nst_bathdesc": "Full Basement,Main Floor Full Bath",
            "nst_belowgradesqfttotal": "1015.0000",
            "nst_bonusyn": "No",
            "nst_communityname": "Calhoun - Isle",
            "nst_diningroomdescription": "Separate/Formal Dining Room",
            "nst_dpresource": "Y",
            "nst_foreclosurestatus": "No",
            "nst_fractionalownershipyn": "No",
            "nst_fuel": "Natural Gas",
            "nst_garagesquarefeet": "390",
            "nst_insurancefee": "0",
            "nst_isnewdevelopment": "No",
            "nst_lastupdatedate": "2023-09-24",
            "nst_lenderowned": "No",
            "nst_lockboxsource": "MAAR",
            "nst_mainlevelfinishedarea": "1015.0000",
            "nst_manufacturedhome": "No",
            "nst_neighborhoodnumber": "South Uptown",
            "nst_officeboard": "MAAR",
            "nst_potentialshortsale": "No",
            "nst_presentuse": "Yearly",
            "nst_proposedtitledate": "2022-09-23",
            "nst_remarksfinancial": "Cash, rehab, or hard money financing only. No FHA/DVA. Preference given for quick close.",
            "nst_rentallicenseyn": "No",
            "nst_schooldistrictnumber": "1",
            "nst_schooldistrictphone": "612-668-0000",
            "nst_specialsearch": "Main Floor Bedroom",
            "nst_sqfttotal": "2230.00",
            "nst_taxwithassessments": "3954.6200",
            "occupanttype": "Owner",
            "offmarketdate": "2022-09-09",
            "originalentrytimestamp": "2022-08-26T13:58:44+00:00",
            "originallistprice": 224900.0,
            "originatingsystemmodificationtimestamp": "2023-09-24T07:46:44+00:00",
            "originatingsystemname": "northstar",
            "parcelnumber": "0402824140173",
            "parkingfeatures": "Detached",
            "photoschangetimestamp": "2022-09-01T03:03:04+00:00",
            "photoscount": 7,
            "postalcity": "Minneapolis",
            "postalcode": "55408",
            "privateremarks": "Agents/Buyers to verify all measurements. Home is sold AS IS - must include AS IS addendum and strike lines 272-273 from the PA - See Agent Supplements. Home will need renovation and clean out (some clean out has been done). Buyer to assume all TISH Required Repairs (no permit required repairs on report). Preference given to cash buyers with a quick close. Call your renovator clients and get them in for a showing. Mask recommended for showings. Call with any questions.",
            "propertysubtype": "Single Family Residence",
            "propertytype": "Residential",
            "publicremarks": "Great renovation opportunity in Uptown! Bring your design ideas and create a one-of-a-kind home. The main floor features a living room, dining room, kitchen, two main floor bedrooms, and a full bath. The spacious upper level third bedroom has good ceiling height. The lower level is partially finished with another full bath. Detached, two car garage. Easy access to local businesses/dining/Lake Bde Maka Ska. Home is part of an Estate. Sold As Is - will not be cleaned out. Cash or renovation financing only.",
            "publicsurveyrange": "24",
            "publicsurveysection": "04",
            "publicsurveytownship": "28",
            "roadfrontagetype": "City Street",
            "roadresponsibility": "Public Maintained Road",
            "roof": "Age 8 Years or Less, Asphalt",
            "roomtype": "Living Room, Dining Room, Family Room, Kitchen, Bedroom 1, Bedroom 2, Bedroom 3, Family Room",
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
            "taxannualamount": 3955.0,
            "taxlegaldescription": "LOT 004 BLOCK 045 REMINGTONS 2ND ADDN TO MPLS",
            "taxyear": 2022,
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
        }
    ]
}


    # Prepare the input text for summarization
    property_address = "3340 Colfax Ave S"
    # check=f"question: What is the close date at {property_address} "
    input_text = f"question: in which year {property_address} built   context: {data}"
    print(input_text)
    # print("***********QUESTION*************:",check)
    # Tokenize the input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=1024)

    # Generate the output
    output_ids = model.generate(input_ids, max_length=50)

    # Decode the output
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    print("*********************Response**********************:",output_text)



def main():
    user_input='in which year 3340 Colfax Ave S, Minneapolis, MN 55408 built?'
    address=extract_address(user_input)
    # property_details=get_details(address)
    property_details={
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
            "colistagentmlsid": "NST502040885",
            "constructionmaterials": "Brick/Stone",
            "contingency": "None",
            "cooling": "None",
            "countyorparish": "Hennepin",
            "cumulativedaysonmarket": 14,
            "daysonmarket": 14,
            "directions": "Hennepin Ave to 33rd St So. East to Colfax and then South to house",
            "dualvariablecompensationyn": 1,
            "electric": "Circuit Breakers, 100 Amp Service",
            "fireplacefeatures": "Living Room",
            "foundationarea": 1015.0,
            "garagespaces": 2.0,
            "heating": "Boiler, Hot Water",
            "highschooldistrict": "Minneapolis",
            "internetaddressdisplayyn": 1,
            "internetautomatedvaluationdisplayyn": 1,
            "internetentirelistingdisplayyn": 1,
            "latitude": 44.9417,
            "levels": "One and One Half",
            "listagentfullname": "Stephanie S Gruver",
            "listagentkey": "NST78361",
            "listagentmlsid": "NST502031846",
            "listagentofficephone": "612-581-5842",
            "listingagreement": "Exclusive Right To Sell",
            "listingcontractdate": "2022-08-26",
            "listingid": "NST6252617",
            "listingkey": "NST7142101",
            "listingterms": "Cash",
            "listofficekey": "NST19238",
            "listofficemlsid": "NST40490",
            "listofficename": "RE/MAX Results",
            "listprice": 224900.0,
            "livingarea": 1605.0,
            "lockboxtype": "Combo",
            "longitude": -93.2923,
            "lotfeatures": "Tree Coverage - Medium",
            "lotsizearea": 0.12,
            "lotsizedimensions": "40x128",
            "lotsizesquarefeet": 5227.2,
            "lotsizeunits": "Acres",
            "mapcoordinate": "120-C1",
            "mapcoordinatesource": "King's Street Atlas",
            "mlgcanuse": "IDX, VOW, BO",
            "mlgcanview": 1,
            "modificationtimestamp": "2023-09-24T07:49:04+00:00",
            "nst_abovegradesqfttotal": "1215.0000",
            "nst_agentowner": "No",
            "nst_ageofproperty": "114",
            "nst_amenitiesunit": "Hardwood Floors,Porch",
            "nst_assessmentpending": "Unknown",
            "nst_assumablemortgage": "Not Assumable",
            "nst_bathdesc": "Full Basement,Main Floor Full Bath",
            "nst_belowgradesqfttotal": "1015.0000",
            "nst_bonusyn": "No",
            "nst_communityname": "Calhoun - Isle",
            "nst_diningroomdescription": "Separate/Formal Dining Room",
            "nst_dpresource": "Y",
            "nst_foreclosurestatus": "No",
            "nst_fractionalownershipyn": "No",
            "nst_fuel": "Natural Gas",
            "nst_garagesquarefeet": "390",
            "nst_insurancefee": "0",
            "nst_isnewdevelopment": "No",
            "nst_lastupdatedate": "2023-09-24",
            "nst_lenderowned": "No",
            "nst_lockboxsource": "MAAR",
            "nst_mainlevelfinishedarea": "1015.0000",
            "nst_manufacturedhome": "No",
            "nst_neighborhoodnumber": "South Uptown",
            "nst_officeboard": "MAAR",
            "nst_potentialshortsale": "No",
            "nst_presentuse": "Yearly",
            "nst_proposedtitledate": "2022-09-23",
            "nst_remarksfinancial": "Cash, rehab, or hard money financing only. No FHA/DVA. Preference given for quick close.",
            "nst_rentallicenseyn": "No",
            "nst_schooldistrictnumber": "1",
            "nst_schooldistrictphone": "612-668-0000",
            "nst_specialsearch": "Main Floor Bedroom",
            "nst_sqfttotal": "2230.00",
            "nst_taxwithassessments": "3954.6200",
            "occupanttype": "Owner",
            "offmarketdate": "2022-09-09",
            "originalentrytimestamp": "2022-08-26T13:58:44+00:00",
            "originallistprice": 224900.0,
            "originatingsystemmodificationtimestamp": "2023-09-24T07:46:44+00:00",
            "originatingsystemname": "northstar",
            "parcelnumber": "0402824140173",
            "parkingfeatures": "Detached",
            "photoschangetimestamp": "2022-09-01T03:03:04+00:00",
            "photoscount": 7,
            "postalcity": "Minneapolis",
            "postalcode": "55408",
            "privateremarks": "Agents/Buyers to verify all measurements. Home is sold AS IS - must include AS IS addendum and strike lines 272-273 from the PA - See Agent Supplements. Home will need renovation and clean out (some clean out has been done). Buyer to assume all TISH Required Repairs (no permit required repairs on report). Preference given to cash buyers with a quick close. Call your renovator clients and get them in for a showing. Mask recommended for showings. Call with any questions.",
            "propertysubtype": "Single Family Residence",
            "propertytype": "Residential",
            "publicremarks": "Great renovation opportunity in Uptown! Bring your design ideas and create a one-of-a-kind home. The main floor features a living room, dining room, kitchen, two main floor bedrooms, and a full bath. The spacious upper level third bedroom has good ceiling height. The lower level is partially finished with another full bath. Detached, two car garage. Easy access to local businesses/dining/Lake Bde Maka Ska. Home is part of an Estate. Sold As Is - will not be cleaned out. Cash or renovation financing only.",
            "publicsurveyrange": "24",
            "publicsurveysection": "04",
            "publicsurveytownship": "28",
            "roadfrontagetype": "City Street",
            "roadresponsibility": "Public Maintained Road",
            "roof": "Age 8 Years or Less, Asphalt",
            "roomtype": "Living Room, Dining Room, Family Room, Kitchen, Bedroom 1, Bedroom 2, Bedroom 3, Family Room",
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
            "taxannualamount": 3955.0,
            "taxlegaldescription": "LOT 004 BLOCK 045 REMINGTONS 2ND ADDN TO MPLS",
            "taxyear": 2022,
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
        }
    ]
}
    t5_prediction=get_answers(address,user_input,property_details)

if __name__ == "__main__":
    main()