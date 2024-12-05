# Ask Benny (Morgan Computer Science Chatbot)

## Description
AskBenny is an AI chatbot well-versed in computer science and Morgan State's suggested course curriculum that acts as an academic advisor for computer science majors. The chatbot can record students' interests through written conversations. Then, using the collected data, it can provide tailored recommendations for courses, clubs, internships, research topics, and more based on the Morgan Website.

## Team Members
- Ana Basoco - Chatbot Webpage Development
- Ashley Pryor - Chatbot Webpage Development
- Godsheritage Adeoye - Web Scrapping & Backend Setup
- Lerone Joyner - Prompt Engineering & Backend Setup

## Installation
(Only works on MacOS)
```bash
# Step-by-step installation instructions
git clone [repository-url]
npm install   # or equivalent for your project
pip install -r requirements.txt
python3 openai.py
node run dev # run this in a seperate terminal from openai.py
```

## Usage
Explain how to use your project. Include code examples if applicable:
```python
# Example code
from project import main
main.run()
```

## Features
- Feature 1: Brief description
- Feature 2: Brief description
- Feature 3: Brief description

## Project Structure
```
SP_MORGAN_CHATBOT/
├── Client/         # Webpage files
   ├── node_module/    # Will appear on npm install (in installation step)
   ├── public/         # Will appear automatically 
      ├── vite.svg     
   ├── src/            # Source files
      ├── assets/
         ├── react.svg  
      ├── App.css      # Style sheet   
      ├── App.jsx      # Main frontend functionality  
      ├── index.css  
      ├── main.jsx  
├── Server/         # Database files
   ├── Server/      # Database files
      ├── App.js    # Configures OpenAI, loads database, interprets text input
      ├── Server.js # Creates and listens to the server
   ├── morgan_edu_data.csv  
   ├── morgan_edu_data.json  
   ├── morgan_edu_data2.csv
   ├── morgan_edu_texts.npy
   ├── openAI.py    # Takes user input and returns 
   ├── pyvenv.cfg
   ├── scrapper.py
   ├── terminal_voice_chatbot.py
   ├── vectorDB.py
├── src/            # Source files
└── README.md       # This file - Documentation
```

## Technologies Used
- Language(s): Python, HTML/CSS/Javascript
- Framework(s): React
- Database: Faiss datbase (Facebook AI Similarity Search)
- Other tools: OpenAI

## Contributing
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Testing
Explain how to run tests:
```bash
npm test  # or equivalent for your project
```

## Known Issues
Can't currently add new data through the user interface. The only way to manipulate the chatbot data is
through the backend file morgan_edu_data.csv.

## Future Improvements
- FAQs Webpage for Prompt Autofilling
- Voice Assistance
- File Uploading for User Questions
