package main

import (
	"fmt"
)

func main() {
	var out int

	for j := 0; j < 20; j++ {
		out = j*j + out
		if out > 12 {
			goto theEnd
		}
	}
theEnd:
	fmt.Println(out)
}
