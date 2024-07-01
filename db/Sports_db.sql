CREATE DATABASE IF NOT EXISTS Sports_db;
USE Sports_db;
-- Ensure the tables are created correctly
CREATE TABLE IF NOT EXISTS Users (
    ID int auto_increment primary key,
    Name varchar(255) NOT null
);
CREATE TABLE IF NOT EXISTS Teams (
    ID int auto_increment primary key,
    Name varchar(255) NOT null,
    Type ENUM('Football', 'Basketball') NOT null
);
CREATE TABLE IF NOT EXISTS Choices (
    ID int auto_increment primary key,
    User_id int,
    Football_team_id int,
    Basketball_team_id int,
    FOREIGN KEY (User_id) REFERENCES Users(ID),
    FOREIGN KEY (Football_team_id) REFERENCES Teams(ID),
    FOREIGN KEY (Basketball_team_id) REFERENCES Teams(ID)
);
-- Insert Football teams
INSERT INTO Teams (Name, Type)
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
    ('Maccabi Petah Tikva', 'Football');
-- Insert Basketball teams
INSERT INTO Teams (Name, Type)
VALUES ('Maccabi Tel Aviv', 'Basketball'),
    ('Hapoel Jerusalem', 'Basketball'),
    ('Hapoel Tel Aviv', 'Basketball'),
    ('Maccabi Rishon LeZion', 'Basketball'),
    ('Hapoel Holon', 'Basketball'),
    ('Maccabi Haifa', 'Basketball'),
    ('Hapoel Eilat', 'Basketball'),
    ('Ironi Nahariya', 'Basketball'),
    ('Hapoel Beer Sheva', 'Basketball'),
    ('Hapoel Gilboa Galil', 'Basketball'),
    ('Bnei Herzliya', 'Basketball'),
    ('Maccabi Ashdod', 'Basketball');