# rr-qa-automation-assignment
Rapyuta Robotics QA - Automation Assignment

Test Strategy:
- Scope: Validate filtering, pagination, and API responses on tmdb-discover.surge.sh.
  
Approach:
- UI automation with Selenium + Pytest
- API validation with Requests
- Data‑driven testing using JSON
- Reporting via pytest-html
- Logging for traceability
  
Test Design Techniques:
- Equivalence partitioning (valid/invalid filters)
- Boundary value analysis (ratings, years)
- Negative testing (known issues like broken slugs, last-page pagination)
- Data-Driven Testing: JSON file () for parameterized runs.

Patterns & Practices
- Page Object Model (POM) for UI selectors (scalable design)
- Pytest Fixtures for browser setup/teardown (conftest.py)
- Parametrization for data-driven tests
- Reusable Utilities for API calls and assertions

Known Defects:
- Slug Access: Direct navigation to /popular may fail.
- Pagination: Last few pages may not load results.



Test Cases:

1. Filtering by Category

- Precondition: User is on home page.
  
Steps:
- Click on category tab (Popular/Trending/Newest/Top Rated).
  
Expected Result: check output data a.c.to category diplayed or not.

2. Filtering by Type (Movies/TV Shows)
   
Steps:
- Select "Movies".
- Verify only movie results are shown.
- Switch to "TV Shows".

Expected Result: output must be only movies.

3. Filtering by Year of Release

Steps:
- Enter year (e.g., 2020).
- Apply filter.

Expected Result: All results should have release year = 2020.

4. Filtering by Rating

Steps:
- Enter rating threshold (e.g., ≥3).
- Apply filter.

Expected Result: All results should have rating ≥ 3.

5. Filtering by Genre

Steps:
- Select genre.

Expected Result: All results belong to selected genre.

6. Combined Filters (Data‑Driven)

Steps:
- Apply multiple filters (Category + Type + Year + Rating + Genre).

Expected Result: Results satisfy all applied filters.

7. Pagination – Next Page

Steps:
- Click "Next".
- Verify results update.

Expected Result: New set of results displayed.

8. Pagination – Last Page (Negative)

Steps:
- Navigate to last page.

Expected Result: Known issue may occur; log defect if results fail to load.

9. Direct Slug Access (Negative)

Steps:
- Open URL https://tmdb-discover.surge.sh/popular.

Expected Result: Page may not load correctly; log defect.

10. API Validation – Popular Movies

Steps:
- Call TMDB API endpoint for popular movies.
- Validate response schema (status 200, JSON keys, No error msg in data).

Expected Result: Response contains results array with valid movie objects.

Reporting & Logging
- Reports: pytest-html generates report.html.
- Logs: Python logging captures steps, failures, and API calls.

CI/CD with Jenkins:

1. Jenkins Setup
- Install Jenkins (on server or container).
- Install Plugins
- Pipeline (Declarative/Scripted)
- HTML Publisher (to publish pytest-html reports)
- Git (for repo checkout)

2. Jenkins High Level Pipeline Flow:
- Checkout Code from GitHub repo (rr-qa-automation-assignment).
- Install Dependencies (pip install -r requirements.txt).
- Run Tests with Pytest:
  - Console output
  - Generate HTML report (pytest --html=report.html --self-contained-html)
- Archive Artifacts (HTML report, logs).
- Publish Report in Jenkins UI.





