
import WebAppValidator from './components/WebAppValidator.tsx';
import 'antd/dist/reset.css'
import ErrorBoundary from './components/ErrorBoundary.tsx';
import { mapTelegramThemeToAntD } from './utils/mapTelegramThemeToAntD'
import type { ThemeConfig } from 'antd/es/config-provider/context'
import { useEffect, useState } from 'react';
import { ConfigProvider } from 'antd';

const App = () => {
  const [themeConfig, setThemeConfig] = useState<ThemeConfig>()
  
  useEffect(() => {
    const tg = window.Telegram?.WebApp

    if (tg?.themeParams) {
      const scheme = tg.colorScheme === 'dark' ? 'dark' : 'light'
      const config = mapTelegramThemeToAntD(tg.themeParams, scheme)
      setThemeConfig(config)
    }
  }, [])
  
  
  return (
    <ErrorBoundary>
      <ConfigProvider theme={themeConfig}>
        <WebAppValidator />
      </ConfigProvider>
    </ErrorBoundary>
  );
};

export default App
