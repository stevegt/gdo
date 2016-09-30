zerofn=/tmp/zero.data
randfn=/tmp/random.data

all: test

test: $(zerofn) $(randfn) test_cdc1

$(randfn): 
	dd if=/dev/urandom bs=9k count=320 > $(randfn)

$(zerofn):
	dd if=/dev/zero bs=9k count=320 > $(zerofn)

test_cdc1:
	time ./cdc1.py < $(zerofn) > /tmp/cdc1.out
	time ./cdc1p.py < $(zerofn) > /tmp/cdc1p.out
	time ./cdc1m.py $(zerofn) > /tmp/cdc1m.out
	diff /tmp/cdc1.out /tmp/cdc1p.out 
	diff /tmp/cdc1.out /tmp/cdc1m.out 
	time ./cdc1.py < $(randfn) > /tmp/cdc1.out
	time ./cdc1p.py < $(randfn) > /tmp/cdc1p.out
	time ./cdc1m.py $(randfn) > /tmp/cdc1m.out
	diff /tmp/cdc1.out /tmp/cdc1p.out 
	diff /tmp/cdc1.out /tmp/cdc1m.out 


