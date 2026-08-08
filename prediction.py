import re
import pandas as pd
import streamlit as st


THRESHOLD = 0.40

MODEL_FEATURES = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges",
    "service_count",
]

SERVICE_COLUMNS = [
    "PhoneService",
    "MultipleLines",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
]


def render_html(content):
    """Cleanly render raw HTML without Streamlit parsing it as a code block."""
    clean_content = re.sub(r"^\s+", "", content, flags=re.MULTILINE)
    st.markdown(clean_content, unsafe_allow_html=True)


def build_model_input(
    gender,
    senior_citizen,
    partner,
    dependents,
    tenure,
    phone_service,
    multiple_lines,
    internet_service,
    online_security,
    online_backup,
    device_protection,
    tech_support,
    streaming_tv,
    streaming_movies,
    contract,
    paperless_billing,
    payment_method,
    monthly_charges,
    total_charges,
):
    """Build the exact feature DataFrame expected by the model."""

    row = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
    }

    row["service_count"] = sum(
        str(row[column]).strip().lower() == "yes"
        for column in SERVICE_COLUMNS
    )

    return pd.DataFrame([row], columns=MODEL_FEATURES)


def show_prediction(model, metrics):
    threshold = float(metrics.get("threshold", THRESHOLD))

    render_html("""
    <div class="prediction-hero">
        <div class="eyebrow">
            PREDICTIVE ANALYTICS
        </div>

        <h1>
            Customer Churn
            <span>Prediction</span>
        </h1>

        <p>
            Enter customer information to estimate churn
            probability and determine the appropriate
            retention action.
        </p>
    </div>
    """)

    render_html(f"""
    <div class="threshold-box">
        <div>
            <strong>Classification threshold</strong>
            <span>{threshold:.2f}</span>
        </div>

        <p>
            Customers with predicted probability ≥
            {threshold:.2f} are classified as high churn risk.
        </p>
    </div>
    """)

    st.markdown("<div class='space'></div>", unsafe_allow_html=True)
    render_html("<div class='section-label'>CUSTOMER PROFILE</div>")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
            "Gender",
            ["Female", "Male"],
        )

        senior_citizen = st.selectbox(
            "Senior Citizen",
            [0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes",
        )

        partner = st.selectbox(
            "Partner",
            ["No", "Yes"],
        )

        dependents = st.selectbox(
            "Dependents",
            ["No", "Yes"],
        )

        tenure = st.number_input(
            "Tenure (months)",
            min_value=0,
            max_value=100,
            value=12,
            step=1,
        )

        phone_service = st.selectbox(
            "Phone Service",
            ["Yes", "No"],
        )

        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["No", "Yes", "No phone service"],
        )

        internet_service = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"],
        )

        online_security = st.selectbox(
            "Online Security",
            ["No", "Yes", "No internet service"],
        )

        online_backup = st.selectbox(
            "Online Backup",
            ["No", "Yes", "No internet service"],
        )

    with col2:
        device_protection = st.selectbox(
            "Device Protection",
            ["No", "Yes", "No internet service"],
        )

        tech_support = st.selectbox(
            "Tech Support",
            ["No", "Yes", "No internet service"],
        )

        streaming_tv = st.selectbox(
            "Streaming TV",
            ["No", "Yes", "No internet service"],
        )

        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["No", "Yes", "No internet service"],
        )

        contract = st.selectbox(
            "Contract",
            [
                "Month-to-month",
                "One year",
                "Two year",
            ],
        )

        paperless_billing = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"],
        )

        payment_method = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)",
            ],
        )

        monthly_charges = st.number_input(
            "Monthly Charges",
            min_value=0.0,
            value=70.0,
            step=1.0,
        )

        total_charges = st.number_input(
            "Total Charges",
            min_value=0.0,
            value=1000.0,
            step=10.0,
        )

    st.markdown("<div class='small-space'></div>", unsafe_allow_html=True)

    service_count_preview = sum(
        value == "Yes"
        for value in [
            phone_service,
            multiple_lines,
            online_security,
            online_backup,
            device_protection,
            tech_support,
            streaming_tv,
            streaming_movies,
        ]
    )

    render_html(f"""
    <div class="prediction-note">
        <strong>Model-ready customer profile</strong>
        <span>
            All customer attributes required by the trained
            Logistic Regression pipeline are included in this
            prediction form.
        </span>
        <small>Service count: {service_count_preview}</small>
    </div>
    """)

    st.markdown("<div class='small-space'></div>", unsafe_allow_html=True)

    predict = st.button(
        "Predict Churn Risk",
        use_container_width=True,
        type="primary",
    )

    if not predict:
        return

    input_data = build_model_input(
        gender=gender,
        senior_citizen=senior_citizen,
        partner=partner,
        dependents=dependents,
        tenure=tenure,
        phone_service=phone_service,
        multiple_lines=multiple_lines,
        internet_service=internet_service,
        online_security=online_security,
        online_backup=online_backup,
        device_protection=device_protection,
        tech_support=tech_support,
        streaming_tv=streaming_tv,
        streaming_movies=streaming_movies,
        contract=contract,
        paperless_billing=paperless_billing,
        payment_method=payment_method,
        monthly_charges=monthly_charges,
        total_charges=total_charges,
    )

    try:
        probability = float(model.predict_proba(input_data)[0][1])
        high_risk = probability >= threshold

        st.markdown("<div class='space'></div>", unsafe_allow_html=True)

        if high_risk:
            render_html(f"""
            <div class="prediction-result high-risk">
                <div class="result-label">
                    HIGH CHURN RISK
                </div>

                <div class="result-probability">
                    {probability:.1%}
                </div>

                <div class="result-title">
                    Immediate retention attention recommended
                </div>

                <p>
                    This customer has a predicted churn
                    probability above the classification threshold.
                    Consider proactive retention intervention.
                </p>

                <div class="action-box">
                    Recommended action:
                    <strong>
                        Review retention offers, contract options,
                        support services and customer experience.
                    </strong>
                </div>
            </div>
            """)

        else:
            render_html(f"""
            <div class="prediction-result low-risk">
                <div class="result-label">
                    LOWER CHURN RISK
                </div>

                <div class="result-probability">
                    {probability:.1%}
                </div>

                <div class="result-title">
                    Customer currently appears relatively stable
                </div>

                <p>
                    The predicted churn probability is below
                    the classification threshold.
                </p>

                <div class="action-box">
                    Recommended action:
                    <strong>
                        Continue normal engagement and monitor
                        future customer behaviour.
                    </strong>
                </div>
            </div>
            """)

    except Exception as error:
        st.error("Prediction could not be generated.")
        st.warning(
            "The prediction form contains the complete feature set "
            "required by the trained model. If this message remains, "
            "the model artifact and training schema are different."
        )
        with st.expander("Technical details"):
            st.exception(error)