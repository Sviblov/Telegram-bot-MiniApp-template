import { Button, Space, Typography } from "antd";
import { useState, useEffect } from "react";

const { Text } = Typography;


interface CounterProps {
  user: TelegramWebAppUser;
  token: string | null;
}


function Counter({ user, token }: CounterProps) {
  const [counter, setCounter] = useState<number>(0);


  const apiUrl = `${import.meta.env.VITE_APP_API_URL}/counter`; 
    // Получение начального значения счетчика с backend

    useEffect(() => {
      fetch(apiUrl+ '/' +user.id, {
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
  
  const updateCounterOnBackend = (newCounter: number) => {
      fetch(apiUrl, {
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
      <Space direction="vertical" align="center" style={{ width: "100%" }}>
        <Text strong style={{ fontSize: "18px" }}>Счётчик: {counter}</Text>
        
        <Button type="primary" size="large" onClick={increment}>Увеличить</Button>
        <Button type="primary" size="large" onClick={decrement}>Уменьшить</Button>
      </Space>
    );
  }

  export default Counter;