--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: connections; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE connections (
    request_id integer NOT NULL,
    pet_id integer,
    owner_id integer,
    seeker_id integer,
    connection_status character varying
);


ALTER TABLE public.connections OWNER TO vagrant;

--
-- Name: connections_request_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE connections_request_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.connections_request_id_seq OWNER TO vagrant;

--
-- Name: connections_request_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE connections_request_id_seq OWNED BY connections.request_id;


--
-- Name: owners; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE owners (
    owner_id integer NOT NULL,
    user_id integer
);


ALTER TABLE public.owners OWNER TO vagrant;

--
-- Name: owners_owner_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE owners_owner_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.owners_owner_id_seq OWNER TO vagrant;

--
-- Name: owners_owner_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE owners_owner_id_seq OWNED BY owners.owner_id;


--
-- Name: pet_photos; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE pet_photos (
    photo_id integer NOT NULL,
    pet_id integer,
    image_url character varying(200),
    caption character varying(100)
);


ALTER TABLE public.pet_photos OWNER TO vagrant;

--
-- Name: pet_photos_photo_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE pet_photos_photo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pet_photos_photo_id_seq OWNER TO vagrant;

--
-- Name: pet_photos_photo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE pet_photos_photo_id_seq OWNED BY pet_photos.photo_id;


--
-- Name: pets; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE pets (
    pet_id integer NOT NULL,
    name character varying(50),
    age integer,
    gender character varying(1),
    size character varying(10),
    color character varying(50),
    breed character varying(50),
    animal_type character varying(3),
    owner_id integer,
    is_available boolean,
    character_details character varying(300),
    health_details character varying(300),
    image_url character varying(200)
);


ALTER TABLE public.pets OWNER TO vagrant;

--
-- Name: pets_pet_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE pets_pet_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pets_pet_id_seq OWNER TO vagrant;

--
-- Name: pets_pet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE pets_pet_id_seq OWNED BY pets.pet_id;


--
-- Name: seekers; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE seekers (
    seeker_id integer NOT NULL,
    user_id integer,
    household_size integer,
    children integer,
    pet_experience character varying(10)
);


ALTER TABLE public.seekers OWNER TO vagrant;

--
-- Name: seekers_seeker_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE seekers_seeker_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.seekers_seeker_id_seq OWNER TO vagrant;

--
-- Name: seekers_seeker_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE seekers_seeker_id_seq OWNED BY seekers.seeker_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant; Tablespace: 
--

CREATE TABLE users (
    user_id integer NOT NULL,
    last_name character varying(50),
    first_name character varying(50),
    email character varying(64),
    password character varying(64),
    phone_number character varying(12),
    birthdate timestamp without time zone,
    occupation character varying(50),
    address character varying(100),
    city character varying(50),
    state character varying(2),
    zipcode character varying(15),
    image_url character varying(200)
);


ALTER TABLE public.users OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE users_user_id_seq OWNED BY users.user_id;


--
-- Name: request_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY connections ALTER COLUMN request_id SET DEFAULT nextval('connections_request_id_seq'::regclass);


--
-- Name: owner_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY owners ALTER COLUMN owner_id SET DEFAULT nextval('owners_owner_id_seq'::regclass);


--
-- Name: photo_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY pet_photos ALTER COLUMN photo_id SET DEFAULT nextval('pet_photos_photo_id_seq'::regclass);


--
-- Name: pet_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY pets ALTER COLUMN pet_id SET DEFAULT nextval('pets_pet_id_seq'::regclass);


--
-- Name: seeker_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY seekers ALTER COLUMN seeker_id SET DEFAULT nextval('seekers_seeker_id_seq'::regclass);


--
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY users ALTER COLUMN user_id SET DEFAULT nextval('users_user_id_seq'::regclass);


--
-- Data for Name: connections; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY connections (request_id, pet_id, owner_id, seeker_id, connection_status) FROM stdin;
1	1	1	4	Interested
2	1	1	2	Interested
\.


--
-- Name: connections_request_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('connections_request_id_seq', 2, true);


--
-- Data for Name: owners; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY owners (owner_id, user_id) FROM stdin;
1	1
2	2
3	3
4	4
5	5
6	6
7	7
8	11
9	12
10	14
11	15
12	16
13	17
14	18
15	19
16	20
17	21
18	22
19	23
\.


--
-- Name: owners_owner_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('owners_owner_id_seq', 19, true);


