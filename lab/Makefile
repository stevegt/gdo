randfn=/tmp/random.data

all: test

test: $(randfn) test_cdc1

$(randfn): 
	dd if=/dev/urandom bs=9k count=320 > $(randfn)

test_cdc1:
	./cdc1.py < $(randfn) > /tmp/cdc1.out
	./cdc1p.py < $(randfn) > /tmp/cdc1p.out
	diff /tmp/cdc1.out /tmp/cdc1p.out 
