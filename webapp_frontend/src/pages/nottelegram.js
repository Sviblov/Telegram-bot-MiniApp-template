import React from 'react';
import '@telegram-apps/telegram-ui/dist/styles.css';
import { Placeholder } from '@telegram-apps/telegram-ui';

function NotTelegram() {
  return (
    <div>
      <Placeholder
        header="Application could be launched only in Telegram"
      >
        <img
          alt="Telegram sticker"
        
          src="https://xelene.me/telegram.gif"
        />
      </Placeholder>
    </div>
  );
}

export default NotTelegram;
