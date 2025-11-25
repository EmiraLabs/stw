package main

import (
	"log"
	"net/http"
)

func main() {
	fs := http.FileServer(http.Dir("./dist"))

	log.Fatal(http.ListenAndServe(":8001", fs))
	log.Println("Serving ./dist on http://localhost:8001")
}
