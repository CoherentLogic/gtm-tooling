package main

import (
	"log"
	"net/http"
	"os"
	"os/user"
	"strconv"
	"flag"
)

func main() {
	
	portFlag := flag.Int("port", 8080, "Port on which the service will listen")
	flag.Parse()

	user, err := user.Current()
	if err != nil {
		log.Fatal(err)
	}
	
	my_homedir := user.HomeDir
	my_pid := strconv.Itoa(os.Getpid())

	pidfile := my_homedir + "/.gtmis.pid"

	f, err := os.Create(pidfile)
	defer f.Close()
	f.WriteString(my_pid)
	f.Sync()

	router := NewRouter()

	port := strconv.Itoa(*portFlag)

	port = ":" + port
	
	log.Println(about())	
	log.Println("Listening on port", strconv.Itoa(*portFlag))
	
	log.Fatal(http.ListenAndServe(port, router))

}

func about() string {
	version := "0.01"

	return "GT.M Instrumentation Service v" + version + " Copyright (C) 2016 Coherent Logic Development"
}
