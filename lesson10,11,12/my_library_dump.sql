--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

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
-- Name: authors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.authors (
    author_id integer NOT NULL,
    first_name character varying(255),
    last_name character varying(255) NOT NULL,
    full_name character varying(255),
    country character varying(255)
);


ALTER TABLE public.authors OWNER TO postgres;

--
-- Name: authors_author_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.authors_author_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authors_author_id_seq OWNER TO postgres;

--
-- Name: authors_author_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.authors_author_id_seq OWNED BY public.authors.author_id;


--
-- Name: books; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.books (
    book_id integer NOT NULL,
    title character varying(255) NOT NULL,
    grade integer
);


ALTER TABLE public.books OWNER TO postgres;

--
-- Name: books_authors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.books_authors (
    book_id integer NOT NULL,
    author_id integer NOT NULL
);


ALTER TABLE public.books_authors OWNER TO postgres;

--
-- Name: books_book_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.books_book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_book_id_seq OWNER TO postgres;

--
-- Name: books_book_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.books_book_id_seq OWNED BY public.books.book_id;


--
-- Name: order_in_series; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.order_in_series (
    book_id integer NOT NULL,
    series_id integer NOT NULL,
    book_number integer
);


ALTER TABLE public.order_in_series OWNER TO postgres;

--
-- Name: series; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.series (
    series_id integer NOT NULL,
    title character varying(255) NOT NULL
);


ALTER TABLE public.series OWNER TO postgres;

--
-- Name: series_series_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.series_series_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.series_series_id_seq OWNER TO postgres;

--
-- Name: series_series_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.series_series_id_seq OWNED BY public.series.series_id;


--
-- Name: authors author_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authors ALTER COLUMN author_id SET DEFAULT nextval('public.authors_author_id_seq'::regclass);


--
-- Name: books book_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books ALTER COLUMN book_id SET DEFAULT nextval('public.books_book_id_seq'::regclass);


--
-- Name: series series_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.series ALTER COLUMN series_id SET DEFAULT nextval('public.series_series_id_seq'::regclass);


--
-- Data for Name: authors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.authors (author_id, first_name, last_name, full_name, country) FROM stdin;
2	Дэниел	Киз	\N	\N
3	Айзек	Азимов	\N	\N
4	Олдос	Хаксли	Олдос Леонард Хаксли	\N
1	Джордж	Оруэлл	Эрик Артур Блэр	\N
5	Джек	Лондон	Джон Гриффит Чейни	\N
7	Венедикт	Ерофеев	\N	\N
8	Джин	Брюэр	\N	\N
9	Фредрик	Бакман	\N	\N
6	Уильям	Голдинг	Уильям Джеральд Голдинг	\N
10	Михаил	Лермонтов	\N	\N
11	Александр	Лурия	\N	\N
12	Эдвин	Эббот	\N	\N
13	Стивен	Кинг	\N	\N
14	Аркадий	Стругацкий	\N	\N
15	Борис	Стругацкий	\N	\N
16	Дэн	Миллмэн	\N	\N
17	Илья	Ильф	\N	\N
18	Евгений	Петров	\N	\N
19	Энди	Вейер	\N	\N
20	Сергей	Лукьяненко	\N	\N
21	Михаил	Булгаков	\N	\N
22	Мариам	Петросян	\N	\N
23	Курт	Воннегут	\N	\N
24	Роберт	Сальваторе	\N	\N
25	Сергей	Довлатов	\N	\N
26	Станислав	Лем	\N	\N
27	Ю	Несбё	\N	\N
28	Харуки	Мураками	\N	\N
31	Даниэль	Дефо	\N	\N
29	Андрей	Круз	\N	\N
\.


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.books (book_id, title, grade) FROM stdin;
2	Зелёная миля	\N
3	Двенадцать стульев	\N
4	Золотой телёнок	\N
9	Морской волк	\N
11	Планета КА-ПЭКС	\N
12	КА-ПЭКС II. На луче света	\N
13	КА-ПЭКС III. На луче света	\N
21	Библиотекарь	\N
22	Несущий смерть	\N
37	Начало	7
1	1984	10
36	Робинзон Крузо	\N
38	Москва	7
39	Прорыв	6
20	Побег из Шоушенка	10
18	Флатландия	10
16	Герой нашего времени	10
25	Улитка на склоне	9
32	Магический кристалл	6
27	Отель "У погибшего альпиниста"	9
26	Пикник на обочине	10
5	Мартин Иден	10
6	Цветы для Элджернона	10
15	Повелитель мух	9
34	Солярис	8
33	Серебрянные стрелы	5
35	Охотник за головами	8
31	Воин	8
29	Отступник	8
30	Изгнанник	8
28	Механическое пианино	8
24	Малыш	10
23	Лангольеры	10
14	Вторая жизнь Уве	9
10	Москва-Петушки	9
8	О дивный новый мир	9
17	Маленькая книжка о большой памяти	10
7	Я, робот	10
\.


--
-- Data for Name: books_authors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.books_authors (book_id, author_id) FROM stdin;
2	13
3	17
3	18
4	17
4	18
9	5
11	8
12	8
13	8
21	13
22	13
37	29
36	31
38	29
39	29
20	13
18	12
16	10
25	14
25	15
32	24
27	14
27	15
26	14
26	15
5	5
6	2
15	6
34	26
33	24
35	27
31	24
29	24
30	24
28	23
24	14
24	15
23	13
14	9
10	7
7	3
8	4
17	11
\.


--
-- Data for Name: order_in_series; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.order_in_series (book_id, series_id, book_number) FROM stdin;
37	2	1
38	2	2
39	2	3
11	1	1
12	1	2
13	1	3
29	3	1
30	3	2
31	3	3
32	4	1
33	4	2
\.


--
-- Data for Name: series; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.series (series_id, title) FROM stdin;
1	КА-ПЭКС
2	Эпоха мёртвых
3	Тёмный эльф
4	Долина ледяного ветра
\.


--
-- Name: authors_author_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.authors_author_id_seq', 31, true);


--
-- Name: books_book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.books_book_id_seq', 39, true);


--
-- Name: series_series_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.series_series_id_seq', 4, true);


--
-- Name: authors authors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.authors
    ADD CONSTRAINT authors_pkey PRIMARY KEY (author_id);


--
-- Name: books_authors books_authors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books_authors
    ADD CONSTRAINT books_authors_pkey PRIMARY KEY (book_id, author_id);


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (book_id);


--
-- Name: order_in_series order_in_series_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_in_series
    ADD CONSTRAINT order_in_series_pkey PRIMARY KEY (book_id, series_id);


--
-- Name: series series_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.series
    ADD CONSTRAINT series_pkey PRIMARY KEY (series_id);


--
-- Name: books_authors books_authors_author_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books_authors
    ADD CONSTRAINT books_authors_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.authors(author_id);


--
-- Name: books_authors books_authors_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.books_authors
    ADD CONSTRAINT books_authors_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(book_id);


--
-- Name: order_in_series order_in_series_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_in_series
    ADD CONSTRAINT order_in_series_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(book_id);


--
-- Name: order_in_series order_in_series_series_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.order_in_series
    ADD CONSTRAINT order_in_series_series_id_fkey FOREIGN KEY (series_id) REFERENCES public.series(series_id);


--
-- PostgreSQL database dump complete
--

