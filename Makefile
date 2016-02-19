all: bin/gtmis

bin/gtmis:
	go build -o bin/gtmis src/rest/*.go

install:
	mkdir -p /etc/gtmis	
	install -o root -g wheel bin/gtmis /usr/sbin
	rm -f /tmp/gtmis
	cp bin/init.rhel6 /tmp/gtmis
	chmod +x /tmp/gtmis
	install -o root -g wheel /tmp/gtmis /etc/init.d