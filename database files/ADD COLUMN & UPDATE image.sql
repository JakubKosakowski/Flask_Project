ALTER TABLE product ADD COLUMN image VARCHAR(200) DEFAULT NULL;

UPDATE product SET image = 'twinings_earl_grey_image.png' WHERE id = 5;