from flask import Flask, jsonify, request
from pathlib import Path
import json
import os
import tempfile

app = Flask(__name__)

DATA_FILE = Path(__file__).parent / "courses.json"

VALID_STATUSES = {
    "Not Started",
    "In Progress",
    "Completed"
}


def read_courses():
    """Read all courses from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def write_courses(courses):
    """Write courses to the JSON file safely."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Write to a temporary file first, then replace the original.
    # This helps avoid leaving a partially written JSON file.
    with tempfile.NamedTemporaryFile(
        "w",
        delete=False,
        dir=DATA_FILE.parent,
        encoding="utf-8"
    ) as temporary_file:
        json.dump(courses, temporary_file, indent=2)
        temporary_file.write("\n")
        temporary_path = temporary_file.name

    os.replace(temporary_path, DATA_FILE)


def find_course(courses, course_id):
    """Find a course by its numeric ID."""
    return next(
        (course for course in courses if course["id"] == course_id),
        None
    )


def validate_course_data(data, partial=False):
    """Validate incoming course data."""
    required_fields = {
        "name",
        "description",
        "target_completion_date",
        "status"
    }

    if not partial:
        missing_fields = required_fields - data.keys()

        if missing_fields:
            return f"Missing fields: {', '.join(sorted(missing_fields))}"

    if "name" in data and not isinstance(data["name"], str):
        return "name must be a string"

    if "description" in data and not isinstance(data["description"], str):
        return "description must be a string"

    if "target_completion_date" in data:
        if not isinstance(data["target_completion_date"], str):
            return "target_completion_date must be a string"
        # A beginner-friendly version can use YYYY-MM-DD strings.
        if len(data["target_completion_date"]) != 10:
            return "target_completion_date must use YYYY-MM-DD format"

    if "status" in data and data["status"] not in VALID_STATUSES:
        return f"status must be one of: {', '.join(VALID_STATUSES)}"

    return None


@app.get("/api/courses")
def get_courses():
    courses = read_courses()

    status = request.args.get("status")
    if status:
        if status not in VALID_STATUSES:
            return jsonify({
                "error": "Invalid status"
            }), 400

        courses = [
            course for course in courses
            if course["status"] == status
        ]

    return jsonify(courses)


@app.get("/api/courses/<int:course_id>")
def get_course(course_id):
    courses = read_courses()
    course = find_course(courses, course_id)

    if course is None:
        return jsonify({"error": "Course not found"}), 404

    return jsonify(course)


@app.post("/api/courses")
def create_course():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Request body must contain JSON"}), 400

    error = validate_course_data(data)
    if error:
        return jsonify({"error": error}), 400

    courses = read_courses()
    next_id = max((course["id"] for course in courses), default=0) + 1

    new_course = {
        "id": next_id,
        "name": data["name"],
        "description": data["description"],
        "target_completion_date": data["target_completion_date"],
        "status": data["status"]
    }

    courses.append(new_course)
    write_courses(courses)

    return jsonify(new_course), 201


@app.put("/api/courses/<int:course_id>")
def update_course(course_id):
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"error": "Request body must contain JSON"}), 400

    error = validate_course_data(data)
    if error:
        return jsonify({"error": error}), 400

    courses = read_courses()
    course = find_course(courses, course_id)

    if course is None:
        return jsonify({"error": "Course not found"}), 404

    course.update({
        "name": data["name"],
        "description": data["description"],
        "target_completion_date": data["target_completion_date"],
        "status": data["status"]
    })

    write_courses(courses)

    return jsonify(course)


@app.patch("/api/courses/<int:course_id>/status")
def update_course_status(course_id):
    data = request.get_json(silent=True)

    if not data or "status" not in data:
        return jsonify({
            "error": "status is required"
        }), 400

    if data["status"] not in VALID_STATUSES:
        return jsonify({
            "error": "Invalid status"
        }), 400

    courses = read_courses()
    course = find_course(courses, course_id)

    if course is None:
        return jsonify({"error": "Course not found"}), 404

    course["status"] = data["status"]
    write_courses(courses)

    return jsonify(course)


@app.delete("/api/courses/<int:course_id>")
def delete_course(course_id):
    courses = read_courses()
    course = find_course(courses, course_id)

    if course is None:
        return jsonify({"error": "Course not found"}), 404

    courses.remove(course)
    write_courses(courses)

    return "", 204


if __name__ == "__main__":
    print("CodeCraftHub API is starting...")
    print(f"Data will be stored in: {DATA_FILE}")
    print("API will be available at: http://localhost:5000")
    app.run(debug=True)
