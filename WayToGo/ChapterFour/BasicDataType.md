# 文件名、关键字与标识符

break	default	func	interface	select
case	defer	go	map	struct
chan	else	goto	package	switch
const	fallthrough	if	range	type
continue	for	import	return	var

append	bool	byte	cap	close	complex	complex64	complex128	uint16
copy	false	float32	float64	imag	int	int8	int16	uint32
int32	int64	iota	len	make	new	nil	panic	uint64
print	println	real	recover	string	true	uint	uint8	uintptr

# Go 程序的基本结构和要素

## 包的概念、导入与可见性
* 包是结构化代码的一种方式：每个程序都由包（通常简称为 pkg）的概念组成，可以使用自身的包或者从其它包中导入内容,每个 Go 文件都属于且仅属于一个包,package main表示一个可独立执行的程序，每个 Go 应用程序都包含一个名为 main 的包,所有的包名都应该使用小写字母
* 标准库
在 Go 的安装文件里包含了一些可以直接使用的包，即标准库, Windows (pkg\windows_386), Linux (pkg\linux_amd64)
* 属于同一个包的源文件必须全部被一起编译，一个包即是编译时的一个单元，因此根据惯例，每个目录都只包含一个包
* 如果对一个包进行更改或重新编译，所有引用了这个包的客户端程序都必须全部重新编译。
* 当你导入多个包时，最好按照字母顺序排列包名,导入包即等同于包含了这个包的所有的代码对象

## 可见性规则
* 当标识符（包括常量、变量、类型、函数名、结构字段等等）以一个大写字母开头
* 标识符如果以小写字母开头，则对包外是不可见的，但是他们在整个包的内部是可见并且可用的
* 使用包的别名,如：import fm "fmt"
* 导入了一个包却没有使用它，则会在构建程序时引发错误

# 包的分级声明和初始化
import 导入包之后定义或声明 0 个或多个常量（const）、变量（var）和类型（type），这些对象的作用域都是全局的（在本包范围内），所以可以被本包中所有的函数调用（如 gotemplate.go 源文件中的 c 和 v），然后声明一个或多个函数（func）

# 函数
* 这是定义一个函数最简单的格式：func functionName()
* main 函数是每一个可执行程序所必须包含的，一般来说都是在启动后第一个执行的函数（如果有 init() 函数则会先执行该函数）
* 符合规范的函数一般写成如下的形式：
func functionName(parameter_list) (return_value_list) {
   …
}
  * parameter_list 的形式为 (param1 type1, param2 type2, …)
  * return_value_list 的形式为 (ret1 type1, ret2 type2, …)
* 只有当某个函数需要被外部包调用的时候才使用大写字母开头，并遵循 Pascal 命名法；否则就遵循骆驼命名法，即第一个单词的首字母小写，其余单词的首字母大写

# 注释
* 注释不会被编译，但可以通过 godoc 来使用
* 单行注释是最常见的注释形式，你可以在任何地方使用以 // 开头的单行注释。多行注释也叫块注释，均已以 /* 开头，并以 */ 结尾

# 类型
* var 声明的变量的值会自动初始化为该类型的零值
* 基本类型，如：int、float、bool、string；
* 结构化的（复合的），如：struct、array、slice、map、channel；
* 只描述类型的行为的，如：interface
* 结构化的类型没有真正的值，它使用 nil 作为默认值

# Go 程序的一般结构
* 在完成包的 import 之后，开始对常量、变量和类型的定义或声明。
* 如果存在 init 函数的话，则对该函数进行定义（这是一个特殊的函数，每个含有该函数的包都会首先执行这个函数）。
* 如果当前包是 main 包，则定义 main 函数。
* 然后定义其余的函数，首先是类型的方法，接着是按照 main 函数中先后调用的顺序来定义相关函数，如果有很多函数，则可以按照字母顺序来进行排序。

## Go 程序的执行（程序启动）顺序如下：
* 按顺序导入所有被 main 包引用的其它包，然后在每个包中执行如下流程：
* 如果该包又导入了其它的包，则从第一步开始递归执行，但是每个包只会被导入一次。
* 然后以相反的顺序在每个包中初始化常量和变量，如果该包含有 init 函数的话，则调用该函数。
* 在完成这一切之后，main 也执行同样的过程，最后调用 main 函数开始执行程序。

# 类型转换
*  Go 语言不存在隐式类型转换，因此所有的转换都必须显式说明
valueOfTypeB = typeB(valueOfTypeA)
类型 B 的值 = 类型 B(类型 A 的值)
a := 5.0
b := int(a)

# 命名规范
* 干净、可读的代码和简洁性是 Go 追求的主要目标。通过 gofmt 来强制实现统一的代码风格。Go 语言中对象的命名也应该是简洁且有意义的。

# 常量
* 常量使用关键字 const 定义，用于存储不会改变的数据
* 常量中的数据类型只可以是布尔型、数字型（整数型、浮点型和复数）和字符串型
* const identifier [type] = value const b string = "abc"
* 常量的值必须是能够在编译时就能够确定的
* 因为在编译期间自定义函数均属于未知，因此无法用于常量的赋值，但内置函数可以使用

# 变量
* 声明变量的一般形式是使用 var 关键字：var identifier type
* var a, b *int
* 一个变量被声明之后，系统自动赋予它该类型的零值：int 为 0，float 为 0.0，bool 为 false，string 为空字符串，指针为 nil
* 变量的命名规则遵循骆驼命名法，即首个单词小写，每个新单词的首字母大写
* 全局变量希望能够被外部包所使用，则需要将首个单词的首字母也大写
* 函数体内声明的变量称之为局部变量，它们的作用域只在函数体内，参数和返回值变量也是局部变量

# 值类型和引用类型