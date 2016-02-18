all: bin/gtmis

bin/gtmis:
	go build -o bin/gtmis src/rest/*.go