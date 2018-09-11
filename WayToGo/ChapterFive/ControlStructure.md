# 控制结构
* if-else 结构
* switch 结构
* select 结构，用于 channel 的选择（第 14.4 节）

# if-else 结构
```
if condition {
	// do something	
}
```
* if 和 else 后的两个代码块是相互独立的分支，只可能执行其中一个。
```
if condition {
	// do something	
} else {
	// do something	
}
```
* 如果你必须使用这种形式，则把尽可能先满足的条件放在前面
```
if condition1 {
	// do something	
} else if condition2 {
	// do something else	
} else {
	// catch-all or default
}
```
* 当 if 结构内有 break、continue、goto 或者 return 语句时，Go 代码的常见写法是省略 else 部分
* if 可以包含一个初始化语句（如：给一个变量赋值）
* if initialization; condition {
	// do something
}
```
if val := 10; val > max {
	// do something
}
```

# 测试多返回值函数的错误
* Go 语言的函数经常使用两个返回值来表示执行是否成功,这样的形式又称之为 comma,ok 模式（pattern）。
* 这是测试 err 变量是否包含一个真正的错误（if err != nil）的习惯用法
```
value, err := pack1.Function1(param1)
if err != nil {
	fmt.Printf("An error occured in pack1.Function1 with parameter %v", param1)
  //os.Exit(1)
	return err
}
```
# switch 结构
```
switch var1 {
	case val1:
		...
	case val2:
		...
	default:
		...
}
```
* 每一个 case 分支都是唯一的，从上至下逐一测试，直到匹配为止
* 一旦成功地匹配到某个分支，在执行完相应代码后就会退出整个 switch 代码块
* 在执行完每个分支的代码后，还希望继续执行后续分支的代码，可以使用 fallthrough 关键字来达到目的

# for 结构
# 基于计数器的迭代
* for 初始化语句; 条件语句; 修饰语句 {}

# 基于条件判断的迭代
* 基本形式为：for 条件语句 {}

# 无限循环
* 一般情况下都会直接写 for { }
* 想要直接退出循环体，可以使用 break 语句（第 5.5 节）或 return 语句直接返回（第 6.1 节）
* 无限循环的经典应用是服务器，用于不断等待和接受新的请求

# for-range 结构
* Go 特有的一种的迭代结构,可以迭代任何一个集合（包括数组和 map，详见第 7 和 8 章）

# Break 与 continue
* 一个 break 的作用范围为该语句出现后的最内部的结构，它可以被用于任何形式的 for 循环（计数器、条件判断等）
* 关键字 continue 忽略剩余的循环体而直接进入下一次循环的过程，但不是无条件执行下一次循环，执行之前依旧需要满足循环的判断条件
* 关键字 continue 只能被用于 for 循环中

# 标签与 goto
* for、switch 或 select 语句都可以配合标签（label）形式的标识符使用，即某一行第一个以冒号（:）结尾的单词
* 标签的名称是大小写敏感的，为了提升可读性，一般建议使用全部大写字母
* goto continue :LABEL