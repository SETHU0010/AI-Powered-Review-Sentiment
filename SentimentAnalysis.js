import { useState } from "react";
import axios from "axios";

function SentimentAnalysis() {
  const [review, setReview] = useState("");
  const [result, setResult] = useState(null);

  const analyzeReview = async () => {
    const res = await axios.post("http://127.0.0.1:8000/review/analyze", {
      user_id: 1, review_text: review
    });
    setResult(res.data);
  };

  return (
    <div className="container">
      <h2>Analyze Sentiment</h2>
      <textarea placeholder="Enter review" onChange={(e) => setReview(e.target.value)} />
      <button onClick={analyzeReview}>Analyze</button>
      {result && (
        <div>
          <p><strong>Sentiment:</strong> {result.sentiment}</p>
          <p><strong>Explanation:</strong> {result.explanation}</p>
        </div>
      )}
    </div>
  );
}

export default SentimentAnalysis;
