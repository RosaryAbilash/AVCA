# Weak Cryptography Policy

Developers must not use deprecated cryptographic algorithms (MD5, SHA1, DES) for hashing or encryption.

Approved controls:
- AES-256-GCM for symmetric encryption
- PBKDF2, Argon2, or bcrypt for password hashing
- SecureRandom for random number generation

Severity: High
CWE: CWE-327

Remediation:
Upgrade the cryptographic implementation to use a modern, industry-standard algorithm and ensure sufficient key lengths.
