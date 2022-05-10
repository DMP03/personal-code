package main

import (
	"fmt"
)

func main() {
	var colours [3]string
	colours[0] = "Red"
	colours[1] = "Green"
	colours[2] = "Blue"
	fmt.Println(colours)
	fmt.Println(colours[0])

	var numbers = [5]int{5, 3, 1, 2, 4}
	fmt.Println(numbers)

	fmt.Println("Number of colurs:", len(colours))
	fmt.Println("Number of numbers:", len(numbers))
}
