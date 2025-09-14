INSERT INTO public.interface_messages
("key", "language", message, "comment")
VALUES('welcome_not_admin', 'ru', 'Добро пожаловать, {}. 

Значение счетчика: {}

/delete чтобы сбросить', 'welcome of new user');
INSERT INTO public.interface_messages
("key", "language", message, "comment")
VALUES('negative_counter', 'ru', 'Задонатить можно только если счетчик больше 0', 'not possible to create negative invoice');
INSERT INTO public.interface_messages
("key", "language", message, "comment")
VALUES('invoice_text', 'ru', 'Спасибо за донат', 'донат');
INSERT INTO public.interface_messages
("key", "language", message, "comment")
VALUES('invoice_title', 'ru', 'Спасибо за донат', 'донат - заголовок');
INSERT INTO public.interface_messages
("key", "language", message, "comment")
VALUES('payment_success', 'ru', 'Спасибо за донат {}', 'спасибо');