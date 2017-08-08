use xhamster;

create table tag(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

create table image(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    src VARCHAR(255) NOT NULL
);


create table download_link(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	quality VARCHAR(20) NOT NULL,
    src VARCHAR(255) NOT NULL
);

create table video(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    duration VARCHAR(255) NOT NULL,
    interaction_count VARCHAR(255) NOT NULL,
    finger_rate VARCHAR(255) NOT NULL,
    created_at timestamp,
    visit_link VARCHAR(255) NOT NULL,
	download_link_id INT UNSIGNED NOT NULL,
    image_id INT UNSIGNED NOT NULL,
    tag_id INT UNSIGNED NOT NULL,
    
    FOREIGN KEY (download_link_id)
      REFERENCES download_link(id)
      ON UPDATE CASCADE ON DELETE RESTRICT,
      
	FOREIGN KEY (image_id)
      REFERENCES image(id)
      ON UPDATE CASCADE ON DELETE RESTRICT,

    FOREIGN KEY (tag_id)
      REFERENCES tag(id)
      ON UPDATE CASCADE ON DELETE RESTRICT
);