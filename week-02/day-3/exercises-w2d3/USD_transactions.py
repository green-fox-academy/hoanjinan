# import xml.etree.ElementTree as ET

# tree = ET.parse('transactions.xml')
# root = tree.getroot()

# for transaction in root.findall("transaction"):
#     from_tran = transaction.find("from").text
#     to_tran = transaction.find("to").text
#     print(from_tran, to_tran)

# print(root[0][2].text)


# for child in root:
#     if child.tag == "transaction":
#         for arribute in child:
#             if arribute.tag == "amount":
#                 if arribute.get("currency") == "USD":
#                     amount = arribute.text
#                     print(amount)
#                     if arribute.tag == "from":
#                         from_atrr = arribute.text
#                         print(from_atrr)


from xml.dom import minidom

content = minidom.parse('transactions.xml')

tag_from = content.getElementsByTagName("from")
tag_to = content.getElementsByTagName("to")
tag_amount = content.getElementsByTagName("amount")

for i in range(len(tag_from)):
    if tag_amount[i].attributes['currency'].value == "USD":
        print(f"From {tag_from[i].firstChild.data} to {tag_to[i].firstChild.data} with amount of {tag_amount[i].firstChild.data} in USD")
    