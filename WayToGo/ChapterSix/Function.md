# 函数介绍
* Go是编译型语言，所以函数编写的顺序是无关紧要的；鉴于可读性的需求，最好把 main() 函数写在文件的前面
* 普通的带有名字的函数
* 匿名函数或者lambda函数（参考 第 6.8 节）
* 方法（Methods，参考 第 10.6 节）
* 除了main()、init()函数外，其它所有类型的函数都可以有参数与返回值。函数参数、返回值以及它们的类型被统称为函数签名
* 函数不能在其它函数里面声明（不能嵌套），不过我们可以通过使用匿名函数（参考 第 6.8 节）来破除这个限制

# 函数参数与返回值
* 任何一个有返回值（单个或多个）的函数都必须以 return 或 panic（参考 第 13 章）结尾
* 没有参数的函数通常被称为 niladic 函数（niladic function）

# 按值传递,按引用传递
* Go 默认使用按值传递来传递参数，也就是传递参数的副本
* 指针也是变量类型，有自己的地址和值，通常指针的值指向一个变量的地址。所以，按引用传递也是按值传递
* 几乎在任何情况下，传递指针（一个32位或者64位的值）的消耗都比传递副本来得少
* 切片（slice）、字典（map）、接口（interface）、通道（channel）这样的引用类型都是默认使用引用传递

# 命名的返回值
* 尽量使用命名返回值：会使代码更清晰、更简短，同时更加容易读懂。

# 空白符
* 空白符用来匹配一些不需要的值，然后丢弃掉

# 改变外部变量
* 传递指针给函数不但可以节省内存（因为没有复制变量的值），而且赋予了函数直接修改外部变量的能力

# 传递变长参数
* 函数的最后一个参数是采用 ...type 的形式，那么这个函数就可以处理一个变长的参数  func myFunc(a, b, arg ...int) {}
* 如果参数被存储在一个 slice 类型的变量 slice 中，则可以通过 slice... 的形式来传递参数，调用变参函数
* 但是如果变长参数的类型并不是都相同的呢？使用结构、使用空接口

# defer 和追踪
* 关键字 defer 允许我们推迟到函数返回之前（或任意位置执行 return 语句之后）一刻才执行某个语句或函数
* 关键字 defer 允许我们进行一些函数执行完成后的收尾工作
* 关闭文件流 （详见 第 12.2 节） defer file.Close()
* 解锁一个加锁的资源 （详见 第 9.3 节）mu.Lock()  defer mu.Unlock() 
* 打印最终报告  printHeader()  defer printFooter()
* 关闭数据库链接  defer disconnectFromDB()
* 使用 defer 语句实现代码追踪
* 使用 defer 语句来记录函数的参数与返回值

# 内置函数
* close	用于管道通信
* len、cap	len 用于返回某个类型的长度或数量（字符串、数组、切片、map 和管道）；cap 是容量的意思，用于返回某个类型的最大容量（只能用于切片和 map）
* new、make  new 和 make 均是用于分配内存、new 用于值类型和用户定义的类型，如自定义结构，make 用于内置引用类型（切片、map 和管道）
* copy、append  用于复制和连接切片
* panic、recover	两者均用于错误处理机制
* print、println	底层打印函数（详见第 4.2 节），在部署环境中建议使用 fmt 包
* complex、real imag	用于创建和操作复数（详见第 4.5.2.2 节）

# 递归函数
* 使用递归函数时经常会遇到的一个重要问题就是栈溢出：一般出现在大量的递归调用导致的程序栈内存分配耗尽
* 通过一个名为懒惰求值的技术解决，在 Go 语言中，我们可以使用管道（channel）和 goroutine（详见第 14.8 节）来实现

# 将函数作为参数
* 将函数作为参数的最好的例子是函数 strings.IndexFunc()
* 函数的签名是 func IndexFunc(s string, f func(c int) bool) int，它的返回值是在函数 f(c) 返回 true、-1 或从未返回时的索引值

# 闭包
* 当我们不希望给函数起名字的时候，可以使用匿名函数
* 可以被赋值于某个变量，即保存函数的地址到变量中
* 可以直接对匿名函数进行调用：func(x, y int) int { return x + y } (3, 4)
* 它们被允许调用定义在其它环境下的变量。闭包可使得某个函数捕捉到一些外部状态

# 应用闭包 : 将函数作为返回值

# 使用闭包调试
```
where := func() {
	_, file, line, _ := runtime.Caller(1)
	log.Printf("%s:%d", file, line)
}
where()
// some code
where()
// some more code
where
```

# 计算函数执行时间
* 使用 time 包中的 Now() 和 Sub 函数
```
start := time.Now()
longCalculation()
end := time.Now()
delta := end.Sub(start)
fmt.Printf("longCalculation took this amount of time: %s\n", delta)
```

# 通过内存缓存来提升性能
* 通过在内存中缓存和重复利用相同计算的结果，称之为内存缓存
```
package main

import (
	"fmt"
	"time"
)

const LIM = 41

var fibs [LIM]uint64

func main() {
	var result uint64 = 0
	start := time.Now()
	for i := 0; i < LIM; i++ {
		result = fibonacci(i)
		fmt.Printf("fibonacci(%d) is: %d\n", i, result)
	}
	end := time.Now()
	delta := end.Sub(start)
	fmt.Printf("longCalculation took this amount of time: %s\n", delta)
}
func fibonacci(n int) (res uint64) {
	// memoization: check if fibonacci(n) is already known in array:
	if fibs[n] != 0 {
		res = fibs[n]
		return
	}
	if n <= 1 {
		res = 1
	} else {
		res = fibonacci(n-1) + fibonacci(n-2)
	}
	fibs[n] = res
	return
}
```