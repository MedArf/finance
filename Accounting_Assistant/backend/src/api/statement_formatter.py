import os
import pandas
from app import app
from json import loads, dumps

app=app.get_app()
df= pandas.read_csv(os.path.join(app.root_path, '../..', 'resources', 'wise-transaction-history.csv'))
parse = loads(results)
print(dumps(parse, indent=4))
#Should iterate through bank apis connected for that user
def get_entries(user_id):
    #Eventually,the entries file should be built by getting statements from all connected bank apis
    entries_file = os.path.join(app.root_path, '../..', 'resources', 'wise-transaction-history.csv')
    df = pandas.read_csv(entries_file)
    results=df.to_json(orient="split")
    parse = loads(results)
    return dumps(parse, indent=4)



