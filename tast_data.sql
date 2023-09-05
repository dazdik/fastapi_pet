INSERT INTO hotels (name, location, services, room_quantity, image_id) VALUES
('Чалпан', 'ул Щорса, 5 Б, Абакан', '["Бассейн", "Wi-fi"]', 55, 1),
('Азия Бизнес', 'Улица Кирова , д.114, стр. 1, Абакан', '["Бассейн", "Wi-fi"]', 75, 2),
('Pillars', 'улица Сибирская, д.19, Красноярск', '["Бассейн", "Wi-fi", "Ресторан"]', 90, 3),
('Sky Центр Красноярск', 'улица Марковского, д.45/1, Красноярск', '["Бассейн", "Wi-fi", "Ресторан"]', 100, 4),
('Урал', 'улица Ленина, д.58, Пермь', '["Бассейн", "Wi-fi", "Ресторан", "Фитнес"]', 50, 5);

INSERT INTO rooms (hotel_id, name, description, price, services, quantity, image_id) VALUES
(1, 'Standard', 'Двухместный номер с балконом', 4600, '["Ванная комната", "Wi-fi", "Кондиционер"]', 2, 1),
(2, 'Deluxe', 'Двухместный номер', 9500, '["Ванная комната", "Wi-fi", "Кондиционер", "Телевизор", "Сейф", "Затемненные шторы"]', 2, 2),
(3, 'Standard', 'Двухместный номер', 6000, '["Ванная комната", "Wi-fi", "Кондиционер"]', 2, 3),
(4, 'Standard', 'Двухместный номер', 4800, '["Ванная комната", "Wi-fi", "Кондиционер"]', 2, 4),
(5, 'Полулюкс', 'Двухместный номер с балконом', 8200, '["Ванная комната", "Wi-fi", "Кондиционер", "Телевизор", "Сейф", "Затемненные шторы"]', 2, 5);

INSERT INTO users (email, hashed_password) VALUES
    ('test_user@example.com', 'hashed_password_1'),
    ('test_user2@example.com', 'hashed_password_2');


INSERT INTO bookings (room_id, user_id, date_to, date_from, price) VALUES
    (1, 1, '2023-09-10', '2023-09-15', 4600),
    (2, 2, '2023-09-12', '2023-09-17', 9500);
