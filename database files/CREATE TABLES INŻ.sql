CREATE TABLE account (
    id          SERIAL NOT NULL,
    login       VARCHAR(50) NOT NULL,
    password    VARCHAR(30) NOT NULL,
    customer_id BIGINT NOT NULL,
    status_id   INT NOT NULL
);

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE UNIQUE INDEX account__idx ON
    account (
        customer_id
    ASC );

ALTER TABLE account ADD CONSTRAINT account_pk PRIMARY KEY ( id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE customer (
    id                 SERIAL NOT NULL,
    first_name         VARCHAR(50) NOT NULL,
    last_name          VARCHAR(50) NOT NULL,
    email              VARCHAR(100) NOT NULL,
    date_of_birth      DATE NOT NULL,
    address            VARCHAR(100) NOT NULL,
    city               VARCHAR(100) NOT NULL,
    postal_code        VARCHAR(20) NOT NULL,
    country            VARCHAR(100) NOT NULL,
    phone_number       VARCHAR(20),
    account_id 		   INT NOT NULL
);

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE UNIQUE INDEX customer__idx ON
    customer (
        account_id
    ASC );

ALTER TABLE customer ADD CONSTRAINT customer_pk PRIMARY KEY ( id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE "order" (
    id                   SERIAL NOT NULL,
    customer_id          BIGINT,
    order_date           DATE NOT NULL,
    order_price          DECIMAL(9, 2) NOT NULL,
    delivery_address     VARCHAR(100) NOT NULL,
    delivery_city        VARCHAR(100) NOT NULL,
    delivery_postal_code VARCHAR(20) NOT NULL,
    delivery_country     VARCHAR(100) NOT NULL
);

ALTER TABLE "order" ADD CONSTRAINT order_pk PRIMARY KEY ( id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE order_detail (
    order_id   BIGINT NOT NULL,
    product_id INT NOT NULL,
    quantity   SMALLINT NOT NULL,
    price      DECIMAL(9, 2) NOT NULL
);

ALTER TABLE order_detail ADD CONSTRAINT order_detail_pk PRIMARY KEY ( product_id,
                                                                      order_id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE product (
    id                 SERIAL NOT NULL,
    type_of_product_id BIGINT,
    supplier_id        INT,
    name               VARCHAR(50) NOT NULL,
    description        TEXT NOT NULL,
    medical_properties TEXT,
    quentity_per_unit  VARCHAR(20) NOT NULL,
    unit_price         DECIMAL(4, 2) NOT NULL,
    units_in_stock     SMALLINT NOT NULL,
    units_in_order     SMALLINT NOT NULL,
    reorder_level      SMALLINT NOT NULL
);

ALTER TABLE product ADD CONSTRAINT product_pk PRIMARY KEY ( id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE status (
    id   SERIAL NOT NULL,
    name VARCHAR(30) NOT NULL
);

ALTER TABLE status ADD CONSTRAINT status_pk PRIMARY KEY ( id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE supplier (
    id           SERIAL NOT NULL,
    company_name VARCHAR(50) NOT NULL,
    contact_name VARCHAR(100) NOT NULL,
    address      VARCHAR(60) NOT NULL,
    postal_code  VARCHAR(15) NOT NULL,
    city         VARCHAR(15) NOT NULL,
    country      VARCHAR(30) NOT NULL,
    phone        VARCHAR(24),
    email        VARCHAR(100)
);

ALTER TABLE supplier ADD CONSTRAINT supplier_pk PRIMARY KEY ( id );

-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE type_of_product (
    id                  SERIAL NOT NULL,
    name                VARCHAR(30) NOT NULL,
    brewing_time        VARCHAR(15),
    brewing_temperature VARCHAR(15),
    amount_per_cup      VARCHAR(30)
);

ALTER TABLE type_of_product ADD CONSTRAINT type_of_product_pk PRIMARY KEY ( id );

ALTER TABLE account
    ADD CONSTRAINT account_customer_fk FOREIGN KEY ( customer_id )
        REFERENCES customer ( id );

ALTER TABLE account
    ADD CONSTRAINT account_status_fk FOREIGN KEY ( status_id )
        REFERENCES status ( id );

ALTER TABLE customer
    ADD CONSTRAINT customer_account_fk FOREIGN KEY ( account_id )
        REFERENCES account ( id );

ALTER TABLE "order"
    ADD CONSTRAINT order_customer_fk FOREIGN KEY ( customer_id )
        REFERENCES customer ( id );

ALTER TABLE order_detail
    ADD CONSTRAINT order_detail_order_fk FOREIGN KEY ( order_id )
        REFERENCES "order" ( id );

ALTER TABLE order_detail
    ADD CONSTRAINT order_detail_product_fk FOREIGN KEY ( product_id )
        REFERENCES product ( id );

ALTER TABLE product
    ADD CONSTRAINT product_supplier_fk FOREIGN KEY ( supplier_id )
        REFERENCES supplier ( id );

ALTER TABLE product
    ADD CONSTRAINT product_type_of_product_fk FOREIGN KEY ( type_of_product_id )
        REFERENCES type_of_product ( id );