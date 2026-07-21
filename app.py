import streamlit as st

# --- APP CONFIG & HEADER ---
st.title("NutriSync: Your Health Companion")
st.write("Welcome to your team's Vasudha project portal!")

with st.form(key='profile_form'):
    st.subheader("Your Personal Profile & Daily Log")
    
    # Age & General Demographics
    age = st.number_input("Age", min_value=1, max_value=120, value=15)
    
    # Auto-categorizing age group for backend logic
    if age <= 12:
        age_group = "Child"
    elif age <= 19:
        age_group = "Teenager"
    elif age <= 59:
        age_group = "Adult"
    else:
        age_group = "Senior Citizen"
    
    st.write(f"*Detected Age Category:* **{age_group}**")
    
    gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Prefer not to say", "Other"])
    if gender == "Other":
        gender_other = st.text_input("Please specify your gender")
        
    is_pregnant = False
    if gender == "Female":
        is_pregnant = st.checkbox("Are you currently pregnant? (Special category)")
        
    # Physical Metrics
    weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
    height = st.number_input("Height (cm)", min_value=1, step=1)
    
    st.markdown("---")
    st.subheader("Today's Health & Intake Check")
    
    # Nutrient Intake & Dieting Check (to catch skipping food)
    nutrient_intake = st.text_area(
        "What have you eaten today? (Log your meals/nutrient intake):",
        placeholder="e.g., Only skipped breakfast, had a small salad for lunch..."
    )
    
    appetite = st.selectbox("How is your appetite today?", ["Good", "Low", "None (Skipping meals)", "Overeating"])
    hydration = st.slider("Glasses of water today", 0, 15, 0)
    
    submit_button = st.form_submit_button(label='Update Profile & Analyze')

if submit_button:
    st.success("Data analyzed successfully!")
    
    # Smart warning for dangerous dieting/skipping food
    if "None" in appetite or "Low" in appetite or len(nutrient_intake.strip()) < 10:
        st.warning("⚠️ **NutriBuddy Alert:** Your logged intake or appetite seems very low today. Skipping meals or drastic dieting can lead to nutrient deficiencies and fatigue rather than healthy weight management. Make sure you're nourishing your body!")
    else:
        st.info("👍 Your logged pattern looks balanced. Keep prioritizing regular, healthy meals and hydration!")

# --- TIP OF THE DAY ---
st.markdown("---")
st.info("💡 **Tip of the Day:** Did you know that drinking a glass of water first thing in the morning helps jumpstart your metabolism and hydrates your brain for the day ahead?")

# --- TEAM DEMO CHAT FEATURE ---
st.subheader("💬 Ask NutriBuddy")
user_query = st.text_input("Ask a quick health or nutrition question:")
if st.button("Send to AI"):
    if user_query:
        st.write(f"**NutriBuddy:** That's a great question about '{user_query}'! Based on your profile inputs, staying hydrated and keeping a balanced intake is key today.")
    else:
        st.warning("Please type a question first.")