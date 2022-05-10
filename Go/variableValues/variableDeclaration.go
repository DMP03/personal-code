package main

import (
	"fmt"
)

const aConst int = 64

func main() {

	var aString string = "This is Go!" //declaring a variable follows {var [nameHere] [variable type] = [value]}
	fmt.Println(aString)
	fmt.Printf("The variable's type is %T\n", aString) //%T is placeholder function, \n is newline as print statements are naturally concatinated when using printf

	var anInt int = 42
	fmt.Println(anInt)
	fmt.Printf("The variable's type is %T\n", anInt)

	var defaultInt int
	fmt.Println(defaultInt)

	var anotherStr = "This is another string"
	fmt.Println(anotherStr)
	fmt.Printf("The variable's type is %T\n", anotherStr)

	var anotherInt = 53
	fmt.Println(anotherInt)
	fmt.Printf("This variable's type is %T\n", anotherInt)

	myString := "This is also a string"
	fmt.Println(myString)
	fmt.Printf("The variable's type is %T\n", myString)

	fmt.Println(aConst)
	fmt.Printf("The variable's type is %T\n", aConst)
}
