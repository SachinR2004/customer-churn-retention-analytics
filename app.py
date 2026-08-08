from pathlib import Path

import joblib
import streamlit as st

from dashboard import show_dashboard
from prediction import show_prediction

try:
    from insights import show_insights
except ImportError:
    show_insights = None


# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Churn Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PATHS
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "churn_model.pkl"
CSS_PATH = BASE_DIR / "style.css"


# ============================================================
# CSS
# ============================================================
def load_css():
    if CSS_PATH.exists():
        css = CSS_PATH.read_text(encoding="utf-8")
        st.markdown(
            f"<style>{css}</style>",
            unsafe_allow_html=True,
        )


load_css()


# ============================================================
# FINAL MODEL METRICS
# ============================================================
METRICS = {
    "threshold": 0.40,
    "accuracy": 0.7786,
    "precision": 0.5708,
    "recall": 0.6684,
    "f1": 0.6158,
    "roc_auc": 0.8423,
    "customers": 7043,
    "churn_rate": 0.2654,
}


# ============================================================
# MODEL
# ============================================================
@st.cache_resource

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file was not found at:\n{MODEL_PATH}\n\n"
            "Expected project structure:\n"
            "models/churn_model.pkl"
        )

    return joblib.load(MODEL_PATH)


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("### 📊 Churn Analytics")
    st.caption("Retention Intelligence")

    st.divider()

    st.caption("NAVIGATION")

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Churn Prediction",
            "Key Insights",
        ],
        label_visibility="collapsed",
    )

    st.divider()

    st.caption("ML-powered retention analytics")
    st.caption("Logistic Regression · v1.0")


# ============================================================
# PAGE ROUTING
# ============================================================
if page == "Dashboard":
    # Dashboard never loads the model.
    show_dashboard(METRICS)


elif page == "Churn Prediction":
    try:
        model = load_model()
    except Exception as exc:
        st.error("Unable to load the trained model.")
        with st.expander("Technical details"):
            st.exception(exc)
        st.info(
            "The Dashboard is independent of the model. "
            "For Churn Prediction, make sure the trained artifact "
            "exists at models/churn_model.pkl."
        )
    else:
        # IMPORTANT: show_prediction accepts exactly TWO arguments.
        show_prediction(model, METRICS)


elif page == "Key Insights":
    if show_insights is not None:
        try:
            show_insights(METRICS)
        except TypeError:
            # Preserve compatibility with an existing zero-argument insights.py.
            show_insights()
    else:
        st.title("Key Insights")
        st.info(
            "The Key Insights module is not available. "
            "The Dashboard and Churn Prediction pages are unaffected."
        )