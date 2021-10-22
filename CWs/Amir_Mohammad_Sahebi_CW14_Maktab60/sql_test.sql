CREATE TABLE "users" (
  "id" SERIAL PRIMARY KEY,
  "username" varchar(50),
  "first_name" varchar(50),
  "last_name" varchar(50),
  "age" int,
  "birthday" datetime,
  "email" varcharacter(50),
  "create_at" timestamp
);

CREATE TABLE "blogs" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(50),
  "url" varchar(50),
  "des" varchar,
  "create_at" timestamp
);

CREATE TABLE "blog_user" (
  "id" SERIAL PRIMARY KEY,
  "user_id" int,
  "blog_id" int
);

CREATE TABLE "posts" (
  "id" SERIAL PRIMARY KEY,
  "blog_id" int,
  "polished_at" timestamp,
  "create_at" timestamp
);

CREATE TABLE "tags" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(50),
  "create_at" timestamp
);

CREATE TABLE "likes" (
  "id" SERIAL PRIMARY KEY,
  "user_id" int,
  "post_id" int,
  "create_at" timestamp
);

CREATE TABLE "post_tag" (
  "id" SERIAL PRIMARY KEY,
  "post_id" int,
  "tag_id" int
);

CREATE TABLE "comments" (
  "id" SERIAL PRIMARY KEY,
  "post_id" int,
  "user_id" int,
  "reply_id" int,
  "email" varchar(50),
  "texts" varchar(1200),
  "create_at" timestamp
);

CREATE TABLE "login_activities" (
  "id" SERIAL PRIMARY KEY,
  "user_id" int,
  "ip_address" varchar(15),
  "country" varchar(10),
  "create_at" timestamp
);

ALTER TABLE "blog_user" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "blog_user" ADD FOREIGN KEY ("blog_id") REFERENCES "blogs" ("id");

ALTER TABLE "posts" ADD FOREIGN KEY ("blog_id") REFERENCES "blogs" ("id");

ALTER TABLE "likes" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "likes" ADD FOREIGN KEY ("post_id") REFERENCES "posts" ("id");

ALTER TABLE "post_tag" ADD FOREIGN KEY ("post_id") REFERENCES "posts" ("id");

ALTER TABLE "post_tag" ADD FOREIGN KEY ("tag_id") REFERENCES "tags" ("id");

ALTER TABLE "comments" ADD FOREIGN KEY ("post_id") REFERENCES "posts" ("id");

ALTER TABLE "comments" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "comments" ADD FOREIGN KEY ("reply_id") REFERENCES "comments" ("id");

ALTER TABLE "login_activities" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");
