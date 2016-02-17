package main

import (
	"log"
	"net/http"
	"fmt"
	"os"
)

func main() {

	fmt.Print(about())

	router := NewRouter()
	port := os.Getenv("GTMIS_PORT")

	if len(port) == 0 {
		port = "8080"
	}

	fmt.Print("Listening on port " + port + "\n")

	port = ":" + port

	log.Fatal(http.ListenAndServe(port, router))
}

func about() string {
	version := "0.01"

	return "GT.M Instrumentation Service v" + version + "\n Copyright (C) 2016 Coherent Logic Development\n\n"
}
