# AI-Powered Travel Planner

Welcome to the AI-Powered Travel Planner, a personalized trip planning application built with Streamlit. This tool helps users plan their perfect vacation by generating customized itineraries based on user input.

## Features

- **Step 1: Initial Trip Details**
  - Users provide basic trip details, including destination, budget, duration, purpose, and preferences.
  
- **Step 2: Refining Preferences**
  - Users refine their preferences by providing dietary restrictions, attraction types, mobility concerns, and accommodation preferences.
  
- **Step 3: Personalized Itinerary**
  - Based on the provided details, the application generates a personalized travel itinerary, including day-by-day activity suggestions.

- **CSV Data Logging**
  - All input data is logged and saved in a CSV file for future reference.

## Installation

To run this application locally, follow the steps below:

### Prerequisites

- Python 3.x
- Streamlit
- Pandas

### Install dependencies

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/ai-powered-travel-planner.git
    ```

2. Install the required Python packages:
    ```bash
    pip install streamlit pandas
    ```

### Run the Application

To start the app, run the following command in the terminal:
```bash
streamlit run app.py
```

The app will open in your default web browser.

## How It Works

1. **Step 1**: Users input basic trip details like destination, budget, trip duration, purpose, and preferences.
2. **Step 2**: Users refine their preferences by specifying dietary restrictions, mobility concerns, and accommodation type.
3. **Step 3**: A personalized itinerary is generated, showcasing a detailed, day-by-day plan based on user preferences.
4. **CSV Logging**: All user input is saved into a `trip_details.csv` file for tracking and future reference.

## CSV Format

The CSV file stores the following columns:

- **Destination**: The destination of the trip (e.g., Paris, Tokyo, New York).
- **Budget**: The budget level (e.g., Low, Moderate, Luxury).
- **Trip Duration**: The duration of the trip in days.
- **Trip Purpose**: The purpose of the trip (e.g., leisure, adventure, cultural exploration).
- **Preferences**: User preferences such as food, activities, and places to visit.
- **Dietary Preferences**: Any dietary preferences or restrictions (e.g., vegetarian, vegan, none).
- **Attraction Type**: The type of attractions the user prefers (e.g., Hidden Gems, Top-rated Attractions, Mix of Both).
- **Mobility Concerns**: Whether the user has mobility concerns (e.g., Yes, No).
- **Accommodation Type**: The preferred type of accommodation (e.g., Luxury, Budget-Friendly, Centrally Located).

### Example CSV Data:

```csv
Destination,Budget,Trip Duration,Trip Purpose,Preferences,Dietary Preferences,Attraction Type,Mobility Concerns,Accommodation Type
Paris,Moderate,5,Leisure,Food,Vegetarian,Top-rated Attractions,No,Luxury
Tokyo,Low,7,Adventure,Activities,None,Mix of Both,Yes,Budget-Friendly
New York,Luxury,3,Cultural Exploration,Places to Visit,Vegan,Top-rated Attractions,No,Centrally Located
Rome,Moderate,10,Leisure,Food and Culture,None,Hidden Gems,No,Luxury
Barcelona,Low,4,Adventure,Activities and Culture,None,Mix of Both,Yes,Budget-Friendly
```

## Contributing

We welcome contributions to enhance the functionality and improve the app. If you'd like to contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
This README provides a clear description of how to set up, use, and contribute to the project, along with details about the app's functionality and the CSV logging.
