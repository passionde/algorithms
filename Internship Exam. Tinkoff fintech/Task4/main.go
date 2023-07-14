package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func isBoring(counter map[int]int) bool {
	reverseMap := make(map[int]int)
	for _, val := range counter {
		reverseMap[val]++
	}

	// проверка на все единицы
	if len(reverseMap) == 1 {
		_, ok := reverseMap[1]
		return ok
	}

	if len(reverseMap) == 2 {
		// получение всех ключей
		keys := make([]int, 0, 2)
		for key, _ := range reverseMap {
			keys = append(keys, key)
		}

		if val := reverseMap[keys[0]]; val == 1 {
			return math.Abs(float64(keys[0]-keys[1])) == 1 || keys[0] == 1 || keys[1] == 1
		}

		if val := reverseMap[keys[1]]; val == 1 {
			return math.Abs(float64(keys[0]-keys[1])) == 1 || keys[0] == 1 || keys[1] == 1
		}
	}

	return false
}

func searchMaxPrefix(arr []int, counter map[int]int) int {
	for i := len(arr); i >= 0; i-- {

		if isBoring(counter) {
			//fmt.Println(arr[:i])
			return i
		}

		counter[arr[i-1]]--
		if counter[arr[i-1]] == 0 {
			delete(counter, arr[i-1])
		}
	}
	return 2
}

func main() {
	in := bufio.NewReader(os.Stdin)

	var count, dig int
	fmt.Fscan(in, &count)

	arr := make([]int, 0, count)
	counter := make(map[int]int)

	for i := 0; i < count; i++ {
		fmt.Fscan(in, &dig)
		arr = append(arr, dig)
		counter[dig]++
	}

	fmt.Println(searchMaxPrefix(arr, counter))

}

// 13    1 2 3 1 2 2 3 3 3 1 4 4 5
// 10    1 2 4 2 3 1 3 9 15 23
// 5     1 2 3 4 5