--
-- Data for Name: pet_photos; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY pet_photos (photo_id, pet_id, image_url, caption) FROM stdin;
1	1	/static/images/pet_photos/ghost01.gif	When I was a wee pup.
2	1	/static/images/pet_photos/ghost02.jpg	On the iron throne with my badass BFF.
3	9	/static/images/pet_photos/gingerale01.jpg	With my mom.
4	9	/static/images/pet_photos/gingerale02.jpg	Chilling on my favorite throw
5	9	/static/images/pet_photos/gingerale03.jpg	I love Santa.
6	6	/static/images/pet_photos/hobbes01.jpg	I like to hold hands while napping.
7	6	/static/images/pet_photos/hobbes02.jpg	
8	6	/static/images/pet_photos/hobbes03.jpg	Rub my cheeks.=)
9	6	/static/images/pet_photos/hobbes04.jpg	I love belly rubs.
10	11	/static/images/pet_photos/junior01.jpg	
11	12	/static/images/pet_photos/rusty01.jpg	Chillin'
12	12	/static/images/pet_photos/rusty02.jpg	I love to climb.
13	4	/static/images/pet_photos/lady01.jpg	With my human BFF.
14	13	/static/images/pet_photos/marley01.jpg	I love Christmas time treats.
15	13	/static/images/pet_photos/marley02.jpg	Hanging with my mom.
16	13	/static/images/pet_photos/marley03.jpg	Hanging with my mom.
17	10	/static/images/pet_photos/peenutbutter01.jpg	
18	10	/static/images/pet_photos/peenutbutter02.jpg	I love walks.
19	10	/static/images/pet_photos/peenutbutter03.jpg	
20	2	/static/images/pet_photos/summer01.jpg	I watch over my human BFF every night.
21	2	/static/images/pet_photos/summer02.jpg	OMG! I am adorable as a pup.
22	5	/static/images/pet_photos/greywind01.jpg	We are fierce!
23	5	/static/images/pet_photos/greywind02.jpg	Me as a pup.
24	14	/static/images/pet_photos/emmalucy01.jpg	Hanging with my buddy.
25	15	/static/images/pet_photos/emmalucy01.jpg	Hanging with my buddy.
\.


--
-- Name: pet_photos_photo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('pet_photos_photo_id_seq', 25, true);


--
-- Data for Name: pets; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY pets (pet_id, name, age, gender, size, color, breed, animal_type, owner_id, is_available, character_details, health_details, image_url) FROM stdin;
1	Ghost	6	M	140lbs	white	direwolf	dog	1	t	Super loyal, badass warrior, independent traveler, and perfect right hand guard in battle.	Runt at birth but no longer now	/static/images/pet_profiles/ghost.gif
2	Summer	6	M	138lbs	light beige and white	direwolf	dog	4	t	Super loyal and protector of Bran Stark. Always saving Bran and his friends from white walkers.	Sporting battle scars.	/static/images/pet_profiles/summer.jpg
3	Nymeria	6	F	139lbs	grey and white	direwolf	dog	2	t	Faithful to Arya, biter of Joffrey		/static/images/pet_profiles/nymeria.jpg
4	Lady	6	F	128lbs	grey and white	direwolf	dog	3	t	Superfriendly and gullible. Saintly.	Bleeding stab wounds.	/static/images/pet_profiles/lady.jpg
5	Grey Wind	6	M	141lbs	grey and white	direwolf	dog	5	t	Super loyal, badass warrior. Notorious reputation for fighting in battles.	Bleeding stab wounds.	/static/images/pet_profiles/greywind.jpg
6	Hobbes	3	M	14lbs	orange with black stripes	tabby	cat	6	t	Snuggle master, purring machine. Loves all humans and wants to play all the time. Highly motivated by food and is always hungry. Loves to welcome my favorite humans at the door.		/static/images/pet_profiles/hobbes.jpg
7	Choe	7	F	12lbs	brown	tabby	cat	12	t	Diva. Catitude level high. Really independent.		/static/images/pet_profiles/choe.jpg
8	Jiao Jiao	5	F	11lbs	parti	Pomeranian	dog	15	t	catlike	splendid	/static/images/pet_profiles/jiaojiao.jpg
9	Ginger Ale	15	F	18lbs	brown and white	dachshund/beagle	dog	8	t	Loves to sleep. Likes to be tucked in to her bed. She has a heating pad in her bed so she loves napping even more. She loves eating cucumbers as a snack. Loves car rides. She loves to roll around. She's horrible and always gets in my purse.	Poor thing is old but she's actually pretty healthy. A slight heart murmur and hearing is kind of going but otherwise she's really healthy.	/static/images/pet_profiles/gingerale.jpg
10	Peenut Butter	4	M	12lbs	golden brown	Chihuahua/Pomeranian Mix	dog	9	t	Trained, calm, sweet, enjoys going for runs		/static/images/pet_profiles/peenutbutter.jpg
11	Junior	7	M	100lbs	yellow	Labrador	dog	11	t	exuberant, friendly, likes to play ball	walks under 3 miles long are better and he doesn't like to walk on hot surfaces	/static/images/pet_profiles/junior.jpg
12	Rusty	13	F	16.8lbs	orange and white	maine coon	cat	11	t	good hunter	healthy	/static/images/pet_profiles/rusty.jpg
13	Marley	4	M	88lbs	black	labradoodle	dog	17	t	Lots of energy and loves to play. Wants to be everyone's best friend.	healthy	/static/images/pet_profiles/marley.jpg
14	Emma	10	F	67lbs	ginger with white markings	pitbull	dog	18	t	very affectionate with people. Loves walks, belly rubs and sitting next to you on the sofa. Also likes a good game of tug and wrestling. Only likes dogs she's been properly introduced to. She and Emma get along great and if you take them both they're good entertainment.		/static/images/pet_profiles/emma.jpg
15	Lucy	2	F	15lbs	white and tan	longhair chihuahua	dog	18	t	ery sweet. Good for jogs and loves to chase the ball. She and Emma get along great and if you take them both they're good entertainment.		/static/images/pet_profiles/lucy.jpg
\.


--
-- Name: pets_pet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('pets_pet_id_seq', 15, true);


--
-- Data for Name: seekers; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY seekers (seeker_id, user_id, household_size, children, pet_experience) FROM stdin;
1	13	5	3	True
2	8	0	0	False
3	10	9	3	True
4	9	0	0	True
\.


--
-- Name: seekers_seeker_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('seekers_seeker_id_seq', 4, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY users (user_id, last_name, first_name, email, password, phone_number, birthdate, occupation, address, city, state, zipcode, image_url) FROM stdin;
1	Snow	John	jsnow@gmail.com	484529593079221494	415-555-5555	1980-12-01 00:00:00	King of the North	123 Lake St	San Francisco	CA	94121	/static/images/users/johnsnow.jpg
2	Stark	Arya	astark@gmail.com	484529593079221494	415-555-5555	1986-01-01 00:00:00	Assassin	123 Lake St	San Francisco	CA	94121	/static/images/users/aryastark.jpg
3	Stark	Sansa	sstark@gmail.com	484529593079221494	415-555-5555	1984-08-14 00:00:00	Heir to Winterfell	123 Lake St	San Francisco	CA	94121	/static/images/users/sansastark.jpg
4	Stark	Bran	bstark@gmail.com	484529593079221494	415-555-5555	1988-03-01 00:00:00	The Raven	123 Lake St	San Francisco	CA	94121	/static/images/users/branstark.jpg
5	Stark	Robb	rstark@gmail.com	484529593079221494	415-555-5555	1979-09-11 00:00:00	former King of the North	123 Lake St	San Francisco	CA	94121	/static/images/users/robbstark.jpg
6	Ma	Yenly	ymmisc@gmail.com	484529593079221494	415-555-5555	1978-12-04 00:00:00	Software Engineering Fellow	456 Geary St	San Francisco	CA	94121	/static/images/users/yen.jpg
7	White	Walter	wwhite@gmail.com	484529593079221494	415-555-5555	1949-10-04 00:00:00	Chemistry Teacher	123 Mission St	San Francisco	CA	94110	/static/images/users/walterwhite.jpg
8	Pinkman	Jesse	jpinkman@gmail.com	484529593079221494	415-555-5555	1998-04-01 00:00:00	college student	456 Mission St	San Francisco	CA	94110	/static/images/users/jessepinkman.jpg
9	Lannister	Tyrion	tyrion@gmail.com	484529593079221494	415-555-5555	1975-07-11 00:00:00	Queen's Hand	123 Heartwood Drive	Oakland	CA	94611	/static/images/users/tyrion.jpg
10	Targaryen	Dani	dtargaryen@gmail.com	484529593079221494	415-555-5555	1995-01-01 00:00:00	Mother of Dragons	123 Heartwood Drive	Oakland	CA	94611	/static/images/users/dani.jpg
11	Tayaran	Taraneh	tara@gmail.com	484529593079221494	415-555-5555	1995-02-14 00:00:00	Software Engineer	123 Howard St	San Francisco	CA	94103	/static/images/users/taraneh.jpg
12	Hoang	Vivian	vivian@gmailc.om	484529593079221494	415-555-5555	1995-05-29 00:00:00	Software Engineer	789 Mission St	San Francisco	CA	94110	/static/images/users/vivian.jpg
13	Lannister	Cersei	cersei@gmail.com	484529593079221494	415-555-5555	1972-10-31 00:00:00	Queen Mother	123 Valencia St	San Francisco	CA	94110	/static/images/users/cersei.png
14	Lannister	Jamie	jamie@gmail.com	484529593079221494	415-555-5555	1972-10-31 00:00:00	King's Guard	123 Valencia St	San Francisco	CA	94110	/static/images/users/jamiel.jpg
15	Bard	Lori	lori@gmail.com	484529593079221494	415-555-5555	1995-08-08 00:00:00	Software Engineer	123 Mountain Ave	Oakland	CA	94611	/static/images/users/lori.jpg
16	Parr	Bob	bob@gmail.com	484529593079221494	415-555-5555	1973-09-18 00:00:00	Mr. Incredible	234 Mountain Ave	Oakland	CA	94611	/static/images/users/mrincredible.jpg
17	Best	Lucius	lbest@gmail.com	484529593079221494	415-555-5555	1977-06-03 00:00:00	Frozone	345 Mountain Ave	Oakland	CA	94611	/static/images/users/frozon.jpg
18	Parr	Violet	violet@gmail.com	484529593079221494	415-555-5555	2000-12-25 00:00:00	student	234 Mountain Ave	Oakland	CA	94611	/static/images/users/violet.jpg
19	Liu	Francis	francis@gmail.com	484529593079221494	415-555-5555	1995-11-04 00:00:00	Software Engineer	123 Howard St	San Francisco	CA	94103	/static/images/users/francis.jpg
20	Foundation	Nine Lives	ninelives@gmail.com	484529593079221494	415-555-5555	2000-06-15 00:00:00	Cat Shelter	234 Howard St	San Francisco	CA	94103	/static/images/users/ninelives.jpg
21	Shih	Jessica	jessica@gmail.com	484529593079221494	415-555-5555	1985-08-16 00:00:00	PR Manager	234 Lake St	San Francisco	CA	94121	/static/images/users/jessica.jpg
22	Patel	Manisha	manisha@gmail.com	484529593079221494	415-555-5555	1995-05-28 00:00:00	Software Engineer	123 Lakeshore Ave	Oakland	CA	94612	/static/images/users/manisha.jpg
23	Rescue	Rocket Dog	rocketdog@gmail.com	484529593079221494	415-555-5555	2001-03-01 00:00:00	Dog Shelter	456 Mountain Ave	Oakland	CA	94611	/static/images/users/rocketdog.png
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('users_user_id_seq', 23, true);


--
-- Name: connections_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY connections
    ADD CONSTRAINT connections_pkey PRIMARY KEY (request_id);


--
-- Name: owners_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY owners
    ADD CONSTRAINT owners_pkey PRIMARY KEY (owner_id);


--
-- Name: pet_photos_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY pet_photos
    ADD CONSTRAINT pet_photos_pkey PRIMARY KEY (photo_id);


--
-- Name: pets_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY pets
    ADD CONSTRAINT pets_pkey PRIMARY KEY (pet_id);


--
-- Name: seekers_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY seekers
    ADD CONSTRAINT seekers_pkey PRIMARY KEY (seeker_id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: connections_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY connections
    ADD CONSTRAINT connections_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES owners(owner_id);


--
-- Name: connections_pet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY connections
    ADD CONSTRAINT connections_pet_id_fkey FOREIGN KEY (pet_id) REFERENCES pets(pet_id);


--
-- Name: connections_seeker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY connections
    ADD CONSTRAINT connections_seeker_id_fkey FOREIGN KEY (seeker_id) REFERENCES seekers(seeker_id);


--
-- Name: owners_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY owners
    ADD CONSTRAINT owners_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: pet_photos_pet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY pet_photos
    ADD CONSTRAINT pet_photos_pet_id_fkey FOREIGN KEY (pet_id) REFERENCES pets(pet_id);


--
-- Name: pets_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY pets
    ADD CONSTRAINT pets_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES owners(owner_id);


--
-- Name: seekers_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY seekers
    ADD CONSTRAINT seekers_user_id_fkey FOREIGN KEY (user_id) REFERENCES users(user_id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

