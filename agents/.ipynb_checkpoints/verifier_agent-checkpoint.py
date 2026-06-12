# agents/verifier_agent.py

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


class VerifierAgent:

    def __init__(self):

        self.llm = VLLMClient()
        self.vector_store = PolicyVectorStore()

    # =====================================================
    # Policy Retrieval
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
                f"[VerifierAgent] Policy Retrieval Error: {ex}"
            )

            return "No relevant policies found."

    # =====================================================
    # Verify Remediation
    # =====================================================

    def verify(
        self,
        original_code: str,
        fixed_code: str,
        audit_report: Dict[str, Any],
        remediation_report: Dict[str, Any],
        file_name: str
    ) -> Dict[str, Any]:

        policies = self.retrieve_policies(
            fixed_code
        )

        system_prompt = """
You are AVCA Verification Agent.

You are a Senior Application Security Reviewer.

Your job is to verify whether the remediated code
actually resolves the vulnerabilities identified
during the audit phase.

IMPORTANT RULES

1. Verify only findings present in the audit report.

2. Compare:
   - Original Code
   - Audit Findings
   - Remediated Code

3. Determine whether each finding is:

   RESOLVED
   PARTIALLY_RESOLVED
   NOT_RESOLVED

4. Do NOT invent vulnerabilities.

5. Do NOT speculate.

6. Use evidence from the code.

OUTPUT RULES

Return ONLY valid JSON.

Do NOT use markdown.

Do NOT wrap JSON in code blocks.

The first character must be {

The last character must be }

Required Schema:

{
  "file_name": "",
  "verification_status": "",
  "compliance_score": 0,
  "resolved_count": 0,
  "remaining_count": 0,
  "resolved_findings": [],
  "remaining_findings": [],
  "security_summary": "",
  "deployment_recommendation": ""
}

verification_status values:

PASS
PASS_WITH_WARNINGS
FAIL
"""

        user_prompt = f"""
Enterprise Policies

{policies}

================================================

Audit Report

{json.dumps(audit_report, indent=2)}

================================================

Remediation Report

{json.dumps(remediation_report, indent=2)}

================================================

Original Code

{original_code}

================================================

Remediated Code

{fixed_code}

================================================

Perform security verification.
"""

        response = self.llm.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=0.1,
            max_tokens=1024
        )

        return self._safe_json_parse(
            response=response,
            file_name=file_name,
            audit_report=audit_report
        )

    # =====================================================
    # Safe JSON Parse
    # =====================================================

    def _safe_json_parse(
        self,
        response: str,
        file_name: str,
        audit_report: Dict[str, Any]
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

                return json.loads(
                    cleaned
                )

            except Exception:

                match = re.search(
                    r"\{.*\}",
                    cleaned,
                    re.DOTALL
                )

                if match:

                    return json.loads(
                        match.group(0)
                    )

                raise ValueError()

        except Exception:

            total_findings = audit_report.get(
                "total_findings",
                0
            )

            return {
                "file_name": file_name,
                "verification_status": "FAIL",
                "compliance_score": 0,
                "resolved_count": 0,
                "remaining_count": total_findings,
                "resolved_findings": [],
                "remaining_findings": [
                    {
                        "title":
                            "Verification Parsing Failure"
                    }
                ],
                "security_summary":
                    "Unable to verify remediation output.",
                "deployment_recommendation":
                    "Manual security review required."
            }

    # =====================================================
    # Dashboard Metrics
    # =====================================================

    def build_dashboard_metrics(
        self,
        verification_report: Dict[str, Any]
    ) -> Dict[str, Any]:

        resolved = verification_report.get(
            "resolved_count",
            0
        )

        remaining = verification_report.get(
            "remaining_count",
            0
        )

        total = resolved + remaining

        success_rate = 0

        if total > 0:

            success_rate = round(
                (resolved / total) * 100,
                2
            )

        return {
            "verification_status":
                verification_report.get(
                    "verification_status"
                ),
            "compliance_score":
                verification_report.get(
                    "compliance_score",
                    0
                ),
            "resolved_findings":
                resolved,
            "remaining_findings":
                remaining,
            "success_rate":
                success_rate
        }

    # =====================================================
    # Markdown Report
    # =====================================================

    def report_to_markdown(
        self,
        report: Dict[str, Any]
    ) -> str:

        lines = []

        lines.append(
            "# Verification Report"
        )

        lines.append("")

        lines.append(
            f"**Verification Status:** "
            f"{report.get('verification_status')}"
        )

        lines.append(
            f"**Compliance Score:** "
            f"{report.get('compliance_score')}"
        )

        lines.append(
            f"**Resolved Findings:** "
            f"{report.get('resolved_count')}"
        )

        lines.append(
            f"**Remaining Findings:** "
            f"{report.get('remaining_count')}"
        )

        lines.append("")
        lines.append("---")
        lines.append("")

        lines.append(
            report.get(
                "security_summary",
                ""
            )
        )

        lines.append("")
        lines.append("## Deployment Recommendation")
        lines.append("")

        lines.append(
            report.get(
                "deployment_recommendation",
                ""
            )
        )

        return "\n".join(lines)


# =========================================================
# Local Test
# =========================================================

if __name__ == "__main__":

    original_code = """
String query =
"SELECT * FROM users WHERE name='"
+ username +
"'";
"""

    fixed_code = """
String query =
"SELECT * FROM users WHERE name=?";

PreparedStatement stmt =
conn.prepareStatement(query);

stmt.setString(
    1,
    username
);

ResultSet rs =
stmt.executeQuery();
"""

    audit_report = {
        "file_name": "LoginDAO.java",
        "overall_risk": "High",
        "compliance_score": 20,
        "total_findings": 1,
        "findings": [
            {
                "title":
                    "SQL Injection Vulnerability",
                "severity":
                    "Critical",
                "cwe":
                    "CWE-89"
            }
        ]
    }

    remediation_report = {
        "file_name":
            "LoginDAO.java",
        "remediation_summary":
            "Fixed SQL Injection."
    }

    verifier = VerifierAgent()

    result = verifier.verify(
        original_code=original_code,
        fixed_code=fixed_code,
        audit_report=audit_report,
        remediation_report=remediation_report,
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
        verifier.report_to_markdown(
            result
        )
    )
