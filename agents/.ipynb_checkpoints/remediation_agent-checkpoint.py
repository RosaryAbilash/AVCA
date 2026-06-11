from core.vllm_client import VLLMClient

class RemediationAgent:
    def __init__(self):
        self.vllm_client = VLLMClient()

    def generate_fix(self, original_code: str, audit_report: str) -> str:
        system_prompt = f"""You are AVCA's Remediation Agent, an elite DevSecOps coding assistant.
Rewrite this vulnerable Java code to be perfectly secure based on the Audit Report.

SECURITY AUDIT REPORT:
{audit_report}

INSTRUCTIONS:
1. Fix ALL vulnerabilities mentioned.
2. Do NOT alter core business logic.
3. Output ONLY the raw, fixed Java code. No markdown, no conversation."""

        fixed_code = self.vllm_client.generate_chat_completion(
            system_prompt=system_prompt,
            user_content=f"Rewrite this code securely:\n{original_code}",
            temperature=0.1 # Ultra-low for deterministic code generation
        )
        
        # Strip markdown for clean UI rendering
        return fixed_code.replace("```java", "").replace("```", "").strip()