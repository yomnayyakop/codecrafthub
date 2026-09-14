# codecrafthub
CodeCraftHub
CodeCraftHub is a beginner-friendly learning platform API built with Python and Flask.

It allows developers to track courses they want to learn. Each course includes a name, description, target completion date, current learning status, and automatically generated metadata.

This project is designed to help beginners learn the fundamentals of REST APIs, including:

HTTP methods
JSON request and response bodies
CRUD operations
URL parameters
HTTP status codes
File-based data storage
Note: CodeCraftHub does not use a database. Course data is stored in a local file called
courses.json
.

Features
Create new courses
View all courses
View one course by ID
Update an existing course
Delete a course
Automatically generate course IDs
Automatically generate course creation timestamps
Validate required fields
Validate course status values
Validate dates in
YYYY-MM-DD
format
Automatically create
courses.json
if it does not exist
Return helpful JSON error messages
Store course data without requiring a database or authentication
Technologies Used
Python
Flask
JSON
curl
for API testing
Requirements
Before installing the project, make sure you have:

Python 3.8 or newer
A terminal or command prompt
pip
, Python's package installer
Optional:
curl
for testing API requests
Check whether Python is installed:

python --version
On some systems, use:

python3 --version
Check whether
pip
is installed:

pip --version
Or:

pip3 --version
Project Structure
A simple project structure looks like this:

codecrafthub/
├── app.py
├── courses.json
├── requirements.txt
└── README.md
app.py
This is the main Flask application. It contains:

Flask configuration
API routes
Request validation
JSON file reading and writing
Error handling
CRUD operations
courses.json
This file stores all courses.

The file is automatically created by the application if it does not already exist.

A new, empty file contains:

[]
After courses are added, it may look like this:

[
  {
    "id": 1,
    "name": "REST API Fundamentals",
    "description": "Learn HTTP methods, status codes, JSON, and REST API design.",
    "target_date": "2026-10-15",
    "status": "Not Started",
    "created_at": "2026-09-14T12:30:45.123456Z"
  }
]
requirements.txt
This file lists the Python packages required by the project.

Example:

Flask==3.0.0
README.md
This documentation file explains how to install, run, use, and test the project.

Installation
1. Download or clone the project
If the project is stored in a Git repository, clone it with:

git clone https://github.com/your-username/codecrafthub.git
Move into the project directory:

cd codecrafthub
If you downloaded a ZIP file, extract it and open a terminal inside the extracted project folder.

2. Create a virtual environment
A virtual environment keeps this project's packages separate from other Python projects.

Windows
python -m venv venv
Activate it:

venv\Scripts\activate
macOS or Linux
python3 -m venv venv
Activate it:

source venv/bin/activate
After activation, your terminal may display
(venv)
at the beginning of the command line.

3. Install the dependencies
Install Flask from
requirements.txt
:

pip install -r requirements.txt
If your system uses
pip3
, run:

pip3 install -r requirements.txt
If a
requirements.txt
file is not available, Flask can be installed directly:

pip install Flask
4. Check the project files
Make sure your project directory contains
app.py
:

ls
On Windows, use:

dir
You should see files similar to:

app.py
requirements.txt
README.md
The
courses.json
file does not need to exist yet. The application creates it automatically when it starts.

Running the Application
1. Start the Flask server
From the project directory, run:

python app.py
On macOS or Linux, you may need:

python3 app.py
You should see output similar to:

 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
The API is now available at:

http://127.0.0.1:5000
The main course endpoint is:

http://127.0.0.1:5000/api/courses
2. Stop the server
To stop the Flask server, press:

Ctrl+C
REST API Concepts
REST APIs allow applications to communicate using HTTP requests.

Each request usually includes:

A URL
An HTTP method
Optional request data
A response from the server
CodeCraftHub uses these HTTP methods:

Method	Meaning	CodeCraftHub use
GET
Read data	Get courses
POST
Create data	Add a course
PUT
Update data	Replace a course
DELETE
Remove data	Delete a course
The API returns data in JSON format.

Course Data Format
Each course has the following fields:

Field	Description
id
Automatically generated numeric ID
name
Required course name
description
Required course description
target_date
Required date in
YYYY-MM-DD
format
status
Required learning status
created_at
Automatically generated UTC timestamp
Valid status values
The
status
field must contain one of these exact values:

Not Started
In Progress
Completed
Example course
{
  "id": 1,
  "name": "REST API Fundamentals",
  "description": "Learn HTTP methods, status codes, JSON, and REST API design.",
  "target_date": "2026-10-15",
  "status": "Not Started",
  "created_at": "2026-09-14T12:30:45.123456Z"
}
API Endpoints
Base URL:

http://127.0.0.1:5000
1. Create a course
Request
POST /api/courses
curl
example
curl -i -X POST http://127.0.0.1:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "REST API Fundamentals",
    "description": "Learn HTTP methods, status codes, JSON, and REST API design.",
    "target_date": "2026-10-15",
    "status": "Not Started"
  }'
