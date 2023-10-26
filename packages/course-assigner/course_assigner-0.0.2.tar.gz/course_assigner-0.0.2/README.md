course_assigner
========

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

course_assigner is a Python library for assigning students to courses based on a preference list. The documentation below should help you understand the parameters passed to the course_assigner functions and what they return, but I recommend starting with examples. Check out the examples in the [samples folder](/samples)

Installation instructions
-------------------------

    python3 -m pip install --upgrade pip
	python3 -m pip install course_assigner

## Classes
The course_assigner library has one method:
   - `assign`: assigns 

# assign

*import course_assigner.assign*

```python
	from course_assigner import assign
```

*request syntax*

```python

    assigned_courses = assign(
        courses = {
            course1: {
                "min": course 1 min,
                "max": course 1 max
            },
            course2: {
                "min": course 2 min,
                "max": course 2 max
            },
            ...
            courseN: {
                "min": course N min,
                "max": course N max
            }
        },
        preferences = {
            student_key1: [
                student 1 most wanted course,
                student 1 second most wanted course,
                ...
                student 1 least wanted course
            ],
            student_key2: [
                student 2 most wanted course,
                student 2 second most wanted course,
                ...
                student 2 least wanted course                
            ],
            ...
            student_keyN: [
                student N most wanted course,
                student N second most wanted course,
                ...
                student N least wanted course                
            ],
        }
    )

```

*parameters*
   - `courses` *(dict)*: A dictionary which shows all of the courses which the student can sign up for. The key in each pair is the name of the course. The value has an additional dictionairy with keys "min" and "max". The value for key "min" is the minimum number of people that can sign up for the course, and the value for key "max" is the maximum number of people that can sign up for the course. If there are no minimums or maximums, the value of "min" should be 0 and the value of "max" should be the total number of students.
   - `preferences` *(dict)*: A dictionary value which lists the preferences for each student. The key in each pair is the name or identifier for the student. The value is a list of student preferences in which the entry at index 0 is the most preferred course and the entry at index n-1 (for a list of length n) is the least preferred course.

*response syntax*

```python

    {
        "student_key1":student 1 assigned course,
        "student_key2":student 2 assigned course,
        ...
        "student_keyN":student N assigned course
    }

```