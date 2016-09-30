# GDO Laboratory

This directory contains rough drafts and half-baked ideas, many of
which are pseudocode, most of which are wrong.  Nothing here is
supposed to make sense or be useful for anything whatsoever.  A very
small subset may graduate from here to elsewhere in the repository.

## To Do

- write a daemon 
    - http to serve javascript GUI
    - websocket
- internode protocol
    - open connection
    - tx bid/ask list 
    - rx bid/ask list, fills, and chunks
    - tx bid/ask list, fills, and chunks
    - ...
    - close connection
    - discard order book 
- run rolling hash over concatenated hashes?
    - maybe with a smaller word size?
- merge cdc1, cdh1, and rough_draft_pseudocode into db_sqlite
    - turn the stream hash in cdh1 into a root hash of the hash tree;
      https://en.wikipedia.org/wiki/Hash_list
      https://en.wikipedia.org/wiki/Merkle_tree
- create a vanilla DB superclass for future storage methods
- finish put.py
- finish get.py
- finish db_sqlite.py
- cdch as higher-performance version of cdc1+cdh1 
- reimplement cdc1p in C
- ECDSA signing
- ECDH for shared key agreement
- rename cdc1m to cdch16?
