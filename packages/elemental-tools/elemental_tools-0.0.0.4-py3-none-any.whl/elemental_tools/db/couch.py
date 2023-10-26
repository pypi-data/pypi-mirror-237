from cloudant.client import CouchDB
from cloudant.result import Result, ResultByKey
from time import sleep


class CollectionAbstraction:
	timeout = 10

	def __init__(self, connection):
		self.connection = connection

	def find_one(self, selector):
		# Find the first document matching the selector
		result = self.connection.get_query_result(selector)
		try:
			return next((e for e in result))
		except StopIteration:
			return None

	def find_many(self, selector):
		# Find all documents matching the selector
		return list(self.connection.get_query_result(selector))

	def insert(self, doc, upsert=False, upsert_selector: dict = None, constraints: list = None):

		if constraints:
			for constraint in constraints:
				if len(self.connection.get_query_result(constraint).all()):
					raise ValueError("Duplicate constraint for %s" % constraint)

		if upsert and upsert_selector is None:
			raise Exception('You must specify a upsert_selector')

		# Check if the document already exists
		existing_doc = None
		if upsert_selector:
			existing_doc = self.find_one({"_id": doc["_id"]})

		if existing_doc is not None:
			if upsert and upsert_selector:
				# Update the existing document
				existing_doc.update(doc)
				self.connection.save(existing_doc)
				return existing_doc
			else:
				return None
		else:
			# Insert the new document
			_doc = self.connection.create_document(doc)
			if '_rev' in _doc.keys():
				_doc.save()
				return _doc
			else:
				return None

	def update(self, selector, update_fields, upsert=False):
		# Check if the document already exists
		existing_doc = self.connection.get_query_result(selector)
		if len(existing_doc.all()):
			# generate the new documents
			docs = []
			previous_docs = list(existing_doc)

			# remove the existing document
			for doc in previous_docs:
				previous_row = self.connection[doc["_id"]]
				previous_row.fetch()
				previous_row.delete()

			for doc in previous_docs:
				del doc['_rev']
				new_doc = dict(doc)
				for field, value in update_fields.items():
					if "_rev" not in field:
						new_doc[field] = value
				docs.append(new_doc)

			current_timeout = 0
			while not self.timeout <= current_timeout:
				current_timeout += 1
				sleep(0.1)


			# Update the existing documents
			update = self.connection.bulk_docs(docs)
			result = [update_doc for update_doc in update if "ok" in update_doc.keys()]

			if not len(result):
				return None

			return result
		elif upsert:
			# Insert a new document
			_doc = self.connection.create_document(update_fields)
			if '_rev' in _doc.keys():
				_doc.save()
				return _doc
			else:
				return None
		else:
			return None

	def delete(self, selector):
		# Check if the document exists
		existing_doc = self.connection.get_query_result(selector)
		result = []
		for doc in existing_doc:
			result.append(doc)
			self.connection[doc['_id']].fetch()
			self.connection[doc['_id']].delete()

		if result:
			return True
		else:
			return False


class Connect:

	def __init__(self, url, db_user, db_pass, connect=True, auto_renew=True, *args, **kwargs):
		self.server = CouchDB(db_user, db_pass, url=url, connect=True, auto_renew=True, *args, **kwargs)

	def collection(self, name):

		try:
			self.server[name]
		except KeyError:
			self.server.create_database(name)

		return CollectionAbstraction(self.server[name])


# usage:
if __name__ == '__main__':
	url = "http://vault.local:5984"
	database = Connect(url=url, db_user='admin', db_pass=1205, connect=True, auto_renew=True)
	collection = database.collection('test')

	# insert one:
	print(f"""insert: {collection.insert(doc={'name': "test"}, constraints=[{'name': {"$eq": "test"}}])}, expected result: document""")
	input("waiting for input...")

	# find_one:
	#print(f"""find_one: {collection.find_one(selector={'name': {"$eq": "test"}})}, expected result: document""")
	#input("waiting for input...")
#
	## find_many:
	#print(f"""find_many: {collection.find_many(selector={'name': {"$eq": "test"}})}, expected result: document""")
	#input("waiting for input...")
#
	## update:
	#print(f"""update: {collection.update(selector={'name': {"$eq": "test"}}, update_fields={'name': "test1"})}, expected result: document""")
	#input("waiting for input...")
#
	## delete:
	#print(f"""delete: {collection.delete(selector={"name": {"$eq": "test1"}})}, expected result: {True}""")
	#input("waiting for input...")
#
	## delete:
	#print(f"""delete: {collection.delete(selector={"name": {"$eq": "test1"}})}, expected result: {False}""")
	#input("waiting for input...")
#
#