import csv

CUST_FILE_NAME = "data\cust.csv"
ORDERS_FILE_NAME = "data\orders.csv"

custDB = []
ordersDB = []


def getID(name: str) -> int:
    return next(item["id"] for item in custDB if item["name"] == name)


def getShopping(id: int) -> list:
    return [int(d["sum"]) for d in ordersDB if d["cust_id"] == id]


def calcSum(db: list) -> int:
    return sum(db)


def getNameFromUser() -> str:
    return input("Enter Name: ")


def printTotalOrder(name: str):
    id = getID(name)
    custShopping = getShopping(id)
    sum = calcSum(custShopping)
    print("Total orders: " + str(sum) + "$")


def readFileToList(fileName: str, listDB: list):
    with open(fileName, newline='') as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        for row in reader:
            listDB.append(row)
    return


def init():
    readFileToList(CUST_FILE_NAME, custDB)
    readFileToList(ORDERS_FILE_NAME, ordersDB)


def main():

    init()
    while(1):
        name = getNameFromUser()
        if (name == "q"):
            break
        elif not any(d["name"] == name for d in custDB):
            print("Customer \"" + name + "\" does not exist")
        else:
            printTotalOrder(name)
    return


main()
