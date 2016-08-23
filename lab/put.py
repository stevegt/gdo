#!/usr/bin/python

import db_sqlite
from cdc1 import *

class CNode(object):

	def __init__(self, src):
		self.src = src

	def put(self, src):

def gen_chunks():
	cdc = CDC1(1027, 16)
	cdc1_init(cdc, lambda: sys.stdin.read(1))
	fh = hashlib.sha256()
	hashes = []
	while True:
		size = cdc1_get_chunk(cdc)
		if size == 0:
			break
		h = hashlib.sha256(cdc.chunk)
		fh.update(cdc.chunk)
		k = "sha256:%s" % h.hexdigest()
		hashes.append(k)
		yield k, buffer(cdc.chunk), 'b'

db = db_sqlite.Db('/tmp/foo.db')
db.open()
db.create_tables()
cur = db.conn.cursor()
cur.executemany(
	"insert into chunks ('hash', 'chunk') values (?, ?)", gen_chunks())
db.close()

