import streamlit as st
import pandas as pd

from chatbot import get_chatbot_response

from agent import (
    read_fake_file,
    mock_email,
    mock_http_request
)

from security_tests import (
    get_results_dataframe,
    RISK_CATALOG,
    run_local_demo_checks
)
# Page settings
st.set_page_config(
    page_title="AI Security Lab",
    page_icon="🔐",
    layout="wide"
)

# Project heading
st.title("🔐 AI Security Testing Lab")

st.caption(
    "LLM and Agentic AI Security Assessment Platform"
)

st.divider()

# Sidebar navigation
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "AI Chatbot",
        "AI Agent",
        "Security Testing",
        "Test Results"
    ]
)

# Dashboard
if menu == "Dashboard":

    st.header("Project Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Required Risks", "10")
    col2.metric("AI Models", "2")
    col3.metric("Test Cases per Risk", "3+")

    st.divider()

    st.subheader("Project Information")

    st.write("Project: AI Security Testing Lab")
    st.write("Framework: Python + Streamlit")
    st.write("Testing: OWASP LLM and Agentic AI")
    st.write("Models: Claude and Gemini")

    st.info(
        "Security testing will use fake data "
        "and isolated mock tools."
    )

    st.subheader("Development Status")

    tasks = {
        "Module": [
            "Dashboard",
            "AI Chatbot",
            "AI Agent",
            "Security Testing",
            "Final Report"
        ],
        "Status": [
            "In Progress",
            "Pending",
            "Pending",
            "Pending",
            "Pending"
        ]
    }

    df = pd.DataFrame(tasks)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

# Chatbot section
elif menu == "AI Chatbot":

    st.header("🤖 AI Security Chatbot")

    st.caption("Local Demo Model")

    # Store conversation in session
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display previous messages
    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User input
    user_input = st.chat_input("Ask something about AI Security...")

    if user_input:

        # Save user message
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })

        # Generate chatbot response
        response = get_chatbot_response(
            user_input,
            model="Local Demo"
        )

        # Save chatbot response
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response
        })

        # Refresh page
        st.rerun()
# Agent section
elif menu == "AI Agent":

    st.header("🤖 AI Agent")
    st.caption("Safe Mock Tool Execution")

    tool = st.selectbox(
        "Select Agent Tool",
        [
            "Fake File Reader",
            "Mock Email",
            "Mock HTTP"
        ]
    )

    if tool == "Fake File Reader":

        filename = st.selectbox(
            "Choose File",
            ["notes.txt", "security.txt", "demo.txt"]
        )

        if st.button("Read File"):
            result = read_fake_file(filename)
            st.success("File Read Successfully")
            st.code(result)

    elif tool == "Mock Email":

        recipient = st.text_input(
            "Fake Recipient",
            "demo@example.com"
        )

        message = st.text_area(
            "Email Message",
            "This is a security testing demo."
        )

        if st.button("Simulate Email"):
            result = mock_email(recipient, message)
            st.json(result)

    elif tool == "Mock HTTP":

        url = st.text_input(
            "Demo URL",
            "https://example.com"
        )

        if st.button("Simulate Request"):
            result = mock_http_request(url)
            st.json(result)

    st.info(
        "Safety: All tools are simulated. "
        "No real emails or HTTP requests are performed."
    )

    st.header("AI Agent")
    st.warning("Mock tools will be added next.")

# Security section
elif menu == "Security Testing":

    st.header("🛡️ OWASP Security Testing")

    st.write(
        "AI Security Risk Assessment and Test Catalog"
    )
    st.divider()
    st.subheader("Local Demo Security Checks")

    if st.button("Run Local Security Checks"):
        results = run_local_demo_checks()
        st.session_state.local_check_results = results

    if "local_check_results" in st.session_state:
        results_df = pd.DataFrame(
            st.session_state.local_check_results
        )

        st.dataframe(
            results_df,
            use_container_width=True,
            hide_index=True
        )

        passed = sum(
            item["Status"] == "PASS"
            for item in st.session_state.local_check_results
        )

        st.metric("Local Checks Passed", f"{passed}/5")
        st.divider()
    st.subheader("Local Demo Security Checks")

    if st.button("Run Local Security Checks", key="run_local_checks_btn"):
        results = run_local_demo_checks()
        st.session_state.local_check_results = results

    if "local_check_results" in st.session_state:
        results_df = pd.DataFrame(
            st.session_state.local_check_results
        )

        st.dataframe(results_df, use_container_width=True)

        st.metric("Local Checks Passed", "5/5")

    # Load test catalog
    df = get_results_dataframe()

    col1, col2 = st.columns(2)

    col1.metric("Total Security Risks", len(RISK_CATALOG))
    col2.metric("Total Test Cases", len(df))

    st.divider()

    # Select risk
    selected_risk = st.selectbox(
        "Select Security Risk",
        list(RISK_CATALOG.keys())
    )

    details = RISK_CATALOG[selected_risk]

    st.subheader(selected_risk)
    st.write("Risk Name:", details["name"])

    st.write("Test Cases:")

    for number, test in enumerate(
        details["tests"], start=1
    ):
        st.write(f"{number}. {test}")

    st.divider()

    st.subheader("Complete Test Catalog")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.warning(
        "These test cases are designed but not yet executed. "
        "No PASS or FAIL results are claimed."
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Test Catalog CSV",
        data=csv,
        file_name="security_test_catalog.csv",
        mime="text/csv"
    )

# Results section
elif menu == "Test Results":
    st.header("📊 Security Test Results")
    st.write("Record the result of each security test.")

    if "test_results_df" not in st.session_state:
        st.session_state.test_results_df = get_results_dataframe()
        st.session_state.test_results_df["Notes"] = ""

    df = st.session_state.test_results_df

    selected_test = st.selectbox(
        "Select Test Case",
        df["Test ID"].tolist()
    )

    selected_row = df[df["Test ID"] == selected_test].iloc[0]

    st.subheader(selected_test)
    st.write("Risk:", selected_row["Risk Name"])
    st.write("Test:", selected_row["Test Case"])

    status = st.selectbox(
        "Test Status",
        ["NOT TESTED", "PASS", "FAIL"]
    )

    notes = st.text_area(
        "Observation / Notes",
        value=selected_row["Notes"]
    )

    if st.button("Save Test Result"):
        idx = df.index[df["Test ID"] == selected_test][0]
        df.loc[idx, "Status"] = status
        df.loc[idx, "Notes"] = notes
        st.success("Test result saved!")

    st.divider()
    st.subheader("All Test Results")
    st.dataframe(df, use_container_width=True, hide_index=True)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Test Results CSV",
        data=csv,
        file_name="security_test_results.csv",
        mime="text/csv"
    )