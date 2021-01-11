CREATE TABLE library (
    lib_id VARCHAR(255) PRIMARY KEY,
    name TEXT,
    credential TEXT
);

CREATE TABLE cart (
    name TEXT PRIMARY KEY,
    library VARCHAR(255) NOT NULL,
    endpoint TEXT,
    cart_type varchar(255),
    is_enable BOOL DEFAULT TRUE
);

