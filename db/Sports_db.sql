CREATE DATABASE IF NOT EXISTS Sports_db;
USE Sports_db;
CREATE TABLE IF NOT EXISTS Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS Teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS Choices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    User_id INT,
    Football_team_id INT,
    Basketball_team_id INT,
    FOREIGN KEY (User_id) REFERENCES Users(id),
    FOREIGN KEY (Football_team_id) REFERENCES Teams(id),
    FOREIGN KEY (Basketball_team_id) REFERENCES Teams(id)
);
DELETE FROM Teams;
INSERT INTO Teams (name, type)
VALUES ('Maccabi Tel Aviv', 'Football'),
    ('Maccabi Haifa', 'Football'),
    ('Hapoel Beer Sheva', 'Football'),
    ('Beitar Jerusalem', 'Football'),
    ('Hapoel Tel Aviv', 'Football'),
    ('Ironi Kiryat Shmona', 'Football'),
    ('Hapoel Haifa', 'Football'),
    ('Bnei Sakhnin', 'Football'),
    ('Hapoel Hadera', 'Football'),
    ('Maccabi Netanya', 'Football'),
    ('F.C. Ashdod', 'Football'),
    ('Hapoel Jerusalem', 'Football'),
    ('Hapoel Kfar Saba', 'Football'),
    ('Maccabi Petah Tikva', 'Football'),
    ('Maccabi Tel Aviv', 'Basketball'),
    ('Maccabi Haifa', 'Basketball'),
    ('Hapoel Beer Sheva', 'Basketball'),
    ('Beitar Jerusalem', 'Basketball'),
    ('Hapoel Tel Aviv', 'Basketball'),
    ('Ironi Kiryat Shmona', 'Basketball'),
    ('Hapoel Haifa', 'Basketball'),
    ('Bnei Sakhnin', 'Basketball'),
    ('Hapoel Hadera', 'Basketball'),
    ('Maccabi Netanya', 'Basketball'),
    ('F.C. Ashdod', 'Basketball'),
    ('Hapoel Jerusalem', 'Basketball'),
    ('Hapoel Kfar Saba', 'Basketball'),
    ('Maccabi Petah Tikva', 'Basketball');