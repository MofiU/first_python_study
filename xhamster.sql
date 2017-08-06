use xhamster;

create table tags(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

create table images(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    src VARCHAR(255) NOT NULL
);


create table download_links(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	quality VARCHAR(20) NOT NULL,
    src VARCHAR(255) NOT NULL
);

create table videos(
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    duration VARCHAR(255) NOT NULL,
    interaction_count int,
    created_at timestamp,
    visit_link VARCHAR(255) NOT NULL,
	download_link_id INT UNSIGNED NOT NULL,
    image_id INT UNSIGNED NOT NULL,
    
    FOREIGN KEY (download_link_id)
      REFERENCES download_links(id)
      ON UPDATE CASCADE ON DELETE RESTRICT,
      
	FOREIGN KEY (image_id)
      REFERENCES images(id)
      ON UPDATE CASCADE ON DELETE RESTRICT
);