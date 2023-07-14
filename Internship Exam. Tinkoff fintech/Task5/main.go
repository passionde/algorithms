package main

import (
	"bufio"
	"fmt"
	"os"
)

type segments struct {
	len   int
	cache map[int]int
}

func (s *segments) getAllReasonableSub(arr []int) {
	s.len = len(arr)
	s.cache = make(map[int]int)

	for i := 0; i < len(arr); i++ {
		var sum int
		for j := i; j < len(arr); j++ {
			sum += arr[j]
			if sum == 0 {
				if val, ok := s.cache[i]; (ok && j < val) || !ok {
					s.cache[i] = j
				}
				break
			}
		}
	}
}

func (s *segments) countNormalSegments() int {
	result := 0

	for i := 0; i < s.len; i++ {
		minValue, isFind := s.cache[i]

		for j := i; j < s.len; j++ {
			value, ok := s.cache[j]

			if ok {
				if !isFind {
					isFind = true
					minValue = value
				} else if ok && value <= minValue {
					isFind = true
					minValue = value
				}
			}

			//fmt.Println("i =", i, "j =", j, "minValue", minValue, "if =", isFind)
			if isFind && minValue <= j {
				result += s.len - j
				//fmt.Println("+", s.len-j)
				break
			}
		}
	}
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)

	var count, dig int
	fmt.Fscan(in, &count)

	arr := make([]int, 0, count)

	for i := 0; i < count; i++ {
		fmt.Fscan(in, &dig)
		arr = append(arr, dig)
	}

	var s segments

	s.getAllReasonableSub(arr)
	fmt.Println(s.countNormalSegments())

}
