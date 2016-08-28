

class Db(object):
    
    def put(self, fh):
        '''put a file (or closed-end stream) into the db'''
        start hashing entire stream
        chunk_hashes = []
        for each chunk
        chunk_hash = self.put_chunk(chunk)
        finish hashing stream
             self.put_file(file_hash, chunk_hashes)

    def put_chunk(self, chunk):
        while true
            generate hash using next method
            if hash in db:
            verify bytes
            if mismatch:
                continue
                        else:
            insert chunk into db
                return hash

    def get_chunk(hash):
        
        yield chunk
