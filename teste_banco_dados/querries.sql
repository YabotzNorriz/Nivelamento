-- Criação da database
CREATE database teste;
USE teste;

-- Querry para o arquivo CSV (Relatorio_cadop.csv)
CREATE TABLE cadastro_operadoras (
    REGISTRO_ANS VARCHAR(50),
    CNPJ VARCHAR(20),
    RAZAO_SOCIAL VARCHAR(255),
    NOME_FANTASIA VARCHAR(255),
    MODALIDADE VARCHAR(100),
    LOGRADOURO VARCHAR(255),
    NUMERO VARCHAR(20),
    COMPLEMENTO VARCHAR(255),
    BAIRRO VARCHAR(255),
    CIDADE VARCHAR(255),
    UF CHAR(2),
    CEP VARCHAR(10),
    DDD VARCHAR(3),
    TELEFONE VARCHAR(20),
    FAX VARCHAR(20),
    ENDERECO_ELETRONICO VARCHAR(255),
    REPRESENTANTE VARCHAR(255),
    CARGO_REPRESENTANTE VARCHAR(255),
    REGIAO_DE_COMERCIALIZACAO VARCHAR(10),
    DATA_REGISTRO_ANS DATE
);

-- Querry para os registros anuais dos dois últimos anos (2023 e 2024)
CREATE TABLE contas_financeiras (
    `DATA` DATE,
    REG_ANS VARCHAR(50),
    CD_CONTA_CONTABIL VARCHAR(50),
    DESCRICAO VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(15,2),
    VL_SALDO_FINAL DECIMAL(15,2)
);

-- Carregar os dados CSV que estão dentro do arquivo (Relatorio_cadop.csv)
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Relatorio_cadop - Relatorio_cadop.csv'
INTO TABLE cadastro_operadoras
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Registro_ANS,
 CNPJ,
 Razao_Social,
 Nome_Fantasia,
 Modalidade,
 Logradouro,
 Numero,
 Complemento,
 Bairro,
 Cidade,
 UF,
 CEP,
 DDD,
 Telefone,
 Fax,
 Endereco_eletronico,
 Representante,
 Cargo_Representante,
 Regiao_de_Comercializacao,
 @var_Data_Registro_ANS)
SET Data_Registro_ANS = STR_TO_DATE(@var_Data_Registro_ANS, '%Y-%m-%d');


-- Carregar os dados dos dois últimos anos
-- 1T2023
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/1T2023.csv'
INTO TABLE contas_financeiras
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@var_DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @var_VL_SALDO_INICIAL, @var_VL_SALDO_FINAL)
SET 
	`DATA` = STR_TO_DATE(@var_DATA, '%Y-%m-%d'),
	VL_SALDO_INICIAL = REPLACE(@var_VL_SALDO_INICIAL, ',', '.'),
	VL_SALDO_FINAL = REPLACE(@var_VL_SALDO_FINAL, ',', '.');

-- 2t2023
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/2t2023.csv'
INTO TABLE contas_financeiras
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@var_DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @var_VL_SALDO_INICIAL, @var_VL_SALDO_FINAL)
SET 
	`DATA` = STR_TO_DATE(@var_DATA, '%Y-%m-%d'),
	VL_SALDO_INICIAL = REPLACE(@var_VL_SALDO_INICIAL, ',', '.'),
	VL_SALDO_FINAL = REPLACE(@var_VL_SALDO_FINAL, ',', '.');

-- 3T2023
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/3T2023.csv'
INTO TABLE contas_financeiras
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@var_DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @var_VL_SALDO_INICIAL, @var_VL_SALDO_FINAL)
SET 
    `DATA` = STR_TO_DATE(@var_DATA, '%Y-%m-%d'),
    VL_SALDO_INICIAL = REPLACE(@var_VL_SALDO_INICIAL, ',', '.'),
    VL_SALDO_FINAL = REPLACE(@var_VL_SALDO_FINAL, ',', '.');
 
 -- 4T2023, aqui as datas estão no padrão brasileiro (DD/MM/YYYY), então o tratamento é diferente dos demais
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2023.csv'
INTO TABLE contas_financeiras
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@var_DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @var_VL_SALDO_INICIAL, @var_VL_SALDO_FINAL)
SET 
  DATA = STR_TO_DATE(@var_DATA, '%d/%m/%Y'),
  VL_SALDO_INICIAL = REPLACE(@var_VL_SALDO_INICIAL, ',', '.'),
  VL_SALDO_FINAL = REPLACE(@var_VL_SALDO_FINAL, ',', '.');

-- 1T2024
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/1T2024.csv'
INTO TABLE contas_financeiras
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@var_DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @var_VL_SALDO_INICIAL, @var_VL_SALDO_FINAL)
SET 
    `DATA` = STR_TO_DATE(@var_DATA, '%Y-%m-%d'),
    VL_SALDO_INICIAL = REPLACE(@var_VL_SALDO_INICIAL, ',', '.'),
    VL_SALDO_FINAL = REPLACE(@var_VL_SALDO_FINAL, ',', '.');
    
-- 2t2024
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/2t2024.csv'
INTO TABLE contas_financeiras
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@var_DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @var_VL_SALDO_INICIAL, @var_VL_SALDO_FINAL)
SET 
    `DATA` = STR_TO_DATE(@var_DATA, '%Y-%m-%d'),
    VL_SALDO_INICIAL = REPLACE(@var_VL_SALDO_INICIAL, ',', '.'),
    VL_SALDO_FINAL = REPLACE(@var_VL_SALDO_FINAL, ',', '.');
    
-- 3T2024
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/3T2024.csv'
INTO TABLE contas_financeiras
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@var_DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @var_VL_SALDO_INICIAL, @var_VL_SALDO_FINAL)
SET 
    `DATA` = STR_TO_DATE(@var_DATA, '%Y-%m-%d'),
    VL_SALDO_INICIAL = REPLACE(@var_VL_SALDO_INICIAL, ',', '.'),
    VL_SALDO_FINAL = REPLACE(@var_VL_SALDO_FINAL, ',', '.');

-- 4T2024
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2024.csv'
INTO TABLE contas_financeiras
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@var_DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @var_VL_SALDO_INICIAL, @var_VL_SALDO_FINAL)
SET 
    `DATA` = STR_TO_DATE(@var_DATA, '%Y-%m-%d'),
    VL_SALDO_INICIAL = REPLACE(@var_VL_SALDO_INICIAL, ',', '.'),
    VL_SALDO_FINAL = REPLACE(@var_VL_SALDO_FINAL, ',', '.');
    
-- Quais as 10 operadoras com maiores despesas em no último trimestre?
SELECT 
    REG_ANS AS Operadora, 
    SUM(CAST(REPLACE(VL_SALDO_FINAL, ',', '.') AS DECIMAL(15,2))) AS Total_Despesas
FROM 
    contas_financeiras
WHERE 
	DESCRICAO LIKE "%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%"
    AND STR_TO_DATE(DATA, '%Y-%m-%d') BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY 
    REG_ANS
ORDER BY 
    Total_Despesas DESC
LIMIT 10;

-- Quais as 10 operadoras com maiores despesas em no último ano?
SELECT 
    REG_ANS AS Operadora, 
    SUM(CAST(REPLACE(VL_SALDO_FINAL, ',', '.') AS DECIMAL(15,2))) AS Total_Despesas
FROM 
    contas_financeiras
WHERE 
	DESCRICAO LIKE "%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%"
    AND STR_TO_DATE(DATA, '%Y-%m-%d') BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY 
    REG_ANS
ORDER BY 
    Total_Despesas DESC
LIMIT 10;