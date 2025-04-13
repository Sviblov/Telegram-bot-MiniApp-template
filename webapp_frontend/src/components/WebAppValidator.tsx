import  { useEffect, useState } from "react";
import ValidatedApp from "./ValidatedApp";


// Интерфейс для пользователя


function WebAppValidator(){
  const [user, setUser] = useState<TelegramWebAppUser | null>(null); // Типизируем состояние пользователя
  const [isValid, setIsValid] = useState<boolean>(false); // Типизируем состояние валидации
  const [loading, setLoading] = useState<boolean>(true); // Типизируем состояние загрузки
  const [initDataUnsafe, setInitDataUnsafe] = useState<any>(null); // Состояние для initDataUnsafe
  const [token, setToken] = useState<string | null>(null); // Добавляем состояние для токена
  

  useEffect(() => {
    const tg = window.Telegram.WebApp; // Telegram WebApp API
    const initData: string = tg.initData; // Типизируем initData как строку
    const initDataUnsafe = tg.initDataUnsafe;

    const apiUrl = `${import.meta.env.VITE_APP_API_URL}/validate`; // Используем переменную окружения
    
    // Отправляем initData на сервер для валидации
    fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ init_data: initData }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.valid) {
          setIsValid(true);
          setUser(initDataUnsafe.user); 
          setInitDataUnsafe(initDataUnsafe); // Сохраняем initDataUnsafe
        // Устанавливаем пользователя
          setToken(data.token);
        } else {
          setIsValid(false);
        }
      })
      .catch(() => {
       
        setIsValid(false);
      })
      .finally(() => {
        setLoading(false); // Завершаем загрузку
      });
  }, []);

  // Показываем индикатор загрузки, пока запрос выполняется
  if (loading) return <div>🔄 Загрузка...</div>;

  // Показываем сообщение об ошибке, если валидация не удалась
  if (!isValid || !user) return <div>⛔ Ошибка валидации Telegram</div>;

  // Показываем сообщение об успешной валидации
  return (
    <ValidatedApp initData={initDataUnsafe} token={token}/>
  );
}

export default WebAppValidator;