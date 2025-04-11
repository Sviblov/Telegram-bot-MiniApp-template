// App.js
import { useEffect, useState } from "react";
import Homepage from "./pages/Homepage"; // Импортируем компонент

function App() {
  const [user, setUser] = useState(null);
  const [isValid, setIsValid] = useState(false);
  const [loading, setLoading] = useState(true); // Добавляем состояние загрузки

  useEffect(() => {
    const tg = window.Telegram.WebApp;
    const initData = tg.initData;
    const initDataUnsafe = tg.initDataUnsafe;

    const apiUrl = process.env.REACT_APP_API_URL + "/validate";

   // Отправляем initData на сервер для валидации
    fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ init_data: initData })
    })
      .then(res => res.json())
      .then(data => {
        if (data.valid) {
          setIsValid(true);
          setUser(initDataUnsafe.user);
          localStorage.setItem("token", data.token);
        } else {
          setIsValid(false);
        }
      })
      .catch((error) => {
        console.error("Ошибка валидации:", error);
        setIsValid(false);
      })
      .finally(() => {
        setLoading(false); // Завершаем загрузку
      });
   
   }, []);
 // Показываем индикатор загрузки, пока запрос выполняется
  if (loading) return <div>🔄 Загрузка...</div>;

 
  if (!isValid || !user) return <div>⛔ Ошибка валидации Telegram</div>;
   

  return <Homepage user={user} />;
}

export default App;