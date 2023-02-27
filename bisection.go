package main

import (
	"fmt"
	"math"
)

// getting result of f(x), when numerical techniques more commonly involve iterative
func getResult(x float64) float64 {
	return (x*x*x - 4*x + 9)
}

func bisection(a, b float64) float64 {
	// checking if assumed a and b interval is correct
	if getResult(a)*getResult(b) >= 0 {
		return -1
	}
	c := a
	interations := 1
	fmt.Printf("Iteration: 1\tx1=%f  x2=%f\n", a, b)
	// calculating until correct to 4 digits after .
	for {
		// obtaining results of each x from interval
		c = (a + b) / 2

		if getResult(c)*getResult(a) < 0 {
			b = c
		} else {
			a = c
		}
		// counting iteration number
		interations++
		fmt.Printf("Iteration: #%d x%d=%f\n", interations, interations+1, c)
		if math.Abs(getResult(c)) <= 0.0001 {
			break
		}
	}
	return c
}

func main() {
	fmt.Println()
	var a float64 = -3
	var b float64 = -2
	c := bisection(a, b)
	fmt.Println()
	fmt.Printf("Root: %f", c)
}
