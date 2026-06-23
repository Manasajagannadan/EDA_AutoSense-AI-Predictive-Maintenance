# import streamlit as st
# import requests

# API_URL = "http://127.0.0.1:8000/predict"

# st.title("Predictive Maintenance Dashboard")

# st.subheader("Machine Parameters")

# Type = st.number_input("Type", value=0)

# Air_temperature_K = st.number_input(
#     "Air Temperature (K)",
#     value=298.0
# )

# Process_temperature_K = st.number_input(
#     "Process Temperature (K)",
#     value=308.0
# )

# Rotational_speed_rpm = st.number_input(
#     "Rotational Speed (RPM)",
#     value=1500.0
# )

# Torque_Nm = st.number_input(
#     "Torque (Nm)",
#     value=40.0
# )

# Tool_wear_min = st.number_input(
#     "Tool Wear (min)",
#     value=10.0
# )

# if st.button("Predict"):

#     payload = {
#         "Type": Type,
#         "Air_temperature_K": Air_temperature_K,
#         "Process_temperature_K": Process_temperature_K,
#         "Rotational_speed_rpm": Rotational_speed_rpm,
#         "Torque_Nm": Torque_Nm,
#         "Tool_wear_min": Tool_wear_min,

#         "Thermal_Stress_Index":
#             Process_temperature_K - Air_temperature_K,

#         "Wear_Efficiency":
#             Tool_wear_min / Rotational_speed_rpm,

#         "Operational_Load_Index":
#             Torque_Nm * Rotational_speed_rpm,

#         "Temperature_Ratio":
#             Process_temperature_K / Air_temperature_K,

#         "Failure_Risk_Score":
#             Torque_Nm * Tool_wear_min
#     }

#     response = requests.post(
#         API_URL,
#         json=payload
#     )

#     result = response.json()

#     st.success(
#         f"Status: {result['status']}"
#     )

#     st.metric(
#         "Failure Probability",
#         f"{result['failure_probability']:.4%}"
#     )


import streamlit as st
import requests

st.set_page_config(
    page_title="AutoSense AI",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ AutoSense AI")
st.subheader("Intelligent Predictive Maintenance System")

st.sidebar.header("Machine Parameters")

machine_type = st.sidebar.selectbox(
    "Machine Type",
    [0, 1, 2]
)

air_temp = st.sidebar.number_input(
    "Air Temperature (K)",
    value=298.2
)

process_temp = st.sidebar.number_input(
    "Process Temperature (K)",
    value=308.7
)

rpm = st.sidebar.number_input(
    "Rotational Speed (RPM)",
    value=1408
)

torque = st.sidebar.number_input(
    "Torque (Nm)",
    value=40
)

tool_wear = st.sidebar.number_input(
    "Tool Wear (min)",
    value=9
)

if st.sidebar.button("Predict Failure"):

    thermal_stress = process_temp - air_temp
    wear_efficiency = tool_wear / (rpm + 1)
    operational_load = torque * rpm
    temperature_ratio = process_temp / air_temp
    failure_risk_score = torque * tool_wear

    payload = {
        "Type": machine_type,
        "Air_temperature_K": air_temp,
        "Process_temperature_K": process_temp,
        "Rotational_speed_rpm": rpm,
        "Torque_Nm": torque,
        "Tool_wear_min": tool_wear,
        "Thermal_Stress_Index": thermal_stress,
        "Wear_Efficiency": wear_efficiency,
        "Operational_Load_Index": operational_load,
        "Temperature_Ratio": temperature_ratio,
        "Failure_Risk_Score": failure_risk_score
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload,
            timeout=10
        )

        response.raise_for_status()

        result = response.json()

        st.header("Prediction Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Machine Status",
                result["status"]
            )

        with col2:
            st.metric(
                "Risk Level",
                result["risk_level"]
            )

        with col3:
            st.metric(
                "Failure Probability",
                f"{result['failure_probability']:.2f}%"
            )

        st.subheader("Risk Meter")

        risk_score = result["failure_probability"] / 100

        st.progress(risk_score)

        if result["failure_probability"] < 20:
            st.success("🟢 Low Risk")
        elif result["failure_probability"] < 70:
            st.warning("🟡 Medium Risk")
        else:
            st.error("🔴 Critical Risk")

        st.markdown("---")

        if result["status"] == "Failure":
            st.error("⚠️ Machine Failure Predicted")
        else:
            st.success("✅ Machine Operating Normally")

        st.subheader("Recommendation")
        st.info(result["recommendation"])

        st.subheader("Engineered Features")

        c1, c2 = st.columns(2)

        with c1:
            st.write(
                f"Thermal Stress Index: {thermal_stress:.2f}"
            )
            st.write(
                f"Wear Efficiency: {wear_efficiency:.6f}"
            )
            st.write(
                f"Temperature Ratio: {temperature_ratio:.4f}"
            )

        with c2:
            st.write(
                f"Operational Load Index: {operational_load:.2f}"
            )
            st.write(
                f"Failure Risk Score: {failure_risk_score:.2f}"
            )

    except requests.exceptions.ConnectionError:
        st.error(
            "Cannot connect to FastAPI server. Start api.py first."
        )

    except Exception as e:
        st.error(
            f"Error: {str(e)}"
        )

st.markdown("---")
st.caption("AutoSense AI | Predictive Maintenance Dashboard")