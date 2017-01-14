DOMAIN = {
    "user": {
        "schema":{
            "firstname":{
                "type":"string"
            },
            "lastname":{
                "type":"string"
            },
            "password":{
                "type":"string"
            },
            "email":{
                "type":"string"
            },
            "rank":{
                "type":"string"
            }
        }
    },
    "trylogin":{
        "schema":{
            "email":{
                "authen":"string"
            },
            "password":{
                "type":"string"
            }
        }
    },
    "item": {
        "schema":{
            "item_name":{
                "type":"string"
            },
            "user_name_angel":{
                "type":"string"
            },
            "user_name_owner":{
                "type":"string"
            },
            "lost_status":{
                "type":"bool"
            },
            "date":{
                "type":"dict",
                "schema": {
                    "month":{"type":"int"},
                    "day":{"type":"int"},
                    "year":{"type":"int"}
                }
            },
            "location":{
                "type":"dict",
                "schema": {
                    "langtitude":{"type":"double"},
                    "longtitude":{"type":"double"}
                }
            },
            "description":{
                "type":"string"
            }
        }
    }
}

RESOURCE_METHODS = ['GET','POST']
