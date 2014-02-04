# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Contr(models.Model):
    id = models.IntegerField(null=True, blank=True)
    regnum = models.BigIntegerField(null=True, blank=True)
    number = models.TextField(blank=True)
    publishdate = models.TextField(blank=True)
    signdate = models.TextField(blank=True)
    versionnumber = models.IntegerField(null=True, blank=True)
    documentbase = models.TextField(blank=True)
    price = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    currentcontractstage = models.TextField(blank=True)
    protocoldate = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    file = models.ForeignKey('FilesList', null=True, blank=True)

    def get_absolute_url(self):
        return "/obj/Contr/%i"%self.uid


    class Meta:
        db_table = '_contr'

class ContrCurrency(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_currency'

class ContrCustomer(models.Model):
    regnum = models.BigIntegerField(null=True, blank=True)
    fullname = models.TextField(blank=True)
    inn = models.BigIntegerField(null=True, blank=True)
    kpp = models.IntegerField(null=True, blank=True)
    tofk = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_customer'

class ContrDocumentmetas(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_documentmetas'

class ContrDocumentmetasDocumentmeta(models.Model):
    sid = models.TextField(blank=True)
    filename = models.TextField(blank=True)
    docdescription = models.TextField(blank=True)
    url = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrDocumentmetas, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_documentmetas_documentmeta'

class ContrDocumentmetasDocumentmetaCryptosigns(models.Model):
    signature = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrDocumentmetasDocumentmeta, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_documentmetas_documentmeta_cryptosigns'

class ContrExecution(models.Model):
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_execution'

class ContrFinances(models.Model):
    financesource = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_finances'

class ContrFinancesBudget(models.Model):
    code = models.BigIntegerField(null=True, blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrFinances, null=True, db_column='parent_uid', blank=True)
    code_num = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = '_contr_finances_budget'

class ContrFinancesBudgetary(models.Model):
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    kbk = models.TextField(blank=True)
    price = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    comment = models.TextField(blank=True)
    substagemonth = models.TextField(blank=True)
    substageyear = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrFinances, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_finances_budgetary'

class ContrFinancesBudgetlevel(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrFinances, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_finances_budgetlevel'

class ContrFinancesExtrabudget(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrFinances, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_finances_extrabudget'

class ContrFinancesExtrabudgetary(models.Model):
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    kosgu = models.TextField(blank=True)
    price = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    substagemonth = models.TextField(blank=True)
    substageyear = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrFinances, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_finances_extrabudgetary'

class ContrFoundation(models.Model):
    singlecustomer = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_foundation'

class ContrFoundationOrder(models.Model):
    notificationnumber = models.TextField(blank=True)
    lotnumber = models.TextField(blank=True)
    pplacing = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrFoundation, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_foundation_order'

class ContrFoundationOther(models.Model):
    notificationnumber = models.TextField(blank=True)
    pplacing = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrFoundation, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_foundation_other'

class ContrModification(models.Model):
    type = models.TextField(blank=True)
    description = models.TextField(blank=True)
    base = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_modification'

class ContrPricechangereas(models.Model):
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_pricechangereas'

class ContrPrintform(models.Model):
    filename = models.TextField(blank=True)
    docdescription = models.TextField(blank=True)
    url = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_printform'

#class ContrPrintformCryptosigns(models.Model):
#    signature = models.TextField(blank=True)
#    uid = models.IntegerField(primary_key=True)
#    parent_uid = models.ForeignKey(ContrPrintform, null=True, db_column='parent_uid', blank=True)
#    class Meta:
#        db_table = '_contr_printform_cryptosigns'

class ContrProducts(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_products'

class ContrProductsProduct(models.Model):
    name = models.TextField(blank=True)
    price = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    sum = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    quantity = models.TextField(blank=True)
    sid = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrProducts, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_products_product'

class ContrProductsProductCountry(models.Model):
    countrycode = models.IntegerField(null=True, blank=True)
    countryfullname = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrProductsProduct, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_products_product_country'

class ContrProductsProductOkdp(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrProductsProduct, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_products_product_okdp'

class ContrProductsProductOkei(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrProductsProduct, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_products_product_okei'

class ContrScan(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_scan'

class ContrScanDocumentmeta(models.Model):
    sid = models.TextField(blank=True)
    filename = models.TextField(blank=True)
    docdescription = models.TextField(blank=True)
    url = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrScan, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_scan_documentmeta'

class ContrScanDocumentmetaCryptosigns(models.Model):
    signature = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrScanDocumentmeta, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_scan_documentmeta_cryptosigns'

class ContrSinglecustomerreas(models.Model):
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_singlecustomerreas'

class ContrSuppliers(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contr, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_suppliers'

class ContrSuppliersSupplier(models.Model):
    idnumber = models.BigIntegerField(null=True, blank=True)
    idnumberextension = models.BigIntegerField(null=True, blank=True)
    participanttype = models.TextField(blank=True)
    inn = models.BigIntegerField(null=True, blank=True)
    kpp = models.IntegerField(null=True, blank=True)
    organizationform = models.TextField(blank=True)
    organizationname = models.TextField(blank=True)
    factualaddress = models.TextField(blank=True)
    postaddress = models.TextField(blank=True)
    contactemail = models.TextField(blank=True)
    contactphone = models.TextField(blank=True)
    contactfax = models.TextField(blank=True)
    additionalinfo = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrSuppliers, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_suppliers_supplier'

class ContrSuppliersSupplierContactinfo(models.Model):
    lastname = models.TextField(blank=True)
    firstname = models.TextField(blank=True)
    middlename = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrSuppliersSupplier, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_suppliers_supplier_contactinfo'

class ContrSuppliersSupplierCountry(models.Model):
    countrycode = models.IntegerField(null=True, blank=True)
    countryfullname = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrSuppliersSupplier, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contr_suppliers_supplier_country'

class ContrSuppliersSupplierGeocode(models.Model):
    uid = models.ForeignKey(ContrSuppliersSupplier, primary_key=True, db_column='uid')
    palce = models.TextField(blank=True)
    lat = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    lng = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    class Meta:
        db_table = '_contr_suppliers_supplier_geocode'

class Contrprocedure(models.Model):
    regnum = models.BigIntegerField(null=True, blank=True)
    status = models.TextField(blank=True)
    id = models.IntegerField(null=True, blank=True)
    publishdate = models.TextField(blank=True)
    regnum807 = models.TextField(blank=True)
    versionnumber = models.IntegerField(null=True, blank=True)
    currentcontractstage = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    file = models.ForeignKey('FilesList', null=True, blank=True)
    class Meta:
        db_table = '_contrprocedure'

class ContrprocedureDocumentmetas(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contrprocedure, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrprocedure_documentmetas'

class ContrprocedureDocumentmetasDocumentmeta(models.Model):
    sid = models.TextField(blank=True)
    filename = models.TextField(blank=True)
    docdescription = models.TextField(blank=True)
    url = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrprocedureDocumentmetas, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrprocedure_documentmetas_documentmeta'

class ContrprocedureDocumentmetasDocumentmetaCryptosigns(models.Model):
    signature = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrprocedureDocumentmetasDocumentmeta, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrprocedure_documentmetas_documentmeta_cryptosigns'

class ContrprocedureExecutions(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contrprocedure, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrprocedure_executions'

class ContrprocedureExecutionsExecution(models.Model):
    execdate = models.TextField(blank=True)
    documentname = models.TextField(blank=True)
    documentnum = models.TextField(blank=True)
    documentdate = models.TextField(blank=True)
    paid = models.TextField(blank=True)
    product = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrprocedureExecutions, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrprocedure_executions_execution'

class ContrprocedureExecutionsStage(models.Model):
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrprocedureExecutions, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrprocedure_executions_stage'

class ContrprocedureTerminations(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contrprocedure, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrprocedure_terminations'

class ContrprocedureTerminationsTermination(models.Model):
    paid = models.TextField(blank=True)
    terminationdate = models.TextField(blank=True)
    reason = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrprocedureTerminations, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrprocedure_terminations_termination'

class Contrsign(models.Model):
    id = models.IntegerField(null=True, blank=True)
    number = models.TextField(blank=True)
    signdate = models.TextField(blank=True)
    protocoldate = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    file = models.ForeignKey('FilesList', null=True, blank=True)
    class Meta:
        db_table = '_contrsign'

class ContrsignCustomer(models.Model):
    regnum = models.BigIntegerField(null=True, blank=True)
    fullname = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contrsign, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrsign_customer'

class ContrsignFoundation(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contrsign, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrsign_foundation'

class ContrsignFoundationOrder(models.Model):
    notificationnumber = models.TextField(blank=True)
    foundationprotocolnumber = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrsignFoundation, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrsign_foundation_order'

class ContrsignSuppliers(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Contrsign, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrsign_suppliers'

class ContrsignSuppliersSupplier(models.Model):
    idnumberextension = models.BigIntegerField(null=True, blank=True)
    participanttype = models.TextField(blank=True)
    inn = models.BigIntegerField(null=True, blank=True)
    kpp = models.IntegerField(null=True, blank=True)
    organizationname = models.TextField(blank=True)
    factualaddress = models.TextField(blank=True)
    postaddress = models.TextField(blank=True)
    contactemail = models.TextField(blank=True)
    contactphone = models.TextField(blank=True)
    contactfax = models.TextField(blank=True)
    additionalinfo = models.TextField(blank=True)
    organizationform = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrsignSuppliers, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrsign_suppliers_supplier'

class ContrsignSuppliersSupplierContactinfo(models.Model):
    lastname = models.TextField(blank=True)
    firstname = models.TextField(blank=True)
    middlename = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrsignSuppliersSupplier, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrsign_suppliers_supplier_contactinfo'

class ContrsignSuppliersSupplierCountry(models.Model):
    countrycode = models.IntegerField(null=True, blank=True)
    countryfullname = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(ContrsignSuppliersSupplier, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_contrsign_suppliers_supplier_country'

class Notf(models.Model):
    id = models.IntegerField(null=True, blank=True)
    notificationnumber = models.TextField(blank=True)
    versionnumber = models.IntegerField(null=True, blank=True)
    createdate = models.TextField(blank=True)
    ordername = models.TextField(blank=True)
    publishdate = models.TextField(blank=True)
    href = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    file = models.ForeignKey('FilesList', null=True, blank=True)
    class Meta:
        db_table = '_notf'

class NotfCompetitivedocumentprovisioning(models.Model):
    www = models.TextField(blank=True)
    deliveryterm = models.TextField(blank=True)
    deliveryterm2 = models.TextField(blank=True)
    deliveryplace = models.TextField(blank=True)
    deliveryprocedure = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notf, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_competitivedocumentprovisioning'

class NotfCompetitivedocumentprovisioningGuarantee(models.Model):
    procedure = models.TextField(blank=True)
    amount = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfCompetitivedocumentprovisioning, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_competitivedocumentprovisioning_guarantee'

class NotfCompetitivedocumentprovisioningGuaranteeCurrency(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfCompetitivedocumentprovisioningGuarantee, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_competitivedocumentprovisioning_guarantee_currency'

class NotfContactinfo(models.Model):
    orgname = models.TextField(blank=True)
    orgfactaddress = models.TextField(blank=True)
    orgpostaddress = models.TextField(blank=True)
    contactemail = models.TextField(blank=True)
    contactphone = models.TextField(blank=True)
    contactfax = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notf, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_contactinfo'

class NotfContactinfoContactperson(models.Model):
    lastname = models.TextField(blank=True)
    firstname = models.TextField(blank=True)
    middlename = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfContactinfo, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_contactinfo_contactperson'

class NotfDocumentmetas(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notf, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_documentmetas'

class NotfDocumentmetasDocumentmeta(models.Model):
    sid = models.TextField(blank=True)
    filename = models.TextField(blank=True)
    docdescription = models.TextField(blank=True)
    url = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfDocumentmetas, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_documentmetas_documentmeta'

class NotfDocumentmetasDocumentmetaCryptosigns(models.Model):
    signature = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfDocumentmetasDocumentmeta, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_documentmetas_documentmeta_cryptosigns'

class NotfEp(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    url = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notf, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_ep'

class NotfLots(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notf, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots'

class NotfLotsLot(models.Model):
    sid = models.TextField(blank=True)
    ordinalnumber = models.TextField(blank=True)
    subject = models.TextField(blank=True)
    infoproduct = models.TextField(blank=True)
    pricenotset = models.TextField(blank=True)
    quantityundefined = models.TextField(blank=True)
    energytype = models.TextField(blank=True)
    energyserviceeconomy = models.TextField(blank=True)
    appform = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLots, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot'

class NotfLotsLotAuctionitems(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLot, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_auctionitems'

class NotfLotsLotAuctionitemsAuctionitem(models.Model):
    sid = models.TextField(blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotAuctionitems, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_auctionitems_auctionitem'

class NotfLotsLotAuctionproducts(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLot, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_auctionproducts'

class NotfLotsLotAuctionproductsAuctionproduct(models.Model):
    sid = models.TextField(blank=True)
    ordinalnumber = models.TextField(blank=True)
    productname = models.TextField(blank=True)
    trademark = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotAuctionproducts, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_auctionproducts_auctionproduct'

class NotfLotsLotAuctionproductsAuctionproductEquivalenceparam(models.Model):
    sid = models.TextField(blank=True)
    ordinalnumber = models.TextField(blank=True)
    name = models.TextField(blank=True)
    paramtype = models.TextField(blank=True)
    paramvalue = models.TextField(blank=True)
    modifiable = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotAuctionproductsAuctionproduct, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_auctionproducts_auctionproduct_equivalenceparam'

class NotfLotsLotAuctionproductsAuctionproductProductreq(models.Model):
    sid = models.TextField(blank=True)
    ordinalnumber = models.TextField(blank=True)
    requirement = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotAuctionproductsAuctionproduct, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_auctionproducts_auctionproduct_productreq'

class NotfLotsLotCurrency(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLot, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_currency'

class NotfLotsLotCustomerreqs(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLot, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_customerreqs'

class NotfLotsLotCustomerreqsCustomerreq(models.Model):
    sid = models.TextField(blank=True)
    quantity = models.TextField(blank=True)
    maxprice = models.TextField(blank=True)
    deliveryplace = models.TextField(blank=True)
    deliveryterm = models.TextField(blank=True)
    financesource = models.TextField(blank=True)
    paymentcondition = models.TextField(blank=True)
    additionalinfo = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotCustomerreqs, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_customerreqs_customerreq'

class NotfLotsLotCustomerreqsCustomerreqCustomer(models.Model):
    regnum = models.BigIntegerField(null=True, blank=True)
    fullname = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotCustomerreqsCustomerreq, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_customerreqs_customerreq_customer'

class NotfLotsLotCustomerreqsCustomerreqGuaranteeapp(models.Model):
    procedure = models.TextField(blank=True)
    settlementaccount = models.TextField(blank=True)
    personalaccount = models.TextField(blank=True)
    bik = models.TextField(blank=True)
    amount = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotCustomerreqsCustomerreq, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_customerreqs_customerreq_guaranteeapp'

class NotfLotsLotCustomerreqsCustomerreqGuaranteecontract(models.Model):
    procedure = models.TextField(blank=True)
    isbail = models.TextField(blank=True)
    amount = models.TextField(blank=True)
    settlementaccount = models.TextField(blank=True)
    personalaccount = models.TextField(blank=True)
    bik = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotCustomerreqsCustomerreq, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_customerreqs_customerreq_guaranteecontract'

class NotfLotsLotCustomerreqsCustomerreqKbk(models.Model):
    kbk1 = models.TextField(blank=True)
    kbk2 = models.TextField(blank=True)
    kbk3 = models.TextField(blank=True)
    kbk4 = models.TextField(blank=True)
    kbk5 = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotCustomerreqsCustomerreq, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_customerreqs_customerreq_kbk'

class NotfLotsLotDocumentreqs(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLot, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_documentreqs'

class NotfLotsLotDocumentreqsDocumentreq(models.Model):
    sid = models.TextField(blank=True)
    ordinalnumber = models.TextField(blank=True)
    reqvalue = models.TextField(blank=True)
    docname = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotDocumentreqs, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_documentreqs_documentreq'

class NotfLotsLotLotdocreqs(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLot, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_lotdocreqs'

class NotfLotsLotNotiffeats(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLot, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_notiffeats'

class NotfLotsLotNotiffeatsNotiffeat(models.Model):
    prefvalue = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotNotiffeats, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_notiffeats_notiffeat'

class NotfLotsLotNotiffeatsNotiffeatPlacementfeat(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotNotiffeatsNotiffeat, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_notiffeats_notiffeat_placementfeat'

class NotfLotsLotProducts(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLot, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_products'

class NotfLotsLotProductsProduct(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfLotsLotProducts, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_lots_lot_products_product'

class NotfModification(models.Model):
    initiativetype = models.TextField(blank=True)
    modificationdate = models.TextField(blank=True)
    info = models.TextField(blank=True)
    authoritytype = models.TextField(blank=True)
    authorityname = models.TextField(blank=True)
    desnumber = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notf, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_modification'

class NotfNotifcom(models.Model):
    p1date = models.TextField(blank=True)
    p2date = models.TextField(blank=True)
    p3date = models.TextField(blank=True)
    p1place = models.TextField(blank=True)
    p2place = models.TextField(blank=True)
    signterm = models.TextField(blank=True)
    p3place = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notf, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_notifcom'

class NotfNotifplacement(models.Model):
    deliveryterm = models.TextField(blank=True)
    deliveryplace = models.TextField(blank=True)
    additionalinfo = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notf, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_notifplacement'

class NotfNotifplacementGuaranteeapp(models.Model):
    procedure = models.TextField(blank=True)
    settlementaccount = models.TextField(blank=True)
    personalaccount = models.TextField(blank=True)
    bik = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfNotifplacement, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_notifplacement_guaranteeapp'

class NotfNotifplacementGuaranteecontract(models.Model):
    procedure = models.TextField(blank=True)
    isbail = models.TextField(blank=True)
    settlementaccount = models.TextField(blank=True)
    personalaccount = models.TextField(blank=True)
    bik = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfNotifplacement, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_notifplacement_guaranteecontract'

class NotfNotifplacementNotiffeats(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfNotifplacement, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_notifplacement_notiffeats'

class NotfNotifplacementNotiffeatsNotiffeat(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfNotifplacementNotiffeats, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_notifplacement_notiffeats_notiffeat'

class NotfNotifplacementNotiffeatsNotiffeatPlacementfeat(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfNotifplacementNotiffeatsNotiffeat, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_notifplacement_notiffeats_notiffeat_placementfeat'

class NotfOrder(models.Model):
    placerorgtype = models.TextField(blank=True)
    initiatororgrole = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notf, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_order'

class NotfOrderInitiator(models.Model):
    regnum = models.BigIntegerField(null=True, blank=True)
    fullname = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfOrder, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_order_initiator'

class NotfOrderPlacer(models.Model):
    regnum = models.BigIntegerField(null=True, blank=True)
    fullname = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfOrder, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_order_placer'

class NotfPlacingway(models.Model):
    code = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notf, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_placingway'

class NotfPrintform(models.Model):
    filename = models.TextField(blank=True)
    url = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notf, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_printform'

class NotfPrintformCryptosigns(models.Model):
    signature = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotfPrintform, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notf_printform_cryptosigns'

class Notifcancel(models.Model):
    id = models.IntegerField(null=True, blank=True)
    notificationnumber = models.TextField(blank=True)
    versionnumber = models.IntegerField(null=True, blank=True)
    uid = models.IntegerField(primary_key=True)
    file = models.ForeignKey('FilesList', null=True, blank=True)
    class Meta:
        db_table = '_notifcancel'

class NotifcancelDocumentmetas(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notifcancel, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notifcancel_documentmetas'

class NotifcancelDocumentmetasDocumentmeta(models.Model):
    sid = models.TextField(blank=True)
    filename = models.TextField(blank=True)
    docdescription = models.TextField(blank=True)
    url = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotifcancelDocumentmetas, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notifcancel_documentmetas_documentmeta'

class NotifcancelDocumentmetasDocumentmetaCryptosigns(models.Model):
    signature = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotifcancelDocumentmetasDocumentmeta, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notifcancel_documentmetas_documentmeta_cryptosigns'

class NotifcancelLots(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notifcancel, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notifcancel_lots'

class NotifcancelLotsLot(models.Model):
    ordinalnumber = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotifcancelLots, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notifcancel_lots_lot'

class NotifcancelModification(models.Model):
    initiativetype = models.TextField(blank=True)
    modificationdate = models.TextField(blank=True)
    info = models.TextField(blank=True)
    authoritytype = models.TextField(blank=True)
    authorityname = models.TextField(blank=True)
    desnumber = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notifcancel, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notifcancel_modification'

class NotifcancelPrintform(models.Model):
    filename = models.TextField(blank=True)
    url = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Notifcancel, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notifcancel_printform'

class NotifcancelPrintformCryptosigns(models.Model):
    signature = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(NotifcancelPrintform, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_notifcancel_printform_cryptosigns'

class Prtk(models.Model):
    notificationnumber = models.TextField(blank=True)
    protocolnumber = models.TextField(blank=True)
    versionnumber = models.IntegerField(null=True, blank=True)
    place = models.TextField(blank=True)
    protocoldate = models.TextField(blank=True)
    signdate = models.TextField(blank=True)
    publishdate = models.TextField(blank=True)
    href = models.TextField(blank=True)
    foundationprotocolnumber = models.TextField(blank=True)
    parentprotocolnumber = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    file = models.ForeignKey('FilesList', null=True, blank=True)
    class Meta:
        db_table = '_prtk'

class PrtkCommission(models.Model):
    regnumber = models.TextField(blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Prtk, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_commission'

class PrtkCommissionProtcommems(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkCommission, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_commission_protcommems'

class PrtkCommissionProtcommemsProtcommem(models.Model):
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(blank=True)
    present = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkCommissionProtcommems, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_commission_protcommems_protcommem'

class PrtkCommissionProtcommemsProtcommemRole(models.Model):
    roleid = models.IntegerField(null=True, blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkCommissionProtcommemsProtcommem, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_commission_protcommems_protcommem_role'

class PrtkDocumentmetas(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Prtk, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_documentmetas'

class PrtkDocumentmetasDocumentmeta(models.Model):
    sid = models.TextField(blank=True)
    filename = models.TextField(blank=True)
    docdescription = models.TextField(blank=True)
    url = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkDocumentmetas, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_documentmetas_documentmeta'

class PrtkDocumentmetasDocumentmetaCryptosigns(models.Model):
    signature = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkDocumentmetasDocumentmeta, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_documentmetas_documentmeta_cryptosigns'

class PrtkModification(models.Model):
    initiativetype = models.TextField(blank=True)
    modificationdate = models.TextField(blank=True)
    info = models.TextField(blank=True)
    authorityname = models.TextField(blank=True)
    desnumber = models.TextField(blank=True)
    authoritytype = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Prtk, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_modification'

class PrtkPrintform(models.Model):
    filename = models.TextField(blank=True)
    url = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Prtk, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_printform'

class PrtkPrintformCryptosigns(models.Model):
    signature = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkPrintform, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_printform_cryptosigns'

class PrtkProtlots(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(Prtk, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots'

class PrtkProtlotsProtlot(models.Model):
    lotnumber = models.TextField(blank=True)
    allabsent = models.TextField(blank=True)
    contractmulti = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlots, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot'

class PrtkProtlotsProtlotApps(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlot, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps'

class PrtkProtlotsProtlotAppsApp(models.Model):
    journalnumber = models.TextField(blank=True)
    appdate = models.TextField(blank=True)
    admitted = models.TextField(blank=True)
    commoninfo = models.TextField(blank=True)
    participantpresent = models.TextField(blank=True)
    apprating = models.TextField(blank=True)
    appformat = models.TextField(blank=True)
    price = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    goodsdelivered = models.TextField(blank=True)
    expensesinfo = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotApps, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app'

class PrtkProtlotsProtlotAppsAppAdmress(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsApp, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_admress'

class PrtkProtlotsProtlotAppsAppAdmressAdmres(models.Model):
    admitted = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppAdmress, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_admress_admres'

class PrtkProtlotsProtlotAppsAppAdmressAdmresApprejreas(models.Model):
    explanation = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppAdmressAdmres, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_admress_admres_apprejreas'

class PrtkProtlotsProtlotAppsAppAdmressAdmresApprejreasNsire(models.Model):
    id = models.IntegerField(null=True, blank=True)
    reason = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppAdmressAdmresApprejreas, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_admress_admres_apprejreas_nsire'

class PrtkProtlotsProtlotAppsAppAdmressAdmresProtcommem(models.Model):
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppAdmressAdmres, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_admress_admres_protcommem'

class PrtkProtlotsProtlotAppsAppAdmressAdmresProtcommemRole(models.Model):
    roleid = models.BigIntegerField(null=True, blank=True)
    name = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppAdmressAdmresProtcommem, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_admress_admres_protcommem_role'

class PrtkProtlotsProtlotAppsAppAdmressApprejreas(models.Model):
    explanation = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppAdmress, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_admress_apprejreas'

class PrtkProtlotsProtlotAppsAppAdmressApprejreasNsirejectrea(models.Model):
    id = models.IntegerField(null=True, blank=True)
    reason = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppAdmressApprejreas, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_admress_apprejreas_nsirejectrea'

class PrtkProtlotsProtlotAppsAppAppparts(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsApp, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_appparts'

class PrtkProtlotsProtlotAppsAppApppartsApppart(models.Model):
    participanttype = models.TextField(blank=True)
    inn = models.BigIntegerField(null=True, blank=True)
    kpp = models.IntegerField(null=True, blank=True)
    idnumber = models.TextField(blank=True)
    idnumberextension = models.TextField(blank=True)
    organizationname = models.TextField(blank=True)
    factualaddress = models.TextField(blank=True)
    postaddress = models.TextField(blank=True)
    additionalinfo = models.TextField(blank=True)
    organizationform = models.TextField(blank=True)
    contactemail = models.TextField(blank=True)
    contactphone = models.TextField(blank=True)
    contactfax = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppAppparts, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_appparts_apppart'

class PrtkProtlotsProtlotAppsAppApppartsApppartContactinfo(models.Model):
    lastname = models.TextField(blank=True)
    firstname = models.TextField(blank=True)
    middlename = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppApppartsApppart, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_appparts_apppart_contactinfo'

class PrtkProtlotsProtlotAppsAppApppartsApppartCountry(models.Model):
    countrycode = models.IntegerField(null=True, blank=True)
    countryfullname = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppApppartsApppart, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_appparts_apppart_country'

class PrtkProtlotsProtlotAppsAppContrconds(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsApp, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_contrconds'

class PrtkProtlotsProtlotAppsAppContrcondsContrcond(models.Model):
    condvalue = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppContrconds, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_contrconds_contrcond'

class PrtkProtlotsProtlotAppsAppContrcondsContrcondCrit(models.Model):
    id = models.IntegerField(null=True, blank=True)
    criteriontype = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppContrcondsContrcond, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_contrconds_contrcond_crit'

class PrtkProtlotsProtlotAppsAppLastprice(models.Model):
    price = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    date = models.TextField(blank=True)
    increaseinitialprice = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsApp, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_lastprice'

class PrtkProtlotsProtlotAppsAppReqcomps(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsApp, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_reqcomps'

class PrtkProtlotsProtlotAppsAppReqcompsReqcomp(models.Model):
    ordinalnumber = models.TextField(blank=True)
    availabilitytype = models.TextField(blank=True)
    reason = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotAppsAppReqcomps, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_apps_app_reqcomps_reqcomp'

class PrtkProtlotsProtlotCriterias(models.Model):
    nir = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlot, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_criterias'

class PrtkProtlotsProtlotCriteriasManual(models.Model):
    criterionvalue = models.TextField(blank=True)
    evalvalue = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotCriterias, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_criterias_manual'

class PrtkProtlotsProtlotCriteriasManualChildrencriteria(models.Model):
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(blank=True)
    criterionvalue = models.TextField(blank=True)
    evalvalue = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotCriteriasManual, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_criterias_manual_childrencriteria'

class PrtkProtlotsProtlotCriteriasManualNsievalcriterion(models.Model):
    id = models.IntegerField(null=True, blank=True)
    name = models.TextField(blank=True)
    order = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotCriteriasManual, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_criterias_manual_nsievalcriterion'

class PrtkProtlotsProtlotDocumentreqs(models.Model):
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlot, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_documentreqs'

class PrtkProtlotsProtlotDocumentreqsDocumentreq(models.Model):
    sid = models.TextField(blank=True)
    ordinalnumber = models.TextField(blank=True)
    reqvalue = models.TextField(blank=True)
    uid = models.IntegerField(primary_key=True)
    parent_uid = models.ForeignKey(PrtkProtlotsProtlotDocumentreqs, null=True, db_column='parent_uid', blank=True)
    class Meta:
        db_table = '_prtk_protlots_protlot_documentreqs_documentreq'

class AdygeyaRespContr(models.Model):
    regnum = models.BigIntegerField(null=True, blank=True)
    publishdate = models.TextField(blank=True)
    signdate = models.TextField(blank=True)
    price = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    fullname = models.TextField(blank=True)
    organizationform = models.TextField(blank=True)
    organizationname = models.TextField(blank=True)
    factualaddress = models.TextField(blank=True)
    postaddress = models.TextField(blank=True)
    lat = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    lng = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    class Meta:
        db_table = 'adygeya_resp_contr'

class CustomersOrgs(models.Model):
    url = models.TextField(blank=True)
    own_spz = models.BigIntegerField(null=True, blank=True)
    polnomochie_org = models.TextField(blank=True)
    full_name = models.TextField(blank=True)
    short_name = models.TextField(blank=True)
    inn = models.BigIntegerField(null=True, blank=True)
    kpp = models.TextField(blank=True)
    org_type = models.TextField(blank=True)
    org_level = models.TextField(blank=True)
    buget_code = models.BigIntegerField(null=True, blank=True)
    buget_name = models.TextField(blank=True)
    admin_prin_spz = models.BigIntegerField(null=True, blank=True)
    admin_prin_name = models.TextField(blank=True)
    upper_org_spz = models.BigIntegerField(null=True, blank=True)
    okopf = models.BigIntegerField(null=True, blank=True)
    okogu = models.BigIntegerField(null=True, blank=True)
    okpo = models.BigIntegerField(null=True, blank=True)
    okved = models.TextField(blank=True)
    ogrn = models.BigIntegerField(null=True, blank=True)
    place = models.TextField(blank=True)
    okato = models.BigIntegerField(null=True, blank=True)
    upoln_organ = models.TextField(blank=True)
    telefon = models.TextField(blank=True)
    fax = models.TextField(blank=True)
    post_adress = models.TextField(blank=True)
    email = models.TextField(blank=True)
    contact_person = models.TextField(blank=True)
    timezone = models.TextField(blank=True)
    innetaddress = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)
    upper_org_name = models.TextField(blank=True)
    id = models.BigIntegerField(primary_key=True)
    class Meta:
        db_table = 'customers_orgs'


class FilesList(models.Model):
    uid = models.IntegerField()
    path = models.CharField(max_length=4000, unique=True, blank=True)
    insert_time = models.DateTimeField(null=True, blank=True)
    inserted = models.NullBooleanField()
    lock_time = models.DateTimeField(null=True, blank=True)
    locked = models.NullBooleanField()
    class Meta:
        db_table = 'files_list'
