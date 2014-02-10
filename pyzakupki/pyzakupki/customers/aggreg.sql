create table customers_contr_aggr as (
SELECT 
  _contr_customer.regnum,  
  _contr_customer.inn, 
  _contr_customer.kpp, 
  sum(_contr.price),
  count(_contr.price)
FROM 
  public._contr, 
  public._contr_customer
WHERE 
  _contr_customer.parent_uid = _contr.uid group by _contr_customer.regnum,inn,kpp
);

create or replace function customer_contr_aggr_mv_insert() returns trigger as'
declare
begin
    if exists (select 1 from customers_contr_aggr where regnum=NEW.regnum and inn=NEW.inn and kpp=NEW.kpp)
   then 
        update customers_contr_aggr set sum=sum+(select _contr.price from public._contr where _contr.uid = NEW.parent_uid ) where regnum=NEW.regnum and inn=NEW.inn and kpp=NEW.kpp;
        update customers_contr_aggr set count=count+1 where regnum=NEW.regnum and inn=NEW.inn and kpp=NEW.kpp;
   else insert into customers_contr_aggr (regnum,inn,kpp,sum,count) values (new.regnum,new.inn,new.kpp,(select _contr.price from public._contr where _contr.uid = NEW.parent_uid),1);
   end if;
   return NEW;
end;
'LANGUAGE  plpgsql;


CREATE TRIGGER customer_contr_aggr_ins
AFTER INSERT ON public._contr_customer FOR EACH ROW 
EXECUTE PROCEDURE customer_contr_aggr_mv_insert();
