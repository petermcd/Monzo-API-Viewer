drop table if exists monzo;

create table monzo
(
    id            serial primary key,
    access_token  text      not null,
    client_id     text      not null,
    client_secret text      not null,
    expiry_date   timestamp not null,
    refresh_token text      null
);
