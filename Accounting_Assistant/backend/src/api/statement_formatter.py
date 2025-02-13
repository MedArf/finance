import os
import pandas
from json import loads, dumps
import json
class AccountingEntry(json.JSONEncoder):
  def __init__(self, reference, date, amount, category, subcategory):
    self.reference=reference
    self.date=date
    self.amount=amount
    self.category=category
    self.subcategory=subcategory


MappingRules = {
  "operation_date": {"Bourso": "dateOp", "Wise":"Created on"},
  "amount": {"Bourso": "amount", "Wise":"Created on"},
  "reference": {"Bourso": "label", "Wise":"reference"},
  "category": {"Bourso": "categoryParent", "Wise":"category"},
  "subcategory": {"Bourso": "category", "Wise":"category"},
}
final_columns = ["operation_date", "amount", "reference", "category", "subcategory"]

def get_entries(user_id):
    #Eventually,the entries file should be built by getting statements from all connected bank apis
    entries_file = os.path.join(os.getcwd(), 'resources', 'export-operations-28-01-2025_10-21-43.csv')
    df = pandas.read_csv(entries_file, sep=';')
    #for banks for that user, get all bank apis registered
    bank_name = "Bourso"
    regex_expr = ""
    map_columns={}
    for col in final_columns:
      print ("col"+col)
      print ("old"+MappingRules[col][bank_name])
      map_columns[MappingRules[col][bank_name]]=col
      regex_expr+=col+"|"
    print(map_columns)
    print(regex_expr)
    df.rename(columns=map_columns, inplace=True)

    regex_expr = regex_expr[:-1]
    print(df.filter(regex=regex_expr, axis=1))
    results=df.filter(regex=regex_expr, axis=1).to_json(orient="records")

    return json.loads(results)
