package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, _ := os.Open("../inputs/day01.txt")
	scanner := bufio.NewScanner(file)

	var lines []string
	var lastval int
	var val int
	var total int

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	lastval, _ = strconv.Atoi(lines[0])
	total = 0

	for _, line := range lines {
		val, _ = strconv.Atoi(line)
		if val > lastval {
			total += 1
		}
		lastval = val
	}

	fmt.Println(total)

}
