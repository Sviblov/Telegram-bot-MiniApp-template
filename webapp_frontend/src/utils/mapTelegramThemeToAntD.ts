import type { ThemeConfig } from 'antd/es/config-provider/context'
import { theme } from 'antd'

export function mapTelegramThemeToAntD(
  params: TelegramWebAppThemeParams,
  colorScheme: 'light' | 'dark'
): ThemeConfig {
  return {
    algorithm: colorScheme === 'dark' ? theme.darkAlgorithm : theme.defaultAlgorithm,
    token: {
      colorPrimary: params.button_color || '#1677ff',
      colorTextBase: params.text_color || (colorScheme === 'dark' ? '#ffffff' : '#000000'),
      colorBgBase: params.bg_color || (colorScheme === 'dark' ? '#000000' : '#ffffff'),
      colorLink: params.link_color || '#1677ff',
    },
    components: {
      Button: {
        motion: false,
      },
    },
  }
} 