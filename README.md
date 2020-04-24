# artify

## Project setup
Seting up the project needs [docker](https://www.docker.com/products/docker-desktop) to be installed.
Run this command and the app should open on localhost:3000
```
./scripts/start.sh
```



### API Notes
# Person Registry Service

## Usage

All responses will have the form

```json
{
    "message": "Description of what happened",
    "data": "Mixed type holding the content of the response"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all people

**Definition**

`GET /people/`

**Response**

- `200 OK` on success

```json
[
    {
        "id": "ejq1a1kopd42j238ee89fhpcr90",
        "name": "Tiit",
        "agreed": true,
        "skills": [
            "Manufacturing",
            "Coding"
        ]
    },
    {
        "id": "oic29jkb96fb8q3eh506ia3rgen",
        "name": "Lennu",
        "agreed": true,
        "skills": [
            "Manufacturing",
            "Construction materials",
            "Electronics and Optics",
        ]
    }
]
```

### Registering a new person

**Definition**

`POST /people/`

**Arguments**

- `"id":string` a globally unique identifier for this session
- `"name":string` a name for this person
- `"agreed":bool` has the person agreed to the terms
- `"skills":list<string>` list of skills that the person has 

If a person with the given identifier already exists, the existing person will be overwritten.

**Response**

- `201 Created` on success

```json
{
    "id": "oic29jkb96fb8q3eh506ia3rgen",
    "name": "Lennu",
    "agreed": true,
    "skills": [
        "Manufacturing",
        "Construction materials",
        "Electronics and Optics",
    ]
}
```

## Lookup people details

`GET /people/<name>`

**Response**

- `404 Not Found` if the person does not exist
- `200 OK` on success

```json
{
    "id": "oic29jkb96fb8q3eh506ia3rgen",
    "name": "Lennu",
    "agreed": true,
    "skills": [
        "Manufacturing",
        "Construction materials",
        "Electronics and Optics",
    ]
}
```

## Delete a person

**Definition**

`DELETE /person/<id>`

**Response**

- `404 Not Found` if the person does not exist
- `204 No Content` on success

### List all skills

**Definition**

`GET /skills/`

**Response**

- `200 OK` on success

```json
[
    {
        "skill": [
            "Coding"
        ]
    },
    {
        "skill": [
            "Manufacturing",
        ]
    },
]
```
### Delete a skill

**Definition**

`DELETE /skills/`

**Response**

- `404 Not Found` if the skill does not exist
- `204 No Content` on success

### Add a skill

**Definition**

`POST /skills/`

**Arguments**

- `"skill":string` a skills that the person has

**Response**

- `200 OK` on success

```json
[
    {
        "skill": [
            "Coding"
        ]
    }
]
```

