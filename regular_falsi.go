package main

import (
	"fmt"
	"math"
)

const (
	MAX_ITER = 10
)

// obtaining result of f(x)
func getResult(x float64) float64 {
	res := math.Pow(x, 4) - 32
	return res
}

// x2 = x0 - ( (x1-x0) / (f(x1) - f(x0)) ) * f(x0)
func regulaFalsi(a, b float64) {
	// checking if interval is correct
	if getResult(a)*getResult(b) >= 0 {
		fmt.Println("interval not correct")
		return
	}

	var c float64

	for i := 0; i < MAX_ITER; i++ {

		// Finding interim value based on regularFalsi method formula
		c = (a*getResult(b) - b*getResult(a)) / (getResult(b) - getResult(a))

		// Checking if the values if found correct up to 3 digits after .
		if getResult(c) < 0.001 && getResult(c) > 0 {
			break
		} else if getResult(c)*getResult(a) < 0 {
			b = c
		} else {
			a = c
		}
		fmt.Printf("%v Root: %v, result: %v\n", i+1, c, getResult(c))

	}
	fmt.Printf("Root: %v, result: %v", c, getResult(c))
}

func main() {
	// starting values
	var a float64 = 2
	var b float64 = 3

	regulaFalsi(a, b)
}
