# Command Injection Prevention Policy

Developers must never pass untrusted input directly to operating system shells.

Approved controls:
- java.lang.ProcessBuilder
- Avoid Runtime.exec()
- Strict input validation and sanitization

Severity: Critical
CWE: CWE-78

Remediation:
Use ProcessBuilder and pass arguments as a secure array of strings rather than concatenating them into a single command string.
