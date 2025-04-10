// App.js
import { useEffect, useState } from "react";
import UserGreeting from "./components/UserValidated"; // Импортируем компонент

function App() {
  const [user, setUser] = useState(null);
  const [isValid, setIsValid] = useState(false);

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
        } else {
          setIsValid(false);
        }
      });
   
   }, []);

 
  if (!isValid || !user) return <div>⛔ Ошибка валидации Telegram</div>;


  return <UserGreeting user={user} />;
}

export default App;