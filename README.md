# Trinity

Trinity is a speech-activated desktop assistant designed to simplify tasks, provide useful information, and entertain users through its interactive and witty responses. From playing music to fetching weather updates, Trinity is your go-to assistant to enhance productivity and add a bit of flair to your daily routine.

# Features
    - Voice Activation: Interact with Trinity using natural language commands.
    - Weather Updates: Get real-time weather information for any city.
    - Open Applications: Launch applications like Notepad and Paint.
    - Website Navigation: Open websites by simply stating their names.
    - Music Player: Play random local MP3 files from your directory.
    - Custom Greetings: Enjoy personalized and quirky responses.

# How It Works
    Trinity listens for the wake word "Trinity" and then responds to your commands.
    Once activated, it processes your request and executes the desired task.


# Prerequisites
- Python Version 3.7+
- Packages:
    speechrecognition
    pywin32
    requests
- A microphone and speaker(ofcourse).

# Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Shekhar719/Trinity.git
   cd Trinity
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OpenWeatherMap API key to the `config.py` file:
   ```python
   weatherApi = "Your openweathermap api_key"
   directory = "YOUR MUSICC FOLDER"
   apps = [
            ["Notepad", "C:\\Windows\\system32\\notepad.exe"],
            ["Chrome", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"]
          ]
   ```
   these things can be easily be tracked usign #TODO

# Running the Assistant
Run the following command to start Trinity:
```bash
python trinity.py
```

# User Instructions
1. Activate Trinity
   - By saying "Trinity".
2. Use natural language to give commands. Examples:
   - "Play music."
   - "Weather in New York?"
   - "Open Notepad."
   - "Open Google."

3. EXIT Trinity by saying "Dasvidaniya".
   - That's the russian word for goodbye.

# Command List:
- Trinity: "Trinity " for activation from standby.
- Weather: "Weather in London?" for weather report. Setup API in config first.
- Music: "Play music." to play local mp3 files. Setup directory in config first.
- Applications: "Open Notepad" or "Open Paint. Setup Apps in config first "
- Websites: "Open YouTube" or "Open GitHub."
- Standby Mode: "Pause" or "Standby" or "Enough".
- EXIT: "Dasvidaniya" to quit.

# Fine Adjustments:
- Many "#TODO" has been included in the code for your personalization

# Author
This project was created and maintained by Gaurav Shekhar.
Feel free to reach out at gaurav.shekhar7197@gmail.com for suggestions or contributions!
