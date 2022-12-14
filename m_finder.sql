PGDMP     :    7                z            m_finder    14.6    14.6 "               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16444    m_finder    DATABASE     l   CREATE DATABASE m_finder WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE m_finder;
                postgres    false            ?            1259    16486    images    TABLE     k  CREATE TABLE public.images (
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
    DROP TABLE public.images;
       public         heap    postgres    false            ?            1259    16485    images_imageid_seq    SEQUENCE     ?   CREATE SEQUENCE public.images_imageid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.images_imageid_seq;
       public          postgres    false    212                       0    0    images_imageid_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.images_imageid_seq OWNED BY public.images.imageid;
          public          postgres    false    211            ?            1259    16508    location    TABLE     ?   CREATE TABLE public.location (
    locationid integer NOT NULL,
    city character varying(255),
    region character varying(255),
    country character varying(255),
    latitude character varying(255),
    longitude character varying(255)
);
    DROP TABLE public.location;
       public         heap    postgres    false            ?            1259    16507    location_locationid_seq    SEQUENCE     ?   CREATE SEQUENCE public.location_locationid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.location_locationid_seq;
       public          postgres    false    214                       0    0    location_locationid_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.location_locationid_seq OWNED BY public.location.locationid;
          public          postgres    false    213            ?            1259    16517    roles    TABLE     X   CREATE TABLE public.roles (
    roleid integer NOT NULL,
    role_name text NOT NULL
);
    DROP TABLE public.roles;
       public         heap    postgres    false            ?            1259    16516    roles_roleid_seq    SEQUENCE     ?   CREATE SEQUENCE public.roles_roleid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.roles_roleid_seq;
       public          postgres    false    216                       0    0    roles_roleid_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.roles_roleid_seq OWNED BY public.roles.roleid;
          public          postgres    false    215            ?            1259    16446    users    TABLE     .  CREATE TABLE public.users (
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
    DROP TABLE public.users;
       public         heap    postgres    false            ?            1259    16445    users_userid_seq    SEQUENCE     ?   CREATE SEQUENCE public.users_userid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.users_userid_seq;
       public          postgres    false    210                       0    0    users_userid_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.users_userid_seq OWNED BY public.users.userid;
          public          postgres    false    209            m           2604    16489    images imageid    DEFAULT     p   ALTER TABLE ONLY public.images ALTER COLUMN imageid SET DEFAULT nextval('public.images_imageid_seq'::regclass);
 =   ALTER TABLE public.images ALTER COLUMN imageid DROP DEFAULT;
       public          postgres    false    212    211    212            p           2604    16511    location locationid    DEFAULT     z   ALTER TABLE ONLY public.location ALTER COLUMN locationid SET DEFAULT nextval('public.location_locationid_seq'::regclass);
 B   ALTER TABLE public.location ALTER COLUMN locationid DROP DEFAULT;
       public          postgres    false    213    214    214            q           2604    16520    roles roleid    DEFAULT     l   ALTER TABLE ONLY public.roles ALTER COLUMN roleid SET DEFAULT nextval('public.roles_roleid_seq'::regclass);
 ;   ALTER TABLE public.roles ALTER COLUMN roleid DROP DEFAULT;
       public          postgres    false    215    216    216            k           2604    16449    users userid    DEFAULT     l   ALTER TABLE ONLY public.users ALTER COLUMN userid SET DEFAULT nextval('public.users_userid_seq'::regclass);
 ;   ALTER TABLE public.users ALTER COLUMN userid DROP DEFAULT;
       public          postgres    false    209    210    210            
          0    16486    images 
   TABLE DATA                 public          postgres    false    212   ?$                 0    16508    location 
   TABLE DATA                 public          postgres    false    214   ?%                 0    16517    roles 
   TABLE DATA                 public          postgres    false    216   '                 0    16446    users 
   TABLE DATA                 public          postgres    false    210   '                  0    0    images_imageid_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.images_imageid_seq', 4, true);
          public          postgres    false    211                       0    0    location_locationid_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.location_locationid_seq', 22, true);
          public          postgres    false    213                       0    0    roles_roleid_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.roles_roleid_seq', 1, false);
          public          postgres    false    215                       0    0    users_userid_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.users_userid_seq', 3, true);
          public          postgres    false    209            u           2606    16494    images images_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_pkey PRIMARY KEY (imageid);
 <   ALTER TABLE ONLY public.images DROP CONSTRAINT images_pkey;
       public            postgres    false    212            w           2606    16515    location location_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_pkey PRIMARY KEY (locationid);
 @   ALTER TABLE ONLY public.location DROP CONSTRAINT location_pkey;
       public            postgres    false    214            y           2606    16524    roles roles_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (roleid);
 :   ALTER TABLE ONLY public.roles DROP CONSTRAINT roles_pkey;
       public            postgres    false    216            s           2606    16454    users users_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (userid);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    210            {           2606    16495    images images_userid_fkey    FK CONSTRAINT     {   ALTER TABLE ONLY public.images
    ADD CONSTRAINT images_userid_fkey FOREIGN KEY (userid) REFERENCES public.users(userid);
 C   ALTER TABLE ONLY public.images DROP CONSTRAINT images_userid_fkey;
       public          postgres    false    212    3187    210            z           2606    16525    users users_roleid_fkey    FK CONSTRAINT     y   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_roleid_fkey FOREIGN KEY (roleid) REFERENCES public.roles(roleid);
 A   ALTER TABLE ONLY public.users DROP CONSTRAINT users_roleid_fkey;
       public          postgres    false    3193    216    210            
   ^  x?ՒMo?0???V/m?? ?c?J??n?J?+J!-ـ H??K?n???I???v剷q??`??Q??g???u0?=?????״b??Wl???\?t??uY˛!??ֱ3/?p??T?N?jr*Y?R?@??I??k7?/?u?;n?;?ك(???G84???B?:?&?h?6qb5?+??,)ƶ??\L<s?!??[? l? r=??}?su#?????v??Ìܑ???Ȉ#???=?0?b? )y?M???֢?e??U՝?/????	?>??,2?z?????'?????0?hY"X?e#,#??????Fč??
?%??6d?	M&???,           x???Ok?0???"??????]?N=? 7?vwkC	H2???]7?\:??y?????S???????	??N?YgڦWF??9?}?Z?Sd???n2??????.}8?z]V??͋??FY?S?KD?ּ+????Q?c3?;??p??q??q\?q???!??>&??)?`?<'??I"q??۪?~?"?, ?A?Hx??s9???.?????n??+??_?㩅???O?D??Y??' ?1?4<?S?OSL쩌??=??p?| ?{?         T   x???v
Q???W((M??L?+??I-V? Q?):
 :>/17US!??'?5XA?HGA=1%73O]Ӛ˓?&????? ?(?         G  x????NA??<??6?V????R?@?????d??D{???3?D?h?pc˿???V???????;t?U???omӢɐ??Q??Q?5t??1Ҿ?@w1??2F'h?w߄?Ɨv?h;??v?????#??E`*WG??q]??"??e?dG??e????f?}54O?09??G???1KB????c?Y?Cߝ?51c#,??cKe*uFh?-ǘ??r!S?álB?`?L????????t??l4??????x????#???%?'*z???F.??˽W??q.ɹ 4B?"?? !)?\??r	JK?V?4?0?Q*C???????$åy     