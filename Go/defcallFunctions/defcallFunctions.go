package main

import (
	"fmt"
)

func main() {

	doSomething()
	sum := addValues(6, 9)
	fmt.Println("The sum is:", sum)

	multiSum, multiCount := addAllValues(4, 7, 6, 2, 3)
	fmt.Println("Sum of multiple values:", multiSum)
	fmt.Println("Count of items:", multiCount)
}

func doSomething() {
	fmt.Println("Doing something")
}

func addValues(val1 int, val2 int) int {
	return val1 + val2
}

func addAllValues(values ...int) (int, int) {
	total := 0
	for _, v := range values {
		total += v
	}
	return total, len(values)
}
