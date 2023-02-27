package main

import (
	"fmt"
	"math"
)

// Obtaining result of f(x)
func getResult(x float64) float64 {
	return x*x*x - 2*x - 5
}

// Obtaining result of derivative of f(x)
func getDerivative(x float64) float64 {
	return 3*x*x - 2
}

// xn+1 = xn - f(xn)/f'(xn)
func newtonRaphson(x float64) {
	// finding h based on the newthon raphson method f(x)/f'(x)
	h := getResult(x) / getDerivative(x)
	// divided difference formula only for unqeual intervals
	iterations := 0
	for math.Abs(h) >= 0.001 {
		// counting iterations
		iterations++
		fmt.Printf("Iteration: %d x=%v\n", iterations, x)
		h = getResult(x) / getDerivative(x)
		// obtaining new value for x
		x = x - h
	}

	fmt.Printf("Root:%v\tres:%v\n", x, getResult(x))
}

func main() {
	var x0 float64 = 1 // starting value
	newtonRaphson(x0)
}
