# API Automation Testing Framework

A data-driven API automation testing framework built with **Python, pytest, Excel, requests, MySQL, and Allure**.

## Features

- Read and execute API test cases from Excel
- Render variables with Jinja2 and reuse extracted values across test cases
- Support HTTP headers, query parameters, form data, JSON payloads, and file uploads
- Assert HTTP responses with JSONPath or response text
- Assert and extract data from MySQL
- Generate Allure test reports
- Clean up test data after the test session

## Project Structure

```text
.
├── config/
│   ├── config.py          # Local configuration; keep it private
│   └── config.example.py  # Safe configuration template
├── data/
│   └── 测试用例示例.xlsx   # Sample Excel test cases
├── file/
│   └── 1.jpg              # Sample upload file
├── testcases/
│   └── test_runner.py     # Parameterized test runner
├── utils/
│   ├── analyse_case.py    # Build request data from a case
│   ├── asserts.py         # HTTP and database assertions
│   ├── extractor.py       # JSON and database extraction
│   ├── excel_utils.py     # Excel reader
│   ├── send_request.py    # HTTP and MySQL clients
│   └── allure_utils.py    # Allure metadata
├── conftest.py            # pytest fixtures and cleanup
├── pytest.ini             # pytest logging configuration
├── requirements.txt       # Python dependencies
└── run.py                 # Test and report entry point
```

## Requirements

- Python 3.10 or later
- A reachable API service under test
- MySQL, when database assertions, extraction, or cleanup are used
- Allure Commandline, when generating an HTML report

## Installation

```bash
git clone <your-repository-url>
cd <your-repository-directory>
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install Allure Commandline if needed:

```bash
# npm
npm install -g allure-commandline

# macOS Homebrew
brew install allure
```

## Configuration

Copy the template and update it for your environment:

```bash
# Windows
copy config\config.example.py config\config.py

# Linux/macOS
cp config/config.example.py config/config.py
```

Configure the following values in `config/config.py`:

- `BASE_URL`: API base URL
- `EXCEL_FILE`: Excel test-case file path
- `SHEET_NAME`: worksheet name
- `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`: MySQL connection settings
- `SQL1`, `SQL2`, `SQL3`: cleanup statements for test data

**Never commit `config/config.py` to a public repository.** It may contain credentials and internal service addresses. Keep only placeholders in `config/config.example.py`.

The second row of the Excel sheet contains field names. Test data starts from the third row, and a case runs only when `is_true` is truthy.

## Running Tests

Run pytest directly:

```bash
pytest -vs testcases/test_runner.py
```

Run tests and generate an Allure HTML report:

```bash
python run.py
```

The generated report is written to `report/html_report`. Open its `index.html`, or serve the report with:

```bash
allure serve report/json_report
```

## Excel Case Fields

| Field | Description |
| --- | --- |
| `id`, `feature`, `story`, `title` | Case identity and Allure metadata |
| `method`, `path` | HTTP method and relative path |
| `headers`, `params`, `data`, `json`, `files` | Request values represented as Python-literal strings |
| `check`, `expected` | JSONPath assertion path and expected value |
| `sql_check`, `sql_expected` | Database assertion SQL and expected value |
| `jsonExData`, `sqlExData` | Extraction expressions for later cases |
| `is_true` | Whether the case should run |

## Security and Data Safety

- The framework evaluates request and extraction expressions with `eval()`. Run only trusted Excel files.
- The cleanup fixture runs after the test session. Verify that its SQL targets test data only.
- Check the sample workbook and upload files for real tokens, credentials, personal information, or proprietary data before publishing.
- Add an open-source license, such as MIT, before distributing the project publicly.

---

# API 接口自动化测试框架

这是一个基于 **Python、pytest、Excel、requests、MySQL 和 Allure** 的数据驱动接口自动化测试框架。

## 功能特性

- 从 Excel 批量读取并执行接口测试用例
- 使用 Jinja2 渲染变量，支持跨用例复用提取数据
- 支持请求头、查询参数、表单、JSON 请求体和文件上传
- 支持使用 JSONPath 或响应文本进行 HTTP 响应断言
- 支持 MySQL 数据库断言和数据提取
- 生成 Allure 测试报告
- 测试会话结束后清理测试数据

## 项目结构

```text
.
├── config/
│   ├── config.py          # 本地配置；请勿公开提交
│   └── config.example.py  # 安全的配置模板
├── data/
│   └── 测试用例示例.xlsx   # Excel 测试用例示例
├── file/
│   └── 1.jpg              # 文件上传示例
├── testcases/
│   └── test_runner.py     # 参数化测试入口
├── utils/
│   ├── analyse_case.py    # 根据用例构造请求数据
│   ├── asserts.py         # HTTP 和数据库断言
│   ├── extractor.py       # JSON 和数据库数据提取
│   ├── excel_utils.py     # Excel 读取
│   ├── send_request.py    # HTTP 和 MySQL 客户端
│   └── allure_utils.py    # Allure 元数据
├── conftest.py            # pytest fixture 和清理逻辑
├── pytest.ini             # pytest 日志配置
├── requirements.txt       # Python 依赖
└── run.py                 # 测试和报告入口
```

## 环境要求

- Python 3.10 或更高版本
- 可以访问的被测 API 服务
- 使用数据库断言、提取或清理功能时需要 MySQL
- 生成 HTML 报告时需要 Allure Commandline

## 安装

```bash
git clone <your-repository-url>
cd <your-repository-directory>
python -m venv .venv
```

激活虚拟环境：

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Linux/macOS
source .venv/bin/activate
```

