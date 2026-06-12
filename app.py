import pandas as pd
import streamlit as st
from pathlib import Path

from agents.auditor_agent import AuditorAgent
from agents.remediation_agent import RemediationAgent
from agents.verifier_agent import VerifierAgent

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AVCA",
    page_icon="🛡️",
    layout="wide"
)

# ==========================================================
# AGENTS
# ==========================================================

@st.cache_resource
def load_agents():
    return (
        AuditorAgent(),
        RemediationAgent(),
        VerifierAgent()
    )

auditor_agent, remediation_agent, verifier_agent = load_agents()

# ==========================================================
# SESSION STATE
# ==========================================================

defaults = {
    "audit_result": None,
    "remediation_result": None,
    "verification_result": None,
    "source_code": "",
    "selected_file": None
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ==========================================================
# HEADER
# ==========================================================

st.title("🛡️ AVCA - Agentic Vulnerability Compliance Auditor")

st.info(
    """
🏆 **Hackathon Track Coverage**

**AGENT_028:** Auditor Agent → Remediation Agent → Verification Agent

**FINETUNE_001:** Qwen2.5-14B-Instruct + LoRA Security Remediation Fine-Tuning

**RAG:** FAISS Enterprise Policy Retrieval for Context-Aware Vulnerability Analysis
"""
)
# st.markdown("""
# ### 🏆 Hackathon Track Coverage

# #### ✅ AGENT_028 — Multi-Agent Security Orchestration

# - Auditor Agent
# - Remediation Agent
# - Verification Agent

# #### ✅ FINETUNE_001 — Security Fine-Tuning Pipeline

# - Qwen2.5-14B-Instruct
# - LoRA Fine-Tuning Architecture
# - Security Remediation Specialization

# #### ✅ Retrieval Augmented Generation (RAG)

# - FAISS Vector Store
# - Enterprise Security Policies
# - Context-Aware Vulnerability Detection
# """)

st.divider()

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header("Project Controls")

code_dir = Path("data/test_code")

files = []

if code_dir.exists():
    files = sorted(
        [p.name for p in code_dir.glob("*") if p.is_file()]
    )

selected_file = st.sidebar.selectbox(
    "Select Source File",
    files
)

run_pipeline = st.sidebar.button(
    "🚀 Run AVCA Pipeline",
    use_container_width=True
)

# ==========================================================
# LOAD CODE
# ==========================================================

source_code = ""

if selected_file:

    file_path = code_dir / selected_file

    if file_path.exists():

        source_code = file_path.read_text(
            encoding="utf-8"
        )

        st.session_state.source_code = source_code
        st.session_state.selected_file = selected_file

# ==========================================================
# EXECUTE PIPELINE
# ==========================================================

if run_pipeline and source_code:

    with st.spinner("Running Auditor Agent..."):

        audit_result = auditor_agent.analyze_code(
            source_code=source_code,
            file_name=selected_file
        )

    st.session_state.audit_result = audit_result

    with st.spinner("Running Remediation Agent..."):

        remediation_result = remediation_agent.remediate(
            source_code=source_code,
            audit_report=audit_result,
            file_name=selected_file
        )

    st.session_state.remediation_result = remediation_result

    with st.spinner("Running Verification Agent..."):

        verification_result = verifier_agent.verify(
            original_code=source_code,
            fixed_code=remediation_result.get(
                "fixed_code",
                ""
            ),
            audit_report=audit_result,
            remediation_report=remediation_result,
            file_name=selected_file
        )

    st.session_state.verification_result = verification_result

    st.success(
        "✅ AVCA pipeline completed successfully."
    )


# ==========================================================
# TABS
# ==========================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔍 Audit",
    "🛠 Remediation",
    "✅ Verification",
    "📊 Executive Dashboard",
    "🏗 Architecture"
])

# ==========================================================
# AUDIT TAB
# ==========================================================

with tab1:

    st.subheader("Source Code")

    st.code(
        st.session_state.source_code,
        language="java"
    )

    audit = st.session_state.audit_result

    if audit:

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Risk Level",
            audit.get("overall_risk", "Unknown")
        )

        c2.metric(
            "Compliance Score",
            audit.get("compliance_score", 0)
        )

        c3.metric(
            "Findings",
            audit.get("total_findings", 0)
        )

        findings = audit.get(
            "findings",
            []
        )

        if findings:

            table_rows = []

            for f in findings:

                table_rows.append({
                    "Severity": f.get("severity"),
                    "CWE": f.get("cwe"),
                    "Finding": f.get("title"),
                    "Component": f.get(
                        "affected_component"
                    )
                })

            st.subheader(
                "Security Findings"
            )

            st.dataframe(
                pd.DataFrame(table_rows),
                use_container_width=True
            )

        st.divider()

        st.markdown(
            auditor_agent.report_to_markdown(
                audit
            )
        )

