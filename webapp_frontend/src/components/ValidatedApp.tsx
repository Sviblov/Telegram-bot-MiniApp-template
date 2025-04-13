import Counter from "./Counter";


interface ValidatedAppProps {
  initData: typeof window.Telegram.WebApp.initDataUnsafe; // Передаем пользователя как проп
  token: string | null;
}

  const ValidatedApp = ({ initData, token }: ValidatedAppProps, ) => {

    return (
      <div>
        <h1>Успешная валидация</h1>
        <p>Пользователь: {initData.user?.first_name}</p>
        <Counter 
          user={initData.user}
          token={token} // Передаем токен в компонент Counter
        />
      </div>
    );
  };
  
  export default ValidatedApp;