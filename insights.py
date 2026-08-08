import streamlit as st


def html(content):
    st.html(content)


def section_label(text):

    html(
        f"""
        <div class="section-label">
            {text}
        </div>
        """
    )


def show_insights(metrics):

    # ========================================================
    # HERO
    # ========================================================

    html(
        """
        <section class="hero">

            <div class="eyebrow">
                MODEL INTERPRETATION
            </div>

            <h1>
                Key Churn
                <span>Drivers</span>
            </h1>

            <p>
                Factors identified by the final Logistic Regression
                model and translated into actionable retention
                strategies.
            </p>

        </section>
        """
    )


    # ========================================================
    # RISK DRIVERS
    # ========================================================

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    section_label("HIGHER CHURN RISK")

    left, right = st.columns(2)

    with left:

        html(
            """
            <div class="insight-card risk">

                <div class="insight-label">
                    HIGHER RISK
                </div>

                <h2>
                    Fiber Optic Internet
                </h2>

                <p>
                    Fiber optic customers show substantially
                    higher churn odds in the final model.
                </p>

            </div>
            """
        )

    with right:

        html(
            """
            <div class="insight-card risk">

                <div class="insight-label">
                    HIGHER RISK
                </div>

                <h2>
                    Electronic Check
                </h2>

                <p>
                    Electronic check payment is associated
                    with higher churn risk.
                </p>

            </div>
            """
        )


    # ========================================================
    # LOWER RISK
    # ========================================================

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    section_label("LOWER CHURN RISK")

    left, right = st.columns(2)

    with left:

        html(
            """
            <div class="insight-card positive">

                <div class="insight-label">
                    PROTECTIVE FACTOR
                </div>

                <h2>
                    Longer-term Contracts
                </h2>

                <p>
                    One-year and especially two-year contracts
                    are associated with lower churn.
                </p>

            </div>
            """
        )

    with right:

        html(
            """
            <div class="insight-card positive">

                <div class="insight-label">
                    PROTECTIVE FACTOR
                </div>

                <h2>
                    Online Security & Tech Support
                </h2>

                <p>
                    Customers using these services show
                    lower churn odds.
                </p>

            </div>
            """
        )


    # ========================================================
    # RETENTION STRATEGY
    # ========================================================

    st.markdown("<div class='section-space'></div>", unsafe_allow_html=True)

    section_label("RECOMMENDED RETENTION STRATEGY")

    recommendations = [

        "Target high-risk fiber-optic customers with proactive retention offers.",

        "Encourage longer-term contracts through discounts or incentives.",

        "Promote Online Security and Tech Support services.",

        "Investigate customers using electronic-check payments.",

        "Prioritize newer customers for early retention interventions."
    ]


    for recommendation in recommendations:

        html(
            f"""
            <div class="recommendation">

                <span class="recommendation-arrow">
                    →
                </span>

                {recommendation}

            </div>
            """
        )