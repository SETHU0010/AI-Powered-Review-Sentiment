import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import SentimentAnalysis from "./pages/SentimentAnalysis";
import Login from "./pages/Login";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/analyze" element={<SentimentAnalysis />} />
      </Routes>
    </Router>
  );
}

export default App;
