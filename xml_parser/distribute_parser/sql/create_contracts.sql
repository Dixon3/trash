--Start Create Tables-------------------------------------
create table _contr (id integer,regNum bigint,number text,publishDate text,signDate text,versionNumber integer,documentBase text,price numeric,currentContractStage text,protocolDate text,uid bigint primary key, file_id integer references files_list(id) on delete cascade );
create table _contrProcedure (regNum bigint,status text,id integer,publishDate text,regNum807 text,versionNumber integer,currentContractStage text,uid bigint primary key,file_id integer references files_list(id) on delete cascade);
create table _contrProcedure_documentMetas (uid bigint primary key, parent_uid bigint references _contrProcedure(uid) on delete cascade );
create table _contrProcedure_documentMetas_documentMeta (sid text,fileName text,docDescription text,url text,uid bigint primary key, parent_uid bigint references _contrProcedure_documentMetas(uid) on delete cascade );
create table _contrProcedure_documentMetas_documentMeta_cryptoSigns (signature text,uid bigint primary key, parent_uid bigint references _contrProcedure_documentMetas_documentMeta(uid) on delete cascade );
create table _contrProcedure_executions (uid bigint primary key, parent_uid bigint references _contrProcedure(uid) on delete cascade );
create table _contrProcedure_executions_execution (execDate text,documentName text,documentNum text,documentDate text,paid text,product text,uid bigint primary key, parent_uid bigint references _contrProcedure_executions(uid) on delete cascade );
create table _contrProcedure_executions_stage (month integer,year integer,uid bigint primary key, parent_uid bigint references _contrProcedure_executions(uid) on delete cascade );
create table _contrProcedure_terminations (uid bigint primary key, parent_uid bigint references _contrProcedure(uid) on delete cascade );
create table _contrProcedure_terminations_termination (paid text,terminationDate text,reason text,uid bigint primary key, parent_uid bigint references _contrProcedure_terminations(uid) on delete cascade );
create table _contrSign (id integer,number text,signDate text,protocolDate text,uid bigint primary key,file_id integer references files_list(id) on delete cascade);
create table _contrSign_customer (regNum bigint,fullName text,uid bigint primary key, parent_uid bigint references _contrSign(uid) on delete cascade );
create table _contrSign_foundation (uid bigint primary key, parent_uid bigint references _contrSign(uid) on delete cascade );
create table _contrSign_foundation_order (notificationNumber text,foundationProtocolNumber text,uid bigint primary key, parent_uid bigint references _contrSign_foundation(uid) on delete cascade );
create table _contrSign_suppliers (uid bigint primary key, parent_uid bigint references _contrSign(uid) on delete cascade );
create table _contrSign_suppliers_supplier (participantType text,inn bigint,kpp integer,organizationName text,factualAddress text,postAddress text,contactEMail text,contactPhone text,contactFax text,additionalInfo text,organizationForm text,uid bigint primary key, parent_uid bigint references _contrSign_suppliers(uid) on delete cascade );
create table _contrSign_suppliers_supplier_contactInfo (lastName text,firstName text,middleName text,uid bigint primary key, parent_uid bigint references _contrSign_suppliers_supplier(uid) on delete cascade );
create table _contrSign_suppliers_supplier_country (countryCode integer,countryFullName text,uid bigint primary key, parent_uid bigint references _contrSign_suppliers_supplier(uid) on delete cascade );
create table _contr_currency (code text,name text,uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_customer (regNum bigint,fullName text,inn bigint,kpp integer,tofk text,uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_documentMetas (uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_documentMetas_documentMeta (sid text,fileName text,docDescription text,url text,uid bigint primary key, parent_uid bigint references _contr_documentMetas(uid) on delete cascade );
create table _contr_documentMetas_documentMeta_cryptoSigns (signature text,uid bigint primary key, parent_uid bigint references _contr_documentMetas_documentMeta(uid) on delete cascade );
create table _contr_execution (month integer,year integer,uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_finances (financeSource text,uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_finances_budget (code text,name text,uid bigint primary key, parent_uid bigint references _contr_finances(uid) on delete cascade );
create table _contr_finances_budgetLevel (code text,name text,uid bigint primary key, parent_uid bigint references _contr_finances(uid) on delete cascade );
create table _contr_finances_budgetary (month integer,year integer,KBK text,price numeric,comment text,substageMonth text,substageYear text,uid bigint primary key, parent_uid bigint references _contr_finances(uid) on delete cascade );
create table _contr_finances_extrabudget (code text,name text,uid bigint primary key, parent_uid bigint references _contr_finances(uid) on delete cascade );
create table _contr_finances_extrabudgetary (month integer,year integer,KOSGU text,price numeric,substageMonth text,substageYear text,uid bigint primary key, parent_uid bigint references _contr_finances(uid) on delete cascade );
create table _contr_foundation (singleCustomer text,uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_foundation_order (notificationNumber text,lotNumber text,pplacing text,uid bigint primary key, parent_uid bigint references _contr_foundation(uid) on delete cascade );
create table _contr_foundation_other (notificationNumber text,pplacing text,uid bigint primary key, parent_uid bigint references _contr_foundation(uid) on delete cascade );
create table _contr_modification (type text,description text,base text,uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_priceChangeReas (id integer,name text,comment text,uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_printForm (fileName text,docDescription text,url text,uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_printForm_cryptoSigns (signature text,uid bigint primary key, parent_uid bigint references _contr_printForm(uid) on delete cascade );
create table _contr_products (uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_products_product (name text,price numeric,sum numeric,quantity text,sid text,uid bigint primary key, parent_uid bigint references _contr_products(uid) on delete cascade );
create table _contr_products_product_OKDP (code text,name text,uid bigint primary key, parent_uid bigint references _contr_products_product(uid) on delete cascade );
create table _contr_products_product_OKEI (code text,name text,uid bigint primary key, parent_uid bigint references _contr_products_product(uid) on delete cascade );
create table _contr_products_product_country (countryCode integer,countryFullName text,uid bigint primary key, parent_uid bigint references _contr_products_product(uid) on delete cascade );
create table _contr_scan (uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_scan_documentMeta (sid text,fileName text,docDescription text,url text,uid bigint primary key, parent_uid bigint references _contr_scan(uid) on delete cascade );
create table _contr_scan_documentMeta_cryptoSigns (signature text,uid bigint primary key, parent_uid bigint references _contr_scan_documentMeta(uid) on delete cascade );
create table _contr_singleCustomerReas (id integer,name text,uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_suppliers (uid bigint primary key, parent_uid bigint references _contr(uid) on delete cascade );
create table _contr_suppliers_supplier (participantType text,inn bigint,kpp integer,organizationForm text,organizationName text,factualAddress text,postAddress text,contactEMail text,contactPhone text,contactFax text,additionalInfo text,uid bigint primary key, parent_uid bigint references _contr_suppliers(uid) on delete cascade );
create table _contr_suppliers_supplier_contactInfo (lastName text,firstName text,middleName text,uid bigint primary key, parent_uid bigint references _contr_suppliers_supplier(uid) on delete cascade );
create table _contr_suppliers_supplier_country (countryCode integer,countryFullName text,uid bigint primary key, parent_uid bigint references _contr_suppliers_supplier(uid) on delete cascade );
create table _contr_suppliers_supplier_legalForm (code integer,singularName text,uid bigint primary key, parent_uid bigint references _contr_suppliers_supplier(uid) on delete cascade );

--End Create Tables---------------------------------------
