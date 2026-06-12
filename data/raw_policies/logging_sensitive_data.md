# Sensitive Data Logging Policy

Developers must ensure that Personally Identifiable Information (PII), credentials, and financial data are never written to application logs.

Approved controls:
- Data masking and redaction filters in the logging framework (e.g., Logback/Log4j)
- Overriding toString() on sensitive domain objects
- Tokenization

Severity: Medium
CWE: CWE-532

Remediation:
Implement a regex-based redaction filter in the logger configuration or mask the specific variable before logging.
