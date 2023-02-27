package main

import (
	"fmt"
	"math"
)

// obtaining result of f(x)
func getResult(x float64) float64 {
	res := (x*x*x - 3*x + 1)
	return res
}

func secant(x1, x2, E float64) {
	var n float64 = 0
	var xm float64 = 0
	var x0 float64 = 0
	var c float64 = 0
	if getResult(x1)*getResult(x2) < 0 {
		// obtaining the interm value
		x0 = (x1*getResult(x2) - x2*getResult(x1)) / (getResult(x2) - getResult(x1))
		// checking if x0 is root
		c = getResult(x1) * getResult(x0)
		x1 = x2
		x2 = x0
		n++
		// obtaining result of first x value
		xm = (x1*getResult(x2) - x2*getResult(x1)) / (getResult(x2) - getResult(x1))

		iterations := 2
		for math.Abs(xm-x0) >= E {
			fmt.Printf("x%d=%v\n", iterations, x2)
			iterations++
			// obtaining the interm value
			x0 = (x1*getResult(x2) - x2*getResult(x1)) / (getResult(x2) - getResult(x1))
			// check if x0 is root
			c = getResult(x1) * getResult(x0)
			x1 = x2
			x2 = x0
			// counting iterations
			n++
			// outputing if c is root
			if c == 0 {
				break
			}
			xm = (x1*getResult(x2) - x2*getResult(x1)) / (getResult(x2) - getResult(x1))
		}

		fmt.Printf("Root: %v, \t value: %v", x0, getResult(x0))
		fmt.Println("Iterations: ", n)
	} else {
		fmt.Println("No root in the given interval")
	}
}

func main() {
	var x0 float64 = 1
	var x1 float64 = 2
	var E float64 = 0.0001
	secant(x0, x1, E)
}
