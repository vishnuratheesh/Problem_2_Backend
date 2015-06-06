CREATE TABLE "csr" (
  "id" SERIAL,
  "name" varchar(255),
  "level" varchar(15),
  PRIMARY KEY ("id") 
  );

CREATE TABLE "problem_types" (
  "id" SERIAL,
  "problem_type" varchar(255),
  PRIMARY KEY ("id") 
  );

CREATE TABLE "customers" (
  "id" SERIAL,
  "name" varchar(255),
  "address" varchar(255),
  "mobile" varchar(255),
  "joined_on" timestamp(6),
  PRIMARY KEY ("id") 
  );

CREATE TABLE "status" (
  "id" SERIAL,
  "status" varchar(255),
  PRIMARY KEY ("id") 
  );

CREATE TABLE "tickets" (
  "id" SERIAL,
  "created_date" timestamp(6),
  "last_updated" timestamp(6),
  "closed_date" timestamp(6),
  "cust_id" integer references customers(id),
  "prob_id" integer references problem_types(id),
  "status_id" integer references status(id),
  "assigned_to" integer references csr(id),
  "comments" char(255)
  PRIMARY KEY ("id") 
  );


-- Inserts for CSR table
insert into csr(name,level) values('Daniel', 'S');
insert into csr(name,level) values('Adam', 'L1');
insert into csr(name,level) values('Tom', 'L2');
insert into csr(name,level) values('Harry', 'L3');

--- Inserts for  problem_types table
insert into problem_types(problem_type) values('Billing');
insert into problem_types(problem_type) values('Product');
insert into problem_types(problem_type) values('Delivery');
insert into problem_types(problem_type) values('Promo Codes');
insert into problem_types(problem_type) values('Others');
insert into problem_types(problem_type) values('Internal');


-- Inserts for customers
insert into customers(name,address,mobile,joined_on) values('Tom Hanks', '324, 6th Lane, Big City, Some Country', '9741231823', now());
insert into customers(name,address,mobile,joined_on) values('Ramesh Kumar', '324, 6th Lane, Big City, Some Country', '8050502999', now());
insert into customers(name,address,mobile,joined_on) values('Hari Lal', '324, 6th Lane, Big City, Some Country', '7738998794', now());
insert into customers(name,address,mobile,joined_on) values('Vishnu Ratheesh', '324, 6th Lane, Big City, Some Country', '9870873212', now());

-- Inserts for status
insert into status(status) values('New');
insert into status(status) values('Open');
insert into status(status) values('Closed');

-- Inserts for tickets
insert into tickets(created_date,cust_id,prob_id,status_id,comments) values(now(),1,2,1,'Major issue, this need it resolved.');




---------

select T.id, T.cust_id, C.name, C.mobile, T.prob_id, P.problem_type, T.status_id, S.status, T.comments, T.assigned_to
from tickets T, customers C, problem_types P, status S
where  T.cust_id = C.id and T.prob_id = P.id and T.status_id = S.id