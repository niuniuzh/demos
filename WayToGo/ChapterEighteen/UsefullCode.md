# 出于性能考虑的实用代码片段
# 字符串
* 如何修改字符串中的一个字符：
```
str:="hello"
c:=[]byte(str)
c[0]='c'
s2:= string(c) // s2 == "cello"
```
* 如何获取字符串的子串：
```
substr := str[n:m]
```
* 如何使用for或者for-range遍历一个字符串：
```
for i:=0; i < len(str); i++ {
… = str[i]
}
for ix, ch := range str {
…
}
```
* 如何获取一个字符串的字节数：len(str)
* 如何获取一个字符串的字符数：最快速：utf8.RuneCountInString(str)  len([]int(str))
* 如何连接字符串：最快速： with a bytes.Buffer（参考章节7.2）Strings.Join()（参考章节4.7）使用+=：
* 如何解析命令行参数：使用os或者flag包

# 数组和切片
* 创建：arr1 := new([len]type)  slice1 := make([]type, len)
* 初始化：arr1 := [...]type{i1, i2, i3, i4, i5}  arrKeyValue := [len]type{i1: val1, i2: val2}  var slice1 []type = arr1[start:end]
* 如何截断数组或者切片的最后一个元素：line = line[:len(line)-1]

# 映射
* 创建： map1 := make(map[keytype]valuetype)
* 初始化： map1 := map[string]int{"one": 1, "two": 2}
```
for key, value := range map1 {
…
}
```
* 如何在一个映射中检测键key1是否存在：val1, isPresent = map1[key1]
* 如何在映射中删除一个键：delete(map1, key1)

# 结构体
* 创建：
```
type struct1 struct {
    field1 type1
    field2 type2
    …
}
ms := new(struct1)
```
* 初始化：ms := &struct1{10, 15.5, "Chris"}
* 当结构体的命名以大写字母开头时，该结构体在包外可见。 通常情况下，为每个结构体定义一个构建函数，并推荐使用构建函数初始化结构体

# 接口
* 如何检测一个值v是否实现了接口Stringer
```
if v, ok := v.(Stringer); ok {
    fmt.Printf("implements String(): %s\n", v.String())
}
```
* 如何使用接口实现一个类型分类函数
```
func classifier(items ...interface{}) {
    for i, x := range items {
        switch x.(type) {
        case bool:
            fmt.Printf("param #%d is a bool\n", i)
        case float64:
            fmt.Printf("param #%d is a float64\n", i)
        case int, int64:
            fmt.Printf("param #%d is an int\n", i)
        case nil:
            fmt.Printf("param #%d is nil\n", i)
        case string:
            fmt.Printf("param #%d is a string\n", i)
        default:
            fmt.Printf("param #%d’s type is unknown\n", i)
        }
    }
}
```

# 函数
```
func protect(g func()) {
    defer func() {
        log.Println("done")
        // Println executes normally even if there is a panic
        if x := recover(); x != nil {
            log.Printf("run time panic: %v", x)
        }
    }()
    log.Println("start")
    g()
}
```

# 文件
* 如何打开一个文件并读取：
```
file, err := os.Open("input.dat")
  if err != nil {
    fmt.Printf("An error occurred on opening the inputfile\n" +
      "Does the file exist?\n" +
      "Have you got acces to it?\n")
    return
  }
  defer file.Close()
  iReader := bufio.NewReader(file)
  for {
    str, err := iReader.ReadString('\n')
    if err != nil {
      return // error or EOF
    }
    fmt.Printf("The input was: %s", str)
  }
```
* 如何通过切片读写文件
```
func cat(f *file.File) {
  const NBUF = 512
  var buf [NBUF]byte
  for {
    switch nr, er := f.Read(buf[:]); true {
    case nr < 0:
      fmt.Fprintf(os.Stderr, "cat: error reading from %s: %s\n",
        f.String(), er.String())
      os.Exit(1)
    case nr == 0: // EOF
      return
    case nr > 0:
      if nw, ew := file.Stdout.Write(buf[0:nr]); nw != nr {
        fmt.Fprintf(os.Stderr, "cat: error writing from %s: %s\n",
          f.String(), ew.String())
      }
    }
  }
}
```

# 协程（goroutine）与通道（channel）
* 1 出于性能考虑建议使用带缓存的通道：
* 2 限制一个通道的数据数量并将它们封装成一个数组：
* 如何使用for或者for-range遍历一个通道
```
for v := range ch {
    // do something with v
}
```
* 如何检测一个通道ch是否关闭
```
for {
    if input, open := <-ch; !open {
        break
    }
    fmt.Printf("%s", input)
}
```
* 如何通过一个通道让主程序等待直到协程完成
* 通道的工厂模板：以下函数是一个通道工厂，启动一个匿名函数作为协程以生产通道：
```
func pump() chan int {
    ch := make(chan int)
    go func() {
        for i := 0; ; i++ {
            ch <- i
        }
    }()
    return ch
}
```
* 通道迭代器模板：
* 如何限制并发处理请求的数量：参考章节14.11
* 如何在多核CPU上实现并行计算：参考章节14.13
* 如何终止一个协程：runtime.Goexit()
* 简单的超时模板：
```
timeout := make(chan bool, 1)
go func() {
    time.Sleep(1e9) // one second  
    timeout <- true
}()
select {
    case <-ch:
    // a read from ch has occurred
    case <-timeout:
    // the read from ch has timed out
}
```
* 如何使用输入通道和输出通道代替锁：
```
func Worker(in, out chan *Task) {
    for {
        t := <-in
        process(t)
        out <- t
    }
}
```
* 如何在同步调用运行时间过长时将之丢弃：参考章节14.5 第二个变体
* 如何在通道中使用计时器和定时器：参考章节14.5
* 典型的服务器后端模型：参考章节14.4

# 网络和网页应用
* 制作、解析并使模板生效：var strTempl = template.Must(template.New("TName").Parse(strTemplateHTML))
* 在网页应用中使用HTML过滤器过滤HTML特殊字符：{{html .}} 或者通过一个字段 FieldName {{ .FieldName |html }}

# 其他
如何在程序出错时终止程序：
```
if err != nil {
   fmt.Printf("Program stopping with error %v", err)
   os.Exit(1)
}
if err != nil { 
	panic("ERROR occurred: " + err.Error())
}
```

# 出于性能考虑的最佳实践和建议
* 尽可能的使用:=去初始化声明一个变量（在函数内部）；
* 尽可能的使用字符代替字符串；
* 尽可能的使用切片代替数组；
* 尽可能的使用数组和切片代替映射（详见参考文献15）；
* 如果只想获取切片中某项值，不需要值的索引，尽可能的使用for range去遍历切片，这比必须查询切片中的每个元素要快一些；
* 当数组元素是稀疏的（例如有很多0值或者空值nil），使用映射会降低内存消耗；
* 初始化映射时指定其容量；
* 当定义一个方法时，使用指针类型作为方法的接受者；
* 在代码中使用常量或者标志提取常量的值；
* 尽可能在需要分配大量内存时使用缓存；
* 使用缓存模板（参考章节15.7）。