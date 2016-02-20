all: bin/gtmis

clean:
	rm -f bin/gtmis

bin/gtmis:
	go build -o bin/gtmis src/rest/*.go

install:
	mkdir -p /usr/share/gtmis/agents
	install -o root -g wheel -m 755 src/agents/*.py /usr/share/gtmis/agents
	mkdir -p /etc/gtmis
	echo "vista:8080" > /etc/gtmis/instances	
	install -o root -g wheel bin/gtmis /usr/sbin
	rm -f /tmp/gtmis
	cp bin/init.rhel6 /tmp/gtmis
	chmod +x /tmp/gtmis
	install -o root -g wheel /tmp/gtmis /etc/init.d
	chkconfig --add gtmis
	service gtmis start

uninstall:
	service gtmis stop
	chkconfig --del gtmis
	rm -f /etc/init.d/gtmis
	rm -rf /usr/share/gtmis
	rm -rf /etc/gtmis
	rm -f /usr/sbin/gtmis