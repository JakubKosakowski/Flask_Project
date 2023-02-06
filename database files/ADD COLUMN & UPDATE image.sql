ALTER TABLE product ADD COLUMN image VARCHAR(200) DEFAULT NULL;

UPDATE product SET image = 'caykur_earl_grey_image.png' WHERE id = 2;

UPDATE product SET image = 'twinings_english_breakfast_image.png' WHERE id = 4;

UPDATE product SET image = 'twinings_earl_grey_image.png' WHERE id = 5;

UPDATE product SET image = 'twinings_lady_grey_image.png' WHERE id = 6;

UPDATE product SET image = 'lipton_earl_grey_image.png' WHERE id = 10;

UPDATE product SET image = 'lipton_green_tea_loose_image.png' WHERE id = 11;