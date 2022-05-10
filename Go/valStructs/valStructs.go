package main

import (
	"fmt"
)

func main() {
	tabby := Cat{"Tabby", 5}
	fmt.Println(tabby)
	fmt.Printf("%+v\n", tabby)
	fmt.Printf("Breed: %v\nWeight: %v\n", tabby.Breed, tabby.Weight)
	tabby.Weight = 4
	fmt.Printf("Breed: %v\nWeight: %v\n", tabby.Breed, tabby.Weight)

}

// Cat is a struct
type Cat struct {
	Breed  string
	Weight int
}
