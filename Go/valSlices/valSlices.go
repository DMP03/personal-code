package main

import (
	"fmt"
	"sort"
)

func main() {
	var colours = []string{"Red", "Blue", "Yellow"}
	fmt.Println(colours)
	colours = append(colours, "Green")
	fmt.Println(colours)

	colours = append(colours[1:len(colours)])
	fmt.Println(colours)
	colours = append(colours[:len(colours)-1])
	fmt.Println(colours)

	numbers := make([]int, 5, 5)
	numbers[0] = 134
	numbers[1] = 72
	numbers[2] = 32
	numbers[3] = 12
	numbers[4] = 136
	fmt.Println(numbers)

	numbers = append(numbers, 235)
	fmt.Println(numbers)

	sort.Ints(numbers)
	fmt.Println(numbers)

}
