from elemental_tools.db.mongo import Connect, Index


database = Connect("mongodb://192.168.1.10:27017/", "test_database")

database.collection('test_collection')

_test_indexes = [
	Index(['name', 'value'], unique=True),
	Index(['email', 'cnpj'], unique=True)
]


database.set_indexes('test_collection', _test_indexes)

