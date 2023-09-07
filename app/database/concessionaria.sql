CREATE TABLE  IF NOT EXISTS veiculos(
    vei_id TINYINT(11) NOT NULL PRIMARY KEY,
    vei_tipo varchar(100) NOT NULL,
    vei_marca varchar(100) NOT NULL,
    vei_modelo varchar(100) NOT NULL,
    vei_cor varchar(100) NOT NULL,
    vei_ano_fabricacao varchar(45) NOT NULL,
    vei_estado varchar(45),
    vei_quilometragem varchar(45),
    vei_passagem varchar(45),
    vei_pagamento varchar(100),
    vei_foto varchar(45) not null

);