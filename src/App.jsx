import { useState } from 'react'
import './App.css'
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css'
import { MainContainer, ChatContainer, MessageList, Message, MessageInput, TypingIndicator, ConversationHeader, Avatar, VoiceCallButton } from "@chatscope/chat-ui-kit-react"

const API_KEY = "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"

function App() {
  const [isTyping, setIsTyping] = useState(false)
  const [messages, setMessages] = useState([
    {
      message: "Hi, I am Morgan's Chatbot! What can I help you with?",
      direction: "incoming",
      sender: "ChatGPT"
    }
  ])

  const handleSend = async(message) => {
    const newMessage = {
      message: message,
      direction: "outgoing",
      sender: "user",
    }

    const newMessages = [...messages, newMessage]

    //update messages state
    setMessages(newMessages);

    // set a typing indicator
    setIsTyping(true);

    // process message to chatgpt
    await processMessageToChatGPT(newMessages);
  }

  async function processMessageToChatGPT(chatMessages) {
    let apiMessages = chatMessages.map((messageObject) => {
      let role = "";
      if (messageObject.sender === "ChatGPT") {
        role="assistant"
      } else {
        role="user"
      }
      return {role: role, content: messageObject.message}
    });

    const systemMessage = {
      role: "system",
      content: "Explain like a college administrator" // Explain like a college administrator
    }

    const apiRequestBody = {
      "model": "gpt-3.5-turbo",
      "messages": [
        systemMessage,
        ...apiMessages
      ]
    }

    await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(apiRequestBody)
    }).then((data) => {
      return data.json();
    }).then ((data) => {
      console.log(data.choices[0].message.content);
      setMessages(
        [...chatMessages, {
          message: data.choices[0].message.content,
          sender: "ChatGPT",
          direction: "incoming"
        }]
      );
      setIsTyping(false)
    });
  }

  return (
      <div className="App">
        <div style={{position: "absolute", width: "100%", height: "100%" }}>
          
          <ConversationHeader>
            <Avatar name='Morgan Chatbot' src='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.mascotdb.com%2Fsites%2Fdefault%2Ffiles%2Flogos%2F40577.jpg&f=1&nofb=1&ipt=a3b77ebdd67e4e43746d7fa2ac7e09fdf98ad75e4719dff2e71ddf77aecc1b3a&ipo=images'/>
            <ConversationHeader.Content userName="Ask Benny Chat"/>
          </ConversationHeader>

          <MainContainer>
            <ChatContainer className='my-container'>
              <MessageList 
              scrollBehavior='smooth'
              style={{backgroundColor: "#ea8556"}}
              typingIndicator={isTyping ? <TypingIndicator content="Benny is typing"/>: null}
              >
                {messages.map((messages , i) => {
                  return <Message key={i} model={messages} />
                })}
              </MessageList>
              <MessageInput placeholder='Type message here' onSend={handleSend}/>
            </ChatContainer>
          </MainContainer>
        </div>
    </div>
  )
}

export default App
