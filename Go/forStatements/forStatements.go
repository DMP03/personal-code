package main

import (
	"fmt"
)

func main() {

	colours := []string{"Red", "Blue", "Green"}
	fmt.Println(colours)

	for i := 0; i < len(colours); i++ {
		fmt.Println(colours[i])
	}

	for i := range colours {
		fmt.Println(colours[i])
	}

	for _, colour := range colours {
		fmt.Println(colour)
	}

	value := 1
	for value < 10 {
		fmt.Println("Value:", value)
		value++
	}

	sum := 1
	for sum < 1000 {
		sum += sum
		fmt.Println("Sum:", sum)
		if sum > 200 {
			goto theEnd
		}
	}

theEnd:
	fmt.Println("End of program")
}
