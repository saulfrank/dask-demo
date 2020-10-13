package main

import (
	"mydb/database"
	"mydb/database/models"
)

func main() {
	database.Connect()
	database.DBConn.AutoMigrate(
		&models.Property{},
	)
	defer database.DBConn.Close()
}
