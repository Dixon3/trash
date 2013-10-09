----Start----


CREATE TABLE import_log
(
      uid serial NOT NULL,
      file_id bigint,
      path text,
      "time" timestamp without time zone,
      sql text,
      error text,
      CONSTRAINT import_log_pk PRIMARY KEY (uid)
)
