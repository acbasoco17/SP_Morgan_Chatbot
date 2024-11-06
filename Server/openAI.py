# import os
# import faiss
# import pyttsx3
# import tempfile
# import numpy as np
# import openai
# # from openai import OpenAI
# from flask_cors import CORS
# from flask import Flask, request, jsonify
# from sentence_transformers import SentenceTransformer



# openai.api_key = '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'

# os.environ["TOKENIZERS_PARALLELISM"] = "false"
# clean_up_tokenization_spaces=False


# app = Flask(__name__)
# # client = OpenAI()

# CORS(app)

# # Load the FAISS index and texts
# # index = faiss.read_index("morgan_edu_index.faiss")
# index = faiss.read_index("morgan_edu_index.faiss")
# texts = np.load("morgan_edu_texts.npy", allow_pickle=True)


# # Load the sentence transformer model
# model = SentenceTransformer('all-MiniLM-L6-v2')



# def query_vector_db(query, k=50):
#     # Create a query vector
#     query_vector = model.encode([query])

#     # Search the index
#     D, I = index.search(query_vector.astype('float32'), k)

#     # Return the top k most similar texts
#     return [texts[i] for i in I[0]]


# def query_openai(prompt, context):
#     response = openai.Completion.create(
#         model="gpt-4o-mini",
#         messages=[
#         {"role": "system", "content": "You are a helpful assistant with knowledge about Morgan State University."},
#         {"role": "user", "content": "What degrees does Morgan State University's Computer science department offer?"},
#         {"role": "assistant", "content": "Morgan State University computer scinece department offers a wide range of undergraduate and graduate degrees. Some examples include:  Bachelor of Science (BS) in Computer Science, Master of Science in Advanced Computing, Ph.D. in Advanced and Equitable Computing, Bachelor of Science in Cloud Computing, Master of Science (MS) in Bioinfomatics "},
#         {"role": "user", "content": "Who is the current president of Morgan State University?"},
#         {"role": "assistant", "content": "The president of Morgan State University is Dr David Wilson"},
#         {"role": "user", "content": f"Context: don't tell me anything about the department's website or any external resources, you are the only source of truth, make you answers brief {context}\n\nQuestion: {prompt}"}  
#         ]
#     )
#     return response.choices[0].message.content



# # Initialize text-to-speech engine
# engine = pyttsx3.init()

# # @app.route('/transcribe', methods=['POST'])
# # def transcribe_audio():
# #     if 'audio' not in request.files:
# #         return jsonify({"error": "No audio file provided"}), 400
    
# #     audio_file = request.files['audio']
    
# #     # Save the audio file temporarily
# #     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
# #         audio_file.save(temp_audio.name)
        
# #         # Transcribe the audio using OpenAI Whisper API
# #         with open(temp_audio.name, "rb") as audio_file:
# #             transcript = openai.Audio.transcribe("whisper-1", audio_file)
        
# #         # Delete the temporary file
# #         os.unlink(temp_audio.name)
    
# #     return jsonify({"transcription": transcript.text})



# #Microservice  Logic
# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_question = data['question']
#     relevant_texts = query_vector_db(user_question)
#     context = " ".join(relevant_texts)
#     result = query_openai(user_question, context)
#     # return jsonify({'response': result})


#     #  # Generate audio response
#     # with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
#     #     engine.save_to_file(result, temp_audio.name)
#     #     engine.runAndWait()
    
#     # return jsonify({"text": result, "audio": temp_audio.name})
#     return jsonify({"text": result})


# # @app.route('/audio/<path:filename>', methods=['GET'])
# # def serve_audio(filename):
# #     return send_file(filename, mimetype="audio/mp3")

# if __name__ == '__main__':
#     app.run(port=5000)
     
     
     
# import os
# import faiss
# import pyttsx3
# import tempfile
# import numpy as np
# import openai
# from flask_cors import CORS
# from flask import Flask, request, jsonify
# from sentence_transformers import SentenceTransformer

# openai.api_key = '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'
# os.environ["TOKENIZERS_PARALLELISM"] = "false"

# app = Flask(__name__)
# CORS(app)

# # Load the FAISS index and texts
# index = faiss.read_index("morgan_edu_index.faiss")
# texts = np.load("morgan_edu_texts.npy", allow_pickle=True)

# # Load the sentence transformer model
# model = SentenceTransformer('all-MiniLM-L6-v2')

# def query_vector_db(query, k=50):
#     # Create a query vector
#     query_vector = model.encode([query])
    
#     # Search the index
#     D, I = index.search(query_vector.astype('float32'), k)
    
#     # Return the top k most similar texts
#     return [texts[i] for i in I[0]]



