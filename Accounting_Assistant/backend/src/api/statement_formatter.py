import os
import pandas
from json import loads, dumps

def get_entries(user_id):
    #Eventually,the entries file should be built by getting statements from all connected bank apis
    entries_file = os.path.join(os.getcwd(), 'resources', 'wise-transaction-history.csv')
    df = pandas.read_csv(entries_file)
    results=df.to_json(orient="split")
    print(results)
    parse = loads(results)
    return dumps(parse, indent=4)

def test_get_entries():
    print(get_entries(1))

