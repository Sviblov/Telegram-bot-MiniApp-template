import React from "react";
import Counter from "../components/Counter";


function Homepage({ user }) {
  const apiUrl = process.env.REACT_APP_API_URL;
  const token = localStorage.getItem("token");

  return (
    <div>
      <h1>👋 Привет, {user.first_name}!</h1>
      <p>Ты авторизован через Telegram Mini App.</p>
      <Counter user={user} apiUrl={apiUrl} token={token} />

    </div>
  );
}

export default Homepage;