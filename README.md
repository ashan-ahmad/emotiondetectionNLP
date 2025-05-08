# Emotion Detection Application

This project is an AI-based web application that performs emotion detection on customer feedback using IBM Watson NLP libraries. The application analyzes text input and identifies emotions such as anger, disgust, fear, joy, and sadness, along with their respective scores and the dominant emotion.

## Features
- Analyze text input to detect emotions.
- Provides scores for anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion in the text.
- Web deployment using Flask for user interaction.
- Error handling for invalid or blank inputs.
- Static code analysis for code quality assurance.

## Project Structure
```
final_project/
│
├── EmotionDetection/
│   ├── __init__.py
│   ├── emotion_detection.py
│
├── static/
│   └── mywebscript.js
│
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Setup Instructions

### Prerequisites
- Python 3.x
- `requests` library (Install using `pip install requests`)
- Flask (Install using `pip install flask`)
- PyLint (Optional, for static code analysis: `pip install pylint`)

### Steps to Run the Application
1. **Clone the Repository**  
   Clone the project repository to your local machine:
   ```bash
   git clone <repository-url>
   cd final_project
   ```

2. **Run the Emotion Detection Script**  
   Test the `emotion_detection.py` script in a Python shell:
   ```python
   from EmotionDetection.emotion_detection import emotion_detector
   print(emotion_detector("I love this new technology."))
   ```

3. **Run Unit Tests**  
   Execute the unit tests to validate the application:
   ```bash
   python test_emotion_detection.py
   ```

4. **Deploy the Application**  
   Start the Flask server:
   ```bash
   python server.py
   ```
   Access the application at `http://localhost:5000`.

5. **Test the Web Application**  
   Enter text in the web interface to analyze emotions.

### Error Handling
- For blank inputs, the application returns a message: `Invalid text! Please try again!`.

### Static Code Analysis
Run PyLint on `server.py` to ensure code quality:
```bash
pylint server.py
```

## Example Output
For the input text: `I love my life`, the application returns:
```json
{
  "anger": 0.006274985,
  "disgust": 0.0025598293,
  "fear": 0.009251528,
  "joy": 0.9680386,
  "sadness": 0.049744144,
  "dominant_emotion": "joy"
}
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
