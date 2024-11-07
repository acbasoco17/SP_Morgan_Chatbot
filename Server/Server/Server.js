const http = require("http");
const App = require("./App")

const server = http.createServer(App);

let PORT = process.env.PORT || 1234;
server.listen(PORT, () => {
  console.log(`Server is running on Port: ${PORT}...`);
});
