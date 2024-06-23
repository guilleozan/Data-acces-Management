-- Create the database
CREATE DATABASE article_hub;
USE article_hub;

-- Create the Users table
CREATE TABLE Users (
    user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('Administrator', 'Tutor', 'Student') NOT NULL
);

-- Create the Categories table
CREATE TABLE Categories (
    category_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- Create the Articles table
CREATE TABLE Articles (
    article_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    category_id INT UNSIGNED NOT NULL,
    type VARCHAR(50),
    born DATE,
    died DATE,
    nationality VARCHAR(50),
    known_for VARCHAR(255),
    notable_work VARCHAR(255),
    about TEXT,
    year YEAR,
    medium VARCHAR(255),
    dimensions VARCHAR(255),
    location VARCHAR(255),
    designed_by VARCHAR(255),
    developer VARCHAR(255),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- Create the Keywords table
CREATE TABLE Keywords (
    keyword_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    keyword VARCHAR(50) NOT NULL UNIQUE
);

-- Create the ArticleKeywords table
CREATE TABLE ArticleKeywords (
    article_id INT UNSIGNED NOT NULL,
    keyword_id INT UNSIGNED NOT NULL,
    PRIMARY KEY (article_id, keyword_id),
    FOREIGN KEY (article_id) REFERENCES Articles(article_id) ON DELETE CASCADE,
    FOREIGN KEY (keyword_id) REFERENCES Keywords(keyword_id) ON DELETE CASCADE
);

-- Insert initial data into Categories
INSERT INTO Categories (name) VALUES ('Arts'), ('Mathematics'), ('Technology');
