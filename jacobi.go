package main

import (
	"fmt"
)

// obtaining results of x1
// 13x+5y+-3z+u=18
func findx1(x2, x3, x4 float64) float64 {
	return (18 - x4 + 3*x3 - 5*x2) / 13
}

// obtaining results of x2
// 2x+12y+z-4u=13
func findx2(x1, x3, x4 float64) float64 {
	return (13 + 4*x4 - x3 - 2*x1) / 12
}

// obtaining results of x3
// x-4y+10z+u=29
func findx3(x1, x2, x4 float64) float64 {
	return (29 - x4 - x1 + 4*x2) / 10
}

// obtaining results of x4
// 2x+y-3z+9u=31
func findx4(x1, x2, x3 float64) float64 {
	return (31 - x2 - 2*x1 + 3*x3) / 9
}

func jacobi() {
	// var x1, x2, x3 float64
	// x1, x2, x3 = findx1(x2, x3), findx2(x1, x3), findx3(x1, x2)
	x1, x2, x3, x4 := 0.0, 0.0, 0.0, 0.0
	tmpx1, tmpx2, tmpx3, tmpx4 := 0.0, 0.0, 0.0, 0.0
	for i := 0; i < 100; i++ {
		// finding each element based on previous values
		tmpx1 = findx1(x2, x3, x4)
		tmpx2 = findx2(x1, x3, x4)
		tmpx3 = findx3(x1, x2, x4)
		tmpx4 = findx4(x1, x2, x3)
		// saving elements for the next calculations
		x1 = tmpx1
		x2 = tmpx2
		x3 = tmpx3
		x4 = tmpx4
		fmt.Printf("Iteration #%d x1: %v,\tx2: %v,\tx3: %v,\tx4:%v\n", i+1, x1, x2, x3, x4)
		//time.Sleep(1 * time.Second)
	}
}

func main() {
	jacobi()
}
