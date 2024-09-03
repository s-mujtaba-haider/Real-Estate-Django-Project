import usaddress


textex = [
    "The office is located at 470 Westfield Street West Springfield MA 01089.",
    "You can find the shop at 632 Westfield Street WEST SPRINGFIELD MA 01089.",
    "Visit our store at 2040 Boston Rd Wilbraham MA 01095 for great deals.",
    "Our main branch is at 136 Dwight Road, Suite LONGMEADOW MA 01106.",
    "Stop by our location at 928 Belmont Ave Springfield MA 01108.",
    "Our services are available at 85 Post Office Park Ste D Wilbraham MA 01095.",
    "We are located at 632 Westfield Street WEST SPRINGFIELD MA 01089.",
    "Check out our facility at 200 TRIANGLE ST AMHERST MA 01002.",
    "The clinic is at 136 DWIGHT RD STE LONGMEADOW MA 01106.",
    "Our warehouse is at 398 East St Ludlow MA 01056.",
    "Find us at 1763 NORTHAMPTON ST HOLYOKE MA 01040.",
    "Our headquarters is at 11 Herbert P Almgren Drive AGAWAM MA 01001.",
    "The plant is situated at 11 Herbert P Almgren Drive AGAWAM MA 01001.",
    "Visit us at 267 S. Westfield St. AGAWAM MA 01030.",
    "Our office is at 136 DWIGHT RD STE LONGMEADOW MA 01106.",
    "We are located at 45 Lyman Street WESTBOROUGH MA 01581.",
    "Our store is at 300 Pleasant Street NORTHAMPTON MA 01060.",
    "You can find us at 632 Westfield Street WEST SPRINGFIELD MA 01089.",
    "Our branch is at 136 DWIGHT RD STE LONGMEADOW MA 01106.",
    "The facility is located at 121 RICHMOND RD LUDLOW MA 01056.",
    "We are situated at 1763 NORTHAMPTON ST HOLYOKE MA 01040.",
    "Our office can be found at 185 EAST ST LUDLOW MA 01056-3410.",
    "Visit our shop at 150 FRONT ST UNIT WEST SPRINGFIELD MA 01089.",
    "Our main office is at 407 Suite Longmeadow MA 01106.",
    "The facility is located at 66 dwight rd Longmeadow MA 01106.",
    "We offer services at 85 Post Office Park Ste D Wilbraham MA 01095.",
    "Our office is at 17 Main St., Suite Lee MA 01238.",
    "Visit us at 2 Lyman Street South Hadley MA 01075.",
    "We are located at 2 Lyman Street South Hadley MA 01075.",
    "Our office is at 31 COURT ST FL WESTFIELD MA 01085-3502.",
    "You can find us at 267 S. Westfield St. AGAWAM MA 01030.",
    "Our clinic is at 136 DWIGHT RD STE LONGMEADOW MA 01106.",
    "Visit our office at 383 COLLEGE ST AMHERST MA 01002.",
    "We are located at 158 N King St NORTHAMPTON MA 01060.",
    "The store is at 28 N MAPLE ST NORTHAMPTON MA 01062.",
    "Our facility is at 136 DWIGHT RD STE LONGMEADOW MA 01106.",
    "Visit us at 112 MAIN ST NORTHAMPTON MA 01060.",
    "Our office is at 200 Triangle Street Amherst MA 01002.",
    "Find us at 190 University Drive Amherst MA 01002 see you soon",
    "We are located at 4 Meeting House Rd Chelmsford MA 01824 to meet",
    "Our store is at 158 N King St NORTHAMPTON MA 01060 at afternoon",
    "Visit us at 92 Main Street Florence MA 01062 we will be available"
]


for text in textex:
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
    print("user question -> ",text)
    print("extracted address -> ",full_address)
    print("******************************")