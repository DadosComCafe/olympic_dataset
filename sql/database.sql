CREATE DATABASE olympic_dataset;
\c olympic_dataset;

CREATE TABLE IF NOT EXISTS country (
        id SERIAL PRIMARY KEY,
        nome_pais VARCHAR(100),
        sigla VARCHAR(2),
        presente_nas_olimpiadas Boolean
    );

CREATE TABLE IF NOT EXISTS sport (
        id SERIAL PRIMARY KEY,
        sigla VARCHAR(10),
        nome VARCHAR(30),
        estacao VARCHAR(30)
    );