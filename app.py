import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="FraudShield",
    page_icon="🛡️",
    layout="wide"
)

# NAVY BLUE DESIGN
st.markdown("""
<style>
.stApp {
    background-color: #071A35;
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
.stButton>button {
    background-color: #1769AA;
    color: white;
    border-radius: 10px;
    border: none;
}
div[data-testid="stMetric"] {
    background-color: #102B50;
    padding: 18px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("🛡️ FraudShield")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home Dashboard",
        "Fraud Detection",
        "Batch Detection",
        "Data Analysis",
        "Fraud Trends",
        "Safety Tips",
        "About Project"
    ]
)

# DEMONSTRATION DATA
np.random.seed(42)

df = pd.DataFrame({
    "Transaction Amount": np.random.randint(100, 50000, 200),
    "Transaction Hour": np.random.randint(0, 24, 200),
    "Failed Attempts": np.random.randint(0, 6, 200),
    "New Device": np.random.randint(0, 2, 200)
})

# DEMONSTRATION RISK SCORING
def calculate_risk(amount, hour, failed, device):
    score = 0

    if amount > 30000:
        score += 30

    if hour < 5:
        score += 20

    if failed >= 3:
        score += 25

    if device == "Yes":
        score += 25

    return min(score, 100)


# HOME DASHBOARD
if page == "Home Dashboard":

    st.title("🛡️ FraudShield")
    st.subheader("Cyber Fraud Detection System")

    st.write(
        "An educational application demonstrating "
        "how data analysis can help identify "
        "potentially suspicious transactions."
    )

    st.info(
        "This version uses demonstration data and "
        "illustrative risk rules."
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Sample Transactions", "200")
    c2.metric("Project Period", "2022–2024")
    c3.metric("Detection System", "Prototype")

    st.subheader("Project Overview")

    st.write("""
    FraudShield demonstrates how Python, data analysis
    and machine learning techniques can support
    financial fraud detection.
    """)


# FRAUD DETECTION
elif page == "Fraud Detection":

    st.title("🔍 Fraud Detection")

    st.write("Enter transaction details below.")

    amount = st.number_input(
        "Transaction Amount (₹)",
        min_value=0
    )

    hour = st.slider(
        "Transaction Hour",
        0, 23
    )

    failed = st.number_input(
        "Failed Login Attempts",
        min_value=0
    )

    device = st.selectbox(
        "Is this a new device?",
        ["No", "Yes"]
    )

    if st.button("Analyse Transaction"):

        score = calculate_risk(
            amount, hour, failed, device
        )

        st.subheader("Analysis Result")

        st.metric("Illustrative Risk Score", f"{score}/100")

        if score >= 60:
            st.error("High Risk – Suspicious Pattern")
        elif score >= 30:
            st.warning("Medium Risk – Review Required")
        else:
            st.success("Low Risk – No Major Warning Signs")

        st.caption(
            "This is a rule-based educational demonstration, "
            "not a confirmed fraud decision."
        )


# BATCH DETECTION
elif page == "Batch Detection":

    st.title("📁 Batch Transaction Analysis")

    file = st.file_uploader(
        "Upload transaction CSV",
        type=["csv"]
    )

    if file is not None:

        data = pd.read_csv(file)

        st.subheader("Uploaded Dataset")
        st.dataframe(data)

        st.write("Total Records:", len(data))

        st.download_button(
            "Download Original CSV",
            data=data.to_csv(index=False),
            file_name="transactions.csv",
            mime="text/csv"
        )


# DATA ANALYSIS
elif page == "Data Analysis":

    st.title("📊 Data Analysis")

    st.info(
        "These charts use randomly generated demonstration "
        "transactions, not official fraud statistics."
    )

    st.subheader("Transaction Amount Distribution")

    fig, ax = plt.subplots()

    ax.hist(
        df["Transaction Amount"],
        bins=15
    )

    ax.set_xlabel("Transaction Amount")
    ax.set_ylabel("Number of Transactions")

    st.pyplot(fig)

    st.subheader("Transactions by Hour")

    hourly = df["Transaction Hour"].value_counts().sort_index()

    st.bar_chart(hourly)

    st.subheader("Dataset Preview")

    st.dataframe(df.head(10))


# FRAUD TRENDS
elif page == "Fraud Trends":

    st.title("📈 Indian Cyber Fraud Trends")

    st.write("Reporting period: 2022–2024")

    st.info("""
    Official statistics will be added here after
    verifying the NCRB, MHA, I4C and CERT-In reports.

    Different sources report different indicators.
    They will be displayed separately.
    """)

    st.write("Sources to be used:")

    st.markdown("""
    - NCRB – Crime in India
    - Ministry of Home Affairs (MHA)
    - Indian Cyber Crime Coordination Centre (I4C)
    - CERT-In
    """)


# SAFETY TIPS
elif page == "Safety Tips":

    st.title("🛡️ Cyber Safety Tips")

    tips = [
        "Never share your OTP.",
        "Never share your UPI PIN.",
        "Avoid unknown payment links.",
        "Do not download unknown APK files.",
        "Use strong passwords.",
        "Enable two-factor authentication.",
        "Verify payment requests.",
        "Report suspected financial fraud immediately."
    ]

    for tip in tips:
        st.success("✔ " + tip)

    st.subheader("Indian Cybercrime Helpline")

    st.header("1930")

    st.write("Official reporting portal: https://cybercrime.gov.in/")


# ABOUT PROJECT
elif page == "About Project":

    st.title("ℹ️ About FraudShield")

    st.subheader("Project Objective")

    st.write("""
    To demonstrate how data analysis and machine learning
    can help identify potentially suspicious financial
    transaction patterns.
    """)

    st.subheader("Technologies Used")

    st.write("""
    - Python
    - NumPy
    - Pandas
    - Matplotlib
    - Streamlit
    - Machine Learning (planned integration)
    """)

    st.subheader("Project Period")

    st.write("2022–2024")

    st.subheader("Future Scope")

    st.write("""
    - Machine learning integration
    - Improved fraud prediction
    - Real-time transaction monitoring
    - Advanced data visualisation
    """)
