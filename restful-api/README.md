# RESTful API

Consuming and building RESTful APIs: HTTP basics, `curl`, the `requests` library, a server with `http.server`, a Flask
API, and API security with basic authentication, JWT and roles. Scripts are tested with Python 3.9.

## Files

| File | Description |
| --- | --- |
| `task_02_requests.py` | `fetch_and_print_posts()` prints the status code and post titles from JSONPlaceholder; `fetch_and_save_posts()` writes `id`, `title`, `body` to `posts.csv`. |
| `task_03_http_server.py` | `http.server` API on port 8000: `/`, `/data` (JSON), `/status`, `/info`, and 404 for anything else. |
| `task_04_flask.py` | Flask API with `/`, `/data`, `/status`, `/users/<username>` and `POST /add_user`. |
| `task_05_basic_security.py` | Flask API with basic auth (`/basic-protected`), JWT login (`/login`, `/jwt-protected`) and an admin-only route. |

## 0. HTTP and HTTPS

- **HTTP** sends data as plain text: anyone on the path can read or change it.
- **HTTPS** is HTTP over TLS: the data is encrypted, its integrity is checked, and the certificate proves the server's identity.
  It uses port 443 instead of 80.

A **request** has a method, a path and a version (`GET /posts HTTP/1.1`), headers (`Host`, `Accept`, ...) and an optional
body. A **response** has a version, a status code and a reason (`HTTP/1.1 200 OK`), headers (`Content-Type`, ...) and a body.

| Method | Description | Use case |
| --- | --- | --- |
| GET | Retrieves data | Fetch a web page or a list of posts |
| POST | Creates a resource | Submit a form, add a new user |
| PUT | Replaces a resource | Update a whole user profile |
| PATCH | Changes part of a resource | Change only the email of a user |
| DELETE | Removes a resource | Delete a post |

| Status code | Description | Scenario |
| --- | --- | --- |
| 200 OK | The request succeeded | A page or API resource is returned |
| 201 Created | A resource was created | A POST added a new user |
| 400 Bad Request | The request is malformed | The JSON body is invalid |
| 401 Unauthorized | Authentication is missing or wrong | No token, or a wrong password |
| 403 Forbidden | Authenticated but not allowed | A normal user calls an admin route |
| 404 Not Found | The resource does not exist | A wrong URL |
| 500 Internal Server Error | The server failed | An unhandled exception in the API |

## 1. curl

```
curl --version
curl https://jsonplaceholder.typicode.com/posts
curl -I https://jsonplaceholder.typicode.com/posts
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

`-I` shows only the headers, `-X` sets the method and `-d` sends data. The POST returns the created post with `"id": 101`.

## Requirements

```
pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended
```
