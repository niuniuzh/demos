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
* int、float、bool 和 string 这些基本类型都属于值类型，使用这些类型的变量直接指向存在内存中的值
* 数组（第 7 章）和结构（第 10 章）这些复合类型也是值类型
* 等号 = 将一个变量的值赋值给另一个变量时，如：j = i，实际上是在内存中将 i 的值进行了拷贝
* 内存地址被称之为指针（你可以从上图中很清晰地看到，第 4.9 节将会详细说明），这个指针实际上也被存在另外的某一个字中
* 指针（第 4.9 节）属于引用类型，其它的引用类型还包括 slices（第 7 章），maps（第 8 章）和 channel（第 13 章）。被引用的变量会存储在堆中，以便进行垃圾回收，且比栈拥有更大的内存空间内存地址被称之为指针（你可以从上图中很清晰地看到，第 4.9 节将会详细说明），这个指针实际上也被存在另外的某一个字中

# 打印
* func Printf(format string, list of variables to be printed)

# 简短形式，使用 := 赋值操作符
* 简写为 a := 50 或 b := false。a 和 b 的类型（int 和 bool）将由编译器自动推断。
* 在相同的代码块中，我们不可以再次对于相同名称的变量使用初始化声明，例如：a := 20 就是不被允许的

# init 函数
* 这是一类非常特殊的函数，它不能够被人为调用，而是在每个包完成初始化后自动执行，并且执行优先级比 main 函数高
* 每个源文件都只能包含一个 init 函数,初始化总是以单线程执行，并且按照包的依赖关系顺序执行

# 基本类型和运算符
* 一元运算符只可以用于一个值的操作（作为后缀），而二元运算符则可以和两个值或者操作数结合（作为中缀）

#  布尔类型 bool
* 布尔型的值只可以是常量 true 或者 false
* 两个类型相同的值可以使用相等 == 或者不等 != 运算符来进行比较
* Go 对于值之间的比较有非常严格的限制，只有两个类型相同的值才可以进行比较
* 在格式化输出时，你可以使用 %t 来表示你要输出的值为布尔型
* 布尔值（以及任何结果为布尔值的表达式）最常用在条件结构的条件语句中，例如：if、for 和 switch 结构

# 数字类型
##　整型 int 和浮点型 float
* Go 语言支持整型和浮点型数字，并且原生支持复数
* int 和 uint 在 32 位操作系统上，它们均使用 32 位（4 个字节），在 64 位操作系统上，它们均使用 64 位（8 个字节）
* uintptr 的长度被设定为足够存放一个指针即可；
* 整型的零值为 0，浮点型的零值为 0.0,float32 精确到小数点后 7 位，float64 精确到小数点后 15 位

# 格式化说明符
* 在格式化字符串里，%d 用于格式化整数（%x 和 %X 用于格式化 16 进制表示的数字），%g 用于格式化浮点型（%f 输出浮点数，%e 输出科学计数表示法），%0d 用于规定输出定长的整数，其中开头的数字 0 是必须的
* %n.mg 用于表示数字 n 并精确到小数点后 m 位，除了使用 g 之外，还可以使用 e 或者 f，例如：使用格式化字符串 %5.2e 来输出 3.4 的结果为 3.40e+00

# 数字值转换
* 当进行类似 a32bitInt = int32(a32Float) 的转换时，小数点后的数字将被丢弃
	if 0 <= n && n <= math.MaxUint8 { // conversion is safe
		return uint8(n), nil
	}

# 复数
* Go 拥有以下复数类型
complex64 (32 位实数和虚数)
complex128 (64 位实数和虚数)
* 复数使用 re+imI 来表示，其中 re 代表实数部分，im 代表虚数部分，I 代表根号负 1
var c1 complex64 = 5 + 10i
fmt.Printf("The value is: %v", c1)
c = complex(re, im)
* 函数 real(c) 和 imag(c) 可以分别获得相应的实数和虚数部分

# 位运算
* %b 是用于表示位的格式化标识符
* 按位与 &
* 按位或 |
* 按位异或 ^
* 位清除 &^
* 按位补足 ^
* 位左移 <<
* 位右移 >>

