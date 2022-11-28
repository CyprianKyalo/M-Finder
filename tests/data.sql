INSERT INTO user (name, email, password)
VALUES
  ('test', 'test@gm.com', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'other@gm.com', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

-- INSERT INTO images (title, body, author_id, created)
-- VALUES
--   ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');

INSERT INTO images (name, time, location, age, description, phone, filename, status, updated_at) 
VALUES 
	(1, 'Pius', '21:21', 'location', 32, 'description', 53343, 'filename.jpg', 0, 2022);