package main

import (
	"os/exec"
	"fmt"
	"net/http"
	"log"
)

func InstanceData(w http.ResponseWriter, r *http.Request) {

	cmd := exec.Command("python", GetAgentPath() + "InstanceData.py")

	output, err := cmd.CombinedOutput()

	if err != nil {
		log.Println("Error: ", err)
		fmt.Fprint(w, "Internal service error or server misconfiguration.")
		
	} else {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
		fmt.Fprint(w, string(output)) 
	}

}

func ServiceInfo(w http.ResponseWriter, r *http.Request) {

	w.Header().Set("Content-Type", "text/html; charset=UTF-8")

	fmt.Fprint(w, "<html><head><title>GT.M Instrumentation Service</title></head>")
	fmt.Fprint(w, "<body>")

	fmt.Fprint(w, "<h1>GT.M Instrumentation Service Endpoints</h1><table>")
	fmt.Fprint(w, "<tr><th>Endpoint</th><th>Method</th><th>Description</th></tr>")

	for _, route := range routes {
		link := "<tr><td><a href=\"" + route.Pattern + "\">" + route.Pattern + "</a></td><td>" + route.Method + "</td><td>" + route.HelpText + "</td></tr>"
		fmt.Fprint(w, link)
	}

	fmt.Fprint(w, "</table></body></html>")

}

func GetAgentPath() string {
	return "/usr/share/gtmis/agents/"
}
