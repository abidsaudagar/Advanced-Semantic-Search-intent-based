indexMapping = {
    "properties":{
        "ProductID":{
            "type":"long"
        },
        "ProductName":{
            "type":"text"
        },
        "ProductBrand":{
            "type":"text"
        },
        "Gender":{
            "type":"text"
        },
        "Price (INR)":{
            "type":"long"
        },
        "NumImages":{
            "type":"long"
        },
        "Description":{
            "type":"text"
        },
        "PrimaryColor":{
            "type":"text"
        },
        "NameDescription":{
            "type":"text"
        },
        "NameDescriptionVector":{
            "type":"dense_vector",
            "dims": 1536,
            "index":True,
            "similarity": "l2_norm"
        }

    }
}