# 逻辑运算符
* Go 中拥有以下逻辑运算符：==、!=（第 4.5.1 节）、<、<=、>、>=

# 算术运算符
* 常见可用于整数和浮点数的二元运算符有 +、-、* 和 /
* 取余运算符只能作用于整数：9 % 4 -> 1
* 带有 ++ 和 -- 的只能作为语句，而非表达式
* 在运算时 溢出 不会产生错误，Go 会简单地将超出位数抛弃

# 随机数
* rand 包实现了伪随机数的生成
* 函数 rand.Float32 和 rand.Float64 返回介于 [0.0, 1.0) 之间的伪随机数，其中包括 0.0 但不包括 1.0
* 函数 rand.Intn 返回介于 [0, n) 之间的伪随机数
* Seed(value) 函数来提供伪随机数的生成种子，一般情况下都会使用当前时间的纳秒级数字

# 运算符与优先级
优先级 	运算符
 7 		^ !
 6 		* / % << >> & &^
 5 		+ - | ^
 4 		== != < <= >= >
 3 		<-
 2 		&&
 1 		||

# 类型别名
* 在 type TZ int 中，TZ 就是 int 类型的新名称

# 字符类型
* byte 类型是 uint8 的别名，对于只占用 1 个字节的传统 ASCII 编码的字符来说，完全没有问题。
* 例如：var ch byte = 'A',字符使用单引号括起来  var ch byte = 65 或 var ch byte = '\x41'
* （\x 总是紧跟着长度为 2 的 16 进制数）
* 另外一种可能的写法是 \ 后面紧跟着长度为 3 的八进制数，例如：\377
* 前缀 \u 则总是紧跟着长度为 4 的 16 进制数，前缀 \U 紧跟着长度为 8 的 16 进制数
* 格式化说明符 %c 用于表示字符；当和字符配合使用时，%v 或 %d 会输出用于表示该字符的整数；%U 输出格式为 U+hhhh 的字符串
* 判断是否为字母：unicode.IsLetter(ch)
* 判断是否为数字：unicode.IsDigit(ch)
* 判断是否为空白符号：unicode.IsSpace(ch)

# 字符串
* 字符串是一种值类型，且值不可变,字符串是字节的定长数组
* 解释字符串:
  * \n：换行符
  * \r：回车符
  * \t：tab 键
  * \u 或 \U：Unicode 字符
  * \\：反斜杠自身
