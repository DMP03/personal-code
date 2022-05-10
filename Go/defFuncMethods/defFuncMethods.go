package main

import (
	"fmt"
)

func main() {
	tabby := Cat{"Tabby", 5, "Meow!"}
	fmt.Println(tabby)
	fmt.Printf("%+v\n", tabby)
	fmt.Printf("Breed: %v\nWeight: %v\n", tabby.Breed, tabby.Weight)
	tabby.Weight = 4
	fmt.Printf("Breed: %v\nWeight: %v\n", tabby.Breed, tabby.Weight)

	tabby.Speak()
	tabby.Sound = "Purr!"
	tabby.Speak()
	tabby.SpeakThreeTimes()

}

// Cat is a struct
type Cat struct {
	Breed  string
	Weight int
	Sound  string
}

func (d Cat) Speak() {
	fmt.Println(d.Sound)
}

func (d Cat) SpeakThreeTimes() {
	d.Sound = fmt.Sprintf("%v %v %v", d.Sound, d.Sound, d.Sound)
	fmt.Println(d.Sound)
}
