#!/usr/bin/python

import db_sqlite
from cdc1 import *

def get_kv():
	cdc = CDC1(1027, 16)
	cdc1_init(cdc, lambda: sys.stdin.read(1))
	while True:
		size = cdc1_get_chunk(cdc)
		if size == 0:
			break
		h = hashlib.sha256(cdc.chunk)
		k = "sha256:%s" % h.hexdigest()
		yield k, buffer(cdc.chunk)

db = db_sqlite.Db('/tmp/foo.db')
db.open()
cur = db.conn.cursor()
k = "sha256:bfa75aec64ca6e00ea0a80a9b8426d7fc0ad960f6ee0d08d2a6a338ec4e564ca"
for row in cur.execute('select value from kvstore where key=?', (k,)):
	value = row[0]
	sys.stdout.write(value)
db.close()