安装 Python 依赖：

```bash
pip install -r requirements.txt
```

如需生成 Allure 报告，请安装 Allure Commandline：

```bash
# npm
npm install -g allure-commandline

# macOS Homebrew
brew install allure
```

## 配置

复制配置模板，并根据实际环境修改：

```bash
# Windows
copy config\config.example.py config\config.py

# Linux/macOS
cp config/config.example.py config/config.py
```

在 `config/config.py` 中配置：

- `BASE_URL`：接口基础地址
- `EXCEL_FILE`：Excel 测试用例文件路径
- `SHEET_NAME`：工作表名称
- `DB_HOST`、`DB_PORT`、`DB_NAME`、`DB_USER`、`DB_PASSWORD`：MySQL 连接信息
- `SQL1`、`SQL2`、`SQL3`：测试数据清理 SQL

**不要将 `config/config.py` 提交到公开仓库。**其中可能包含数据库密码和内部服务地址；`config.example.py` 中只应保留占位值。

Excel 工作表第二行是字段名，第三行开始是测试数据；只有 `is_true` 为真时才会执行该用例。

## 运行测试

直接使用 pytest：

```bash
pytest -vs testcases/test_runner.py
```

运行测试并生成 Allure HTML 报告：

```bash
python run.py
```

报告生成在 `report/html_report`，打开其中的 `index.html` 即可；也可以使用以下命令查看：

```bash
allure serve report/json_report
```

## Excel 用例字段

| 字段 | 说明 |
| --- | --- |
| `id`、`feature`、`story`、`title` | 用例标识和 Allure 元数据 |
| `method`、`path` | HTTP 方法和相对路径 |
| `headers`、`params`、`data`、`json`、`files` | 使用 Python 字面量字符串表示的请求数据 |
| `check`、`expected` | JSONPath 断言路径和期望值 |
| `sql_check`、`sql_expected` | 数据库断言 SQL 和期望值 |
| `jsonExData`、`sqlExData` | 提供给后续用例使用的提取表达式 |
| `is_true` | 是否执行该用例 |

## 安全和数据注意事项

- 框架使用 `eval()` 解析请求和提取表达式，只运行可信的 Excel 文件。
- 清理 fixture 会在测试会话结束时执行，请确认 SQL 只操作测试数据。
- 发布前请检查示例 Excel 和上传文件，确认不含真实 token、密码、个人信息或公司业务数据。
- 公开发布前请补充 MIT 等合适的开源许可证。
