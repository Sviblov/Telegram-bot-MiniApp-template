interface TelegramWebAppUser {
    id: number
    is_bot: boolean
    first_name: string
    last_name?: string
    username?: string
    language_code?: string
    is_premium?: boolean
    added_to_attachment_menu?: boolean
    allows_write_to_pm?: boolean
    photo_url?: string
  }
  
  interface TelegramWebAppThemeParams {
    bg_color?: string
    text_color?: string
    hint_color?: string
    link_color?: string
    button_color?: string
    button_text_color?: string
    secondary_bg_color?: string
  }
  
  interface TelegramWebAppPopupButton {
    id: string
    type?: 'default' | 'ok' | 'close' | 'cancel' | 'destructive'
    text: string
  }
  
  interface TelegramWebApp {
    /** WebApp version */
    version: string
  
    /** Platform: android, ios, or web */
    platform: string
  
    /** Color scheme: 'light' or 'dark' */
    colorScheme: 'light' | 'dark'
  
    /** Theme parameters */
    themeParams: TelegramWebAppThemeParams
  
    /** Whether the app is expanded */
    isExpanded: boolean
  
    /** Current viewport height */
    viewportHeight: number
  
    /** Stable viewport height */
    viewportStableHeight: number
  
    /** Whether the app has requested closing confirmation */
    isClosingConfirmationEnabled: boolean
  
    /** Initial data string (for validation on backend) */
    initData: string
  
    /** Unsafe parsed init data */
    initDataUnsafe: {
      query_id?: string
      user?: TelegramWebAppUser
      receiver?: TelegramWebAppUser
      start_param?: string
      can_send_after?: number
      chat_type?: string
      chat_instance?: string
    }
  
    /** Expands the Web App to full height */
    expand(): void
  
    /** Closes the Web App */
    close(): void
  
    /** Sends data to the bot via `web_app_data` */
    sendData(data: string): void
  
    /** Opens a link in the default browser */
    openLink(url: string, options?: { try_instant_view?: boolean }): void
  
    /** Opens a link in Telegram (e.g. t.me/username) */
    openTelegramLink(url: string): void
  
    /** Displays a native alert dialog */
    showAlert(message: string, callback?: () => void): void
  
    /** Displays a native confirmation dialog */
    showConfirm(message: string, callback: (ok: boolean) => void): void
  
    /** Displays a native popup with custom buttons */
    showPopup(
      params: {
        title?: string
        message: string
        buttons?: TelegramWebAppPopupButton[]
      },
      callback: (buttonId: string) => void
    ): void
  
    /** Enables confirmation on close */
    enableClosingConfirmation(): void
  
    /** Disables confirmation on close */
    disableClosingConfirmation(): void
  
    /** Notifies Telegram that the Web App is ready */
    ready(): void
  
    /** Registers an event listener */
    onEvent(
      eventType:
        | 'themeChanged'
        | 'viewportChanged'
        | 'mainButtonClicked'
        | 'backButtonClicked'
        | 'settingsButtonClicked',
      eventHandler: () => void
    ): void
  
    /** Unregisters an event listener */
    offEvent(
      eventType:
        | 'themeChanged'
        | 'viewportChanged'
        | 'mainButtonClicked'
        | 'backButtonClicked'
        | 'settingsButtonClicked',
      eventHandler: () => void
    ): void
  
    /** Back button control */
    BackButton: {
      isVisible: boolean
      onClick(callback: () => void): void
      offClick(callback: () => void): void
      show(): void
      hide(): void
    }
  
    /** Settings button control */
    SettingsButton: {
      onClick(callback: () => void): void
      offClick(callback: () => void): void
    }
  
    /** Main button control */
    MainButton: {
      text: string
      color?: string
      textColor?: string
      isVisible: boolean
      isActive: boolean
      isProgressVisible: boolean
  
      setText(text: string): this
      onClick(callback: () => void): void
      offClick(callback: () => void): void
      show(): this
      hide(): this
      enable(): this
      disable(): this
      showProgress(leaveActive?: boolean): this
      hideProgress(): this
      setParams(params: {
        text?: string
        color?: string
        text_color?: string
        is_active?: boolean
        is_visible?: boolean
      }): this
    }
  }
  
declare global {
    interface Window {
      Telegram: {
        WebApp: TelegramWebApp
      }
    }
    type TelegramWebAppUser = TelegramWebAppUser
    type TelegramWebAppThemeParams = TelegramWebAppThemeParams
  }

export {}