create table company
	(store_code serial NOT NULL,
    store_name character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    passwd character varying(255) NOT NULL,
    phone character varying(255) NOT NULL,
    PRIMARY KEY (store_code)	
);
	
create table advertisement
	(ad_code serial NOT NULL,
     store_code serial NOT NULL,
     title character varying(255) NOT NULL,
     contents character varying(255) NOT NULL,
     summary character varying(255) NOT NULL,
     image bytea NOT NULL,
     start_date date NOT NULL,
     deadline date NOT NULL,
     PRIMARY KEY (ad_code),
	 foreign key (store_code) references company(store_code)
		on delete set null
	);

create table report
	(ad_code serial NOT NULL,
     click_num integer NOT NULL,
     click_per integer NOT NULL,
     benefit integer NOT NULL,
     benefit_per integer NOT NULL,
     preference integer NOT NULL,
     measure_date date NOT NULL,
     PRIMARY KEY (ad_code),
	 foreign key (ad_code) references advertisement(ad_code)
		on delete set null
	);
	
create table customer
	(customer_ID serial NOT NULL,
    type1 character varying(255) NOT NULL,
    type2 character varying(255) NOT NULL,
    type3 character varying(255) NOT NULL,
    PRIMARY KEY (customer_ID)
	);
