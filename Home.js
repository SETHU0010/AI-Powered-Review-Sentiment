import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="container">
      <h1>Welcome to AI Sentiment Analysis</h1>
      <Link to="/login"><button>Login</button></Link>
      <Link to="/analyze"><button>Analyze Sentiment</button></Link>
    </div>
  );
}

export default Home;
