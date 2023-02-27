package main

import (
	"fmt"
)

// finding value of 1st x
// 20x+y-2z=17
// 3x+20y-z=-18
// 2x-3y+20z=25
func findx1(x2, x3 float64) float64 {
	return (17 + 2*x3 - x2) / 20
}

// finding value of 2nd x
func findx2(x1, x3 float64) float64 {
	return (-18 + x3 - 3*x1) / 20
}

// finding value of 3rd x
func findx3(x1, x2 float64) float64 {
	return (25 - 2*x1 + 3*x2) / 20
}

// correct formula to check if error is E=1+Δ
func gauss_seidal() {
	x1, x2, x3 := 0.0, 0.0, 0.0
	for i := 0; i < 10; i++ {
		// finding values based on their value from system of equalities
		x1 = findx1(x2, x3)
		x2 = findx2(x1, x3)
		x3 = findx3(x1, x2)
		fmt.Printf("Iteration #%d x1: %v,\tx2: %v,\tx3: %v\n", i+1, x1, x2, x3)
		//time.Sleep(1 * time.Second)
	}
}

func main() {
	gauss_seidal()
}
