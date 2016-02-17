package main

import (
	"os/exec"
	"fmt"
	"net/http"
	"os"
)

func InstanceData(w http.ResponseWriter, r *http.Request) {

	cmd := exec.Command("python", GetAgentPath() + "InstanceData.py")

	output, err := cmd.CombinedOutput()

	if err != nil {
		fmt.Fprint(w, "Internal error")
	} else {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
		fmt.Fprint(w, string(output)) 
	}

}

func ServiceInfo(w http.ResponseWriter, r *http.Request) {

	w.Header().Set("Content-Type", "text/html; charset=UTF-8")

	fmt.Fprint(w, "<html><head><title>GT.M Instrumentation Service</title></head><body>")
	fmt.Fprint(w, "Endpoints: <br><br><a href=/InstanceData>/InstanceData</a> [GET] <br><a href=/ServiceInfo>/ServiceInfo</a> [GET]</body></html>")

}

func GetAgentPath() string {

	agents_path := os.Getenv("GTMIS_AGENTS_PATH")

	if len(agents_path) == 0 {
		agents_path = "../agents"
	}

	return agents_path + "/"

}
