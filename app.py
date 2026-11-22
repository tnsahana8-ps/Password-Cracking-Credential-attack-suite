
import streamlit as st
import json
import os

from modules.password_analyzer import analyze_password
from modules.dictionary_generator import generate_dictionary
from modules.hash_generator import generate_hash, identify_hash
from modules.attack_simulator import dictionary_simulation

st.set_page_config(
    page_title="Password Cracking & Credential Attack Suite",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Password Cracking & Credential Attack Suite")

st.write(
    "A Python-based cybersecurity toolkit for password "
    "security assessment and controlled attack simulation."
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Password Strength Analyzer",
        "Dictionary Generator",
        "Hash Generator",
        "Attack Simulator",
        "Security Audit Report"
    ]
)

if "audit" not in st.session_state:
    st.session_state.audit = {}

if page == "Home":

    st.header("Project Dashboard")

    st.success("Cybersecurity Toolkit Ready")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Core Modules", "4")

    with col2:
        st.metric("Application Status", "Active")

    st.subheader("Project Objectives")

    st.write("""
    - Analyze password strength.
    - Generate sample password dictionaries.
    - Demonstrate password hashing.
    - Simulate dictionary-based attacks.
    - Generate security audit reports.
    """)

elif page == "Password Strength Analyzer":

    st.header("Password Strength Analyzer")

    password = st.text_input(
        "Enter a sample password",
        type="password"
    )

    if st.button("Analyze Password"):

        if password:

            result = analyze_password(password)

            st.session_state.audit["password_analysis"] = result

            st.subheader("Analysis Results")

            st.write("Strength:", result["strength"])
            st.write("Score:", result["score"], "/5")
            st.write("Estimated Entropy:", result["entropy"], "bits")

            st.write("Recommendations:")

            for suggestion in result["suggestions"]:
                st.warning(suggestion)

        else:
            st.error("Please enter a sample password.")

elif page == "Dictionary Generator":

    st.header("Dictionary Generator")

    if st.button("Generate Sample Dictionary"):

        words = generate_dictionary()

        os.makedirs("sample_data", exist_ok=True)

        with open("sample_data/test_dictionary.txt", "w") as f:
            f.write("\n".join(words))

        st.session_state.audit["dictionary_count"] = len(words)

        st.success(f"{len(words)} sample entries generated.")

        st.dataframe({"Sample Entries": words})

        st.download_button(
            "Download Dictionary",
            "\n".join(words),
            file_name="test_dictionary.txt"
        )

elif page == "Hash Generator":

    st.header("Password Hash Generator")

    password = st.text_input(
        "Enter a dummy password",
        type="password"
    )

    if st.button("Generate Hash"):

        if password:

            hashed = generate_hash(password)

            st.session_state.audit["hash_type"] = identify_hash(hashed)

            st.code(hashed)

            st.info("Hash Type: " + identify_hash(hashed))

        else:
            st.error("Enter a sample password.")

elif page == "Attack Simulator":

    st.header("Controlled Dictionary Attack Simulation")

    st.info(
        "This demonstration uses synthetic credentials "
        "and a local test dataset only."
    )

    if st.button("Run Simulation"):

        sample_password = "student"

        test_words = [
            "welcome",
            "testing",
            "student",
            "computer"
        ]

        target_hash = generate_hash(sample_password)

        result = dictionary_simulation(
            target_hash,
            test_words
        )

        st.session_state.audit["simulation"] = result

        st.write("Match Found:", result["match_found"])
        st.write("Attempts:", result["attempts"])

        st.success("Simulation completed.")

elif page == "Security Audit Report":

    st.header("Security Audit Report")

    st.write("Review the results collected from the modules.")

    if st.button("Generate Audit Report"):

        report = {
            "Project": "Password Cracking & Credential Attack Suite",
            "Audit Results": st.session_state.audit,
            "Recommendation": [
                "Use long and unique passwords.",
                "Enable multi-factor authentication.",
                "Avoid password reuse.",
                "Use secure password hashing algorithms.",
                "Monitor repeated failed login attempts."
            ]
        }

        report_json = json.dumps(report, indent=4)

        st.download_button(
            "Download Security Audit Report",
            report_json,
            file_name="security_audit_report.json",
            mime="application/json"
        )

        st.success("Audit report generated successfully.")

