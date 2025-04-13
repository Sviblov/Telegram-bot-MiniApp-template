import Counter from "./Counter";
import { Card, Typography } from 'antd'


const { Title, Paragraph } = Typography

interface ValidatedAppProps {
  initData: typeof window.Telegram.WebApp.initDataUnsafe; // Передаем пользователя как проп
  token: string | null;
}

  const ValidatedApp = ({ initData, token }: ValidatedAppProps, ) => {

    return (
      <Card
      style={{
        margin: 24,
        borderRadius: 12,
        backgroundColor: 'var(--tg-theme-bg-color)',
        color: 'var(--tg-theme-text-color)',
        boxShadow: '0 0 8px rgba(0, 0, 0, 0.05)',
      }}
      variant="borderless"
    >
      <Typography style={{ color: 'inherit' }}>
        <Title level={3} style={{ color: 'inherit', marginBottom: 12 }}>
          ✅ Успешная валидация
        </Title>
        <Paragraph style={{ fontSize: 16 }}>
          Пользователь: <strong>{initData.user?.first_name}</strong>
        </Paragraph>

        <Counter user={initData.user} token={token} />
      </Typography>
    </Card>
    );
  };
  
  export default ValidatedApp;