from api.statement_formatter import get_entries
def test_get_entries():
  entries = get_entries(1)
  assert len(entries) > 0


def test_get_entries_fields():
  entries = get_entries(1)
  assert 'Amount' in entries[0]
  assert 'Date' in entries[0]
  assert 'Category' in entries[0]
