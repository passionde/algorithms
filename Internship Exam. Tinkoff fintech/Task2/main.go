package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, k int // джуны, сеньеры, кол-во проверок

	fmt.Fscan(in, &n)
	fmt.Fscan(in, &m)
	fmt.Fscan(in, &k)

	result := (n * k) / m

	if (n*k)%m != 0 {
		result++
	}

	fmt.Println(result)
}
