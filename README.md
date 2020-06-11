# Capstone Casting Agency Project
This is the final project of Udacity Full Stack Web Developer Nanodegree

The Project is the backend of a Casting Agency Company that hires actors and produce movies.

There are different roles with different permissions for people who work in the agency.

The Project Contains:

Database modeling with PostgreSQL & SQLAlchemy
APIs to performance CRUD Operations on database with Flask
Automated testing with Unittest
Automatad testing with Postman
Authorization & Role based authentication control with Auth0
Web server deployment on Heroku

## Heroku Link
```

  ```

## Getting Started
nstalling Dependencies
Python 3.8.2
Follow instructions to install the latest version of python for your platform in the python docs

Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by running:

 ```
  $ pip install -r requirements.txt
  ```

## Running the server

First ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

 ```
export FLASK_APP=app.py;
export FLASK_ENV=debug;
  ```
To run the server, execute:

 ```
flask run --reload
  ```
The --reload flag will detect file changes and restart the server automatically.

## Casting Agency Specification

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

### Data Models
Movie with attributes title and release date
Actor with attributes name, age and gender
Casting with attributes actor_id and movie_id

### Endpoints
- GET /actors, /movies and /casting
- POST /actors, /movies and /casting
- PATCH /actors, /movies/ and /casting
- DELETE /actors, /movies/ and /casting

### Roles
- Casting Assistant
has following permissions for actions.
1. get:movies, get:actors, get:casting

- Casting Director
has following permissions for actions.
1. get:movies, get:actors, get:casting
2. post:actors, post:casting
3. patch:movies, patch:actors, patch:casting
4. delete:actors, delete:casting

- Executive Producer
has following permissions for actions.
1. get:movies, get:actors, get:casting
2. post:movies, post:actors, post:casting
3. patch:movies, patch:actors, patch:casting
4. delete:actors, delete:actors, delete:casting
<<<<<<< HEAD
=======

## Authentication (bearer tokens)

Casting Assistant

 ```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRkS1AtMXhwRHl2U0Z5X0V2U2s0YSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWdlbmN5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWRmZGUxNjY2NjE0NDAwMTNiZTczN2UiLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1OTE4Mjc3MjAsImV4cCI6MTU5MTgzNDkyMCwiYXpwIjoiR1A1N3RvTFVDYzh5cTBhREZyZjBla242VHZZUnVXeFMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.kfMbgd-ENpe0otQ5Ck-CXrmOh6fKJ7Ayg-Nai9dvTRXnq4vik6jpaWWzsQWg3mGzDidfIVjtBmlx1wjPVz3_0WDRGHsszYbR4t7gvrgLyDHE2YVHT8wukHSVA0o-kjAbKcD3m1eIj4UQUVe60lCwkbtQpUTN1O2RNgtz3HTSJCV38jjOmSRgJ-aHTt2JMbOnp3xhUtbRneI6rYjhK8CLi1rV8bOLhzuMqOnsbkl2z-HKb7LqehXyiHjIBB9u8-8NvTAnUIBLpuwlTph9FDt1cpx2okEKHGp-u-5l6YFQz4JjDK_3FzxlF8B1vqirAjg4juekSTV2RbFuOSDENBv4_w
  ```

Casting Director
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRkS1AtMXhwRHl2U0Z5X0V2U2s0YSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWdlbmN5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWRmZGRmOGYyYTc4MzAwMTk2MDIwMGYiLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1OTE3MzQxNzQsImV4cCI6MTU5MTc0MTM3NCwiYXpwIjoiR1A1N3RvTFVDYzh5cTBhREZyZjBla242VHZZUnVXeFMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3QgYWN0b3JzIl19.ECBE-mEoMPjULJBbE_R5snMXKIbpB6-0dMdSaXfFv9Ztr5LjZmHjv0QjX_zP1V4fnzdGBHj1ZilRIfMvB2dmVQF5AGoqXu3PWloiR5DrsGPE6iQF6c3oGbsz-sqOkrfK5fAc02tY6YCkcYvr_wVBV5fWWJ60yCpTgTW_FLPgV54GgBz1Bki1JX-5kNuIRvkukpg7V8jhXQ9V241gdLYKrEcA2RkBwc1wfnMcmHVy_40xa3Zjcq_y16QH-1Cq77_BiezOA1leoSs2vSE0ewmoLZjUf9WJdqsHvZLEMnKsts-fWtoM4WWih1xcZlp_1-dGdXIcj0weA9wzWDsjzxU06g

  ```

Executive Producer
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRkS1AtMXhwRHl2U0Z5X0V2U2s0YSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWdlbmN5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWRmZGRkMmMwZjUxZTAwMTk1YzUwZWQiLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1OTE4MjgxODEsImV4cCI6MTU5MTgzNTM4MSwiYXpwIjoiR1A1N3RvTFVDYzh5cTBhREZyZjBla242VHZZUnVXeFMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0IGFjdG9ycyIsInBvc3Q6bW92aWVzIl19.utOeK0IEN9GsGN6bSTzNXoURJX9Dt3wUAvmFOvs0pI3qpWn7pHjWqNvJ61VPSdkDhUkpkfbTE7Rol6B5tPKEbXS4blu9xoKfoVVztre916cWioIIJpms_btrIK1qDx9ASuswCPWRtV93nZK821OcfV0FDhZ2yQS4obEVX4GmbsDPZW3nxEPZ_CuIdQqP-KtAov5nqLnxqkaH0VmnuFHOIO9JHvYbAxg1JAch5myH6u_1emzAifacw1vkO1xPQuQ0_zm7uyvlmNrc_hdrgpNFBpS62bb4GoCyYqaa3mQTnBJr25FhjhVzWxPzGQig4z-iJHFBfUogMX_yaBI7pfQweA
  ```

