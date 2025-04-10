import React, {useState, useEffect} from "react";

function UserGreeting({ user }) {

const [counter, setCounter] = useState(0);

const apiUrl = process.env.REACT_APP_API_URL + "/counter";

  // Получение начального значения счетчика с backend
  useEffect(() => {
    fetch(apiUrl+"/"+ user.id)
      .then((res) => res.json())
      .then((data) => {
        setCounter(data.counter); // Устанавливаем значение из backend
      })
      .catch((error) => {
        console.error("Ошибка при загрузке счетчика:", error);
      });
  }, [apiUrl]);

const increment = () => {
    const newCounter = counter + 1;
    setCounter(newCounter);
    updateCounterOnBackend(newCounter);
  };
const decrement = () => {
    const newCounter = counter - 1;
    setCounter(newCounter);
    updateCounterOnBackend(newCounter);
  };

const updateCounterOnBackend = (newCounter) => {
    fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        counter: newCounter,
        user_id: user.id,
      }),
    }).catch((error) => {
      console.error("Ошибка при обновлении счетчика:", error);
    });
  };

  return (
    <div>
      <h1>👋 Привет, {user.first_name}!</h1>
      <p>Ты авторизован через Telegram Mini App.</p>
      <p>Счетчик: {counter}</p>
      <button onClick={increment}>Увеличить</button>
      <button onClick={decrement}>Уменьшить</button>
  
    </div>
  );
}

export default UserGreeting;