# API base URL
BASE_URL = "http://127.0.0.1:8888/api/private/v1"

# Excel test-case file
EXCEL_FILE = "./data/测试用例示例.xlsx"
SHEET_NAME = "Sheet1"

# MySQL connection (replace with local test values)
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_NAME = "your_test_database"
DB_USER = "your_test_user"
DB_PASSWORD = "your_test_password"

# Cleanup SQL: limit these statements to data created by the test suite.
SQL1 = 'delete from your_table where test_marker = "your_marker_1"'
SQL2 = 'delete from your_table where test_marker = "your_marker_2"'
SQL3 = 'delete from your_table where test_marker = "your_marker_3"'
