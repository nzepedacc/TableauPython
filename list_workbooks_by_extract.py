# Tableau QA - Workbook Validation by Extract

Tool to identify all workbooks that use a specific extract/datasource in Tableau Cloud or Tableau Server. Useful when a change to an extract affects filters or other elements in workbooks.

## Requirements

- Python 3.8+
- Tableau Cloud (or Tableau Server) account with read permissions

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

### Option 1: Personal Access Token (recommended for Tableau Cloud)

1. In Tableau Cloud: **Settings** → **Personal Access Tokens** → **Create token**
2. Store the token name and value securely

### Option 2: Username and password

Use your Tableau Cloud/Server credentials.

### Option 3: Environment variables

Create a `.env` file or configure in your system:

```
TABLEAU_SERVER=https://your-domain.online.tableau.com
TABLEAU_SITE_ID=site-name
TABLEAU_TOKEN_NAME=my-token
TABLEAU_TOKEN_VALUE=token-value
```

Or with username/password:

```
TABLEAU_SERVER=https://your-domain.online.tableau.com
TABLEAU_SITE_ID=site-name
TABLEAU_USER=your-username
TABLEAU_PASSWORD=your-password
```

## Usage

### 1. List all available datasources

To find the name or ID of the extract you need:

```bash
python list_workbooks_by_extract.py --list-datasources --server https://xxx.online.tableau.com --site "your-site" --token-name TOKEN --token-value "value"
```

Export to CSV:

```bash
python list_workbooks_by_extract.py --list-datasources -o datasources.csv --server ... --token-name ... --token-value ...
```

### 2. Find workbooks that use a specific extract

By datasource name (exact match):

```bash
python list_workbooks_by_extract.py --datasource "Extract Name" --server https://xxx.online.tableau.com --site "your-site" --token-name TOKEN --token-value "value"
```

By exact datasource ID:

```bash
python list_workbooks_by_extract.py --datasource-id "abc-123-def" --server ... --token-name ... --token-value ...
```

### 3. Export results to CSV

```bash
python list_workbooks_by_extract.py -d "My Extract" -o workbooks_affected.csv --server ... --token-name ... --token-value ...
```

### Full example with environment variables

```bash
set TABLEAU_SERVER=https://mycompany.online.tableau.com
set TABLEAU_SITE_ID=sales
set TABLEAU_TOKEN_NAME=qa-script
set TABLEAU_TOKEN_VALUE=xxxxx

python list_workbooks_by_extract.py --datasource "Sales_Extract_2024" -o report.csv
```

## Output

The script shows:

- **Console**: List of workbooks with name, ID, and associated datasource
- **CSV** (if using `-o`): workbook_id, workbook_name, project_id, datasource_id, datasource_name, connection_type, filter_validation, filter_suspect_fields

## Notes

- The **Site ID** in Tableau Cloud is the part after `/site/` in the URL (e.g. if the URL is `.../#/site/sales/projects`, the site is `sales`).
- If using password instead of token, avoid leaving credentials in command history.
- Workbooks with **embedded** datasources are identified by the internal datasource name.
- Name search uses exact match when configured; the script can also fall back to partial match when exactly one datasource matches.
