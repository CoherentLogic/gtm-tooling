package main

import (
	"log"
	"net/http"
	"os"
	"os/user"
	"strconv"
)

func main() {

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
	port := os.Getenv("GTMIS_PORT")

	if len(port) == 0 {
		port = "8080"
	}

	port = ":" + port

	log.Fatal(http.ListenAndServe(port, router))
}

func about() string {
	version := "0.01"

	return "GT.M Instrumentation Service v" + version + "\n Copyright (C) 2016 Coherent Logic Development\n\n"
}
