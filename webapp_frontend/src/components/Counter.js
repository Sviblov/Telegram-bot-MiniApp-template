import React, { useState, useEffect } from "react";
import { Button } from '@telegram-apps/telegram-ui';


function Counter({ user, apiUrl, token }) {
  const [counter, setCounter] = useState(0);
  // const apiUrl = process.env.REACT_APP_API_URL
 
    // Получение начального значения счетчика с backend
    useEffect(() => {
      fetch(apiUrl+ "/counter/"+ user.id, {
        method: "GET",
        headers: {
          "token": `${token}`, // Передаём токен в заголовке
        },
      })
        .then((res) => res.json())
        .then((data) => {
          setCounter(data.counter); // Устанавливаем значение из backend
        })
        .catch((error) => {
          console.error("Ошибка при загрузке счетчика:", error);
        });
    }, [apiUrl, token, user.id]);
  
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
      fetch(apiUrl+ "/counter", {
        method: "POST",
        headers: { "Content-Type": "application/json", "token": `${token}`,},
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
        <p>Счётчик: {counter}</p>
        <Button onClick={increment}>Увеличить</Button>
        <Button onClick={decrement}>Уменьшить</Button>
      </div>
    );
  }

  export default Counter;