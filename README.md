Pytest Automation Framework – Project Documentation
 
1. Project Overview
This project is a Python-based automation testing framework built with pytest, designed to demonstrate automated testing of:
Unit-level logic (Calculator module)
Library management functionality (LibraryAccount module)
Transactions module (adding funds, fees, etc.)
Integration tests (Library + Transaction workflows)
REST API testing (GET, POST, PUT, PATCH, DELETE, error handling)
The framework includes smoke, regression, and negative tests to cover multiple scenarios and edge cases.

2. Objectives
Automate repetitive testing tasks to ensure faster and reliable validation.
Create a scalable framework that can integrate multiple modules and APIs.
Cover all key testing types:
Unit testing
Integration testing
API testing
Use best practices of pytest, including:
Fixtures
Markers (smoke, regression, Integration, StandAlone)
Parametrization
Configuration (pytest.ini)
PageUp-style modeling of modular test design

3. Tools and Frameworks Used
Tool / Library
Purpose
Python 3.11+
Programming language for tests and modules
pytest
Testing framework used for unit, integration, and API tests
pytest-html
Generate HTML test reports
requests
Library to send HTTP requests for API testing
PyCharm
IDE used for development and running tests


4. Project Structure
PyTest_Framework_Demo/
├── src/
│   ├── calculator.py
│   ├── library.py
│   └── transactions.py
│   └── user.py
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   ├── test_calculator.py
│   ├── test_library.py
│   ├── test_transaction.py
│   └── test_user.py
├── pytest.ini
Explanation:
src/ – Contains the core modules (Calculator, Library, Transactions).
tests/ – Contains test files categorized by module or API.
pytest.ini – Central pytest configuration, including markers and default options.
conftest.py – Contains fixtures shared across multiple tests 

5. Fixtures
calc – Returns a Calculator instance for arithmetic tests.
sample_user – Returns a User instance with default balance and a LibraryAccount.
sample_book – Returns a Book instance for library tests.
get_book_by_title – Helper to fetch a borrowed book from a LibraryAccount by title.
get_book_by_title_and_author – Helper to fetch a borrowed book from a LibraryAccount by title and author.
library_users – Returns a list of LibraryAccount instances:
Alice (already borrowed "Python 101")
Bob (starts with no books)
base_url – Base URL for all API tests.
specific_post_endpoint – Returns the endpoint for a specific post (or all posts if no ID provided).
multiple_posts_endpoint – Returns the endpoint for fetching multiple posts.
post_payload – Sample payload for POST requests.
put_payload – Sample payload for PUT requests.
patch_payload – Sample payload for PATCH requests.
get_request / post_request / put_request / patch_request / delete_request – Wrappers around requests methods for reusable HTTP actions.
assert_status_code – Helper to assert the expected HTTP status code.
assert_post_fields – Helper to assert that a single API post contains the required fields (id, userId, title, body).
assert_post_list_fields – Helper to assert that a list of posts contains the required fields, validating multiple entries.
assert_payload_matches – Helper to assert that a payload matches the API response, with optional keys to exclude.
Benefits:
Reduces code duplication
Provides modular and reusable objects
Supports PageUp modeling by providing a single source of truth for test data

6. Test Design and Coverage
6.1 Calculator Module
Operations tested: add, subtract, multiply, divide
Test types:
Smoke → basic operations
Regression → parameterized tests with positive and negative numbers, edge cases
Exception handling → division by zero
Parametrization: @pytest.mark.parametrize used to run tests with multiple input combinations.
6.2 Library Module
Functionality tested: Borrowing and returning books
Key scenarios:
Borrowing new books (success)
Borrowing already borrowed books (failure)
Returning borrowed books (success)
Returning non-borrowed books (failure)
Handling empty book titles (expected failure)
Markers:
Smoke → critical paths (borrow, return)
Regression → edge cases, multiple users, parametrized tests
6.3 Transactions Module
Functionality tested: Adding funds, charging late fees
Test types:
Positive scenarios → adding valid amounts, charging fees within balance
Negative scenarios → negative amounts, charging fees exceeding balance
Parametrization: Multiple scenarios tested using @pytest.mark.parametrize

6.4 User Module
Functionality tested: Managing user balance through funds and fee operations


Key scenarios:


Adding funds (positive, zero, negative, multiple adds)


Paying fees (within balance, exact balance, insufficient balance, multiple payments)


Markers:


Smoke → critical paths (adding valid funds, paying valid fee)


Regression → edge cases and negative scenarios (invalid amounts, insufficient balance, zero deposits, multiple adds/fees)

6.5 API Testing
Endpoints tested:
GET /posts/{id} → single post
GET /posts → multiple posts
POST /posts → create new post
PUT /posts/{id} → update post
PATCH /posts/{id} → partial update
DELETE /posts/{id} → delete post
Error scenarios tested:
Invalid post ID → 404
Invalid endpoint → 404
Assertions:
Status codes
JSON keys (id, title, body) and values
Data types and content

7. Best Practices Followed
PageUp Modeling
Tests are modular, reusable, and organized by functional areas.
Fixtures provide shared objects to minimize duplication.
Markers and Parametrization
Smoke vs regression separation allows selective test execution.
Parametrized tests cover multiple inputs and edge cases.
Error Handling and Negative Tests
Explicit tests for expected failures (pytest.raises, xfail)
Validates API responses with invalid data
Readability and Maintainability
Clear test function names
Inline comments describing test purpose
Separate configuration in pytest.ini
API Testing with JSON Handling
requests library for HTTP methods
.json() used to parse responses
Verified response structure and data types

8. pytest.ini Configuration
[pytest]
markers =
	smoke: Quick critical tests
	regression: Full feature coverage
	integration: Integration transaction tests
    	standAlone: Standalone transaction tests
addopts = -v --html=reports/report.html
addopts → verbosity and HTML report
markers → categorize tests for selective execution

9. Execution Commands
Run all tests:
pytest
Run smoke tests only:
pytest -m smoke
Run regression tests only:
pytest -m regression
Run integration transaction tests only:
pytest -m integration
Run standalone transaction tests only:
pytest -m standalone
Generate HTML report:
pytest --html=reports/report.html

10. Conclusion
This framework provides:
Full automation coverage for unit, integration, and API tests
Reusability and maintainability through fixtures and PageUp design
Scalability — additional modules or APIs can be added easily
Professional best practices — markers, parametrization, JSON validation, error handling, reports
It can serve as a foundation for a real-world automation framework for Python projects.
 

