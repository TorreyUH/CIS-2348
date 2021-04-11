# Torrey Brett
# PSID 1498427

import csv  # import file to read and write csv files
from _ast import Lambda  # Needed to utilize lambda
from datetime import datetime  # Needed to have the recent day and time imported into the program


class Inven_Out:  # class with methods to write new csv files from the required input files
    def __init__(self, item_list):
        self.item_list = item_list

    def entire(self=None):  # csv file is created for the full inventory sorted per project instructions
        with open('C:/Users/Johnny Blaze/Documents/CIS 2348/Project_Files/FullInventory.csv', 'w') as file:
            # writeable file created
            items = self.item_list  # assigns the item as items
            keys = sorted(items.keys(), key=lambda x: items[x]['Manufacturer'])  # sorts the list into list keys
            for item in keys:  # used to iterate through the item within the keys sort
                id = item  # assignment of id to item
                man_name = items[item]['Manufacturer']  # assignment of manufacturer name to list item
                item_type = items[item]['item_type']  # assignment of item type to list item
                price = items[item]['price']  # assignment of price to list item
                service_date = items[item]['service_date']  # assignment of service date to list item
                damaged = items[item]['damaged']  # assignment of a potentially damaged item to list item
                file.write('{}, {}, {}, {}, {}, {}\n'.format(id, man_name, item_type, price, service_date, damaged))

    def type_inventory(self):  # inventory type class
        items = self.item_list  # assigns listed items as items
        types = []  # empty list creation
        keys = sorted(items.keys())  # sorted the keys
        for item in items:  # iterates through the item with items
            item_type = items[item]['item_type']  # assigns the item type to the item list
            if item_type not in types:  # checks if the item type is within the list
                types.append(item_type)  # appends the new item to the list
        for type in types:  # iterates through the list within the types list
            file_name = type.capitalize() + 'Inventory.csv'
        with open('C:/Users/Johnny Blaze/Documents/CIS 2348/Project_Files/Inventory.csv', 'w') as file:
            # csv file is created for the  inventory sorted per project instructions
            for item in keys:  # iterates an item in each keys
                id = item  # assigns the item type to the item list
                man_name = items[item]['Manufacturer']  # assignment of manufacturer name to list item
                price = items[item]['price']  # assignment of price to list item
                service_date = items[item]['service_date']  # assignment of service date to list item
                damaged = items[item]['damaged']  # assignment of a potentially damaged item to list item
                item_type = items[item]['item_type']  # assigns the item type to the item list
                if type == item_type:
                    file.write('{}, {}, {}, {}, {}\n'.format(id, man_name, price, service_date, damaged))

    def past_service_date(self):  # past service date class
        items = self.item_list  # assigns listed items as items
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date(),
                      reverse=True)
        with open('C:/Users/Johnny Blaze/Documents/CIS 2348/Project_Files/PastServiceDateInventory.csv', 'w') as file:
            # csv file is created for the past service sorted per project instructions
            for item in keys:
                id = item  # assigns the item type to the item list
                man_name = items[item]['Manufacturer']  # assignment of manufacturer name to list item
                item_type = items[item]['item_type']   # assigns the item type to the item list
                price = items[item]['price']  # assignment of price to list item
                service_date = items[item]['service_date']  # assignment of service date to list item
                damaged = items[item]['damaged']  # assignment of a potentially damaged item to list item
                today = datetime.now().date()  # utilizes the import to have the date and time of
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()  # makes the date into a string
                expired = service_expiration < today  # compares the string date of today to the service expiration date
                if expired: # if the item is expired
                    file.write('{}, {}, {}, {}, {}, {}\n'.format(id, man_name, item_type, price, service_date, damaged))
                    # used to write the new lines into the csv files

    def damaged_item(self):  # damaged item  class
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open('C:/Users/Johnny Blaze/Documents/CIS 2348/Project_Files/DamagedInventory.csv', 'w') as file:
            # csv file is created for the damaged inventory sorted per project instructions
            for item in keys:  # iterate through each item within the keys sort
                id = item  # assigns the item type to the item list
                man_name = items[item]['Manufacturer']  # assignment of manufacturer name to list item
                item_type = items[item]['item_type']  # assigns the item type to the item list
                price = items[item]['price']  # assignment of price to list item
                service_date = items[item]['service_date']  # assignment of service date to list item
                damaged = items[item]['damaged']  # assignment of a potentially damaged item to list item
                if damaged:
                    file.write('{}, {}, {}, {}, {}\n'.format(id, man_name, item_type, price, service_date))
                    # used to write the new lines into the csv files


if __name__ == '__main__':
    items = {}  #empty dictionary for the items
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']  # sets the names into the files and
    # will only use the files of the like name
    for file in files:  # for each file in the list
        with open(file, 'r') as csv_file:   # open the file and allow it to be read
            csv_reader = csv.reader(csv_file, delimiter=',')  # reads the csv file and uses the , as a separator or
            # delimiter
            for line in csv_reader:  # for every line in the file
                item_id = line[0]  # ID is the first or 0 element in the line
                if file == files[0]:  # file one
                    items[item_id] = {}  # creates a dictionary
                    man_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['Manufacturer'] = man_name.strip()  # first element
                    items[item_id]['item_type'] = item_type.strip()  # second element
                    items[item_id]['damaged'] = damaged  # third element
                elif file == files[1]:
                    price = line[1]  # second element
                    items[item_id]['price'] = price # sets the price variable
                elif file == files[2]:
                    service_date = line[1] # second element in line
                    items[item_id]['service_date'] = service_date
    inventory = Inven_Out(items)  # inventory assingned to class
    inventory.entire()  # calls defined function
    inventory.type_inventory()  # calls defined function
    inventory.past_service_date()  # calls defined function
    inventory.damaged_item()  # calls defined function
    types = []
    manufacturers = []
    for item in items:
        checked_manufacturer = items[item]['Manufacturer']
        checked_type = items[item]['item_type']
        if checked_manufacturer not in types:
            manufacturers.append(checked_manufacturer)
        if checked_type not in types:
            types.append(checked_type)
