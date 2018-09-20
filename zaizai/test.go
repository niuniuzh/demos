package main

import (
    "fmt"
    "net/http"
    "encoding/json"
    "database/sql"
     _ "github.com/go-sql-driver/mysql"
     "log"
     "strings"
     "reflect"
     "github.com/gorilla/mux"
)

type response struct{
    Status int `json:"status"`
    Description string `json:"description"`
    Code string `json:"code"`
}

func Response(w http.ResponseWriter, description string,code string, status int) {
    out := &response{status, description, code}
    b, err := json.Marshal(out)
    if err != nil {
        return
    }
    w.WriteHeader(status)
    w.Write(b)
    fmt.Println("hello world")
}

func main() {
    router := mux.NewRouter().StrictSlash(true)
    router.HandleFunc("/login", func (w http.ResponseWriter, r *http.Request) {
        w.Header().Set("content-type", "application/json")
        err := r.ParseForm()
        if err != nil {
            Response(w, "Param error.",  "PARAM_ERROR", 403)
            return
        }
        admin_name := r.FormValue("UserName")
        admin_password := r.FormValue("PassWord")
        if admin_name == "" || admin_password == ""{
            Response(w, "Param error.", "PARAM_ERROR",403)
            return
        }
        db, err := sql.Open("mysql", "root:123@/test?charset=utf8")
        if err != nil {
            log.Println(err)
            Response(w, "Param error.", "PARAM_ERROR",403)
            return
        }
        defer db.Close()
        //查询数据
        rows, err := db.Query("SELECT * FROM book")
        if err != nil {
            log.Println(err)
            Response(w, "Database error.", "DATABASE_ERROR",503)
            return
        }
        fmt.Println(reflect.TypeOf(rows))
        w.Write([]byte(formatToJson(rows)))
    })
    router.HandleFunc("/", func (w http.ResponseWriter, r *http.Request) {
        w.Write([]byte("hahaha"))
    })
    http.ListenAndServe(":8080", router)
}

func formatToJson(rows *sql.Rows)(string) {
    columns, err := rows.Columns()
    if err != nil {
        panic(err.Error())
    }
    values := make([]sql.RawBytes, len(columns))
    scanArgs := make([]interface{}, len(values))
    for i := range values {
        scanArgs[i] = &values[i]
    }
    list := "["
    for rows.Next() {
        err := rows.Scan(scanArgs...)
        if err != nil {
            log.Fatalf("Sacn data error: %s", err.Error())
            panic(err.Error())
        }
        row := "{"
        var value string
        for i, col := range values {
            if col == nil {
                value = "NULL"
            } else {
                value = string(col)
            }
            columName := strings.ToLower(columns[i])
            cell := fmt.Sprintf(`"%v":"%v"`, columName, value)
            row = row + cell + ","
        }
        row = row[0 : len(row)-1]
        row += "}"
        list = list + row + ","
    }
    list = list[0 : len(list)-1]
    list += "]"
    return list
}