* 非解释字符串：
  * 该类字符串使用反引号括起来，支持换行
  * `This is a raw string \n` 中的 `\n\` 会被原样输出。
* C/C++不一样，Go 中的字符串是根据长度限定，而非特殊字符\0
* 函数 len() 来获取字符串所占的字节长度，例如：len(str)
* 字符串 str 的第 1 个字节：str[0]
* 第 i 个字节：str[i - 1]
* 最后 1 个字节：str[len(str)-1]

# 字符串拼接符 +
* 两个字符串 s1 和 s2 可以通过 s := s1 + s2 拼接在一起
* 拼接的简写形式 += 也可以用于字符串
* 循环中使用加号 + 拼接字符串并不是最高效的做法，更好的办法是使用函数 strings.Join()
* 使用字节缓冲（bytes.Buffer）拼接更加给力

# strings 和 strconv 包
# 前缀和后缀
* HasPrefix 判断字符串 s 是否以 prefix 开头
  * strings.HasPrefix(s, prefix string) bool
* HasSuffix 判断字符串 s 是否以 suffix 结尾
  * strings.HasSuffix(s, suffix string) bool

# 字符串包含关系
* Contains 判断字符串 s 是否包含 substr：
  * strings.Contains(s, substr string) bool

# 判断子字符串或字符在父字符串中出现的位置
* Index 返回字符串 str 在字符串 s 中的索引（str 的第一个字符的索引），-1 表示字符串 s 不包含字符串 str：
  * strings.Index(s, str string) int
  * strings.LastIndex(s, str string) int
* 如果 ch 是非 ASCII 编码的字符，建议使用以下函数来对字符进行定位：
  * strings.IndexRune(s string, r rune) int

# 字符串替换
* Replace 用于将字符串 str 中的前 n 个字符串 old 替换为字符串 new，并返回一个新的字符串，如果 n = -1 则替换所有字符串 old 为字符串 new
  * strings.Replace(str, old, new, n) string

# 统计字符串出现次数
* Count 用于计算字符串 str 在字符串 s 中出现的非重叠次数
  * strings.Count(s, str string) int

# 重复字符串
* Repeat 用于重复 count 次字符串 s 并返回一个新的字符串：
  * strings.Repeat(s, count int) string

# 修改字符串大小写
* ToLower 将字符串中的 Unicode 字符全部转换为相应的小写字符:strings.ToLower(s) string
* ToUpper 将字符串中的 Unicode 字符全部转换为相应的大写字符：strings.ToUpper(s) string

# 修剪字符串
* strings.TrimSpace(s) 来剔除字符串开头和结尾的空白符号
* strings.Trim(s, "cut") 来将开头和结尾的 cut 去除掉
* 如果你只想剔除开头或者结尾的字符串，则可以使用 TrimLeft 或者 TrimRight 来实现

# 分割字符串
* strings.Fields(s) 将会利用 1 个或多个空白符号来作为动态长度的分隔符将字符串分割成若干小块
* strings.Split(s, sep) 用于自定义分割符号来对指定字符串进行分割

# 拼接 slice 到字符串
* Join 用于将元素类型为 string 的 slice 使用分割符号来拼接组成一个字符串：
  * strings.Join(sl []string, sep string) string

# 从字符串中读取内容
* strings.NewReader(str) 用于生成一个 Reader 并读取字符串中的内容，然后返回指向该 Reader 的指针
  * Read() 从 []byte 中读取内容
  * ReadByte() 和 ReadRune() 从字符串中读取下一个 byte 或者 rune

# 字符串与其它类型的转换
* 字符串相关的类型转换都是通过 strconv 包实现的,任何类型 T 转换为字符串总是成功的
* 针对从数字类型转换到字符串，Go 提供了以下函数：
  * strconv.Itoa(i int) string 返回数字 i 所表示的字符串类型的十进制数
  * strconv.FormatFloat(f float64, fmt byte, prec int, bitSize int) string 将 64 位浮点型的数字转换为字符串
  * fmt 表示格式（其值可以是 'b'、'e'、'f' 或 'g'），prec 表示精度，bitSize 则使用 32 表示 float32，用 64 表示 float64
* 针对从字符串类型转换为数字类型，Go 提供了以下函数:
  * strconv.Atoi(s string) (i int, err error) 将字符串转换为 int 型
  * strconv.ParseFloat(s string, bitSize int) (f float64, err error) 将字符串转换为 float64 型
  * 这些函数会返回 2 个值，第 1 个是转换后的结果（如果转换成功），第 2 个是可能出现的错误
  * val, err = strconv.Atoi(s)

# 时间和日期
* time 包为我们提供了一个数据类型 time.Time（作为值使用）以及显示和测量时间和日期的功能函数
* 当前时间可以使用 time.Now() 获取，或者使用 t.Day()、t.Minute() 等等来获取时间的一部分
* Duration 类型表示两个连续时刻所相差的纳秒数，类型为 int64。Location 类型映射某个时区的时间，UTC 表示通用协调世界时间

# 指针
* 程序在内存中存储它的值，每个内存块（或字）有一个地址，通常用十六进制数表示
* Go 语言的取地址符是 &，放到一个变量前使用就会返回相应变量的内存地址
* 你可以在指针类型前面加上 * 号（前缀）来获取指针所指向的内容，这里的 * 号是一个类型更改器
* 你不能得到一个文字或常量的地址,
* const i = 5
* ptr := &i //error: cannot take the address of i
* ptr2 := &10 //error: cannot take the address of 10
* 移动指针指向字符串的字节数或数组的某个位置）是不被允许
