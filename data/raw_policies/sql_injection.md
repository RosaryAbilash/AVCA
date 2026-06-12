# SQL Injection Prevention Policy

Developers must never concatenate user input into SQL queries.

Approved controls:

- PreparedStatement
- Parameterized Queries
- ORM Parameter Binding

Severity: Critical

CWE: CWE-89

Remediation:

Use PreparedStatement and bind variables.