Request body
{
  "name": "REST API Fundamentals",
  "description": "Learn HTTP methods, status codes, JSON, and REST API design.",
  "target_date": "2026-10-15",
  "status": "Not Started"
}
The client should not provide
id
or
created_at
. The application generates those fields automatically.

Successful response
Status:

201 Created
Response:

{
  "id": 1,
  "name": "REST API Fundamentals",
  "description": "Learn HTTP methods, status codes, JSON, and REST API design.",
  "target_date": "2026-10-15",
  "status": "Not Started",
  "created_at": "2026-09-14T12:30:45.123456Z"
}
2. Get all courses
Request
GET /api/courses
curl
example
curl -i -X GET http://127.0.0.1:5000/api/courses
Successful response
Status:

200 OK
Response:

[
  {
    "id": 1,
    "name": "REST API Fundamentals",
    "description": "Learn HTTP methods, status codes, JSON, and REST API design.",
    "target_date": "2026-10-15",
    "status": "Not Started",
    "created_at": "2026-09-14T12:30:45.123456Z"
  }
]
If there are no courses, the response is:

[]
3. Get one course
Request
GET /api/courses/<course_id>
Replace
<course_id>
with a real course ID.

curl
example
curl -i -X GET http://127.0.0.1:5000/api/courses/1
Successful response
Status:

200 OK
Response:

{
  "id": 1,
  "name": "REST API Fundamentals",
  "description": "Learn HTTP methods, status codes, JSON, and REST API design.",
  "target_date": "2026-10-15",
  "status": "Not Started",
  "created_at": "2026-09-14T12:30:45.123456Z"
}
4. Update a course
Request
PUT /api/courses/<course_id>
A
PUT
request replaces the editable course information. All required fields must be included.

Example request
curl -i -X PUT http://127.0.0.1:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Advanced REST API Fundamentals",
    "description": "Study advanced REST API design, pagination, and error handling.",
    "target_date": "2026-10-30",
    "status": "In Progress"
  }'
Request body
{
  "name": "Advanced REST API Fundamentals",
  "description": "Study advanced REST API design, pagination, and error handling.",
  "target_date": "2026-10-30",
  "status": "In Progress"
}
Do not include
id
or
created_at
in the request. The application preserves those values.

Successful response
Status:

200 OK
Response:

{
  "id": 1,
  "name": "Advanced REST API Fundamentals",
  "description": "Study advanced REST API design, pagination, and error handling.",
  "target_date": "2026-10-30",
  "status": "In Progress",
  "created_at": "2026-09-14T12:30:45.123456Z"
}
5. Delete a course
Request
DELETE /api/courses/<course_id>
curl
example
curl -i -X DELETE http://127.0.0.1:5000/api/courses/1
Successful response
Status:

200 OK
Response:

{
  "message": "Course with ID 1 was deleted successfully."
}
HTTP Status Codes
CodeCraftHub uses standard HTTP status codes.

Status	Meaning
200 OK
The request completed successfully
201 Created
A new course was created
400 Bad Request
The request contains invalid or missing data
404 Not Found
The course or endpoint does not exist
405 Method Not Allowed
The HTTP method is not supported
500 Internal Server Error
A server or file-storage error occurred
Testing the API
Basic testing sequence
Start the server:

python app.py
Then run these commands in another terminal.

1. Create a course
curl -i -X POST http://127.0.0.1:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python Basics",
    "description": "Learn the fundamentals of Python programming.",
    "target_date": "2026-10-01",
    "status": "Not Started"
  }'
2. Get all courses
curl -i http://127.0.0.1:5000/api/courses
3. Get course 1
curl -i http://127.0.0.1:5000/api/courses/1
4. Update course 1
curl -i -X PUT http://127.0.0.1:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python Basics",
    "description": "Learn Python variables, functions, lists, and dictionaries.",
    "target_date": "2026-10-15",
    "status": "In Progress"
  }'
5. Delete course 1
curl -i -X DELETE http://127.0.0.1:5000/api/courses/1
Test missing fields
This request omits required fields:

curl -i -X POST http://127.0.0.1:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Incomplete Course"
  }'
Expected status:

400 Bad Request
Example response:

{
  "error": "Missing required field(s): description, status, target_date"
}
Test an invalid status
curl -i -X POST http://127.0.0.1:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Invalid Status Course",
    "description": "This course uses an invalid status.",
    "target_date": "2026-12-01",
    "status": "Started"
  }'
Expected status:

400 Bad Request
Example response:

{
  "error": "Invalid status. Status must be one of: Completed, In Progress, Not Started."
}
Test an invalid date
curl -i -X POST http://127.0.0.1:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Invalid Date Course",
    "description": "This course uses an invalid date format.",
    "target_date": "12/01/2026",
    "status": "Not Started"
  }'
Expected status:

400 Bad Request
Example response:

