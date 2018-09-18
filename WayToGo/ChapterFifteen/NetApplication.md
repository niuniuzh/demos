# 网络，模板和网页应用
# tcp服务器
* go会为每一个客户端产生一个协程用来处理请求。我们需要使用net包中网络通信的功能。它包含了用于TCP/IP以及UDP协议、域名解析等方法
* 客户端通过net.Dial创建了一个和服务器之间的连接

# 一个简单的网页服务器
* Http是一个比tcp更高级的协议，它描述了客户端浏览器如何与网页服务器进行通信。

# 访问并读取页面

# 写一个简单的网页应用
```
package main

import (
	"io"
	"net/http"
)

const form = `
	<html><body>
		<form action="#" method="post" name="bar">
			<input type="text" name="in" />
			<input type="submit" value="submit"/>
		</form>
	</body></html>
`

/* handle a simple get request */
func SimpleServer(w http.ResponseWriter, request *http.Request) {
	io.WriteString(w, "<h1>hello, world</h1>")
}

func FormServer(w http.ResponseWriter, request *http.Request) {
	w.Header().Set("Content-Type", "text/html")
	switch request.Method {
	case "GET":
		/* display the form to the user */
		io.WriteString(w, form)
	case "POST":
		/* handle the form data, note that ParseForm must
		   be called before we can extract form data */
		//request.ParseForm();
		//io.WriteString(w, request.Form["in"][0])
		io.WriteString(w, request.FormValue("in"))
	}
}

func main() {
	http.HandleFunc("/test1", SimpleServer)
	http.HandleFunc("/test2", FormServer)
	if err := http.ListenAndServe(":8088", nil); err != nil {
		panic(err)
	}
}
```