# AI_CHATBOT_WITH_NLP-Spacy-

COMPANY : CODTECH IT SOLUTIONS

NAME : KASTURI GHADI

INTERN ID : CT04DG3368

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH KUMAR

DESCRIPTION:

Project Title: AI Chatbot With NLP(spaCy)

As part of my internship project, I developed a simple AI chatbot using Python and spaCy, a popular Natural Language Processing (NLP) library. This chatbot interacts with users through a graphical user interface (GUI) built using Tkinter. The goal was to understand the basics of NLP, improve user engagement through intelligent responses, and explore how machine learning concepts can be applied in real-world applications like virtual assistants.

The chatbot was trained using intent classification. Intents are predefined categories like greetings, weather queries, requests for stories, or even asking for help. Each intent contains example phrases and an appropriate response. When the user types a message, the chatbot uses spaCy’s medium-sized English language model (en_core_web_md) to analyze and compare the meaning of the user input with stored examples. The model returns a similarity score, which helps the chatbot decide which response is the most relevant. One of the most interesting aspects of the project was loading spaCy’s language model that includes word vectors. Word vectors are numerical representations of words in a multi-dimensional space, allowing the chatbot to understand context and meaning better than basic keyword matching. Initially, I faced limitations with the small model (en_core_web_sm), which does not include word vectors. Switching to the medium model (en_core_web_md) helped the chatbot deliver more accurate and natural responses. To make the project more user-friendly, I implemented a GUI using Python’s Tkinter library. This window-based application displays a conversation box, a text input field, and a "Send" button. The user types a message, presses enter, and the chatbot responds in real-time. Each message is color-coded to clearly separate the user’s input from the chatbot’s output. I added multiple intents such as jokes, advice, compliments, weather, and identity. These help showcase the chatbot’s versatility and make the interaction more engaging. For example, when the user types "Tell me a joke," the chatbot responds with a light-hearted joke. If someone types "Who are you?" it explains that it's a chatbot created by a student using Python.

While developing the chatbot, I learned about text preprocessing, natural language similarity, GUI programming, and error handling. I also gained experience in debugging issues related to syntax, dictionary structures, and user input edge cases. One major challenge was handling unknown inputs or phrases not clearly related to a defined intent. I solved this by setting a similarity threshold. If no input crossed the threshold, a default message would be shown asking the user to rephrase. This project helped me understand how rule-based logic and machine learning concepts can be blended to create basic AI systems. Though it's a simple chatbot, it lays the foundation for future enhancements like speech-to-text input, API integration (for weather or news), and memory of past conversations. In conclusion, building this chatbot using spaCy and Python was a great learning experience. It gave me hands-on exposure to NLP, helped improve my programming skills, and allowed me to deliver a real-time working application—all within a beginner-friendly framework.

OUTPUT:
![image](https://github.com/KasturiGhadi/AI_CHATBOT_WITH_NLP-Spacy-/blob/330aa0436cba98e884e3e974b263b885289323d7/Screenshot%202025-07-22%20200018Chatbot.png)
![image](https://github.com/KasturiGhadi/AI_CHATBOT_WITH_NLP-Spacy-/blob/95d497e1d51b77c506dc2acf2b0b8f88db4c45d5/Screenshot%202025-07-22%20200103Chatbot1.png)
