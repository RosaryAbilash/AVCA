from core.vllm_client import VLLMClient
from core.vector_store import LocalPolicyVectorStore

class AuditorAgent:
    def __init__(self):
        self.vllm_client = VLLMClient()
        self.vector_store = LocalPolicyVectorStore()
        
    def analyze_code(self, source_code: str, filename: str) -> str:
        if not source_code.strip(): return "Error: No code provided."
        relevant_rules = self.vector_store.search_relevant_rules(source_code)

        system_prompt = f"""You are AVCA, an elite DevSecOps AI Auditor. 
Analyze the provided code for {filename} against the company's internal policies:
{relevant_rules}

Output a strictly structured report:
- 🔴 CRITICAL FINDINGS: (List vulnerabilities)
- 📖 POLICY VIOLATIONS: (Quote specific policy broken)
- ⚠️ RISK IMPACT: (Explain the danger)
Do NOT provide the fixed code. Provide only the audit report."""

        return self.vllm_client.generate_chat_completion(
            system_prompt=system_prompt,
            user_content=f"Audit this code:\n```java\n{source_code}\n```"
        )