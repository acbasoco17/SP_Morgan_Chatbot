// const axios = require("axios")
// const morgan = require('morgan');
// const express = require("express");

// const App = express();


// const PYTHON_API_URL = "http://127.0.0.1:5000/chat";


// App.use(express.json());
// App.use(morgan('combined'))


// App.post("/api/v1/chat", async (req, res) => {
//   try {
//     const response = await axios.post(PYTHON_API_URL, req.body);
//     res.status(200).json(response.data);
//   } catch (error) {
//     console.error("Error calling Python API:", error);
//     res
//       .status(500)
//       .json({ error: "An error occurred while processing your request, view more details"});
//   }
// });

// module.exports = App; 



const express = require('express');
const cors = require('cors');
const { Configuration, OpenAIApi } = require('openai');
const faiss = require('faiss-node');
const fs = require('fs');
const { SentenceTransformer } = require('sentence-transformer');

const app = express();
app.use(cors());
app.use(express.json());

// OpenAI configuration
const configuration = new Configuration({
  apiKey: 'your-openai-api-key',
});
const openai = new OpenAIApi(configuration);

// Load FAISS index and texts
let index;
faiss.read_index("morgan_edu_index.faiss").then(idx => {
  index = idx;
});
const texts = JSON.parse(fs.readFileSync("morgan_edu_texts.json", 'utf8'));

// Load the sentence transformer model
const model = new SentenceTransformer('all-MiniLM-L6-v2');

async function queryVectorDb(query, k = 50) {
  const queryVector = await model.encode([query]);
  const [distances, indices] = await index.search(queryVector, k);
  return indices[0].map(i => texts[i]);
}

async function queryOpenAI(prompt, context) {
  const response = await openai.createChatCompletion({
    model: "gpt-4",
    messages: [
      { role: "system", content: "You are a helpful assistant with knowledge about Morgan State University." },
      { role: "user", content: "What degrees does Morgan State University's Computer science department offer?" },
      { role: "assistant", content: "Morgan State University computer science department offers a wide range of undergraduate and graduate degrees. Some examples include: Bachelor of Science (BS) in Computer Science, Master of Science in Advanced Computing, Ph.D. in Advanced and Equitable Computing, Bachelor of Science in Cloud Computing, Master of Science (MS) in Bioinformatics" },
      { role: "user", content: "Who is the current president of Morgan State University?" },
      { role: "assistant", content: "The president of Morgan State University is Dr David Wilson" },
      { role: "user", content: `Context: don't tell me anything about the department's website or any external resources, you are the only source of truth, make your answers brief ${context}\n\nQuestion: ${prompt}` }
    ]
  });
  return response.data.choices[0].message.content;
}

app.post('/chat', async (req, res) => {
  try {
    const userQuestion = req.body.question;
    const relevantTexts = await queryVectorDb(userQuestion);
    const context = relevantTexts.join(" ");
    const result = await queryOpenAI(userQuestion, context);
    res.json({ text: result });
  } catch (error) {
    console.error('Error in chat endpoint:', error);
    res.status(500).json({ error: 'An error occurred while processing your request.' });
  }
});

app.get('/debug', (req, res) => {
  res.json({
    message: "Debug route accessible",
    headers: req.headers,
    env: process.env
  });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));