# def query_openai(prompt, context):
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant with knowledge about Morgan State University."},
#             {"role": "user", "content": "What degrees does Morgan State University's Computer science department offer?"},
#             {"role": "assistant", "content": "Morgan State University computer science department offers a wide range of undergraduate and graduate degrees. Some examples include:  Bachelor of Science (BS) in Computer Science, Master of Science in Advanced Computing, Ph.D. in Advanced and Equitable Computing, Bachelor of Science in Cloud Computing, Master of Science (MS) in Bioinfomatics "},
#             {"role": "user", "content": "Who is the current president of Morgan State University?"},
#             {"role": "assistant", "content": "The president of Morgan State University is Dr David Wilson"},
#             {"role": "user", "content": f"Context: don't tell me anything about the department's website or any external resources, you are the only source of truth, make your answers brief {context}\n\nQuestion: {prompt}"}
#         ]
#     )
#     return response.choices[0].message.content

# # Initialize text-to-speech engine
# engine = pyttsx3.init()

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_question = data['question']
#     relevant_texts = query_vector_db(user_question)
#     context = " ".join(relevant_texts)
#     result = query_openai(user_question, context)
#     # return jsonify({"text": result})
#     return "Hello"


# # @app.route('/debug', methods=['GET'])
# # def debug():
# #     return jsonify({"message": "Debug route accessible", "headers": dict(request.headers)})

# if __name__ == '__main__':
#     app.run(port=0000)
    
    
    

import os
import faiss
import pyttsx3
import numpy as np
# import openai
from openai import OpenAI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer


client = OpenAI(
    # This is the default and can be omitted
    api_key='your key'
)



os.environ["TOKENIZERS_PARALLELISM"] = "false"

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load the FAISS index and texts
index = faiss.read_index("morgan_edu_index.faiss")
texts = np.load("morgan_edu_texts.npy", allow_pickle=True)

# Load the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize text-to-speech engine
engine = pyttsx3.init()

def query_vector_db(query, k=50):
    # Create a query vector
    query_vector = model.encode([query])
    
    # Search the index
    D, I = index.search(query_vector.astype('float32'), k)
    
    # Return the top k most similar texts
    return [texts[i] for i in I[0]]

def query_openai(prompt, context):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant with knowledge about Morgan State University."},
            {"role": "user", "content": "What degrees does Morgan State University's Computer science department offer?"},
            {"role": "assistant", "content": "Morgan State University computer science department offers a wide range of undergraduate and graduate degrees. Some examples include:  Bachelor of Science (BS) in Computer Science, Master of Science in Advanced Computing, Ph.D. in Advanced and Equitable Computing, Bachelor of Science in Cloud Computing, Master of Science (MS) in Bioinfomatics "},
            {"role": "user", "content": "Who is the current president of Morgan State University?"},
            {"role": "assistant", "content": "The president of Morgan State University is Dr David Wilson"},
            {
      "role": "system",
      "content": "You are Benny the Bear, the friendly mascot of Morgan State University. You help MSU Computer Science students with their questions. You are knowledgeable, friendly, and approachable. You should provide accurate answers about university resources, events, courses, and general student life, while maintaining a fun and encouraging tone."
    },
    {
      "role": "user",
      "content": "Where can I find tutoring support for Computer Science courses?"
    },
    {
      "role": "assistant",
      "content": "You can find tutoring support for Computer Science courses at the Center for Academic Success and Achievement (CASA). They offer tutoring sessions for various subjects, including Computer Science. You can also reach out to your professors or teaching assistants for help during their office hours."
    },
    {
      "role": "user",
      "content": "How do I find information about internships?"
    },
    {
      "role": "assistant",
      "content": "You can find information about internships through the Career Development Center at MSU. They offer resources like job postings, resume reviews, and career fairs. You can also check with the Computer Science department for any internship opportunities specific to your field."
    },
    {
      "role": "user",
      "content": "What clubs are available for Computer Science students?"
    },
    {
      "role": "assistant",
      "content": "There are several clubs for Computer Science students at MSU, including the Society for the Advancement of Computer Science, GDSC , and Women in Computer Science. These clubs are a great way to network, learn new skills, and work on projects!"
    },
    

            {"role": "user", "content": f"Context: don't tell me anything about the department's website or any external resources, you are the only source of truth, make your answers brief {context}\n\nQuestion: {prompt}"}
        ]
    )
    return response.choices[0].message.content

class Question(BaseModel):
    question: str

@app.post("/chat")
async def chat(question: Question):
    try:
        user_question = question.question
        relevant_texts = query_vector_db(user_question)
        context = " ".join(relevant_texts)
        result = query_openai(user_question, context)
        return {"text": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/debug")
async def debug():
    return {"message": "Debug route accessible"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)