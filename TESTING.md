## How to Test

### Setup
```bash
git clone https://github.com/fchanane04/document-extractor.git
cd document-extractor
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### Sample Files
Add your own test files to the `sample_files/` folder:
```
sample_files/
├── customers.csv    ← CSV with customer data
├── customers.xlsx   ← Excel with customer data
└── invoice.pdf      ← PDF invoice or report
```
> `sample_files/` is not pushed to GitHub — you need to add your own files.


### Run
```bash
# CSV
python main.py --file sample_files/customers.csv

# Excel
python main.py --file sample_files/customers.xlsx

# PDF
python main.py --file sample_files/invoice.pdf

# Save output
python main.py --file sample_files/customers.csv --output result.json

# Switch provider (currently only working with Groq)
python main.py --file sample_files/invoice.pdf --provider groq
```

### Expected Data Format

Your files should contain customer data with these columns
(column names are flexible — the tool auto-detects them):

| Field | Expected Column Names |
|---|---|
| Company Name | company_name, company, business, name |
| Email | email, email_address, billing_email |
| Country | country, country_code, location |
| Industry | industry, sector, business_type |
| Status | status, account_status, state |
| Join Date | joined_at, created_at, start_date |

### Output Example
```json
[
  {
    "company_name": "TechCorp Inc",
    "email": "billing@techcorp.com",
    "country": "US",
    "industry": "SaaS",
    "status": "active",
    "joined_at": "2024-01-15"
  }
]
```

### Requirements
- Python 3.10+
- Groq API key (free at console.groq.com)