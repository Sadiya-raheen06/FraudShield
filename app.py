import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="FraudShield",
    page_icon="🛡️",
    layout="wide"
)

# NAVY BLUE THEME
st.markdown("""
<style>
.stApp {
    background-color: #071A35;
    color: #FFFFFF;
}

[data-testid="stSidebar"] {
    background-color: #102B50;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

h1, h2, h3, p, label {
    color: #FFFFFF !important;
}

div[data-testid="stMetric"] {
    background-color: #163B65;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #2878B8;
}

.stButton button {
    background-color: #1769AA;
    color: white;
    border-radius: 10px;
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


# SAMPLE DATA
np.random.seed(42)

df = pd.DataFrame({
    "Transaction Amount": np.random.randint(100, 50000, 200),
    "Transaction Hour": np.random.randint(0, 24, 200),
    "Failed Attempts": np.random.randint(0, 6, 200),
    "New Device": np.random.randint(0, 2, 200)
})


# RISK CALCULATION
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
        "An educational application for analysing "
        "potentially suspicious financial transactions."
    )

    st.info("Welcome to FraudShield!")

    col1, col2, col3 = st.columns(3)

    col1.metric("Sample Transactions", "200")
    col2.metric("Project Period", "2022–2024")
    col3.metric("System", "Prototype")

    st.subheader("Project Overview")

    st.write("""
    FraudShield demonstrates how data analysis
    and machine learning can support cyber fraud detection.
    """)


# FRAUD DETECTION
elif page == "Fraud Detection":

    st.title("🔍 Fraud Detection")

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

        st.metric("Illustrative Risk Score", f"{score}/100")

        if score >= 60:
            st.error("High Risk – Suspicious Pattern")
        elif score >= 30:
            st.warning("Medium Risk – Review Required")
        else:
            st.success("Low Risk – No Major Warning Signs")

        st.caption(
            "Educational rule-based demonstration, "
            "not a confirmed fraud decision."
        )


# BATCH DETECTION
elif page == "Batch Detection":

    st.title("📁 Batch Detection")

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
            "Download CSV",
            data=data.to_csv(index=False),
            file_name="transactions.csv",
            mime="text/csv"
        )


# DATA ANALYSIS
elif page == "Data Analysis":

    st.title("📊 Data Analysis")

    st.info("Sample demonstration data")

    fig, ax = plt.subplots()

    ax.hist(df["Transaction Amount"], bins=15)

    ax.set_xlabel("Transaction Amount")
    ax.set_ylabel("Number of Transactions")

    fig.patch.set_facecolor("#FFFFFF")

    st.pyplot(fig)

    st.subheader("Transaction Dataset")

    st.dataframe(df.head(10))


# FRAUD TRENDS
elif page == "Fraud Trends":

    st.title("📈 Indian Cyber Fraud Trends")

    st.write("Reporting period: 2022–2024")

    st.info(
        "Verified official statistics will be added "
        "after checking the relevant government reports."
    )

    st.write("Data sources:")

    st.write("- NCRB")
    st.write("- Ministry of Home Affairs")
    st.write("- I4C")
    st.write("- CERT-In")


# SAFETY TIPS
elif page == "Safety Tips":

    st.title("🛡️ Cyber Safety Tips")

    tips = [
        "Never share your OTP.",
        "Never share your UPI PIN.",
        "Avoid unknown payment links.",
        "Do not install unknown APK files.",
        "Use strong passwords.",
        "Enable two-factor authentication.",
        "Verify payment requests.",
        "Report suspected financial fraud immediately."
    ]

    for tip in tips:
        st.success("✔ " + tip)

    st.header("Cybercrime Helpline: 1930")


# ABOUT PROJECT
elif page == "About Project":

    st.title("ℹ️ About FraudShield")

    st.subheader("Project Objective")

    st.write("""
    To demonstrate how data analysis and machine learning
    can help identify potentially suspicious
    financial transaction patterns.
    """)

    st.subheader("Technologies Used")

    st.write("""
    Python, NumPy, Pandas, Matplotlib,
    Streamlit and Scikit-learn.
    """)

    st.subheader("Project Period")
    st.write("2022–2024")

    st.subheader("Future Scope")

    st.write("""
    - Machine learning integration
    - Real-time fraud monitoring
    - Advanced data visualisation
    - Improved fraud prediction
    """)
