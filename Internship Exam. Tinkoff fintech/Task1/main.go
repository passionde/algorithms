package main

import (
	"bufio"
	"fmt"
	"os"
)

func isSorted(arr []int, reverse bool) bool {
	a := arr[0]

	// По убыванию
	if reverse {
		for _, b := range arr[1:] {
			if a > b {
				return false
			}
			a = b
		}
		return true
	}

	// По возрастанию
	for _, b := range arr[1:] {
		if a < b {
			return false
		}
		a = b
	}

	return true
}

func main() {
	digits := make([]int, 4, 4)
	in := bufio.NewReader(os.Stdin)

	for i := 0; i < 4; i++ {
		fmt.Fscan(in, &digits[i])
	}

	if isSorted(digits, true) || isSorted(digits, false) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}

}
