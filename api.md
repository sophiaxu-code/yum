Name:Sophia Xu
NetID:sx53
Challenges Attempted: Tier (I/II/III)

GET ALL USERS

GET /api/users/
Response 
  { "success": true,
    "data": [
      {
        "id": 1,
        "first_name": "Michelle",
        "last_name": "Obama",
        "restaurants": [ <"SERIALIZED RESTAURANT">, ...]
      },
      {
        "id": 2,
        "first_name": "Thomas",
        "last_name": "Jefferson",
        "restaurants" [<"SERIALIZED RESTAURANT">, ...]
      }
    ]

  }

 CREATE A USER

 POST/api/users/
 Request
 {
   "first_name": <"USER INPUT">,
   "last_name": <"USER INPUT">
 }

 Response
 {
   "success": true,
   "data": {
     "id: <"ID">,
     "first_name": <"USER INPUT FOR FIRST_NAME">,
     "last_name": <"USER INPUT FOR LAST_NAME">,
     "restaurants": []
   }
 }

GET A SPECIFIC USER

GET/api/users/{id}/
Response
 {
   "success": true,
   "data": {
     "id: <"ID">,
     "first_name": <"USER INPUT FOR FIRST_NAME">,
     "last_name": <"USER INPUT FOR LAST_NAME">,
     "restaurants": [<"SERIALIZED RESTAURANT">, ...]
   }
 }

UPDATE USER BY ID

POST/api/users/{id}/
Response
{
   "success": true,
   "data": {
     "id: <"ID">,
     "first_name": <"USER INPUT FOR FIRST_NAME">,
     "last_name": <"USER INPUT FOR LAST_NAME">,
     "restaurants": [<"SERIALIZED RESTAURANT">, ...]
   }
 }

DELETE A SPECIFIC USER

DELETE/api/users/{id}/
Response 
{
   "success": true,
   "data": {
     "id: <"ID">,
     "first_name": <"USER INPUT FOR FIRST_NAME">,
     "last_name": <"USER INPUT FOR LAST_NAME">,
     "restaurants": [<"SERIALIZED RESTAURANT">, ...]
}

ADD A RESTAURANT TO A USER

POST/api/users/{id}/restaurants/
Request
{
  "name": <"USER INPUT">,
  "cuisine": <"USER INPUT">,
  "price_level": <"USER INPUT">
}
Response
{
  "success": true,
  "data": <"SERIALIZED USER">
}

GET A SPECIFIC USER'S RESTAURANTS

GET/api/users/{id}/restaurants/
Response
{
  "success": true,
  "data": [<"SERIALIZED RESTAURANT">, ...]
}

GET RESTAURANTS BY PRICE LEVEL

GET/api/users/{id}/restaurants/{pricelevel}/
Response 
{
  "success": true,
  "data": [<"SERIALIZED RESTAURANT">, ...]
}

GET ALL LOCATIONS

GET/api/locations/
Response 
{
  "success": true,
  "data": [<"SERIALIZED LOCATION">, ...]
}

GET LOCATION BY ID

GET/api/locations/{id}/
Response
{
  "success": true,
  "data": <"SERIALIZED LOCATION">
}

ADD LOCATION TO RESTAURANT

POST/api/locations/
Request
{
  "city": <"USER INPUT">,
  "state": <"USER INPUT">,
  "zipcode" <"USER INPUT">,
  "restaurant_id": <"USER INPUT">
}
Response
{
  "success": true,
  "data": <"SERIALIZED RESTAURANT">
}


