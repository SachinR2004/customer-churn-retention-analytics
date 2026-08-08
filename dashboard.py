import re
import streamlit as st


def render_html(content):
    """Cleanly render raw HTML without Streamlit parsing it as a code block."""
    clean_content = re.sub(r"^\s+", "", content, flags=re.MULTILINE)
    st.markdown(clean_content, unsafe_allow_html=True)


def section_label(text):
    render_html(f"""
    <div class="section-label">{text}</div>
    """)


def metric_card(label, value, description):
    render_html(f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-description">{description}</div>
    </div>
    """)


def show_dashboard(metrics):
    """Render the dashboard using the supplied project metrics only."""

    render_html(f"""
    <div class="hero">
        <div class="eyebrow">
            CUSTOMER RETENTION · PREDICTIVE ANALYTICS
        </div>

        <h1>
            Customer Churn
            <span>Analytics</span>
        </h1>

        <p>
            Identify customers at elevated churn risk and
            turn machine learning predictions into practical
            retention decisions.
        </p>

        <div class="model-pill">
            <strong>FINAL MODEL</strong>
            Logistic Regression
            <span>•</span>
            ROC-AUC {metrics["roc_auc"]:.4f}
            <span>•</span>
            Recall {metrics["recall"]:.2%}
            <span>•</span>
            Threshold {metrics["threshold"]:.2f}
        </div>
    </div>
    """)

    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)

    section_label("BUSINESS OVERVIEW")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card(
            "CUSTOMERS",
            f"{metrics['customers']:,}",
            "Customer records analysed",
        )

    with col2:
        metric_card(
            "CHURN RATE",
            f"{metrics['churn_rate']:.2%}",
            "Overall customer churn",
        )

    with col3:
        metric_card(
            "ROC-AUC",
            f"{metrics['roc_auc']:.4f}",
            "Model discrimination",
        )

    with col4:
        metric_card(
            "RECALL",
            f"{metrics['recall']:.2%}",
            "Churners identified",
        )

    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)

    section_label("PROJECT OBJECTIVE")

    render_html("""
    <div class="objective-card">
        <div class="objective-tag">
            BUSINESS GOAL
        </div>

        <h2>
            From churn prediction to
            <span>retention action.</span>
        </h2>

        <p>
            This project analyses customer behaviour and service
            characteristics to identify factors associated with
            customer churn.
        </p>

        <p>
            The final Logistic Regression model estimates churn
            probability so that high-risk customers can be
            identified early and targeted with proactive
            retention strategies.
        </p>
    </div>
    """)

    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)

    section_label("FINAL MODEL PERFORMANCE")

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card(
            "ACCURACY",
            f"{metrics['accuracy']:.2%}",
            "Overall classification accuracy",
        )

    with col2:
        metric_card(
            "PRECISION",
            f"{metrics['precision']:.2%}",
            "Predicted churners that churned",
        )

    with col3:
        metric_card(
            "F1 SCORE",
            f"{metrics['f1']:.2%}",
            "Balance between precision and recall",
        )

    st.markdown("<div class='small-gap'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card(
            "RECALL",
            f"{metrics['recall']:.2%}",
            "Actual churners identified",
        )

    with col2:
        metric_card(
            "ROC-AUC",
            f"{metrics['roc_auc']:.4f}",
            "Ability to separate churn classes",
        )

    with col3:
        metric_card(
            "THRESHOLD",
            f"{metrics['threshold']:.2f}",
            "Final classification threshold",
        )

    st.markdown("<div class='section-gap'></div>", unsafe_allow_html=True)

    render_html(f"""
    <div class="takeaway-card">
        <div class="takeaway-title">
            MODEL TAKEAWAY
        </div>

        <div class="takeaway-main">
            ROC-AUC of
            <span>{metrics["roc_auc"]:.4f}</span>
        </div>

        <p>
            The final Logistic Regression model demonstrates
            good ability to distinguish between customers who
            are more likely and less likely to churn.
        </p>

        <p>
            At the selected threshold of
            <strong>{metrics["threshold"]:.2f}</strong>,
            the model identifies approximately
            <strong>{metrics["recall"]:.1%}</strong>
            of actual churners.
        </p>
    </div>
    """)