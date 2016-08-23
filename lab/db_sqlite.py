#!/usr/bin/python

import sqlite3

class Db(object):

	def __init__(self, fn):
		self.fn = fn

	def create_tables(self):
		cur = self.conn.cursor()
		cur.execute("create table chunks (hash TEXT, chunk BLOB)")
		cur.execute("create table cnodes (hash TEXT, seq INT, chunk TEXT)")
		
	def open(self):
		self.conn = sqlite3.connect(self.fn)

	def close(self):
		self.conn.commit()
		self.conn.close()

	def put(self, src):
		cur = db.conn.cursor()
		cur.executemany(
				"insert into chunks ('hash', 'chunk') values (?, ?)", 
				self.gen_chunks())
		cur.executemany(
				"insert into cnodes ('hash', 'seq', 'chunk') values (?, ?, ?)", 
				self.gen_chunks())


	def gen_chunks(self):
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

