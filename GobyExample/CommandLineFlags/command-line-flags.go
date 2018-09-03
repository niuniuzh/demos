package main

import "flag"
import "fmt"

func main() {
	wordPrt := flag.String("word", "foo", "a string")

	numPtr := flag.Int("numb", 42, "an int")
	boolPtr := flag.Bool("fork", false, "a bool")

	var svar string
	flag.StringVar(&svar, "svar", "bar", "a string var")
	
	flag.Parse()

	fmt.Println("word:", *wordPrt)
	fmt.Println("numb:", *numPtr)
	fmt.Println("fork:", *boolPtr)
	fmt.Println("svar:", svar)
	fmt.Println("tail:", flag.Args())
}