## Error Handling
Errors are returned as JSON objects in the following formats:
>>>>>>> 1505d77ad60c6a2259d242825d5380448d33c6ff

## Authentication (bearer tokens)

Casting Assistant

 ```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRkS1AtMXhwRHl2U0Z5X0V2U2s0YSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWdlbmN5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWRmZGUxNjY2NjE0NDAwMTNiZTczN2UiLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1OTE4Mjc3MjAsImV4cCI6MTU5MTgzNDkyMCwiYXpwIjoiR1A1N3RvTFVDYzh5cTBhREZyZjBla242VHZZUnVXeFMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.kfMbgd-ENpe0otQ5Ck-CXrmOh6fKJ7Ayg-Nai9dvTRXnq4vik6jpaWWzsQWg3mGzDidfIVjtBmlx1wjPVz3_0WDRGHsszYbR4t7gvrgLyDHE2YVHT8wukHSVA0o-kjAbKcD3m1eIj4UQUVe60lCwkbtQpUTN1O2RNgtz3HTSJCV38jjOmSRgJ-aHTt2JMbOnp3xhUtbRneI6rYjhK8CLi1rV8bOLhzuMqOnsbkl2z-HKb7LqehXyiHjIBB9u8-8NvTAnUIBLpuwlTph9FDt1cpx2okEKHGp-u-5l6YFQz4JjDK_3FzxlF8B1vqirAjg4juekSTV2RbFuOSDENBv4_w
  ```

Casting Director
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRkS1AtMXhwRHl2U0Z5X0V2U2s0YSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWdlbmN5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWRmZGRmOGYyYTc4MzAwMTk2MDIwMGYiLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1OTE3MzQxNzQsImV4cCI6MTU5MTc0MTM3NCwiYXpwIjoiR1A1N3RvTFVDYzh5cTBhREZyZjBla242VHZZUnVXeFMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3QgYWN0b3JzIl19.ECBE-mEoMPjULJBbE_R5snMXKIbpB6-0dMdSaXfFv9Ztr5LjZmHjv0QjX_zP1V4fnzdGBHj1ZilRIfMvB2dmVQF5AGoqXu3PWloiR5DrsGPE6iQF6c3oGbsz-sqOkrfK5fAc02tY6YCkcYvr_wVBV5fWWJ60yCpTgTW_FLPgV54GgBz1Bki1JX-5kNuIRvkukpg7V8jhXQ9V241gdLYKrEcA2RkBwc1wfnMcmHVy_40xa3Zjcq_y16QH-1Cq77_BiezOA1leoSs2vSE0ewmoLZjUf9WJdqsHvZLEMnKsts-fWtoM4WWih1xcZlp_1-dGdXIcj0weA9wzWDsjzxU06g

  ```

Executive Producer
```
<<<<<<< HEAD
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlRkS1AtMXhwRHl2U0Z5X0V2U2s0YSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWdlbmN5LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWRmZGRkMmMwZjUxZTAwMTk1YzUwZWQiLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1OTE4MjgxODEsImV4cCI6MTU5MTgzNTM4MSwiYXpwIjoiR1A1N3RvTFVDYzh5cTBhREZyZjBla242VHZZUnVXeFMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0IGFjdG9ycyIsInBvc3Q6bW92aWVzIl19.utOeK0IEN9GsGN6bSTzNXoURJX9Dt3wUAvmFOvs0pI3qpWn7pHjWqNvJ61VPSdkDhUkpkfbTE7Rol6B5tPKEbXS4blu9xoKfoVVztre916cWioIIJpms_btrIK1qDx9ASuswCPWRtV93nZK821OcfV0FDhZ2yQS4obEVX4GmbsDPZW3nxEPZ_CuIdQqP-KtAov5nqLnxqkaH0VmnuFHOIO9JHvYbAxg1JAch5myH6u_1emzAifacw1vkO1xPQuQ0_zm7uyvlmNrc_hdrgpNFBpS62bb4GoCyYqaa3mQTnBJr25FhjhVzWxPzGQig4z-iJHFBfUogMX_yaBI7pfQweA
  ```

## Error Handling
Errors are returned as JSON objects in the following formats:

```
=======
>>>>>>> 1505d77ad60c6a2259d242825d5380448d33c6ff
{
    'success': False,
    'error': 400,
    'message': "bad request"
}

or

{
    'code': 'unauthorized',
    'description': 'Permission not found.'
}
  ```

  The API will return seven error types when requests fail:
<<<<<<< HEAD

- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Sever Error
=======

- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Sever Error

>>>>>>> 1505d77ad60c6a2259d242825d5380448d33c6ff

## Endpoints
- GET /movies
- - General: Retrieve all movies.
- - Permission: Casting Assistant, Casting Director, Executive Producer
- - Request Arguments: JWT token.
- Return: success value and a dictionary of movies.
