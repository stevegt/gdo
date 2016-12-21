# GDO Laboratory

This directory contains rough drafts and half-baked ideas, many of
which are pseudocode, most of which are wrong.  Nothing here is
supposed to make sense or be useful for anything whatsoever.  A very
small subset may graduate from here to elsewhere in the repository.

## To Do

- spike now: access controls
- how to detect changes?
    - so we can hash and distribute
    - file layer
        - inotify
            inotifywait -mr --format "%w%f %e" /tmp
            - detect dirty files
    - block layer
        - see https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/
            - replaced aufs
        - dm-log-userspace 
            - detect dirty blocks
- finish put.py
    - without chunk fault
    - with chunk fault
- finish get.py
- finish db_sqlite.py
- wire protocol is
    - chain completion protocol
    - universal chain protocol
    - universal chain completion protocol
    - microchain protocol
    - pattern completion protocol
    - sequence completion protocol
    - ordered list completion protocol
- chunk fault
    - local disk is a cache
    - cache miss causes chunk retrieval from a peer
- retrieval might be purchase from a trusted peer
    - trust builds over time
    - we rate peers based on latency
    - purchase might be in personal currency, either peer's (if we
      have any) or our own
- think through ultimate use of force
    - local admins can delete chunks
    - local admins can kill processes
    - local admins can filter packets
    - they need to be compensated for resource usage
    - all else is built on those foundations
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
- cdch as higher-performance version of cdc1+cdh1 
- reimplement cdc1p in C
- ECDSA signing
- ECDH for shared key agreement
- rename cdc1m to cdch16?
