# Insecure Deserialization Policy

Developers must not deserialize untrusted data using native serialization mechanisms.

Approved controls:
- Use safe data formats (JSON/XML) with secure parsers (Jackson/Gson)
- Look-ahead ObjectInputStream with strict class allow-lists
- HMAC signatures on serialized objects

Severity: Critical
CWE: CWE-502

Remediation:
Replace native Java serialization with a secure, strongly-typed JSON library like Jackson with default typing disabled.
