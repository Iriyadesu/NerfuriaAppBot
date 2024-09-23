import json

async def ReadConfig():
        with open("config.json", "r") as read_file:
            return json.load(read_file)
        
async def WriteConfig(data):
        with open("config.json", "w") as read_file:
            json_object = json.dumps(data)
            read_file.write(json_object)