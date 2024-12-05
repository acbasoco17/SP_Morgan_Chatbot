import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";
import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  TypingIndicator,
  ConversationHeader,
  Avatar,
  VoiceCallButton,
} from "@chatscope/chat-ui-kit-react";

const API_KEY = "Your API_KEY here";

function App() {
  const [isTyping, setIsTyping] = useState(false);
  const [messages, setMessages] = useState([
    {
      message: "Hi, I am Morgan's Chatbot! What can I help you with?",
      direction: "incoming",
      sender: "ChatGPT",
    },
  ]);

  const handleSend = async (message) => {
    const newMessage = {
      message: message,
      direction: "outgoing",
      sender: "user",
    };

    const newMessages = [...messages, newMessage];

    //update messages state
    setMessages(newMessages);

    // set a typing indicator
    setIsTyping(true);

    // process message to chatgpt
    await processMessageToChatGPT(newMessages);
  };

  async function processMessageToChatGPT(chatMessages) {
    // let apiMessages = chatMessages.pop().message;

    let apiMessages = chatMessages.map((messageObject) => {
      let role = "";
      if (messageObject.sender === "ChatGPT") {
        role = "assistant";
      } else {
        role = "user";
      }
      return { role: role, content: messageObject.message };
    });

    let userMessage = "";
    for (let i = chatMessages.length - 1; i >= 0; i--) {
      if (chatMessages[i].sender !== "ChatGPT") {
        userMessage = chatMessages[i].message;
        break;
      }
    }

    const apiRequestBody = {
      question: userMessage,
    };

    console.log(apiRequestBody);

    await fetch("http://0.0.0.0:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(apiRequestBody),
    })
      .then((data) => {
        return data.json();
      })
      .then((data) => {
        console.log(data.text);
        setMessages([
          ...chatMessages,
          {
            message: data.text,
            sender: "ChatGPT",
            direction: "incoming",
          },
        ]);
        setIsTyping(false);
      });
  }

  // async function processMessageToChatGPT(chatMessages) {
  //   let apiMessages = chatMessages.map((messageObject) => {
  //     let role = "";
  //     if (messageObject.sender === "ChatGPT") {
  //       role="assistant"
  //     } else {
  //       role="user"
  //     }
  //     return {role: role, content: messageObject.message}
  //   });

  //   const systemMessage = {
  //     role: "system",
  //     content: "Explain like a college administrator" // Explain like a college administrator
  //   }

  //   const apiRequestBody = {
  //     "model": "gpt-3.5-turbo",
  //     "messages": [
  //       systemMessage,
  //       ...apiMessages
  //     ]
  //   }

  //   await fetch("https://api.openai.com/v1/chat/completions", {
  //     method: "POST",
  //     headers: {
  //       "Authorization": "Bearer " + API_KEY,
  //       "Content-Type": "application/json"
  //     },
  //     body: JSON.stringify(apiRequestBody)
  //   }).then((data) => {
  //     return data.json();
  //   }).then ((data) => {
  //     console.log(data.choices[0].message.content);
  //     setMessages(
  //       [...chatMessages, {
  //         message: data.choices[0].message.content,
  //         sender: "ChatGPT",
  //         direction: "incoming"
  //       }]
  //     );
  //     setIsTyping(false)
  //   });
  // }

  return (
    <div className="App" style={{ marginTop: "-30px", marginLeft: "-100px", marginRight: "-120px", marginBottom: "-30px" }}>
      <div>
        <ConversationHeader style={{ backgroundColor: "#064684" }}>
          <ConversationHeader.Content>
            <span style={{color: "white"}}><h2>Ask Benny Chat</h2></span>
          </ConversationHeader.Content>
        </ConversationHeader>

        <MainContainer>
          <ChatContainer style={{ width: "2100px", height: "730px", marginTop: "10px" }}>
            <MessageList
              scrollBehavior="smooth"
              typingIndicator={
                isTyping ? <TypingIndicator content="Benny is typing" /> : null
              }
            >
              {messages.map((messages, i) => {
                if (messages.sender == "ChatGPT") {
                  return <Message key={i} model={messages} children={<Avatar src={"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.mascotdb.com%2Fsites%2Fdefault%2Ffiles%2Flogos%2F40577.jpg&f=1&nofb=1&ipt=a3b77ebdd67e4e43746d7fa2ac7e09fdf98ad75e4719dff2e71ddf77aecc1b3a&ipo=images"} name="Benny" />} />;
                }
                return <Message key={i} model={messages} />;
              })}
            </MessageList>
            <MessageInput placeholder="Type message here" onSend={handleSend} />
          </ChatContainer>
        </MainContainer>
      </div>
    </div>
  );
}

export default App;
