ALTER TABLE product ADD COLUMN image VARCHAR(200) DEFAULT NULL;

UPDATE product SET image = 'twinings_english_breakfast_image.png' WHERE id = 4;

UPDATE product SET image = 'twinings_earl_grey_image.png' WHERE id = 5;

UPDATE product SET image = 'twinings_lady_grey_image.png' WHERE id = 6;