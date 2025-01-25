import streamlit as st
import pandas as pd
import os

# Function to handle Step 1: Initial Trip Details
def step_1():
    st.title("AI-Powered Travel Planner")
    st.write("Plan your perfect trip with a personalized itinerary!")

    # Step 1: Gather initial details
    st.header("Step 1: Provide Trip Details")
    with st.form(key='step_1_form'):
        destination = st.text_input("Where would you like to travel?", placeholder="e.g., Paris, Tokyo, New York")
        budget = st.selectbox("What is your budget?", ["Low", "Moderate", "Luxury"])
        trip_duration = st.number_input("How many days is your trip?", min_value=1, max_value=30, step=1)
        trip_purpose = st.text_input("What is the purpose of your trip?", placeholder="e.g., leisure, adventure, cultural exploration")
        preferences = st.text_area("Any specific preferences?", placeholder="e.g., food, activities, places to visit")

        submit_button = st.form_submit_button(label='Submit Initial Details')

    if submit_button:
        if not destination or not trip_duration or not trip_purpose:
            st.warning("Please fill in all required fields.")
        else:
            st.session_state.destination = destination
            st.session_state.budget = budget
            st.session_state.trip_duration = trip_duration
            st.session_state.trip_purpose = trip_purpose
            st.session_state.preferences = preferences
            st.session_state.step = 2
            st.success("Initial details submitted successfully!")

            # Show the "Proceed to Step 2" button after successful submission
            proceed_button = st.button("Proceed to Step 2")
            if proceed_button:
                st.session_state.step = 2  # Move to Step 2
                st.experimental_rerun()  # Rerun to show Step 2


# Function to handle Step 2: Refining Preferences
def step_2():
    st.header("Step 2: Refining Your Preferences")
    
    # Check if Step 1 details are available
    if 'destination' not in st.session_state:
        st.warning("Please complete Step 1 first.")
        return

    with st.form(key='step_2_form'):
        dietary_preferences = st.text_input("Do you have any dietary preferences or restrictions?", placeholder="e.g., vegetarian, vegan, none")
        attraction_type = st.selectbox("What type of attractions are you interested in?", ["Hidden Gems", "Top-rated Attractions", "Mix of Both"])
        mobility_concerns = st.selectbox("Do you have any mobility concerns?", ["No", "Yes"])
        accommodation_type = st.selectbox("What type of accommodation do you prefer?", ["Luxury", "Budget-Friendly", "Centrally Located"])

        submit_button = st.form_submit_button(label='Submit Refinement Details')

    if submit_button:
        st.session_state.dietary_preferences = dietary_preferences
        st.session_state.attraction_type = attraction_type
        st.session_state.mobility_concerns = mobility_concerns
        st.session_state.accommodation_type = accommodation_type
        st.session_state.step = 3
        st.success("Preferences refined successfully! Proceeding to Step 3.")

        # Save details to CSV
        user_data = {
            "Destination": st.session_state.destination,
            "Budget": st.session_state.budget,
            "Trip Duration": st.session_state.trip_duration,
            "Trip Purpose": st.session_state.trip_purpose,
            "Preferences": st.session_state.preferences,
            "Dietary Preferences": st.session_state.dietary_preferences,
            "Attraction Type": st.session_state.attraction_type,
            "Mobility Concerns": st.session_state.mobility_concerns,
            "Accommodation Type": st.session_state.accommodation_type
        }

        # Check if the CSV file exists, and create it with headers if it doesn't
        file_path = "trip_details.csv"
        if not os.path.exists(file_path):
            df = pd.DataFrame([user_data])
            df.to_csv(file_path, mode="w", header=True, index=False)  # Create the file with headers
        else:
            df = pd.DataFrame([user_data])
            df.to_csv(file_path, mode="a", header=False, index=False)  # Append data without headers

        # Display CSV content
        df = pd.read_csv(file_path)
        st.write("Here is the current data in the CSV file:")
        st.dataframe(df)

    # Show the "Proceed to Step 3" button after submission
    proceed_button = st.button("Proceed to Step 3")
    if proceed_button:
        st.session_state.step = 3  # Move to Step 3
        st.experimental_rerun()  # Rerun to show Step 3


# Function to generate activity suggestions
def generate_activity_suggestions(destination, attraction_type, mobility_concerns):
    if mobility_concerns == "Yes":
        return f"Explore accessible attractions in {destination}, such as wheelchair-friendly museums, parks with paved paths, and easy-to-reach cafes."
    elif attraction_type == "Hidden Gems":
        return f"Explore hidden gems in {destination}, such as local parks, museums, and off-the-beaten-path eateries."
    elif attraction_type == "Top-rated Attractions":
        return f"Visit top-rated attractions in {destination}, like famous landmarks, popular museums, and well-known restaurants."
    else:
        return f"Experience a mix of both hidden gems and top-rated attractions in {destination}."

# Function to generate the full itinerary
def generate_itinerary(destination, budget, trip_duration, trip_purpose, preferences, dietary_preferences, attraction_type, mobility_concerns, accommodation_type):
    itinerary = f"""
    ## Travel Itinerary for {destination}

    **Duration**: {trip_duration} days  
    **Budget**: {budget}  
    **Purpose**: {trip_purpose}  
    **Preferences**: {preferences}
    
    **Accommodation**: {accommodation_type}  
    **Dietary Preferences**: {dietary_preferences}  
    **Attraction Type**: {attraction_type}  
    **Mobility Concerns**: {mobility_concerns}
    
    ### Day-by-Day Itinerary:
    """

    # Day 1 activity
    itinerary += f"\n**Day 1**: Arrival in {destination}, check-in at {accommodation_type} accommodation. Explore {generate_activity_suggestions(destination, attraction_type, mobility_concerns)}."

    if trip_duration > 1:
        itinerary += f"\n**Day 2**: Visit top-rated attractions such as famous landmarks and museums. Enjoy local cuisine with your dietary preferences in mind."
    if trip_duration > 2:
        itinerary += f"\n**Day 3**: Explore hidden gems in the area, including local parks, hidden cafes, and more."

    return itinerary

# Main function to control the flow of steps
def main():
    if 'step' not in st.session_state:
        st.session_state.step = 1

    if st.session_state.step == 1:
        step_1()
    elif st.session_state.step == 2:
        step_2()
    elif st.session_state.step == 3:
        destination = st.session_state.destination
        budget = st.session_state.budget
        trip_duration = st.session_state.trip_duration
        trip_purpose = st.session_state.trip_purpose
        preferences = st.session_state.preferences
        dietary_preferences = st.session_state.dietary_preferences
        attraction_type = st.session_state.attraction_type
        mobility_concerns = st.session_state.mobility_concerns
        accommodation_type = st.session_state.accommodation_type

        itinerary = generate_itinerary(destination, budget, trip_duration, trip_purpose, preferences, dietary_preferences, attraction_type, mobility_concerns, accommodation_type)
        st.subheader("Your Personalized Itinerary")
        st.markdown(itinerary)

if __name__ == "__main__":
    main()