# ==========================================================
# REMEDIATION TAB
# ==========================================================

with tab2:

    remediation = (
        st.session_state.remediation_result
    )

    if remediation:

        left, right = st.columns(2)

        with left:

            st.subheader(
                "Original Code"
            )

            st.code(
                st.session_state.source_code,
                language="java"
            )

        with right:

            st.subheader(
                "Remediated Code"
            )

            st.code(
                remediation.get(
                    "fixed_code",
                    ""
                ),
                language="java"
            )

        st.divider()

        st.markdown(
            remediation_agent.remediation_to_markdown(
                remediation
            )
        )

        st.divider()

        st.subheader(
            "Code Diff"
        )

        st.code(
            remediation.get(
                "diff",
                ""
            )
        )

# ==========================================================
# VERIFICATION TAB
# ==========================================================

with tab3:

    verification = (
        st.session_state.verification_result
    )

    if verification:

        status = verification.get(
            "verification_status",
            "UNKNOWN"
        )

        if status == "PASS":
            st.success(
                "🟢 APPROVED FOR DEPLOYMENT"
            )
        else:
            st.error(
                "🔴 DEPLOYMENT BLOCKED"
            )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Status",
            status
        )

        c2.metric(
            "Compliance",
            verification.get(
                "compliance_score",
                0
            )
        )

        c3.metric(
            "Resolved Findings",
            verification.get(
                "resolved_count",
                0
            )
        )

        st.divider()

        st.markdown(
            verifier_agent.report_to_markdown(
                verification
            )
        )

# ==========================================================
# EXECUTIVE DASHBOARD
# ==========================================================

with tab4:

    audit = st.session_state.audit_result
    verification = (
        st.session_state.verification_result
    )

    if audit and verification:

        before_score = audit.get(
            "compliance_score",
            0
        )

        after_score = verification.get(
            "compliance_score",
            0
        )

        improvement = (
            after_score - before_score
        )

        total_findings = audit.get(
            "total_findings",
            0
        )

        resolved = verification.get(
            "resolved_count",
            0
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Initial Score",
            before_score
        )

        c2.metric(
            "Final Score",
            after_score
        )

        c3.metric(
            "Improvement",
            f"+{improvement}"
        )

        c4.metric(
            "Deployment",
            verification.get(
                "verification_status",
                "N/A"
            )
        )

        st.divider()

        st.subheader(
            "Executive Summary"
        )

        st.info(
            f"""
            Findings Identified: {total_findings}

            Findings Resolved: {resolved}

            Compliance Improvement: +{improvement}

            Deployment Status:
            {verification.get('verification_status')}
            """
        )

# ==========================================================
# ARCHITECTURE TAB
# ==========================================================

with tab5:

    st.subheader(
        "AVCA System Architecture"
    )

    st.code(
"""
[Source File Selected]
            │
            ▼
┌──────────────────────┐      ⚡ Pulls Vector Embeddings
│  Auditor Agent       │ ◄─── From FAISS Security Policy DB
└──────────┬───────────┘
            │
            ▼   [Outputs Vulnerability Audit JSON]
┌──────────────────────┐
│  Remediation Agent   │ ◄─── Evaluates LLM Weights Specialization
└──────────┬───────────┘
            │
            ▼   [Outputs Patched Secure Syntax Blocks]
┌──────────────────────┐
│  Verification Agent  │ ◄─── Performs Differential State Validation
└──────────┬───────────┘
            │
            ▼   
 [Deployment PASS/FAIL Metric Signal]
"""
    )

    st.markdown("""
### Technology Stack

- **Agents:** Auditor, Remediation, Verification
- **Model:** Qwen2.5-14B-Instruct
- **Serving:** vLLM
- **RAG:** FAISS + Enterprise Security Policies
- **Fine-Tuning:** LoRA (FINETUNE_001)
- **UI:** Streamlit
- **Language:** Python
""")
