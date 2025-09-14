INSERT INTO public.interface_buttons
("key", menu_key, "language", button_text, "order", "comment", "type", "data")
VALUES('plusCounter', 'welcome_not_admin', 'ru', 'Добавить счетчик', 0, 'add counter', 'callback', 'plusCounter');
INSERT INTO public.interface_buttons
("key", menu_key, "language", button_text, "order", "comment", "type", "data")
VALUES('minusCounter', 'welcome_not_admin', 'ru', 'Добавить счетчик', 1, 'add counter', 'callback', 'minusCounter');
INSERT INTO public.interface_buttons
("key", menu_key, "language", button_text, "order", "comment", "type", "data")
VALUES('donate', 'welcome_not_admin', 'ru', 'Donate', 4, 'payment example', 'callback', 'createInvoice');
INSERT INTO public.interface_buttons
("key", menu_key, "language", button_text, "order", "comment", "type", "data")
VALUES('link', 'welcome_not_admin', 'ru', 'Link', 5, 'Link', 'url', 'https://t.me/meneer_igor');
INSERT INTO public.interface_buttons
("key", menu_key, "language", button_text, "order", "comment", "type", "data")
VALUES('negative_counter', 'negative_counter', 'ru', 'Назад', 0, 'back to main menu', 'callback', 'start');
INSERT INTO public.interface_buttons
("key", menu_key, "language", button_text, "order", "comment", "type", "data")
VALUES('payment_success', 'payment_success', 'ru', 'Назад', 0, 'back', 'callback', 'start');
INSERT INTO public.interface_buttons
("key", menu_key, "language", button_text, "order", "comment", "type", "data")
VALUES('openWebApp', 'welcome_not_admin', 'ru', 'Открыть App', 2, 'open web appp', 'webapp', 'https://193.123.33.81:4000');