use lb;

CREATE TABLE products (
    id BIGINT,
    productcode VARCHAR(255),
    productname VARCHAR(255),
    energy VARCHAR(255),
    consumptiontype VARCHAR(255),
    deleted SMALLINT,
    modificationdate DATETIME,
    Releasedversion BIGINT
);

CREATE TABLE contracts (
    id BIGINT,
    type VARCHAR(255), 
    energy VARCHAR(255), 
    `usage` INT,
    usagenet INT,
    createdat DATETIME,
    startdate DATETIME,
    enddate DATETIME,
    fillingdatecancellation DATETIME,
    cancellationreason VARCHAR(255), 
    city VARCHAR(255), 
    status VARCHAR(255), 
    productid BIGINT,
    modificationdate DATETIME
);



CREATE TABLE prices (
    id BIGINT,
    productid BIGINT,
    pricecomponentid INT,
    productcomponent VARCHAR(255),
    price DECIMAL(38, 19),
    unit VARCHAR(50),
    valid_from DATETIME,
    valid_until DATETIME,
    modificationdate DATETIME
);
