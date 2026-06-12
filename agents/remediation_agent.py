# agents/remediation_agent.py

import json
import difflib
from typing import Dict, Any, List

from core.vllm_client import VLLMClient


class RemediationAgent:
    """
    AVCA Agent 2

    Security Remediation Agent

    Responsibilities:
    ------------------
    1. Consume audit findings
    2. Fix vulnerabilities
    3. Preserve business logic
    4. Generate secure code
    5. Generate remediation summary
    6. Generate code diff
    7. Produce remediation metrics
    """

    def __init__(self):

        self.llm = VLLMClient()

    # =====================================================
    # Main Remediation Pipeline
    # =====================================================

    def remediate(
        self,
        source_code: str,
        audit_report: Dict[str, Any],
        file_name: str
    ) -> Dict[str, Any]:

        system_prompt = """
You are AVCA Remediation Agent.

You are a senior Java Security Engineer and Application Security Expert.

Your responsibility is to generate secure, policy-compliant remediation fixes
for vulnerable Java code.

PRIMARY OBJECTIVE

Fix ONLY the vulnerabilities identified in the audit report.

IMPORTANT RULES

1. Preserve business logic.
2. Preserve application behavior.
3. Preserve existing architecture.
4. Preserve class structure whenever possible.
5. Preserve existing method signatures.
6. Preserve variable names whenever possible.
7. Do NOT perform unnecessary refactoring.
8. Do NOT introduce new classes.
9. Do NOT introduce new constructors unless absolutely required.
10. Do NOT redesign the application.
11. Fix only the reported vulnerabilities.

JAVA REQUIREMENTS

1. Generate valid Java syntax only.
2. Target Java 17 compatibility.
3. Do NOT generate Scala syntax.
4. Do NOT generate Kotlin syntax.
5. Do NOT generate pseudocode.
6. Do NOT omit required imports.
7. Produce compile-ready Java code whenever possible.

SECURITY REQUIREMENTS

1. Apply secure coding best practices.
2. Follow remediation recommendations from the audit report.
3. Use secure APIs when appropriate.
4. Remove vulnerable patterns.
5. Ensure fixes directly address reported findings.

OUTPUT REQUIREMENTS

Return ONLY valid JSON.

Do NOT return markdown.

Do NOT wrap JSON in code blocks.

Required Schema:

{
  "file_name": "",
  "remediation_summary": "",
  "security_improvements": [
    {
      "title": "",
      "description": ""
    }
  ],
  "fixed_code": ""
}

REMEDIATION SUMMARY REQUIREMENTS

- Short and professional.
- Explain what vulnerabilities were fixed.
- Mention major security improvements.

SECURITY IMPROVEMENTS REQUIREMENTS

Each item must contain:

{
  "title": "",
  "description": ""
}

Examples:

{
  "title": "Prevented SQL Injection",
  "description": "Replaced dynamic SQL concatenation with parameterized queries."
}

CODE GENERATION RULES

GOOD:

Original:

String query =
"SELECT * FROM users WHERE name='"
+ username +
"'";

Fixed:

String query =
"SELECT * FROM users WHERE name=?";

PreparedStatement stmt =
conn.prepareStatement(query);

stmt.setString(
    1,
    username
);

BAD:

- Rewriting entire class.
- Adding unrelated security controls.
- Introducing dependency injection frameworks.
- Introducing new architecture.
- Renaming everything.
- Creating unnecessary constructors.

Return JSON only.
"""

        findings_json = json.dumps(
            audit_report,
            indent=2
        )

        user_prompt = f"""
IMPORTANT:

Apply the smallest possible code change
required to fix the vulnerabilities.
Minimize modifications.
Avoid unnecessary refactoring.
Keep the resulting code as close to the
original implementation as possible.

Audit Report:

{findings_json}

====================================================

Original Source Code:

{source_code}

====================================================

Generate remediated code.
"""

        response = self.llm.generate(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=0.1,
            max_tokens=4096
        )

        result = self._safe_json_parse(
            response=response,
            file_name=file_name
        )

        result = self._normalize_result(
            result=result,
            original_code=source_code
        )

        return result

    # =====================================================
    # Safe Parsing
    # =====================================================

    def _safe_json_parse(
        self,
        response: str,
        file_name: str
    ) -> Dict[str, Any]:

        try:

            return json.loads(response)

        except Exception:

            return {
                "file_name": file_name,
                "remediation_summary":
                    "Model output parsing failed.",
                "security_improvements": [],
                "fixed_code": response
            }

    # =====================================================
    # Normalize Output
    # =====================================================

    def _normalize_result(
        self,
        result: Dict[str, Any],
        original_code: str
    ) -> Dict[str, Any]:

        fixed_code = result.get(
            "fixed_code",
            ""
        )

        result["diff"] = self.generate_diff(
            original_code,
            fixed_code
        )

        result["metrics"] = self.generate_metrics(
            result
        )

        return result

    # =====================================================
    # Unified Diff Generator
    # =====================================================

    def generate_diff(
        self,
        original_code: str,
        fixed_code: str
    ) -> str:

        diff = difflib.unified_diff(
            original_code.splitlines(),
            fixed_code.splitlines(),
            fromfile="Original",
            tofile="Remediated",
            lineterm=""
        )

        return "\n".join(diff)

    # =====================================================
    # Metrics Generator
    # =====================================================

    def generate_metrics(
        self,
        remediation_result: Dict[str, Any]
    ) -> Dict[str, Any]:

        improvements = remediation_result.get(
            "security_improvements",
            []
        )

        return {
            "security_improvements_count":
                len(improvements),
            "generated_fix":
                bool(
                    remediation_result.get(
                        "fixed_code",
                        ""
                    )
                )
        }

    # =====================================================
    # Streamlit Display Helpers
    # =====================================================
    
    def remediation_to_markdown(self,remediation_result: Dict[str, Any]) -> str:

        lines = [
            "# Remediation Report",
            "",
            remediation_result.get(
                "remediation_summary",
                "N/A"
            ),
            "",
            "---",
            ""
        ]
    
        improvements = remediation_result.get(
            "security_improvements",
            []
        )
    
        if improvements:
    
            lines.append(
                "## Security Improvements"
            )
    
            lines.append("")
    
            for item in improvements:
    
                if isinstance(item, dict):
    
                    title = str(
                        item.get(
                            "title",
                            "Improvement"
                        )
                    )
    
                    desc = str(
                        item.get(
                            "description",
                            ""
                        )
                    )
    
                    lines.append(
                        f"**🔹 {title}**"
                    )
    
                    if desc.strip():
                        lines.append(desc)
    
                    lines.append("")
    
                else:
    
                    lines.append(
                        f"- {str(item)}"
                    )
    
            lines.append("")
    
        lines.append("---")
        lines.append("")
        lines.append("## Metrics")
        lines.append("")
    
        metrics = remediation_result.get(
            "metrics",
            {}
        )
    
        lines.append(
            f"- Improvements Applied: "
            f"{metrics.get('security_improvements_count', 0)}"
        )
    
        lines.append(
            f"- Fix Generated: "
            f"{metrics.get('generated_fix', False)}"
        )
    
        fixed_code = remediation_result.get(
            "fixed_code",
            ""
        )
    
        if fixed_code:
    
            lines.append("")
            lines.append("---")
            lines.append("")
            lines.append("## Fixed Code")
            lines.append("")
            lines.append("```java")
            lines.append(fixed_code)
            lines.append("```")
    
        return "\n".join(lines)

    # def remediation_to_markdown(
    #     self,
    #     remediation_result: Dict[str, Any]
    # ) -> str:

    #     lines = []

    #     lines.append(
    #         "# Remediation Report"
    #     )

    #     lines.append("")

    #     lines.append(
    #         remediation_result.get(
    #             "remediation_summary",
    #             "N/A"
    #         )
    #     )

    #     lines.append("")

    #     lines.append("---")

    #     lines.append("")

    #     improvements = remediation_result.get(
    #         "security_improvements",
    #         []
    #     )

    #     if improvements:

    #         lines.append(
    #             "## Security Improvements"
    #         )

    #         lines.append("")

    #         for item in improvements:

    #             lines.append(
    #                 f"- {item}"
    #             )

    #     lines.append("")
    #     lines.append("---")
    #     lines.append("")

    #     lines.append(
    #         "## Metrics"
    #     )

    #     metrics = remediation_result.get(
    #         "metrics",
    #         {}
    #     )

    #     lines.append(
    #         f"- Improvements Applied: "
    #         f"{metrics.get('security_improvements_count', 0)}"
    #     )

    #     lines.append(
    #         f"- Fix Generated: "
    #         f"{metrics.get('generated_fix', False)}"
    #     )

    #     return "\n".join(lines)

    # =====================================================
    # Dashboard KPI Helper
    # =====================================================

    def build_dashboard_metrics(
        self,
        audit_report: Dict[str, Any]
    ) -> Dict[str, Any]:

        findings = audit_report.get(
            "findings",
            []
        )

        return {
            "findings_received":
                len(findings),
            "critical_findings":
                len(
                    [
                        f
                        for f in findings
                        if f.get("severity")
                        == "Critical"
                    ]
                ),
            "high_findings":
                len(
                    [
                        f
                        for f in findings
                        if f.get("severity")
                        == "High"
                    ]
                ),
            "medium_findings":
                len(
                    [
                        f
                        for f in findings
                        if f.get("severity")
                        == "Medium"
                    ]
                ),
            "low_findings":
                len(
                    [
                        f
                        for f in findings
                        if f.get("severity")
                        == "Low"
                    ]
                )
        }


# =========================================================
# Local Test
# =========================================================

if __name__ == "__main__":

    vulnerable_code = """
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
"""

    audit_report = {
        "file_name": "LoginDAO.java",
        "overall_risk": "Critical",
        "compliance_score": 25,
        "total_findings": 1,
        "findings": [
            {
                "title": "SQL Injection",
                "severity": "Critical",
                "cwe": "CWE-89"
            }
        ]
    }

    agent = RemediationAgent()

    result = agent.remediate(
        source_code=vulnerable_code,
        audit_report=audit_report,
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
        result["diff"]
    )