// https://github.com/version-1/gin-gorm-gqlgen-sample/blob/master/src/gin_graphql/resolver.go

package models

import (
	"time"
)

type Property struct {
	ID        string `gorm:"PRIMARY_KEY;type:varchar(64);" json:"id"`
	Price int64 `json:"price"`
	TransferDate time.Time `json:"transfer_date"`
	Postcode string `json:"region"`
	PropertyType string `json:"property_type"`
	OldNew string `json:"old_new"`
	Duration string `json:"duration"`
	PrimaryAddressObj string `json:"primary_address_obj"`
	SeccondaryAddressObj string `json:"secondary_address_obj"`
	Street string `json:"street"`
	Locality string `json:"locality"`
	CityTown string `json:"city_town"`
	District string `json:"district"`
	County string `json:"county"`
	PpdCat string `json:"ppd_cat"`
	RecordStat string `json:"record_stat"`
	Price2 float64 `json:"price2"`
}
