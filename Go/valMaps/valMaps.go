package main

import (
	"fmt"
	"sort"
)

func main() {

	cities := make(map[string]string)
	fmt.Println(cities)
	cities["LDN"] = "London"
	cities["BNM"] = "Bournemouth"
	cities["NTH"] = "Nottingham"
	cities["BMH"] = "Birmingham"
	fmt.Println(cities)

	london := cities["LDN"]
	fmt.Println(london)

	delete(cities, "BMH")
	cities["SHF"] = "Sheffield"
	fmt.Println(cities)

	for k, v := range cities {
		fmt.Printf("%v: %v\n", k, v)
	}

	keys := make([]string, len(cities))
	i := 0
	for k := range cities {
		keys[i] = k
		i++
	}

	fmt.Println(keys)
	sort.Strings(keys)
	fmt.Println(keys)

	for i := range keys {
		fmt.Println(cities[keys[i]])
	}

}
