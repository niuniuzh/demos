# 调试器
Go 在这方面的发展还不是很完善。目前可用的调试器是 gdb，最新版均以内置在集成开发环境 LiteIDE 和 GoClipse 中，但是该调试器的调试方式并不灵活且操作难度较大
* 在合适的位置使用打印语句输出相关变量的值（print/println 和 fmt.Print/fmt.Println/fmt.Printf）
* 在 fmt.Printf 中使用下面的说明符来打印有关变量的相关信息
- %+v 打印包括字段在内的实例的完整信息
- %#v 打印包括字段和限定类型名称在内的实例的完整信息
- %T 打印某个类型的完整说明
* 使用 panic 语句（第 13.2 节）来获取栈跟踪信息（直到 panic 时所有被调用函数的列表）。
* 使用关键字 defer 来跟踪代码执行过程（第 6.4 节）。

# 构建并运行 Go 程序
* go build 编译并安装自身包和依赖包
* go install 安装自身包和依赖包

# 格式化代码
* go fmt（gofmt）。这个工具可以将你的源代码格式化成符合官方统一标准的风格，属于语法风格层面上的小型重构
* gofmt 也可以通过在参数 -r 后面加入用双引号括起来的替换规则实现代码的简单重构，规则的格式：<原始内容> -> <替换内容>

# 生成代码文档
go doc 工具会从 Go 程序和包文件中提取顶级声明的首行注释以及每个对象的相关注释，并生成相关文档。
* go doc package 获取包的文档注释，例如：go doc fmt 会显示使用 godoc 生成的 fmt 包的文档注释。
* go doc package/subpackage 获取子包的文档注释，例如：go doc container/list。
* go doc package function 获取某个函数在某个包中的文档注释，例如：go doc fmt Printf 会显示有关 fmt.Printf() 的使用说明。

# 其它工具
* go install 是安装 Go 包的工具，类似 Ruby 中的 rubygems。主要用于安装非标准库的包文件，将源代码编译成对象文件。
* go fix 用于将你的 Go 代码从旧的发行版迁移到最新的发行版，它主要负责简单的、重复的、枯燥无味的修改工作，如果像 API 等复杂的函数修改，工具则会给出文件名和代码行数的提示以便让开发人员快速定位并升级代码。
* go test 是一个轻量级的单元测试框架（第 13 章）。

# 与其它语言进行交互
* [与 C 进行交互](http://golang.org/cmd/cgo)

与 C++ 进行交互
* 编写需要封装的库的 SWIG 接口。
* SWIG 会产生 C 的存根函数。
* 这些库可以使用 cgo 来调用。
* 相关的 Go 文件也可以被自动生成。