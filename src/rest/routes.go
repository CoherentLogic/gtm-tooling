package main

import "net/http"

type Route struct {
	Name        string
	Method      string
	Pattern     string
	HandlerFunc http.HandlerFunc
	HelpText    string
}

type Routes []Route

var routes Routes

func init() {

	routes = Routes {
		Route {
			"Index",
			"GET",
			"/",
			ServiceInfo,
			"Returns a list of instrumentation service endpoints. Synonomous with /ServiceInfo.",
		},
		Route {
			"InstanceData",
			"GET",
			"/InstanceData",
			InstanceData,
			"Returns information about the GT.M instance.",
		},
		Route {
			"ServiceInfo",
			"GET",
			"/ServiceInfo",
			ServiceInfo,
			"Returns a list of instrumentation service endpoints.",
		},
	}
	
}
