package main

import (
	"fmt"
)

func main() {
	theAns := 42
	var result string

	if theAns < 0 {
		result = "Less than zero"
	} else if theAns == 0 {
		result = "Equal to zero"
	} else {
		result = "Greater than zero"
	}

	fmt.Println(result)

	if x := -42; x < 0 {
		result = "Less than zero"
	} else if x == 0 {
		result = "Equal to zero"
	} else {
		result = "Greater than zero"
	}

	fmt.Println(result)

}