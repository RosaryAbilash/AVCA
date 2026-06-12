# Cross-Site Scripting (XSS) Prevention Policy

Developers must never reflect untrusted user input to the browser without contextual output encoding.

Approved controls:
- Context-Aware Output Encoding (e.g., OWASP Java Encoder)
- Modern Frontend Frameworks (React/Angular auto-escaping)
- Strict Content Security Policy (CSP)

Severity: High
CWE: CWE-79

Remediation:
Wrap the user input in a secure encoder before rendering it to the DOM or HTTP response.
