import React from 'react';
import './Home.css';

function Home() {
  return (
    <div className="home">
      <header>
        <h2>amachine.ai</h2>
        <nav>
          <a href="#">Home</a>
          <a href="#">Features</a>
          <a href="#">How it works</a>
          <a href="#">About us</a>
          <a href="#">Pricing</a>
          <a href="#">Contact us</a>
          
        </nav>
        <button class="b1">Sign In</button>
        <button class="b2">Sign Up</button>
      </header>
      <div className="background-image">
        <h1>Welcome to amachine.ai</h1>
        <p>Revolutionizing Education with AI-Powered Assessments</p>
      </div>
    </div>
  );
}

export default Home;