{
  "error": "target_date must use the format YYYY-MM-DD."
}
Test a course that does not exist
curl -i http://127.0.0.1:5000/api/courses/9999
Expected status:

404 Not Found
Example response:

{
  "error": "Course with ID 9999 was not found."
}
Testing with a Web Browser
A browser can send simple
GET
requests.

With the Flask application running, open this URL:

http://127.0.0.1:5000/api/courses
You can also open a specific course:

http://127.0.0.1:5000/api/courses/1
A browser alone is not convenient for
POST
,
PUT
, and
DELETE
requests. For those methods, use:

curl
Postman
Insomnia
A frontend application
Python test code
Testing with Postman
You can use Postman as an alternative to
curl
.

Create a course
Open Postman.

Create a new request.

Select
POST
.

Enter:

http://127.0.0.1:5000/api/courses
Select the Body tab.

Select raw.

Select JSON.

Enter:

{
  "name": "Postman Practice",
  "description": "Practice sending REST API requests with Postman.",
  "target_date": "2026-12-15",
  "status": "Not Started"
}
Click Send.
For
GET
,
PUT
, and
DELETE
, select the matching HTTP method and use the endpoint examples above.

How Data Storage Works
CodeCraftHub uses Python's built-in
json
module.

When the application needs to retrieve courses, it:

Opens
courses.json
.
Converts the JSON text into a Python list.
Uses the list in the API route.
Returns the data as JSON.
When the application needs to save courses, it:

Reads the existing courses.
Adds, updates, or removes a course.
Converts the Python list back into JSON.
Writes the updated data to
courses.json
.
The application automatically creates the file if it does not exist:

[]
This approach is useful for learning, but it is not intended for a large production application.

Troubleshooting
Problem:
python
command is not found
Try:

python3 --version
If that works, use
python3
instead of
python
:

python3 app.py
On Windows, make sure Python was installed and that the option to add Python to the system PATH was selected.

Problem: Flask is not installed
You may see an error such as:

ModuleNotFoundError: No module named 'flask'
Activate your virtual environment and install Flask:

pip install Flask
Or install all project dependencies:

pip install -r requirements.txt
Problem: The server is not running
If
curl
returns a connection error, make sure the Flask application is running:

python app.py
You should see:

Running on http://127.0.0.1:5000
Problem: Port 5000 is already in use
Another application may already be using port
5000
.

You can change the port at the bottom of
app.py
:

app.run(debug=True, port=5001)
Then use:

http://127.0.0.1:5001
For example:

curl http://127.0.0.1:5001/api/courses
Problem:
courses.json
is not created
Make sure:

You started the application from the project directory.
The directory is writable.
Python has permission to create files there.
There is not already a folder named
courses.json
.
The application creates the file automatically when it starts.

Problem: The JSON file contains invalid data
If
courses.json
is manually edited and contains invalid JSON, the API may return a data file error.

A valid empty file should contain:

[]
You can replace the contents of
courses.json
with:

[]
Be aware that this deletes all currently stored courses.

Problem: A POST or PUT request returns
400 Bad Request
Check that:

The request includes the JSON content type header:

Content-Type: application/json
The JSON syntax is valid.

All required fields are included.

The status is one of:

Not Started
In Progress
Completed
The date uses this format:

YYYY-MM-DD
Example of a valid date:

2026-10-15
Problem: A course returns
404 Not Found
Check that:

The course ID exists.
The ID is included in the URL.
The URL is spelled correctly.
Example:

curl http://127.0.0.1:5000/api/courses/1
If course
1
does not exist, the API correctly returns a
404
response.

Problem:
curl
is not available
Windows
You can use:

PowerShell
Postman
Insomnia
Git Bash
Recent versions of Windows include
curl
by default.

macOS or Linux
Install
curl
using your operating system's package manager if needed.

You can also test
GET
endpoints by opening them in a web browser.

Important Limitations
This project uses a JSON file instead of a database because it is intended for learning.

A JSON file is suitable for:

Small projects
Local learning
Personal course tracking
Practicing REST APIs
A JSON file is not ideal for:

Many simultaneous users
Large amounts of data
Complex searches
Concurrent updates
Production applications
Multi-user authentication systems
For a larger application, you could later migrate the project to:

SQLite
PostgreSQL
MySQL
MongoDB
You could also add:

User authentication
Course categories
Progress percentages
Search and filtering
Pagination
A web frontend
Automated unit tests
Summary
CodeCraftHub provides a simple REST API for tracking learning courses.

The main endpoints are:

POST   /api/courses
GET    /api/courses
GET    /api/courses/<course_id>
PUT    /api/courses/<course_id>
DELETE /api/courses/<course_id>
The application stores data in:

courses.json
To start learning, run:

python app.py
Then create your first course:

curl -i -X POST http://127.0.0.1:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "REST API Fundamentals",
    "description": "Learn the basics of REST APIs.",
    "target_date": "2026-10-15",
    "status": "Not Started"
  }'
