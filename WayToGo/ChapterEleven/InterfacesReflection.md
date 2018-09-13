# 接口是什么
* 接口定义了一组方法（方法集），但是这些方法不包含（实现）代码：它们没有被实现（它们是抽象的）。接口里也不能包含变量
```
type Namer interface {
    Method1(param_list) return_type
    Method2(param_list) return_type
    ...
}
```
* Namer 是一个 接口类型
* （按照约定，只包含一个方法的）接口的名字由方法名加 [e]r 后缀组成，例如 Printer、Reader、Writer、Logger、Converter
* 还有一些不常用的方式（当后缀 er 不合适时），比如 Recoverable，此时接口名以 able 结尾，或者以 I 开头（像 .NET 或 Java 中那样）
* Go 语言中的接口都很简短，通常它们会包含 0 个、最多 3 个方法
* 类型不需要显式声明它实现了某个接口：接口被隐式地实现。多个类型可以实现同一个接口
* 实现某个接口的类型（除了实现接口方法外）可以有其他的方法
* 一个类型可以实现多个接口。
* 接口类型可以包含一个实例的引用， 该实例的类型实现了此接口（接口是动态类型）

# 接口嵌套接口
* 一个接口可以包含一个或多个其他的接口，这相当于直接将这些内嵌接口的方法列举在外层接口中一样

# 类型断言：如何检测和转换接口变量的类型
* 一个接口类型的变量 varI 中可以包含任何类型的值,必须有一种方式来检测它的 动态 类型，即运行时在变量中存储的值的实际类型
* 通常我们可以使用 类型断言 来测试在某个时刻 varI 是否包含类型 T 的值：v := varI.(T)     // unchecked type assertion
* varI 必须是一个接口变量，否则编译器会报错
* 类型断言可能是无效的，虽然编译器会尽力检查转换是否有效，但是它不可能预见所有的可能性
```
if v, ok := varI.(T); ok {  // checked type assertion
    Process(v)
    return
}
// varI is not of type T
```
* 应该总是使用上面的方式来进行类型断言

# 类型判断：type-switch
* 接口变量的类型也可以使用一种特殊形式的 switch 来检测：type-switch
```
switch t := areaIntf.(type) {
case *Square:
	fmt.Printf("Type Square %T with value %v\n", t, t)
case *Circle:
	fmt.Printf("Type Circle %T with value %v\n", t, t)
case nil:
	fmt.Printf("nil value: nothing to check?\n")
default:
	fmt.Printf("Unexpected type %T\n", t)
}
```

# 测试一个值是否实现了某个接口
* 接口是一种契约，实现类型必须满足它，它描述了类型的行为，规定类型可以做什么
* 接口彻底将类型能做什么，以及如何做分离开来，使得相同接口的变量在不同的时刻表现出不同的行为，这就是多态的本质
```
type Stringer interface {
    String() string
}

if sv, ok := v.(Stringer); ok {
    fmt.Printf("v implements String(): %s\n", sv.String()) // note: sv, not v
}
```

# 使用方法集与接口
* 在接口上调用方法时，必须有和方法定义时相同的接收者类型或者是可以从具体类型 P 直接可以辨识的
* 指针方法可以通过指针调用
* 值方法可以通过值调用
* 接收者是值的方法可以通过指针调用，因为指针会首先被解引用
* 接收者是指针的方法不可以通过值调用，因为存储在接口中的值没有地址
* Go 语言规范定义了接口方法集的调用规则
* 类型 *T 的可调用方法集包含接受者为 *T 或 T 的所有方法集
* 类型 T 的可调用方法集包含接受者为 T 的所有方法
* 类型 T 的可调用方法集不包含接受者为 *T 的方法

# 第一个例子：使用 Sorter 接口排序
* 一组数字或字符串排序，只需要实现三个方法：反映元素个数的 Len()方法、比较第 i 和 j 个元素的 Less(i, j) 方法以及交换第 i 和 j 个元素的 Swap(i, j) 方法
* Sort 函数接收一个接口类型的参数：Sorter ，它声明了这些方法：
```
type Sorter interface {
    Len() int
    Less(i, j int) bool
    Swap(i, j int)
}
```

# 第二个例子：读和写
* 读和写是软件中很普遍的行为，提起它们会立即想到读写文件、缓存（比如字节或字符串切片）、标准输入输出、标准错误以及网络连接、管道
* 只要类型实现了读写接口，提供 Read() 和 Write 方法，就可以从它读取数据，或向它写入数据

# 空接口
* 空接口或者最小接口 不包含任何方法，它对实现不做任何要求  type Any interface {}
* 任何其他类型都实现了空接口，any 或 Any 是空接口一个很好的别名或缩写

# 构建通用类型或包含不同类型变量的数组
* 我们给空接口定一个别名类型 Element：type Element interface{}
* 然后定义一个容器类型的结构体 Vector，它包含一个 Element 类型元素的切片

# 复制数据切片至空接口切片
* 必须使用 for-range 语句来一个一个显式地复制
```
var dataSlice []myType = FuncReturnSlice()
var interfaceSlice []interface{} = make([]interface{}, len(dataSlice))
for i, d := range dataSlice {
    interfaceSlice[i] = d
}
```

# 通用类型的节点数据结构
* 可以使用空接口作为数据字段的类型，这样我们就能写出通用的代码

# 接口到接口
* 一个接口的值可以赋值给另一个接口变量，只要底层类型实现了必要的方法

# 方法和类型的反射
* 反射可以在运行时检查类型和变量，例如它的大小、方法和 动态 的调用这些方法
* 变量的最基本信息就是类型和值：反射包的 Type 用来表示一个 Go 类型，反射包的 Value 为 Go 值提供了反射接口
* 两个简单的函数，reflect.TypeOf 和 reflect.ValueOf，返回被检查对象的类型和值
* 方法 v.Kind() 返回 reflect.Int。
* 变量 v 的 Interface() 方法可以得到还原（接口）值，所以可以这样打印 v 的值：fmt.Println(v.Interface())

# 通过反射修改(设置)值
* 是否可设置是 Value 的一个属性，并且不是所有的反射值都有这个属性：可以使用 CanSet() 方法测试是否可设置
* v := reflect.ValueOf(x) 函数通过传递一个 x 拷贝创建了 v，那么 v 的改变并不能更改原始的 x。要想 v 的更改能作用到 x，那就必须传递 x 的地址 v = reflect.ValueOf(&x)
* 要想让其可设置我们需要使用 Elem() 函数，这间接的使用指针：v = v.Elem()
* v.setFloat(3.1241)

# 反射结构
* NumField() 方法返回结构内的字段数量；通过一个 for 循环用索引取得每个字段的值 Field(i)