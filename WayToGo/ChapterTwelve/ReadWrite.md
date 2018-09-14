# 读取用户的输入
* 从键盘和标准输入 os.Stdin 读取输入，最简单的办法是使用 fmt 包提供的 Scan 和 Sscan 开头的函数
* Scanln 扫描来自标准输入的文本，将空格分隔的值依次存放到后续的参数内，直到碰到换行
* Scanf 的第一个参数用作格式字符串，用来决定如何读取
* Sscan 和以 Sscan 开头的函数则是从字符串读取
* bufio.NewReader() 构造函数的签名为：func NewReader(rd io.Reader) *Reader
* inputReader = bufio.NewReader(os.Stdin)  inputReader 是一个指向 bufio.Reader 的指针

# 文件读写
* 文件使用指向 os.File 类型的指针来表示的，也叫做文件句柄
* 通过使用 bufio 包提供的读取器（写入器也类似），如上面程序所示，我们可以很方便的操作相对高层的 string 对象，而避免了去操作比较底层的字节
* 一旦读取到文件末尾，变量 readerError 的值将变成非空（事实上，常量 io.EOF 的值是 true）

# 将整个文件的内容读到一个字符串里：
* 如果您想这么做，可以使用 io/ioutil 包里的 ioutil.ReadFile() 方法

# 带缓冲的读取
* 在很多情况下，文件的内容是不按行划分的，或者干脆就是一个二进制文件。在这种情况下，ReadString()就无法使用了，我们可以使用 bufio.Reader 的 Read()  buf := make([]byte, 1024)

# 按列读取文件中的数据
* 如果数据是按列排列并用空格分隔的，你可以使用 fmt 包提供的以 FScan 开头的一系列函数来读取他们

# compress包：读取压缩文件
* compress包提供了读取压缩文件的功能，支持的压缩文件格式为：bzip2、flate、gzip、lzw 和 zlib

# 写文件
* 除了文件句柄，我们还需要 bufio 的 Writer。我们以只写模式打开文件 output.dat，如果文件不存在则自动创建
* outputFile, outputError := os.OpenFile("output.dat", os.O_WRONLY|os.O_CREATE, 0666)
* os.O_RDONLY：只读
* os.O_WRONLY：只写
* os.O_CREATE：创建：如果指定文件不存在，就创建该文件。
* os.O_TRUNC：截断：如果指定文件已存在，就将该文件的长度截为0。
* 在写文件时，不管是 Unix 还是 Windows，都需要使用 0666

# 文件拷贝
* defer 的使用：当打开目标文件时发生了错误，那么 defer 仍然能够确保 src.Close() 执行。如果不这么做，文件会一直保持打开状态并占用资源
* return io.Copy(dst, src)

# 从命令行读取参数
* os 包中有一个 string 类型的切片变量 os.Args，用来处理一些基本的命令行参数，它在程序启动后读取命令行输入的参数

# flag 包
* flag 包有一个扩展功能用来解析命令行选项。但是通常被用来替换基本常量，

# 用 buffer 读取文件
* 参数被认为是文件名，如果文件存在的话就打印文件内容到屏幕。命令行执行 cat test 测试输出

# 用切片读写文件
# 用 defer 关闭文件
```
func data(name string) string {
	f, _ := os.OpenFile(name, os.O_RDONLY, 0)
	defer f.Close() // idiomatic Go code!
	contents, _ := ioutil.ReadAll(f)
	return string(contents)
}
```

# 使用接口的实际例子：fmt.Fprintf

* 下面是 fmt.Fprintf() 函数的实际签名
* func Fprintf(w io.Writer, format string, a ...interface{}) (n int, err error)

# JSON 数据格式
* 数据结构 --> 指定格式 = 序列化 或 编码（传输之前）
* 指定格式 --> 数据格式 = 反序列化 或 解码（传输之后）
* 序列化是在内存中把数据转换成指定格式（data -> string），反之亦然（string -> data structure）
* 编码也是一样的，只是输出一个数据流（实现了 io.Writer 接口）；解码是从一个数据流（实现了 io.Reader）输出到一个数据结构
* JSON 与 Go 类型对应如下
```
bool 对应 JSON 的 booleans
float64 对应 JSON 的 numbers
string 对应 JSON 的 strings
nil 对应 JSON 的 null
```
* 只有验证通过的数据结构才能被编码
```
JSON 对象只支持字符串类型的 key；要编码一个 Go map 类型，map 必须是 map[string]T
Channel，复杂类型和函数类型不能被编码
不支持循环数据结构；它将引起序列化进入一个无限循环
指针可以被编码，实际上是对指针指向的值进行编码
```

# 反序列化：
* UnMarshal() 的函数签名是 func Unmarshal(data []byte, v interface{}) error 把 JSON 解码为数据结构

# 解码任意的数据：
* json 包使用 map[string]interface{} 和 []interface{} 储存任意的 JSON 对象和数组；其可以被反序列化为任何的 JSON blob 存储到接口值中。

# 解码数据到结构
# 编码和解码流
* json 包提供 Decoder 和 Encoder 类型来支持常用 JSON 数据流读写
* func NewDecoder(r io.Reader) *Decoder
* func NewEncoder(w io.Writer) *Encoder

# XML 数据格式
* 包中定义了若干 XML 标签类型：StartElement，Chardata（这是从开始标签到结束标签之间的实际文本），EndElement，Comment，Directive 或 ProcInst
* NewParser 方法持有一个 io.Reader（这里具体类型是 strings.NewReader）并生成一个解析器类型的对象。还有一个 Token() 方法返回输入流里的下一个 XML token。在输入流的结尾处，会返回（nil，io.EOF）

# 用 Gob 传输数据
* Gob 是 Go 自己的以二进制形式序列化和反序列化程序数据的格式；可以在 encoding 包中找到