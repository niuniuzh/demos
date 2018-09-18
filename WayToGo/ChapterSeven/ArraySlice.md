# 声明和初始化
* 数组是具有相同 唯一类型 的一组已编号且长度固定的数据项序列
* 数组长度必须是一个常量表达式，并且必须是一个非负整数
* 声明的格式是：var identifier [len]type

# 数组常量
* 数组值已经提前知道了，那么可以通过 数组常量 的方法来初始化数组
* var arrAge = [5]int{18, 20, 15, 22, 16}  [5]int 可以从左边起开始忽略
* var arrLazy = [...]int{5, 6, 7, 8, 22}  ... 可同样可以忽略，从技术上说它们其实变化成了切片
* key: value syntax  var arrKeyValue = [5]string{3: "Chris", 4: "Ron"}  只有索引 3 和 4 被赋予实际的值，其他元素都被设置为空的字符串

# 多维数组
* 数组通常是一维的，但是可以用来组装成多维数组，例如：[3][5]int，[2][2][2]float64
 
# 将数组传递给函数
* 传递数组的指针
* 使用数组的切片

# 切片概念
* 切片（slice）是对数组一个连续片段的引用
* 优点 因为切片是引用，所以它们不需要使用额外的内存并且比使用数组更有效率，所以在 Go 代码中 切片比数组更常用
* 声明切片的格式是： var identifier []type（不需要说明长度）
* 一个切片在未初始化之前默认为 nil，长度为 0。切片的初始化格式是：var slice1 []type = arr1[start:end]
* slice1 是由数组 arr1 从 start 索引到 end-1 索引之间的元素构成的子集（切分数组，start:end 被称为 slice 表达式）

# 将切片传递给函数
``` 
func sum(a []int) int {
  ...
}
func main() {
	var arr = [5]int{0, 1, 2, 3, 4}
	sum(arr[:])
}
```

# 用 make() 创建一个切片
* 当相关数组还没有定义时，我们可以使用 make() 函数来创建一个切片 同时创建好相关数组：var slice1 []type = make([]type, len)
* 可以简写为 slice1 := make([]type, len)，这里 len 是数组的长度并且也是 slice 的初始长度

# new() 和 make() 的区别
* new(T) 为每个新的类型T分配一片内存，初始化为 0 并且返回类型为*T的内存地址：这种方法 返回一个指向类型为 T，值为 0 的地址的指针，它适用于值类型如数组和结构体（参见第 10 章）；它相当于 &T{}。
* make(T) 返回一个类型为 T 的初始值，它只适用于3种内建的引用类型：切片、map 和 channel（参见第 8 章，第 13 章）

# 多维 切片
* 通过 buffer 串联字符串
* 通过 buffer.WriteString(s) 方法将字符串 s 追加到后面，最后再通过 buffer.String() 方法转换为 string

# For-range 结构
```
for ix, value := range slice1 {
	...
}
```
* 第一个返回值 ix 是数组或者切片的索引，第二个是在该索引位置的值；他们都是仅在 for 循环内部可见的局部变量
* _ 可以用于忽略索引  如果你只需要索引，你可以忽略第二个变量

# 切片重组（reslice）
* 改变切片长度的过程称之为切片重组 reslicing，做法如下：slice1 = slice1[0:end]，其中 end 是新的末尾索引（即长度）

# 切片的复制与追加
* 拷贝切片的 copy 函数和向切片追加新元素的 append 函数
* func append(s[]T, x ...T) []T 其中 append 方法将 0 个或多个具有相同类型 s 的元素追加到切片后面并且返回新的切片

# 字符串、数组和切片的应用
* 可以直接通过 c := []byte(s) 来获取一个字节的切片 c
* 可以通过 copy 函数来达到相同的目的：copy(dst []byte, src string)

# 获取字符串的某一部分
* substr := str[start:end] 可以从字符串 str 获取到从索引 start 开始到 end-1 位置的子字符串

# 字符串和切片的内存结构
* 内存中，一个字符串实际上是一个双字结构，即一个指向实际数据的指针和记录字符串长度的整数

# 修改字符串中的某个字符
* Go 语言中的字符串是不可变的, 您必须先将字符串转换成字节数组，然后再通过修改数组中的元素值来达到修改字符串的目的，最后将字节数组转换回字符串格式
```
s := "hello"
c := []byte(s)
c[0] = 'c'
s2 := string(c) // s2 == "cello
```

# 字节数组对比函数
* Compare 函数会返回两个字节数组字典顺序的整数对比结果，即 0 if a == b, -1 if a < b, 1 if a > b

# 搜索及排序切片和数组
# append 函数常见操作
# 切片和垃圾回收
* 切片的底层指向一个数组，该数组的实际容量可能要大于切片所定义的容量。只有在没有任何切片指向的时候，底层的数组内存才会被释放，这种特性有时会导致程序占用多余的内存