# agents/auditor_agent.py


import json
import re
import uuid
from pathlib import Path
from typing import Dict, Any

import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from core.vllm_client import VLLMClient
from core.vector_store import PolicyVectorStore


class AuditorAgent:

    def __init__(self):

        self.llm = VLLMClient()
        self.vector_store = PolicyVectorStore()

    # =====================================================
    # Retrieve Relevant Policies
    # =====================================================

    def retrieve_policies(
        self,
        source_code: str,
        top_k: int = 5
    ) -> str:

        try:

            results = self.vector_store.search(
                query=source_code,
                k=top_k
            )

            return "\n\n".join(results)

        except Exception as ex:

            print(
                f"[AuditorAgent] Policy Retrieval Error: {ex}"
            )

            return "No relevant policies found."

    # =====================================================
    # Main Audit Function
    # =====================================================

    def analyze_code(
        self,
        source_code: str,
        file_name: str = "Unknown.java"
    ) -> Dict[str, Any]:

        policies = self.retrieve_policies(
            source_code
        )

        system_prompt = """
You are AVCA Security Auditor.

You are a Senior Application Security Engineer.

Your task is to audit Java source code against
enterprise security policies.

IMPORTANT RULES

1. Report ONLY vulnerabilities directly supported
   by evidence in the source code.

2. Never speculate.

3. Never infer vulnerabilities that are not present.

4. Every finding MUST contain evidence.

5. If evidence does not exist,
   do NOT report the vulnerability.

6. Focus on:

   - SQL Injection
   - Hardcoded Secrets
   - XSS
   - Command Injection
   - Path Traversal
   - Insecure Deserialization
   - Weak Cryptography
   - Sensitive Logging

OUTPUT REQUIREMENTS

Return ONLY valid JSON.

DO NOT return markdown.

DO NOT wrap JSON in ```json blocks.

DO NOT explain your answer.

The first character MUST be {

The last character MUST be }

Required Schema:

{
  "file_name": "",
  "overall_risk": "",
  "compliance_score": 0,
  "total_findings": 0,
  "executive_summary": "",
  "findings": [
    {
      "id": "",
      "title": "",
      "severity": "",
      "cwe": "",
      "evidence": "",
      "description": "",
      "impact": "",
      "affected_component": "",
      "remediation_summary": ""
    }
  ]
}
"""

        user_prompt = f"""
Enterprise Policies

{policies}

================================================

File Name

{file_name}

================================================

Java Source Code

{source_code}

================================================

Perform a security audit.
"""

        response = self.llm.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=0.1,
            max_tokens=1024
        )

        result = self._safe_json_parse(
            response=response,
            file_name=file_name
        )

        return result

    # =====================================================
    # JSON Parsing
    # =====================================================

    def _safe_json_parse(
        self,
        response: str,
        file_name: str
    ) -> Dict[str, Any]:

        try:

            cleaned = response.strip()

            cleaned = re.sub(
                r"^```json\s*",
                "",
                cleaned,
                flags=re.IGNORECASE
            )

            cleaned = re.sub(
                r"^```",
                "",
                cleaned
            )

            cleaned = re.sub(
                r"```$",
                "",
                cleaned
            )

            cleaned = cleaned.strip()

            try:
                return json.loads(cleaned)

            except Exception:

                json_match = re.search(
                    r"\{.*\}",
                    cleaned,
                    re.DOTALL
                )

                if json_match:

                    extracted = json_match.group(0)

                    return json.loads(
                        extracted
                    )

                raise ValueError(
                    "No valid JSON found."
                )

        except Exception:

            return {
                "file_name": file_name,
                "overall_risk": "Unknown",
                "compliance_score": 0,
                "total_findings": 1,
                "executive_summary":
                    "Model output parsing failed.",
                "findings": [
                    {
                        "id": str(
                            uuid.uuid4()
                        ),
                        "title":
                            "LLM Parsing Failure",
                        "severity":
                            "Medium",
                        "cwe":
                            "N/A",
                        "evidence":
                            "",
                        "description":
                            response,
                        "impact":
                            "Unable to parse model output.",
                        "affected_component":
                            file_name,
                        "remediation_summary":
                            "Review model response."
                    }
                ]
            }

    # =====================================================
    # Markdown Report
    # =====================================================

    def report_to_markdown(
        self,
        audit_report: Dict[str, Any]
    ) -> str:

        lines = []

        lines.append(
            "# Security Audit Report"
        )

        lines.append("")

        lines.append(
            f"**Risk Level:** "
            f"{audit_report.get('overall_risk')}"
        )

        lines.append(
            f"**Compliance Score:** "
            f"{audit_report.get('compliance_score')}"
        )

        lines.append(
            f"**Total Findings:** "
            f"{audit_report.get('total_findings')}"
        )

        lines.append("")

        lines.append("---")

        findings = audit_report.get(
            "findings",
            []
        )

        for finding in findings:

            lines.append("")
            lines.append(
                f"## {finding.get('title')}"
            )

            lines.append(
                f"- Severity: "
                f"{finding.get('severity')}"
            )

            lines.append(
                f"- CWE: "
                f"{finding.get('cwe')}"
            )

            lines.append(
                f"- Evidence: "
                f"{finding.get('evidence')}"
            )

            lines.append(
                f"- Impact: "
                f"{finding.get('impact')}"
            )

            lines.append(
                f"- Component: "
                f"{finding.get('affected_component')}"
            )

            lines.append(
                f"- Description: "
                f"{finding.get('description')}"
            )

            lines.append(
                f"- Remediation: "
                f"{finding.get('remediation_summary')}"
            )

        return "\n".join(lines)


# =========================================================
# Local Test
# =========================================================

if __name__ == "__main__":

    sample_code = '''
import java.sql.*;

public class LoginDAO {

    public void login(String username)
    throws Exception {

        String query =
        "SELECT * FROM users WHERE name='"
        + username +
        "'";

        Statement stmt =
        conn.createStatement();

        ResultSet rs =
        stmt.executeQuery(query);
    }
}
'''

    agent = AuditorAgent()

    result = agent.analyze_code(
        source_code=sample_code,
        file_name="LoginDAO.java"
    )

    print(
        json.dumps(
            result,
            indent=2
        )
    )

    print("\n")
    print("=" * 80)
    print("\n")

    print(
        agent.report_to_markdown(
            result
        )
    )

