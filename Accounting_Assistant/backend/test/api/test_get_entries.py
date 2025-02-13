from api.statement_formatter import get_entries
import json



def test_get_entries():
  entries = get_entries(1)
  assert len(entries) > 0


def test_get_entries_fields():
  entries = get_entries(1)
  print('entries')
  print(entries)
  print('column')
  assert(entries[len(entries) - 1] is not None)
  assert(entries[len(entries) - 1]['operation_date'] is not None)
  assert(entries[len(entries) - 1]['amount'] is not None)
  assert(entries[len(entries) - 1]['reference'] is not None)
  assert(entries[len(entries) - 1]['category'] is not None)
  assert(entries[len(entries) - 1]['subcategory'] is not None)
