package main

import "fmt"

func main() {
	message := make(chan string)
	singnals := make(chan bool)

	select {
	case msg := <-message:
		fmt.Println("received message", msg)
	default:
		fmt.Println("no message received")
	}

	msg := "hi"
	select {
	case message <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("no message sent")
	}

	select {
	case msg := <-message:
		fmt.Println("received message", msg)
	case sig := <-singnals:
		fmt.Println("received singnal", sig)
	default:
		fmt.Println("no activity")
	}
}