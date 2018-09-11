# 包
# 标准库概述
* fmt、os 等这样具有常用功能的内置包在 Go 语言中有 150 个以上，它们被称为标准库，大部分(一些底层的除外)内置于 Go 本身
* https://gowalker.org/search?q=gorepos

# regexp 包
* 如果是简单模式，使用 Match 方法便可 ok, _ := regexp.Match(pat, []byte(searchIn))
* 变量 ok 将返回 true 或者 false,我们也可以使用 MatchString  ok, _ := regexp.MatchString(pat, searchIn)
* 更多方法中，必须先将正则通过 Compile 方法返回一个 Regexp 对象
```
	searchIn := "John: 2578.34 William: 4567.23 Steve: 5632.18"
	pat := "[0-9]+.[0-9]+" //正则
    re, _ := regexp.Compile(pat)
	//将匹配到的部分替换为"##.#"
	str := re.ReplaceAllString(searchIn, "##.#")
	fmt.Println(str)
	//参数为函数时
	str2 := re.ReplaceAllStringFunc(searchIn, f)
```

# 锁和 sync 包
* 经典的做法是一次只能让一个线程对共享变量进行操作。当变量被一个线程改变时(临界区)，我们为它上锁，直到这个线程执行完成并解锁后，其他线程才能访问它
* Go 语言中这种锁的机制是通过 sync 包中 Mutex 来实现的
* sync.Mutex 是一个互斥锁，它的作用是守护在临界区入口来确保同一时间只能有一个线程进入临界区

# 精密计算和 big 包
* 对于整数的高精度计算 Go 语言中提供了 big 包
* 有用来表示大整数的 big.Int 和表示大有理数的 big.Rat 类型
* 大的整型数字是通过 big.NewInt(n) 来构造的，其中 n 为 int64 类型整数。而大有理数是用过 big.NewRat(N,D) 方法构造。N（分子）和 D（分母）都是 int64 型整数

# 自定义包和可见性
* 要使用短小的不含有 _(下划线)的小写单词来为文件命名
* import 的一般格式如下:import "包的路径或 URL 地址"   import "github.com/org1/pack1”
* 路径是指当前目录的相对路径。
* Import with . :当使用.来做为包的别名时，你可以不通过包名来使用其中的项目  test := ReturnStr()
* Import with _ :pack1包只导入其副作用，也就是说，只执行它的init函数并初始化其中的全局变量

# 导入外部安装包:
* 首先你必须使用 go install（参见第 9.7 节）在你的本地机器上安装它们
* 通过以下方式，一次性安装，并导入到你的代码中  import goex "codesite.ext/author/goExample/goex"

# 包的初始化:
