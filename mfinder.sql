--
-- PostgreSQL database dump
--

-- Dumped from database version 14.6
-- Dumped by pg_dump version 14.6

-- Started on 2022-12-19 20:00:11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3348 (class 1262 OID 16444)
-- Name: m_finder; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE m_finder WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';


ALTER DATABASE m_finder OWNER TO postgres;

\connect m_finder

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 212 (class 1259 OID 16486)
-- Name: images; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.images (
    imageid integer NOT NULL,
    userid bigint,
    name text,
    "time" text,
    location text,
    age text,
    description text,
    phone text,
    filename text,
    status text,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    temp_status integer DEFAULT 0,
    locationid character varying(255)
);


ALTER TABLE public.images OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16485)
-- Name: images_imageid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.images_imageid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.images_imageid_seq OWNER TO postgres;

--
-- TOC entry 3349 (class 0 OID 0)
-- Dependencies: 211
-- Name: images_imageid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.images_imageid_seq OWNED BY public.images.imageid;


--
-- TOC entry 214 (class 1259 OID 16508)
-- Name: location; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.location (
    locationid integer NOT NULL,
    city character varying(255),
    region character varying(255),
    country character varying(255),
    latitude character varying(255),
    longitude character varying(255)
);


ALTER TABLE public.location OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16507)
-- Name: location_locationid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.location_locationid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.location_locationid_seq OWNER TO postgres;

--
-- TOC entry 3350 (class 0 OID 0)
-- Dependencies: 213
-- Name: location_locationid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.location_locationid_seq OWNED BY public.location.locationid;


--
-- TOC entry 216 (class 1259 OID 16517)
-- Name: roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.roles (
    roleid integer NOT NULL,
    role_name text NOT NULL
);


ALTER TABLE public.roles OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 16516)
-- Name: roles_roleid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.roles_roleid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.roles_roleid_seq OWNER TO postgres;

--
-- TOC entry 3351 (class 0 OID 0)
-- Dependencies: 215
-- Name: roles_roleid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.roles_roleid_seq OWNED BY public.roles.roleid;


--
-- TOC entry 210 (class 1259 OID 16446)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    userid integer NOT NULL,
    name text,
    location text,
    contact text,
    email text,
    password text,
    roleid integer,
    status character varying(255),
    CONSTRAINT users_email_check CHECK ((email ~* '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$'::text))
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16445)
-- Name: users_userid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_userid_seq OWNER TO postgres;

--
-- TOC entry 3352 (class 0 OID 0)
-- Dependencies: 209
-- Name: users_userid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_userid_seq OWNED BY public.users.userid;


--
-- TOC entry 3181 (class 2604 OID 16489)
-- Name: images imageid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.images ALTER COLUMN imageid SET DEFAULT nextval('public.images_imageid_seq'::regclass);


--
-- TOC entry 3184 (class 2604 OID 16511)
-- Name: location locationid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.location ALTER COLUMN locationid SET DEFAULT nextval('public.location_locationid_seq'::regclass);


--
-- TOC entry 3185 (class 2604 OID 16520)
-- Name: roles roleid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles ALTER COLUMN roleid SET DEFAULT nextval('public.roles_roleid_seq'::regclass);


--
-- TOC entry 3179 (class 2604 OID 16449)
-- Name: users userid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN userid SET DEFAULT nextval('public.users_userid_seq'::regclass);


--
-- TOC entry 3338 (class 0 OID 16486)
-- Dependencies: 212
-- Data for Name: images; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.images (imageid, userid, name, "time", location, age, description, phone, filename, status, updated_at, temp_status, locationid) VALUES (3, 2, 'John', '00:09', 'Githu', '43', 'Short', '12432109', 'Abel_Pacheco_001.jpg', 'Not Found', '2022-12-18 12:08:45.777554', 0, NULL);
INSERT INTO public.images (imageid, userid, name, "time", location, age, description, phone, filename, status, updated_at, temp_status, locationid) VALUES (4, 2, 'June', '00:22', 'Ruiru', '98', 'Short, Slim', '12432129', 'Donald_Rumsfeld_006.jpg', 'Not Found', '2022-12-18 12:20:28.386725', 0, NULL);
INSERT INTO public.images (imageid, userid, name, "time", location, age, description, phone, filename, status, updated_at, temp_status, locationid) VALUES (2, 2, 'Mark', '00:53', 'Kiambu', '12', 'Tall, Dark', '1243212', 'my_image1.jpg', 'Not Found', '2022-12-19 19:24:19.946222', 1, '22');


--
-- TOC entry 3340 (class 0 OID 16508)
-- Dependencies: 214
-- Data for Name: location; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (5, 'Nairobi', 'Nairobi Province', 'Kenya', '-1.28410000', '36.81550000');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (6, 'Nairobi', 'Nairobi Province', 'Kenya', '-1.28410000', '36.81550000');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (7, 'Nairobi', 'Nairobi Province', 'Kenya', '-1.28410000', '36.81550000');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (8, 'Nairobi', 'Nairobi Province', 'Kenya', '-1.28410000', '36.81550000');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (9, 'Nairobi', 'Nairobi Province', 'Kenya', '-1.28410000', '36.81550000');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (10, 'Nairobi', 'Nairobi Province', 'Kenya', '-1.28410000', '36.81550000');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (11, 'Nairobi', 'Nairobi Province', 'Kenya', '-1.28410000', '36.81550000');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (12, 'Nairobi', 'Nairobi Province', 'Kenya', '-1.28410000', '36.81550000');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (13, NULL, NULL, NULL, '-1.3091961', '36.8225462');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (14, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (15, 'Nairobi', 'Nairobi Province', 'Kenya', '-1.2841', '36.8155');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (16, NULL, NULL, NULL, NULL, NULL);
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (17, 'Nairobi', 'Nairobi Province', 'Kenya', '-1.2841', '36.8155');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (18, 'Nairobi', 'Nairobi Area', 'Kenya', '-1.283329963684082', '36.81666946411133');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (19, 'Nairobi', 'Nairobi Area', 'Kenya', '-1.283329963684082', '36.81666946411133');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (20, 'Nairobi', 'Nairobi Area', 'Kenya', '-1.283329963684082', '36.81666946411133');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (21, 'Nairobi', 'Nairobi Area', 'Kenya', '-1.283329963684082', '36.81666946411133');
INSERT INTO public.location (locationid, city, region, country, latitude, longitude) VALUES (22, 'Nairobi', 'Nairobi Area', 'Kenya', '-1.283329963684082', '36.81666946411133');


--
-- TOC entry 3342 (class 0 OID 16517)
-- Dependencies: 216
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.roles (roleid, role_name) VALUES (2, 'admin');
INSERT INTO public.roles (roleid, role_name) VALUES (1, 'user');


--
-- TOC entry 3336 (class 0 OID 16446)
-- Dependencies: 210
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users (userid, name, location, contact, email, password, roleid, status) VALUES (3, 'admin', 'Kitui', '0736423422', 'admin@mfinder.com', 'pbkdf2:sha256:260000$kmZzUMJogutykJ3d$d8e69e5ddea28e5919c43517e7225745789172df24ae03986f90d8ee9878457b', 2, 'active');
INSERT INTO public.users (userid, name, location, contact, email, password, roleid, status) VALUES (2, 'Fabian', 'Machakos', '0736423422', 'fab@mfinder.com', 'pbkdf2:sha256:260000$cTI2yr9AH9XQobgW$f863f7836ac2a33eb35918343317c79fde79abc9a9e9514a206d45580d5b253d', 1, 'active');


--
-- TOC entry 3353 (class 0 OID 0)
-- Dependencies: 211
-- Name: images_imageid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.images_imageid_seq', 4, true);


--
-- TOC entry 3354 (class 0 OID 0)
-- Dependencies: 213
-- Name: location_locationid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.location_locationid_seq', 22, true);


--
-- TOC entry 3355 (class 0 OID 0)
-- Dependencies: 215
-- Name: roles_roleid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.roles_roleid_seq', 1, false);


--
-- TOC entry 3356 (class 0 OID 0)
-- Dependencies: 209
-- Name: users_userid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_userid_seq', 3, true);


--
-- TOC entry 3189 (class 2606 OID 16494)
-- Name: images images_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_pkey PRIMARY KEY (imageid);


--
-- TOC entry 3191 (class 2606 OID 16515)
-- Name: location location_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_pkey PRIMARY KEY (locationid);


--
-- TOC entry 3193 (class 2606 OID 16524)
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (roleid);


--
-- TOC entry 3187 (class 2606 OID 16454)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (userid);


--
-- TOC entry 3195 (class 2606 OID 16495)
-- Name: images images_userid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_userid_fkey FOREIGN KEY (userid) REFERENCES public.users(userid);


--
-- TOC entry 3194 (class 2606 OID 16525)
-- Name: users users_roleid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_roleid_fkey FOREIGN KEY (roleid) REFERENCES public.roles(roleid);


-- Completed on 2022-12-19 20:00:12

--
-- PostgreSQL database dump complete
--

