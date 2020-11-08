package main

import (
	"bufio"
	"os"
	"strings"
	"time"
)

var ხალხმა_გამოიღვიძა bool = false
var ბიძინა_აზის_ქვეყანას bool = true

func main() {
	// ერთადერთი ცდა
	go func() {
		reader := bufio.NewReader(os.Stdin)
		ხალხის_სიტყვა, _ := reader.ReadString('\n')
		ხალხის_სიტყვა = strings.TrimSpace(ხალხის_სიტყვა)
		if ხალხის_სიტყვა == "მე ვარ მთავარი!" {
			ხალხმა_გამოიღვიძა = true
		}
		println("ხალხმა სიტყვა თქვა: '" + ხალხის_სიტყვა + "'")
	}()

	for ბიძინა_აზის_ქვეყანას {
		if ხალხმა_გამოიღვიძა {
			break
		}
		println("საქართველო იტანჯება!!!")
		time.Sleep(time.Second)
	}
	println("საქართველოს შანსი მიეცა!")
}
