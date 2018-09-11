# Map
* map 是一种特殊的数据结构：一种元素对（pair）的无序集合，pair 的一个元素是 key，对应的另一个元素是 value，所以这个结构也称为关联数组或字典

# 声明、初始化和 make
* map 是引用类型，可以使用如下声明：var map1 map[keytype]valuetype  var map1 map[string]int
* [keytype] 和 valuetype 之间允许有空格，但是 gofmt 移除了空格
* len(map1) 方法可以获得 map 中的 pair 数目
* v := map1[key1] 可以将 key1 对应的值赋值给 v
* 不要使用 new，永远用 make 来构造 map
* 如果你错误的使用 new() 分配了一个引用对象，你会获得一个空引用的指针，相当于声明了一个未初始化的变量并且取了它的地址

# map 容量
* map 可以根据新增的 key-value 对动态的伸缩，因此它不存在固定长度或者最大限制
* 你也可以选择标明 map 的初始容量 capacity，就像这样：make(map[keytype]valuetype, cap)。例如：map2 := make(map[string]float32, 100)

# 用切片作为 map 的值
```
mp1 := make(map[int][]int)
mp2 := make(map[int]*[]int)
```