# yum
backend for a simple app/platform that allows users to save their favorite restaurants or discover new restaurants

## Run
```
python app.py
```

## API Specification
- Users
    - [Get all users](#Get-all-users)
    - [Create a user](#Create-a-user)
    - [Get a specific user](#Get-a-specific-user)
    - [Update a specific user](#Update-a-specific-user)
    - [Delete a user](#Delete-a-user)
- Restaurants
    - [Add a restaurant to a user](#Add-a-restaurant-to-a-user)
    - [Get specific user's restaurants](#Get-specific-users-restaurants)
    - [Get restaurants by price level](#Get-restaurants-by-price-level)
- Locations
    - [Get all locations](#Get-all-locations)
    - [Get a specific location](#Get-a-specific-location)
    - [Add location to restaurant](#Add-location-to-restaurant)


### Get all users
`GET`  `/api/users/`
```json
Response 

{
    "success": true,
    "data": [
        {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "restaurants": [
                 {
                    "id": 1,
                    "name": "McDonald's",
                    "cuisine": "American",
                    "price_level": 5,
                    "locations": [
                        { 
                           "id": 1,
                           "city": "Boston",
                           "state": "Massachusetts",
                           "zipcode": 02108
                        }
                        "..."
                    ]
                     
                  }
                  "..."               
            ]
      }
   ]
}

```

### Create a user
`POST` `/api/users/`
```json
Request

{
    "first_name": "<USER INPUT>",
    "last_name": "<USER INPUT>",
}
```
```json
Response 

{
    "success": true,
    "data": {
        "id": 1,
        "first_name": "<USER INPUT FOR FIRST NAME>",
        "last_name": "<USER INPUT FOR LAST NAME>",
        "restaurants": [
            {
               "id": 1,
                  "name": "McDonald's",
                  "cuisine": "American",
                  "price_level": 5,
                  "locations": [
                      { 
                         "id": 1,
                         "city": "Boston",
                         "state": "Massachusetts",
                         "zipcode": 02108
                      }
                      "..."
                  ]
                }
                "..."         
        ]
     }
}



  
```

### Get a specific user
`GET` `/api/users/{id}/`
```json
Response 

{
    "success": true,
    "data":{
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "restaurants": [
            {
               "id": 1,
                  "name": "McDonald's",
                  "cuisine": "American",
                  "price_level": 1,
                  "locations": [
                      { 
                         "id": 1,
                         "city": "Boston",
                         "state": "Massachusetts",
                         "zipcode": 02108
                      }
                      "..."
                  ]
                }
                "..."         
        ]
    }
} 


```

### Update a specific user
`POST` `/api/users/`
```json
Request

{
    "first_name": "<USER INPUT>",
    "last_name": "<USER INPUT>",
}
```
```json
Response 

{
    "success": true,
    "data": {
        "id": 1,
        "first_name": "<USER INPUT FOR FIRST NAME>",
        "last_name": "<USER INPUT FOR LAST NAME>",
        "restaurants": [
            {
               "id": 1,
                  "name": "McDonald's",
                  "cuisine": "American",
                  "price_level": 1,
                  "locations": [
                      { 
                         "id": 1,
                         "city": "Boston",
                         "state": "Massachusetts",
                         "zipcode": 02108
                      }
                      "..."
                  ]
                }
                "..."         
        ]
    }
} 


```

### Delete a user
`DELETE` `/users/{id}/`
```json
Response

{
    "success": true,
    "data":{
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "restaurants": [
            {
               "id": 1,
                  "name": "McDonald's",
                  "cuisine": "American",
                  "price_level": 1,
                  "locations": [
                      { 
                         "id": 1,
                         "city": "Boston",
                         "state": "Massachusetts",
                         "zipcode": 02108
                      }
                      "..."
                  ]
                }
                "..."         
        ]
    }
} 

```

### Add a restaurant to a user
`POST` `/api/users/{id}/restaurants/`
```json
Request

{
    "name": "<USER INPUT>",
    "cuisine": "<USER INPUT>",
    "price_level": "<USER INPUT>"
}
```
```json
Response 

{
    "success": true,
    "data": {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "restaurants": [
            {
               "id": 1,
                  "name": "<USER INPUT FOR RESTAURANT NAME",
                  "cuisine": "<USER INPUT FOR RESTAURANT CUISINE>",
                  "price_level": <USER INPUT FOR PRICE LEVEL (1-CHEAP, 5-EXPENSIVE)>,
                  "locations": [
                      { 
                         "id": 1,
                         "city": "Boston",
                         "state": "Massachusetts",
                         "zipcode": 02108
                      }
                      "..."
                  ]
                }
                "..."         
        ]
    }
} 



```

### Get specific user's restaurants
`GET` `/api/users/{id}/restaurants/`

```json
Response 

{
    "success": true,
    "data": [
       {
         "id": 1,
            "name": "McDonald's",
            "cuisine": "American",
            "price_level": 5,
            "locations": [
                { 
                   "id": 1,
                   "city": "Boston",
                   "state": "Massachusetts",
                   "zipcode": 02108
                }
                "..."
             ]
        }
        "..."
    ]       
   
}
    
```

### Get restaurants by price level
`GET` `/api/users/{id}/restaurants/{price_level}/

```json
Response 

{
    "success": true,
    "data": [
       {
         "id": 1,
            "name": "McDonald's",
            "cuisine": "American",
            "price_level": <price_level>,
            "locations": [
                { 
                   "id": 1,
                   "city": "Boston",
                   "state": "Massachusetts",
                   "zipcode": 02108
                }
                "..."
             ]
        }
        "..."
    ]       
   
}
    
```



### Get all locations
`GET` `/api/locations/`
```json
Response
{
    "success": true,
    "data": [
        {
            "id": 1,
            "city": "Boston",
            "state": "Massachusetts",
            "zipcode": 02108,
            "restaurants: [
                {
                  "id": 1,
                  "name": "McDonald's",
                  "cuisine": "American",
                  "price_level": 1
                  }
                 "..."
             ]
                           
         }
         "..."
    ]
}

```

### Get a specific location
`GET` `/api/locations/{id}/`
```json
Response
{
    "success": true,
    "data": {
        "id": 1,
        "city": "Boston",
        "state": "Massachusetts",
        "zipcode": 02108,
        "restaurants: [
                {
                  "id": 1,
                  "name": "McDonald's",
                  "cuisine": "American",
                  "price_level": 1
                  }
                 "..."
         ]
    }
}
```

### Add location to restaurant
`POST` `/api/locations/`
```json
Request
{
   "city": <"USER INPUT">,
   "state": <"USER INPUT">,
   "zipcode" <"USER INPUT">,
   "restaurant_id": <"USER INPUT">
}
```
```json
Response
{
    "success": true,
    "data": 
         {
            "id": <USER INPUT FOR RESTAURANT ID>,
            "name": "McDonald's",
            "cuisine": "American",
            "price_level": 1
            "locations: [
                 {
                    "id": 1,
                    "city": "<USER INPUT FOR CITY>",
                    "state": "<USER INPUT FOR STATE>",
                    "zipcode": <USER INPUT FOR ZIPCODE>
                 }
                 "..."
          }
}
```
