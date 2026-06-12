# Path Traversal Prevention Policy

Developers must prevent user input from controlling file system paths to avoid unauthorized file access.

Approved controls:
- Allow-lists for filenames
- Safe Path APIs (e.g., java.nio.file.Paths)
- Stripping directory traversal characters (../)

Severity: High
CWE: CWE-22

Remediation:
Validate the input against a strict allow-list and ensure the resolved absolute path resides within the expected base directory.
