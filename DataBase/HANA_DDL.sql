create table advertiser
	(company_ID varchar(15) not null,
	 email		varchar(15),
	 pw 		varchar(15),
	 phone_number	varchar(7),
	 company_name	varchar(7) not null,
	 primary key (company_ID)
	);
	
create table advertising
	(ad_ID		varchar(15) not null,
	 company_ID varchar(15) not null,
	 group_ID	varchar(5) NOT NULL,
	 ad_title   varchar(20) not null, 
	 ad_text	varchar(200) not null, 
	 ad_category	varchar(15) not null, 
	 image 		varchar(200) not null,
	 target_customer 	varchar(15) not null,
	 start_date		date not null,
	 deadline		date,
	 primary key (ad_ID),
	 foreign key (company_ID) references advertiser(company_ID)
		on delete set null
	);

create table customer_group
	(group_ID	varchar(5) NOT NULL, 
	 age_range	varchar(20) NOT NULL, 
	 gender		varchar(20) NOT NULL, 
	 Cons_category  varchar(20) NOT NULL, 
	 region		varchar(20), 
	 primary key (group_ID)
	);
	

ALTER TABLE advertising
ADD FOREIGN KEY (group_ID)
REFERENCES customer_group(group_ID);


create table report
	(ad_ID	    varchar(15) NOT NULL, 
	 group_ID	varchar(5) NOT NULL,
	 click_num  int NOT NULL,
	 click_per  int,
	 benefit    int NOT NULL,
	 benefit_per int,
	 preference  int,
	 primary key (ad_ID, group_ID),
	 foreign key (ad_ID) references advertising(ad_ID)
		on delete set null,
	 foreign key (group_ID) references customer_group(group_ID)
		on delete set null
	);
	

