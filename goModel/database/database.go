package database

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/postgres"
	"mydb/config"
	"strings"
)

var(
	DBConn *gorm.DB
)

//var DBConn *gorm.DB
//var once sync.Once

func Connect() {

// 	connect := strings.Join([]string{
// 		config.GConf.Database.User, ":",
// 		config.GConf.Database.Password, "@",
// 		"(", config.GConf.Database.Host,":",config.GConf.Database.Port,")/",
// 		config.GConf.Database.Database, "?charset=utf8mb4&parseTime=True&loc=Local",
// 		//"port=", config.GConf.Database.Port, " ",
// 		//"sslmode=", config.GConf.Database.SSL,
// 	}, "")

		connect := strings.Join([]string{
		"user=",config.GConf.Database.User, " ",
		"password=",config.GConf.Database.Password, " ",
		"host=", config.GConf.Database.Host," ",
		"port=", config.GConf.Database.Port," ",
		"dbname=",config.GConf.Database.Database, " ",
		//"port=", config.GConf.Database.Port, " ",
		"sslmode=disable",
	}, "")

	//log.Println(connect)

	//"host=myhost port=myport user=gorm dbname=gorm password=mypassword"
	var err error
	DBConn, err = gorm.Open("postgres", connect)

	if err != nil {
		//fmt.Println(err)
		panic(err.Error())
		//panic("failed to connect database")
	}

	if config.GConf.ENV != "production" {
		DBConn.LogMode(true)
	}
	//fmt.Print(db)

	DBConn.SingularTable(true)
}