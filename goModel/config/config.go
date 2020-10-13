package config

import (
	_ "gopkg.in/validator.v2"
	"os"
)

var GConf = GetConfig()

type Config struct {
	Database Database
	ENV string
}

type Database struct {
	User     string `validate:"nonnil"`
	Password string `validate:"nonnil"`
	Database string `validate:"nonnil"`
	Host  string `validate:"nonnil"`
	Port  string `validate:"nonnil"`
	SSL string `validate:"nonnil"`
}



func GetConfig() Config {

	// ------ database -----
	db_config := Database {}
	db_config.Host = os.Getenv("db_host")
	db_config.Database = os.Getenv("db_database")
	db_config.User = os.Getenv("db_user")
	db_config.Password = os.Getenv("db_pwd")
	db_config.SSL = os.Getenv("db_ssl")
	db_config.Port = os.Getenv("db_port")

	config := Config{
		Database: db_config,
		ENV: os.Getenv("env"),
	}
	return config
}
