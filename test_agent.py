from agents.extraction_agent import run_agent

print("Testing: agent extracting from csv")
result = run_agent("Extract customers from sample_files/customers.csv")
print(result)

print("\nTesting: agent extracting from pdf")
result = run_agent("Extract customers from sample_files/invoice.pdf")
print(result)