package main

import (
	"bufio"
	"fmt"
	"os"
)

func searchLenMinSubst(str string, countLet int) int {
	//countLet = len(str) // todo
	min := -1

	for i := 0; i < countLet-1; i++ {
		cache := map[uint8]interface{}{str[i]: nil}

		for j := i + 1; j < countLet; j++ {
			cache[str[j]] = nil
			presentValue := j - i + 1

			if presentValue >= min && min != -1 {
				continue
			}

			if len(cache) == 4 {
				if presentValue == 4 {
					return 4
				}
				min = presentValue
				break
			}

			if str[i] == str[j] {
				i++
			}
		}
	}
	return min
}

func main() {
	in := bufio.NewReader(os.Stdin)

	var count int
	var str string

	fmt.Fscan(in, &count)
	fmt.Fscan(in, &str)

	fmt.Println(searchLenMinSubst(str, count))
}

// 12 aabbccddbadd
// 16 aaaabbbbccccdddd
// 7 dbbccca
// 7 abcabac
