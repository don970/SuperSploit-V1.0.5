# global variables
import json
import os.path
import traceback

from .errors import Error as error

global path_to_database
path_to_database = ".data/data.json"


class DatabaseManagment:

    def __init__(self):
        pass

    @classmethod
    def directlyModify(cls, data: list):
        print(data)
        try:
            with open(".data/data.json") as file:
                variables = json.load(file)
                file.close()
            if "exploit" in data[0]:
                variables["EXPLOIT"] = data[1]
            if "payload" in data[0]:
                variables["PAYLOAD"] = data[1]
            with open(".data/data.json", "w") as file:
                file.write(json.dumps(variables))
                file.close()
        except Exception:
            error(traceback.format_exc())
            return

    @classmethod
    def get(cls):
        if os.path.lexists(path_to_database):
            with open(path_to_database) as file:
                data = json.load(file)
                file.close()
            return data

    @staticmethod
    def getExploits():
        exploits = []
        for x in os.listdir("exploits/"):
            for i in os.listdir(f"exploits/{x}"):
                exploits.append(f"exploits/{x}/{i}")
        return exploits
    @staticmethod
    def getPayloads():
        exploits = []
        for x in os.listdir("payloads/"):
            for i in os.listdir(f"payloads/{x}"):
                exploits.append(f"payloads/{x}/{i}")
        return exploits