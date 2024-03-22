import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

from scipy.stats import norm
import numpy as np
def perform_ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    # Calculate conversion rates for control and treatment groups
    control_conversion_rate = control_conversions / control_visitors
    treatment_conversion_rate = treatment_conversions / treatment_visitors
    
    # Calculate pooled probability
    pooled_prob = (control_conversions + treatment_conversions) / (control_visitors + treatment_visitors)
    
    # Calculate pooled standard error
    pooled_se = np.sqrt(pooled_prob * (1 - pooled_prob) * (1/control_visitors + 1/treatment_visitors))
    
    # Calculate Z-score for the given confidence level
    if confidence_level == 90:
        z_critical = norm.ppf(0.95)
    elif confidence_level == 95:
        z_critical = norm.ppf(0.975)
    elif confidence_level == 99:
        z_critical = norm.ppf(0.995)
    else:
        raise ValueError("Confidence level should be one of 90, 95, or 99.")
    
    # Calculate margin of error
    margin_of_error = z_critical * pooled_se
    
    # Calculate the difference in conversion rates
    difference = treatment_conversion_rate - control_conversion_rate
    
    # Performing hypothesis testing
    if difference > margin_of_error:
        return "Experiment Group is Better"
    elif difference < -margin_of_error:
        return "Control Group is Better"
    else:
        return "Indeterminate"

result = perform_ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions,confidence_level)
print("AB Test Result:", result)

# Streamlit app
def main():
    st.title("A/B Test Hypothesis Testing")
    
    # Input fields
    control_visitors = st.number_input("Control Group Visitors", min_value=0, step=1)
    control_conversions = st.number_input("Control Group Conversions", min_value=0, step=1)
    treatment_visitors = st.number_input("Treatment Group Visitors", min_value=0, step=1)
    treatment_conversions = st.number_input("Treatment Group Conversions", min_value=0, step=1)
    confidence_level = st.selectbox("Confidence Level", [90, 95, 99])
    
    # Perform A/B test
    if st.button("Perform A/B Test"):
        result = perform_ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
        st.write("Result:", result)

    print(control_visitors)
    print(control_conversions)
    print(treatment_visitors)
    print(treatment_conversions)
    print(confidence_level)

if __name__ == "__main__":
    main()
