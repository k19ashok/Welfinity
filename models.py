# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    id = models.IntegerField(primary_key=True)
    line1 = models.CharField(max_length=255, blank=True, null=True)
    line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=35, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    plus_four = models.CharField(max_length=4, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    foreign_id = models.IntegerField(blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class AmcMiscData(models.Model):
    amc_id = models.CharField(max_length=31)
    pid = models.BigIntegerField(blank=True, null=True)
    map_category = models.CharField(max_length=255)
    map_id = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    soc_provided = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amc_misc_data'


class Amendments(models.Model):
    amendment_id = models.AutoField(primary_key=True)
    amendment_date = models.DateField()
    amendment_by = models.CharField(max_length=50)
    amendment_status = models.CharField(max_length=50, blank=True, null=True)
    pid = models.BigIntegerField()
    amendment_desc = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    modified_by = models.IntegerField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    modified_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amendments'


class AmendmentsHistory(models.Model):
    amendment_id = models.AutoField()
    amendment_note = models.TextField(blank=True, null=True)
    amendment_status = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField()
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amendments_history'


class ApiLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    log_id = models.IntegerField()
    user_id = models.BigIntegerField()
    patient_id = models.BigIntegerField()
    ip_address = models.CharField(max_length=255)
    method = models.CharField(max_length=20)
    request = models.CharField(max_length=255)
    request_url = models.TextField(blank=True, null=True)
    request_body = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_log'


class ApiRefreshToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=40, blank=True, null=True)
    client_id = models.CharField(max_length=80, blank=True, null=True)
    token = models.CharField(unique=True, max_length=128)
    expiry = models.DateTimeField(blank=True, null=True)
    revoked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'api_refresh_token'


class ApiToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=40, blank=True, null=True)
    token = models.CharField(unique=True, max_length=128, blank=True, null=True)
    expiry = models.DateTimeField(blank=True, null=True)
    client_id = models.CharField(max_length=80, blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    context = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_token'


class ArActivity(models.Model):
    pid = models.IntegerField(primary_key=True)
    encounter = models.IntegerField()
    sequence_no = models.PositiveIntegerField()
    code_type = models.CharField(max_length=12)
    code = models.CharField(max_length=20)
    modifier = models.CharField(max_length=12)
    payer_type = models.IntegerField()
    post_time = models.DateTimeField()
    post_user = models.IntegerField()
    session_id = models.PositiveIntegerField()
    memo = models.CharField(max_length=255)
    pay_amount = models.DecimalField(max_digits=12, decimal_places=2)
    adj_amount = models.DecimalField(max_digits=12, decimal_places=2)
    modified_time = models.DateTimeField()
    follow_up = models.CharField(max_length=1)
    follow_up_note = models.TextField(blank=True, null=True)
    account_code = models.CharField(max_length=15)
    reason_code = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.DateTimeField(blank=True, null=True)
    post_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ar_activity'
        unique_together = (('pid', 'encounter', 'sequence_no'),)


class ArSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    payer_id = models.IntegerField()
    user_id = models.IntegerField()
    closed = models.IntegerField()
    reference = models.CharField(max_length=255)
    check_date = models.DateField(blank=True, null=True)
    deposit_date = models.DateField(blank=True, null=True)
    pay_total = models.DecimalField(max_digits=12, decimal_places=2)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    global_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    adjustment_code = models.CharField(max_length=50)
    post_to_date = models.DateField()
    patient_id = models.BigIntegerField()
    payment_method = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'ar_session'


class AuditDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_name = models.CharField(max_length=100)
    field_name = models.CharField(max_length=100)
    field_value = models.TextField(blank=True, null=True)
    audit_master_id = models.BigIntegerField()
    entry_identification = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'audit_details'


class AuditMaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    user_id = models.BigIntegerField()
    approval_status = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    ip_address = models.CharField(max_length=100)
    type = models.IntegerField()
    is_qrda_document = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_master'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AutomaticNotification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    sms_gateway_type = models.CharField(max_length=255)
    provider_name = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    email_sender = models.CharField(max_length=100)
    email_subject = models.CharField(max_length=100)
    type = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'automatic_notification'


class BackgroundServices(models.Model):
    name = models.CharField(primary_key=True, max_length=31)
    title = models.CharField(max_length=127)
    active = models.IntegerField()
    running = models.IntegerField()
    next_run = models.DateTimeField()
    execute_interval = models.IntegerField()
    function = models.CharField(max_length=127)
    require_once = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'background_services'


class Batchcom(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient_id = models.BigIntegerField()
    sent_by = models.BigIntegerField()
    msg_type = models.CharField(max_length=60, blank=True, null=True)
    msg_subject = models.CharField(max_length=255, blank=True, null=True)
    msg_text = models.TextField(blank=True, null=True)
    msg_date_sent = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batchcom'


class BenefitEligibility(models.Model):
    response_id = models.BigIntegerField()
    verification_id = models.BigIntegerField()
    type = models.CharField(max_length=4, blank=True, null=True)
    benefit_type = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    coverage_level = models.CharField(max_length=255, blank=True, null=True)
    coverage_type = models.CharField(max_length=512, blank=True, null=True)
    plan_type = models.CharField(max_length=255, blank=True, null=True)
    plan_description = models.CharField(max_length=255, blank=True, null=True)
    coverage_period = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    percent = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    network_ind = models.CharField(max_length=2, blank=True, null=True)
    message = models.CharField(max_length=512, blank=True, null=True)
    response_status = models.CharField(max_length=1, blank=True, null=True)
    response_create_date = models.DateField(blank=True, null=True)
    response_modify_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'benefit_eligibility'


class Billing(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    code_type = models.CharField(max_length=15, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    encounter = models.IntegerField(blank=True, null=True)
    code_text = models.TextField(blank=True, null=True)
    billed = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    payer_id = models.IntegerField(blank=True, null=True)
    bill_process = models.IntegerField()
    bill_date = models.DateTimeField(blank=True, null=True)
    process_date = models.DateTimeField(blank=True, null=True)
    process_file = models.CharField(max_length=255, blank=True, null=True)
    modifier = models.CharField(max_length=12, blank=True, null=True)
    units = models.IntegerField(blank=True, null=True)
    fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    justify = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=30, blank=True, null=True)
    x12_partner_id = models.IntegerField(blank=True, null=True)
    ndc_info = models.CharField(max_length=255, blank=True, null=True)
    notecodes = models.CharField(max_length=25)
    external_id = models.CharField(max_length=20, blank=True, null=True)
    pricelevel = models.CharField(max_length=31, blank=True, null=True)
    revenue_code = models.CharField(max_length=6)
    chargecat = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing'


class CalendarExternal(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=45)
    source = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_external'


class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    parent = models.IntegerField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    aco_spec = models.CharField(max_length=63)
    codes = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'categories'


class CategoriesSeq(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'categories_seq'


class CategoriesToDocuments(models.Model):
    category_id = models.IntegerField(primary_key=True)
    document_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categories_to_documents'
        unique_together = (('category_id', 'document_id'),)


class Ccda(models.Model):
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    encounter = models.BigIntegerField(blank=True, null=True)
    ccda_data = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    updated_date = models.DateTimeField()
    user_id = models.CharField(max_length=50, blank=True, null=True)
    couch_docid = models.CharField(max_length=100, blank=True, null=True)
    couch_revid = models.CharField(max_length=100, blank=True, null=True)
    hash = models.CharField(max_length=255, blank=True, null=True)
    view = models.IntegerField()
    transfer = models.IntegerField()
    emr_transfer = models.IntegerField()
    encrypted = models.IntegerField()
    transaction_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ccda'
        unique_together = (('pid', 'encounter', 'time'),)


class CcdaComponents(models.Model):
    ccda_components_id = models.AutoField(primary_key=True)
    ccda_components_field = models.CharField(max_length=100, blank=True, null=True)
    ccda_components_name = models.CharField(max_length=100, blank=True, null=True)
    ccda_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ccda_components'


class CcdaFieldMapping(models.Model):
    table_id = models.IntegerField(blank=True, null=True)
    ccda_field = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ccda_field_mapping'


class CcdaSections(models.Model):
    ccda_sections_id = models.AutoField(primary_key=True)
    ccda_components_id = models.IntegerField(blank=True, null=True)
    ccda_sections_field = models.CharField(max_length=100, blank=True, null=True)
    ccda_sections_name = models.CharField(max_length=100, blank=True, null=True)
    ccda_sections_req_mapping = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ccda_sections'


class CcdaTableMapping(models.Model):
    ccda_component = models.CharField(max_length=100, blank=True, null=True)
    ccda_component_section = models.CharField(max_length=100, blank=True, null=True)
    form_dir = models.CharField(max_length=100, blank=True, null=True)
    form_type = models.SmallIntegerField(blank=True, null=True)
    form_table = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ccda_table_mapping'


class ChartTracker(models.Model):
    ct_pid = models.IntegerField(primary_key=True)
    ct_when = models.DateTimeField()
    ct_userid = models.BigIntegerField()
    ct_location = models.CharField(max_length=31)

    class Meta:
        managed = False
        db_table = 'chart_tracker'
        unique_together = (('ct_pid', 'ct_when'),)


class Claims(models.Model):
    patient_id = models.BigIntegerField(primary_key=True)
    encounter_id = models.IntegerField()
    version = models.PositiveIntegerField()
    payer_id = models.IntegerField()
    status = models.IntegerField()
    payer_type = models.IntegerField()
    bill_process = models.IntegerField()
    bill_time = models.DateTimeField(blank=True, null=True)
    process_time = models.DateTimeField(blank=True, null=True)
    process_file = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=30, blank=True, null=True)
    x12_partner_id = models.IntegerField()
    submitted_claim = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'claims'
        unique_together = (('patient_id', 'encounter_id', 'version'),)


class ClinicalPlans(models.Model):
    id = models.CharField(primary_key=True, max_length=31)
    pid = models.BigIntegerField()
    normal_flag = models.IntegerField(blank=True, null=True)
    cqm_flag = models.IntegerField(blank=True, null=True)
    cqm_2011_flag = models.IntegerField(blank=True, null=True)
    cqm_2014_flag = models.IntegerField(blank=True, null=True)
    cqm_measure_group = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'clinical_plans'
        unique_together = (('id', 'pid'),)


class ClinicalPlansRules(models.Model):
    plan_id = models.CharField(primary_key=True, max_length=31)
    rule_id = models.CharField(max_length=31)

    class Meta:
        managed = False
        db_table = 'clinical_plans_rules'
        unique_together = (('plan_id', 'rule_id'),)


class ClinicalRules(models.Model):
    id = models.CharField(primary_key=True, max_length=31)
    pid = models.BigIntegerField()
    active_alert_flag = models.IntegerField(blank=True, null=True)
    passive_alert_flag = models.IntegerField(blank=True, null=True)
    cqm_flag = models.IntegerField(blank=True, null=True)
    cqm_2011_flag = models.IntegerField(blank=True, null=True)
    cqm_2014_flag = models.IntegerField(blank=True, null=True)
    cqm_nqf_code = models.CharField(max_length=10)
    cqm_pqri_code = models.CharField(max_length=10)
    amc_flag = models.IntegerField(blank=True, null=True)
    amc_2011_flag = models.IntegerField(blank=True, null=True)
    amc_2014_flag = models.IntegerField(blank=True, null=True)
    amc_2015_flag = models.IntegerField(blank=True, null=True)
    amc_code = models.CharField(max_length=10)
    amc_code_2014 = models.CharField(max_length=30)
    amc_code_2015 = models.CharField(max_length=30)
    amc_2014_stage1_flag = models.IntegerField(blank=True, null=True)
    amc_2014_stage2_flag = models.IntegerField(blank=True, null=True)
    patient_reminder_flag = models.IntegerField(blank=True, null=True)
    bibliographic_citation = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    funding_source = models.CharField(max_length=255)
    release_version = models.CharField(max_length=255)
    web_reference = models.CharField(max_length=255)
    linked_referential_cds = models.CharField(max_length=50)
    access_control = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'clinical_rules'
        unique_together = (('id', 'pid'),)


class ClinicalRulesLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField()
    uid = models.BigIntegerField()
    category = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinical_rules_log'


class CodeTypes(models.Model):
    ct_key = models.CharField(primary_key=True, max_length=15)
    ct_id = models.IntegerField(unique=True)
    ct_seq = models.IntegerField()
    ct_mod = models.IntegerField()
    ct_just = models.CharField(max_length=15)
    ct_mask = models.CharField(max_length=9)
    ct_fee = models.IntegerField()
    ct_rel = models.IntegerField()
    ct_nofs = models.IntegerField()
    ct_diag = models.IntegerField()
    ct_active = models.IntegerField()
    ct_label = models.CharField(max_length=31)
    ct_external = models.IntegerField()
    ct_claim = models.IntegerField()
    ct_proc = models.IntegerField()
    ct_term = models.IntegerField()
    ct_problem = models.IntegerField()
    ct_drug = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'code_types'


class Codes(models.Model):
    code_text = models.TextField(blank=True, null=True)
    code_text_short = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=25)
    code_type = models.SmallIntegerField(blank=True, null=True)
    modifier = models.CharField(max_length=12)
    units = models.IntegerField(blank=True, null=True)
    fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    superbill = models.CharField(max_length=31)
    related_code = models.CharField(max_length=255)
    taxrates = models.CharField(max_length=255)
    cyp_factor = models.FloatField()
    active = models.IntegerField(blank=True, null=True)
    reportable = models.IntegerField(blank=True, null=True)
    financial_reporting = models.IntegerField(blank=True, null=True)
    revenue_code = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'codes'


class CodesHistory(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=25, blank=True, null=True)
    modifier = models.CharField(max_length=12, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    diagnosis_reporting = models.IntegerField(blank=True, null=True)
    financial_reporting = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    code_type_name = models.CharField(max_length=255, blank=True, null=True)
    code_text = models.TextField(blank=True, null=True)
    code_text_short = models.TextField(blank=True, null=True)
    prices = models.TextField(blank=True, null=True)
    action_type = models.CharField(max_length=25, blank=True, null=True)
    update_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codes_history'


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    foreign_table_name = models.CharField(max_length=255)
    foreign_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'contact'


class ContactAddress(models.Model):
    id = models.BigAutoField(primary_key=True)
    contact_id = models.BigIntegerField()
    address_id = models.BigIntegerField()
    priority = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    use = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    is_primary = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField()
    period_start = models.DateTimeField(blank=True, null=True)
    period_end = models.DateTimeField(blank=True, null=True)
    inactivated_reason = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_address'


class Customlists(models.Model):
    cl_list_slno = models.AutoField(primary_key=True)
    cl_list_id = models.PositiveIntegerField()
    cl_list_item_id = models.PositiveIntegerField(blank=True, null=True)
    cl_list_type = models.PositiveIntegerField()
    cl_list_item_short = models.CharField(max_length=10, blank=True, null=True)
    cl_list_item_long = models.TextField(blank=True, null=True)
    cl_list_item_level = models.IntegerField(blank=True, null=True)
    cl_order = models.IntegerField(blank=True, null=True)
    cl_deleted = models.IntegerField(blank=True, null=True)
    cl_creator = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customlists'


class DatedReminders(models.Model):
    dr_id = models.AutoField(primary_key=True)
    dr_from_id = models.IntegerField(db_column='dr_from_ID')  # Field name made lowercase.
    dr_message_text = models.CharField(max_length=160)
    dr_message_sent_date = models.DateTimeField()
    dr_message_due_date = models.DateField()
    pid = models.BigIntegerField()
    message_priority = models.IntegerField()
    message_processed = models.IntegerField()
    processed_date = models.DateTimeField(blank=True, null=True)
    dr_processed_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dated_reminders'


class DatedRemindersLink(models.Model):
    dr_link_id = models.AutoField(primary_key=True)
    dr_id = models.IntegerField()
    to_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dated_reminders_link'


class DirectMessageLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    msg_type = models.CharField(max_length=1)
    msg_id = models.CharField(max_length=127)
    sender = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    create_ts = models.DateTimeField()
    status = models.CharField(max_length=1)
    status_info = models.CharField(max_length=511, blank=True, null=True)
    status_ts = models.DateTimeField(blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direct_message_log'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocumentTemplateProfiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    template_id = models.PositiveBigIntegerField()
    profile = models.CharField(max_length=64)
    template_name = models.CharField(max_length=255)
    category = models.CharField(max_length=64)
    provider = models.PositiveIntegerField(blank=True, null=True)
    modified_date = models.DateTimeField()
    member_of = models.CharField(max_length=64)
    active = models.IntegerField()
    recurring = models.IntegerField()
    event_trigger = models.CharField(max_length=31)
    period = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'document_template_profiles'
        unique_together = (('profile', 'template_id', 'member_of'),)


class DocumentTemplates(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    provider = models.PositiveIntegerField(blank=True, null=True)
    encounter = models.PositiveIntegerField(blank=True, null=True)
    modified_date = models.DateTimeField()
    profile = models.CharField(max_length=63)
    category = models.CharField(max_length=63)
    location = models.CharField(max_length=255, blank=True, null=True)
    template_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=31, blank=True, null=True)
    send_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    size = models.IntegerField()
    template_content = models.TextField(blank=True, null=True)
    mime = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_templates'
        unique_together = (('pid', 'profile', 'category', 'template_name'),)


class Documents(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    type = models.CharField(max_length=8, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    date_expires = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    thumb_url = models.CharField(max_length=255, blank=True, null=True)
    mimetype = models.CharField(max_length=255, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)
    revision = models.DateTimeField()
    foreign_id = models.BigIntegerField(blank=True, null=True)
    docdate = models.DateField(blank=True, null=True)
    hash = models.CharField(max_length=255, blank=True, null=True)
    list_id = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    drive_uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    couch_docid = models.CharField(max_length=100, blank=True, null=True)
    couch_revid = models.CharField(max_length=100, blank=True, null=True)
    storagemethod = models.IntegerField()
    path_depth = models.IntegerField(blank=True, null=True)
    imported = models.IntegerField(blank=True, null=True)
    encounter_id = models.BigIntegerField()
    encounter_check = models.IntegerField()
    audit_master_approval_status = models.IntegerField()
    audit_master_id = models.IntegerField(blank=True, null=True)
    documentationof = models.CharField(db_column='documentationOf', max_length=255, blank=True, null=True)  # Field name made lowercase.
    encrypted = models.IntegerField()
    document_data = models.TextField(blank=True, null=True)
    deleted = models.IntegerField()
    foreign_reference_id = models.BigIntegerField(blank=True, null=True)
    foreign_reference_table = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'


class DocumentsLegalCategories(models.Model):
    dlc_id = models.AutoField(primary_key=True)
    dlc_category_type = models.PositiveIntegerField()
    dlc_category_name = models.CharField(max_length=45)
    dlc_category_parent = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_legal_categories'


class DocumentsLegalDetail(models.Model):
    dld_id = models.AutoField(primary_key=True)
    dld_pid = models.PositiveIntegerField(blank=True, null=True)
    dld_facility = models.PositiveIntegerField(blank=True, null=True)
    dld_provider = models.PositiveIntegerField(blank=True, null=True)
    dld_encounter = models.PositiveIntegerField(blank=True, null=True)
    dld_master_docid = models.PositiveIntegerField()
    dld_signed = models.PositiveSmallIntegerField()
    dld_signed_time = models.DateTimeField()
    dld_filepath = models.CharField(max_length=75, blank=True, null=True)
    dld_filename = models.CharField(max_length=45)
    dld_signing_person = models.CharField(max_length=50)
    dld_sign_level = models.IntegerField()
    dld_content = models.CharField(max_length=50)
    dld_file_for_pdf_generation = models.TextField()
    dld_denial_reason = models.TextField(blank=True, null=True)
    dld_moved = models.IntegerField()
    dld_patient_comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_legal_detail'


class DocumentsLegalMaster(models.Model):
    dlm_category = models.PositiveIntegerField(blank=True, null=True)
    dlm_subcategory = models.PositiveIntegerField(blank=True, null=True)
    dlm_document_id = models.AutoField(primary_key=True)
    dlm_document_name = models.CharField(max_length=75)
    dlm_filepath = models.CharField(max_length=75)
    dlm_facility = models.PositiveIntegerField(blank=True, null=True)
    dlm_provider = models.PositiveIntegerField(blank=True, null=True)
    dlm_sign_height = models.FloatField()
    dlm_sign_width = models.FloatField()
    dlm_filename = models.CharField(max_length=45)
    dlm_effective_date = models.DateTimeField()
    dlm_version = models.PositiveIntegerField()
    content = models.CharField(max_length=255)
    dlm_savedsign = models.CharField(max_length=255, blank=True, null=True)
    dlm_review = models.CharField(max_length=255, blank=True, null=True)
    dlm_upload_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents_legal_master'


class DrugInventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    drug_id = models.IntegerField()
    lot_number = models.CharField(max_length=20, blank=True, null=True)
    expiration = models.DateField(blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    on_hand = models.IntegerField()
    warehouse_id = models.CharField(max_length=31)
    vendor_id = models.BigIntegerField()
    last_notify = models.DateField(blank=True, null=True)
    destroy_date = models.DateField(blank=True, null=True)
    destroy_method = models.CharField(max_length=255, blank=True, null=True)
    destroy_witness = models.CharField(max_length=255, blank=True, null=True)
    destroy_notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_inventory'


class DrugSales(models.Model):
    sale_id = models.AutoField(primary_key=True)
    drug_id = models.IntegerField()
    inventory_id = models.IntegerField()
    prescription_id = models.IntegerField()
    pid = models.BigIntegerField()
    encounter = models.IntegerField()
    user = models.CharField(max_length=255, blank=True, null=True)
    sale_date = models.DateField()
    quantity = models.IntegerField()
    fee = models.DecimalField(max_digits=12, decimal_places=2)
    billed = models.IntegerField()
    xfer_inventory_id = models.IntegerField()
    distributor_id = models.BigIntegerField()
    notes = models.CharField(max_length=255)
    bill_date = models.DateTimeField(blank=True, null=True)
    pricelevel = models.CharField(max_length=31, blank=True, null=True)
    selector = models.CharField(max_length=255, blank=True, null=True)
    trans_type = models.IntegerField()
    chargecat = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_sales'


class DrugTemplates(models.Model):
    drug_id = models.IntegerField(primary_key=True)
    selector = models.CharField(max_length=255)
    dosage = models.CharField(max_length=10, blank=True, null=True)
    period = models.IntegerField()
    quantity = models.IntegerField()
    refills = models.IntegerField()
    taxrates = models.CharField(max_length=255, blank=True, null=True)
    pkgqty = models.FloatField()

    class Meta:
        managed = False
        db_table = 'drug_templates'
        unique_together = (('drug_id', 'selector'),)


class Drugs(models.Model):
    drug_id = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    name = models.CharField(max_length=255)
    ndc_number = models.CharField(max_length=20)
    on_order = models.IntegerField()
    reorder_point = models.FloatField()
    max_level = models.FloatField()
    last_notify = models.DateField(blank=True, null=True)
    reactions = models.TextField(blank=True, null=True)
    form = models.CharField(max_length=31)
    size = models.CharField(max_length=25)
    unit = models.CharField(max_length=31)
    route = models.CharField(max_length=31)
    substitute = models.IntegerField()
    related_code = models.CharField(max_length=255)
    cyp_factor = models.FloatField()
    active = models.IntegerField(blank=True, null=True)
    allow_combining = models.IntegerField()
    allow_multiple = models.IntegerField()
    drug_code = models.CharField(max_length=25, blank=True, null=True)
    consumable = models.IntegerField()
    dispensable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drugs'


class EligibilityVerification(models.Model):
    verification_id = models.BigAutoField(primary_key=True)
    response_id = models.CharField(max_length=32, blank=True, null=True)
    insurance_id = models.BigIntegerField(blank=True, null=True)
    eligibility_check_date = models.DateTimeField(blank=True, null=True)
    copay = models.IntegerField(blank=True, null=True)
    deductible = models.IntegerField(blank=True, null=True)
    deductiblemet = models.CharField(max_length=1, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eligibility_verification'


class EmployerData(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street_line_2 = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'employer_data'


class EncCategoryMap(models.Model):
    rule_enc_id = models.CharField(max_length=31)
    main_cat_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'enc_category_map'


class ErxNarcotics(models.Model):
    drug = models.CharField(max_length=255)
    dea_number = models.CharField(max_length=5)
    csa_sch = models.CharField(max_length=2)
    narc = models.CharField(max_length=2)
    other_names = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'erx_narcotics'


class ErxRxLog(models.Model):
    prescription_id = models.IntegerField()
    date = models.CharField(max_length=25)
    time = models.CharField(max_length=15)
    code = models.IntegerField()
    status = models.TextField(blank=True, null=True)
    message_id = models.CharField(max_length=100, blank=True, null=True)
    read = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'erx_rx_log'


class ErxTtlTouch(models.Model):
    patient_id = models.PositiveBigIntegerField(primary_key=True)
    process = models.CharField(max_length=11)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'erx_ttl_touch'
        unique_together = (('patient_id', 'process'),)


class ErxWenoDrugs(models.Model):
    drug_id = models.AutoField(primary_key=True)
    rxcui_drug_coded = models.IntegerField(blank=True, null=True)
    generic_rxcui = models.IntegerField(blank=True, null=True)
    drug_db_code_qualifier = models.TextField(blank=True, null=True)
    full_name = models.CharField(max_length=250)
    rxn_dose_form = models.TextField(blank=True, null=True)
    full_generic_name = models.CharField(max_length=250)
    brand_name = models.CharField(max_length=250)
    display_name = models.CharField(max_length=250)
    route = models.TextField(blank=True, null=True)
    new_dose_form = models.CharField(max_length=100, blank=True, null=True)
    strength = models.CharField(max_length=15, blank=True, null=True)
    supress_for = models.TextField(blank=True, null=True)
    display_name_synonym = models.TextField(blank=True, null=True)
    is_retired = models.TextField(blank=True, null=True)
    sxdg_rxcui = models.CharField(max_length=10, blank=True, null=True)
    sxdg_tty = models.TextField(blank=True, null=True)
    sxdg_name = models.CharField(max_length=100, blank=True, null=True)
    psn_drugdescription = models.CharField(max_length=100, blank=True, null=True)
    ncpdp_quantity_term = models.TextField(blank=True, null=True)
    potency_unit_code = models.CharField(max_length=10, blank=True, null=True)
    dea_schedule_no = models.IntegerField(blank=True, null=True)
    dea_schedule = models.CharField(max_length=7, blank=True, null=True)
    ingredients = models.CharField(max_length=100, blank=True, null=True)
    drug_interaction = models.CharField(max_length=100, blank=True, null=True)
    unit_source_code = models.CharField(max_length=3, blank=True, null=True)
    code_list_qualifier = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'erx_weno_drugs'


class EsignSignatures(models.Model):
    tid = models.IntegerField()
    table = models.CharField(max_length=255)
    uid = models.IntegerField()
    datetime = models.DateTimeField()
    is_lock = models.IntegerField()
    amendment = models.TextField(blank=True, null=True)
    hash = models.CharField(max_length=255)
    signature_hash = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'esign_signatures'


class ExportJob(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    user_id = models.CharField(max_length=40)
    client_id = models.CharField(max_length=80)
    status = models.CharField(max_length=40)
    start_time = models.DateTimeField(blank=True, null=True)
    resource_include_time = models.DateTimeField(blank=True, null=True)
    output_format = models.CharField(max_length=128)
    request_uri = models.CharField(max_length=128)
    resources = models.TextField(blank=True, null=True)
    output = models.TextField(blank=True, null=True)
    errors = models.TextField(blank=True, null=True)
    access_token_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'export_job'


class ExtendedLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    recipient = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extended_log'


class ExternalEncounters(models.Model):
    ee_id = models.AutoField(primary_key=True)
    ee_date = models.DateField(blank=True, null=True)
    ee_pid = models.IntegerField(blank=True, null=True)
    ee_provider_id = models.CharField(max_length=255, blank=True, null=True)
    ee_facility_id = models.CharField(max_length=255, blank=True, null=True)
    ee_encounter_diagnosis = models.CharField(max_length=255, blank=True, null=True)
    ee_external_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_encounters'


class ExternalProcedures(models.Model):
    ep_id = models.AutoField(primary_key=True)
    ep_date = models.DateField(blank=True, null=True)
    ep_code_type = models.CharField(max_length=20, blank=True, null=True)
    ep_code = models.CharField(max_length=9, blank=True, null=True)
    ep_pid = models.IntegerField(blank=True, null=True)
    ep_encounter = models.IntegerField(blank=True, null=True)
    ep_code_text = models.TextField(blank=True, null=True)
    ep_facility_id = models.CharField(max_length=255, blank=True, null=True)
    ep_external_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'external_procedures'


class Facility(models.Model):
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=11, blank=True, null=True)
    country_code = models.CharField(max_length=30)
    federal_ein = models.CharField(max_length=15, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    service_location = models.IntegerField()
    billing_location = models.IntegerField()
    accepts_assignment = models.IntegerField()
    pos_code = models.IntegerField(blank=True, null=True)
    x12_sender_id = models.CharField(max_length=25, blank=True, null=True)
    attn = models.CharField(max_length=65, blank=True, null=True)
    domain_identifier = models.CharField(max_length=60, blank=True, null=True)
    facility_npi = models.CharField(max_length=15, blank=True, null=True)
    facility_taxonomy = models.CharField(max_length=15, blank=True, null=True)
    tax_id_type = models.CharField(max_length=31)
    color = models.CharField(max_length=7)
    primary_business_entity = models.IntegerField()
    facility_code = models.CharField(max_length=31, blank=True, null=True)
    extra_validation = models.IntegerField()
    mail_street = models.CharField(max_length=30, blank=True, null=True)
    mail_street2 = models.CharField(max_length=30, blank=True, null=True)
    mail_city = models.CharField(max_length=50, blank=True, null=True)
    mail_state = models.CharField(max_length=3, blank=True, null=True)
    mail_zip = models.CharField(max_length=10, blank=True, null=True)
    oid = models.CharField(max_length=255)
    iban = models.CharField(max_length=50, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    weno_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility'


class FacilityUserIds(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.BigIntegerField(blank=True, null=True)
    facility_id = models.BigIntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=16, blank=True, null=True)
    field_id = models.CharField(max_length=31)
    field_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facility_user_ids'


class FeeSheetOptions(models.Model):
    fs_category = models.CharField(max_length=63, blank=True, null=True)
    fs_option = models.CharField(max_length=63, blank=True, null=True)
    fs_codes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fee_sheet_options'


class FormCarePlan(models.Model):
    id = models.BigIntegerField()
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    encounter = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    codetext = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    external_id = models.CharField(max_length=30, blank=True, null=True)
    care_plan_type = models.CharField(max_length=30, blank=True, null=True)
    note_related_to = models.TextField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    reason_code = models.CharField(max_length=31, blank=True, null=True)
    reason_description = models.TextField(blank=True, null=True)
    reason_date_low = models.DateTimeField(blank=True, null=True)
    reason_date_high = models.DateTimeField(blank=True, null=True)
    reason_status = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_care_plan'


class FormClinicalInstructions(models.Model):
    pid = models.BigIntegerField(blank=True, null=True)
    encounter = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    instruction = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    activity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_clinical_instructions'


class FormClinicalNotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    form_id = models.BigIntegerField()
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    encounter = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    codetext = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    external_id = models.CharField(max_length=30, blank=True, null=True)
    clinical_notes_type = models.CharField(max_length=100, blank=True, null=True)
    clinical_notes_category = models.CharField(max_length=100, blank=True, null=True)
    note_related_to = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_clinical_notes'


class FormDictation(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    dictation = models.TextField(blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_dictation'


class FormEncounter(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    facility = models.TextField(blank=True, null=True)
    facility_id = models.IntegerField()
    pid = models.BigIntegerField(blank=True, null=True)
    encounter = models.BigIntegerField(blank=True, null=True)
    onset_date = models.DateTimeField(blank=True, null=True)
    sensitivity = models.CharField(max_length=30, blank=True, null=True)
    billing_note = models.TextField(blank=True, null=True)
    pc_catid = models.IntegerField()
    last_level_billed = models.IntegerField()
    last_level_closed = models.IntegerField()
    last_stmt_date = models.DateField(blank=True, null=True)
    stmt_count = models.IntegerField()
    provider_id = models.IntegerField(blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    invoice_refno = models.CharField(max_length=31)
    referral_source = models.CharField(max_length=31)
    billing_facility = models.IntegerField()
    external_id = models.CharField(max_length=20, blank=True, null=True)
    pos_code = models.IntegerField(blank=True, null=True)
    parent_encounter_id = models.BigIntegerField(blank=True, null=True)
    class_code = models.CharField(max_length=10)
    shift = models.CharField(max_length=31)
    voucher_number = models.CharField(max_length=255)
    discharge_disposition = models.CharField(max_length=100, blank=True, null=True)
    encounter_type_code = models.CharField(max_length=31, blank=True, null=True)
    encounter_type_description = models.TextField(blank=True, null=True)
    referring_provider_id = models.IntegerField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_encounter'


class FormEyeAcuity(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    scodva = models.CharField(db_column='SCODVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    scosva = models.CharField(db_column='SCOSVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phodva = models.CharField(db_column='PHODVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    phosva = models.CharField(db_column='PHOSVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlodva = models.CharField(db_column='CTLODVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlosva = models.CharField(db_column='CTLOSVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrodva = models.CharField(db_column='MRODVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrosva = models.CharField(db_column='MROSVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    scnearodva = models.CharField(db_column='SCNEARODVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    scnearosva = models.CharField(db_column='SCNEAROSVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrnearodva = models.CharField(db_column='MRNEARODVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrnearosva = models.CharField(db_column='MRNEAROSVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    glareodva = models.CharField(db_column='GLAREODVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    glareosva = models.CharField(db_column='GLAREOSVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    glarecomments = models.CharField(db_column='GLARECOMMENTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    arodva = models.CharField(db_column='ARODVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    arosva = models.CharField(db_column='AROSVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    crodva = models.CharField(db_column='CRODVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    crosva = models.CharField(db_column='CROSVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlodva1 = models.CharField(db_column='CTLODVA1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlosva1 = models.CharField(db_column='CTLOSVA1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pamodva = models.CharField(db_column='PAMODVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pamosva = models.CharField(db_column='PAMOSVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    liodva = models.CharField(db_column='LIODVA', max_length=25)  # Field name made lowercase.
    liosva = models.CharField(db_column='LIOSVA', max_length=25)  # Field name made lowercase.
    wodvanear = models.CharField(db_column='WODVANEAR', max_length=25, blank=True, null=True)  # Field name made lowercase.
    osvanearcc = models.CharField(db_column='OSVANEARCC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    binocva = models.CharField(db_column='BINOCVA', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_acuity'
        unique_together = (('id', 'pid'),)


class FormEyeAntseg(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    odschirmer1 = models.CharField(db_column='ODSCHIRMER1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    osschirmer1 = models.CharField(db_column='OSSCHIRMER1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    odschirmer2 = models.CharField(db_column='ODSCHIRMER2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    osschirmer2 = models.CharField(db_column='OSSCHIRMER2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    odtbut = models.CharField(db_column='ODTBUT', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ostbut = models.CharField(db_column='OSTBUT', max_length=25, blank=True, null=True)  # Field name made lowercase.
    osconj = models.CharField(db_column='OSCONJ', max_length=25, blank=True, null=True)  # Field name made lowercase.
    odconj = models.TextField(db_column='ODCONJ', blank=True, null=True)  # Field name made lowercase.
    odcornea = models.TextField(db_column='ODCORNEA', blank=True, null=True)  # Field name made lowercase.
    oscornea = models.TextField(db_column='OSCORNEA', blank=True, null=True)  # Field name made lowercase.
    odac = models.TextField(db_column='ODAC', blank=True, null=True)  # Field name made lowercase.
    osac = models.TextField(db_column='OSAC', blank=True, null=True)  # Field name made lowercase.
    odlens = models.TextField(db_column='ODLENS', blank=True, null=True)  # Field name made lowercase.
    oslens = models.TextField(db_column='OSLENS', blank=True, null=True)  # Field name made lowercase.
    odiris = models.TextField(db_column='ODIRIS', blank=True, null=True)  # Field name made lowercase.
    osiris = models.TextField(db_column='OSIRIS', blank=True, null=True)  # Field name made lowercase.
    pupil_normal = models.CharField(db_column='PUPIL_NORMAL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    odpupilsize1 = models.CharField(db_column='ODPUPILSIZE1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    odpupilsize2 = models.CharField(db_column='ODPUPILSIZE2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    odpupilreactivity = models.CharField(db_column='ODPUPILREACTIVITY', max_length=25, blank=True, null=True)  # Field name made lowercase.
    odapd = models.CharField(db_column='ODAPD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ospupilsize1 = models.CharField(db_column='OSPUPILSIZE1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ospupilsize2 = models.CharField(db_column='OSPUPILSIZE2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ospupilreactivity = models.CharField(db_column='OSPUPILREACTIVITY', max_length=25, blank=True, null=True)  # Field name made lowercase.
    osapd = models.CharField(db_column='OSAPD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dimodpupilsize1 = models.CharField(db_column='DIMODPUPILSIZE1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dimodpupilsize2 = models.CharField(db_column='DIMODPUPILSIZE2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dimodpupilreactivity = models.CharField(db_column='DIMODPUPILREACTIVITY', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dimospupilsize1 = models.CharField(db_column='DIMOSPUPILSIZE1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dimospupilsize2 = models.CharField(db_column='DIMOSPUPILSIZE2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dimospupilreactivity = models.CharField(db_column='DIMOSPUPILREACTIVITY', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pupil_comments = models.TextField(db_column='PUPIL_COMMENTS', blank=True, null=True)  # Field name made lowercase.
    odkthickness = models.CharField(db_column='ODKTHICKNESS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    oskthickness = models.CharField(db_column='OSKTHICKNESS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    odgonio = models.CharField(db_column='ODGONIO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    osgonio = models.CharField(db_column='OSGONIO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    antseg_comments = models.TextField(db_column='ANTSEG_COMMENTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_antseg'
        unique_together = (('id', 'pid'),)


class FormEyeBase(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_eye_base'


class FormEyeBiometrics(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    odk1 = models.CharField(db_column='ODK1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odk2 = models.CharField(db_column='ODK2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odk2axis = models.CharField(db_column='ODK2AXIS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osk1 = models.CharField(db_column='OSK1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osk2 = models.CharField(db_column='OSK2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osk2axis = models.CharField(db_column='OSK2AXIS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odaxiallength = models.CharField(db_column='ODAXIALLENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osaxiallength = models.CharField(db_column='OSAXIALLENGTH', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odpdmeasured = models.CharField(db_column='ODPDMeasured', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ospdmeasured = models.CharField(db_column='OSPDMeasured', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odacd = models.CharField(db_column='ODACD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osacd = models.CharField(db_column='OSACD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odw2w = models.CharField(db_column='ODW2W', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osw2w = models.CharField(db_column='OSW2W', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odlt = models.CharField(db_column='ODLT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oslt = models.CharField(db_column='OSLT', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_biometrics'
        unique_together = (('id', 'pid'),)


class FormEyeExternal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    rul = models.TextField(db_column='RUL', blank=True, null=True)  # Field name made lowercase.
    lul = models.TextField(db_column='LUL', blank=True, null=True)  # Field name made lowercase.
    rll = models.TextField(db_column='RLL', blank=True, null=True)  # Field name made lowercase.
    lll = models.TextField(db_column='LLL', blank=True, null=True)  # Field name made lowercase.
    rbrow = models.TextField(db_column='RBROW', blank=True, null=True)  # Field name made lowercase.
    lbrow = models.TextField(db_column='LBROW', blank=True, null=True)  # Field name made lowercase.
    rmct = models.TextField(db_column='RMCT', blank=True, null=True)  # Field name made lowercase.
    lmct = models.TextField(db_column='LMCT', blank=True, null=True)  # Field name made lowercase.
    radnexa = models.TextField(db_column='RADNEXA', blank=True, null=True)  # Field name made lowercase.
    ladnexa = models.TextField(db_column='LADNEXA', blank=True, null=True)  # Field name made lowercase.
    rmrd = models.CharField(db_column='RMRD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lmrd = models.CharField(db_column='LMRD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rlf = models.CharField(db_column='RLF', max_length=25, blank=True, null=True)  # Field name made lowercase.
    llf = models.CharField(db_column='LLF', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rvfissure = models.CharField(db_column='RVFISSURE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lvfissure = models.CharField(db_column='LVFISSURE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    odhertel = models.CharField(db_column='ODHERTEL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    oshertel = models.CharField(db_column='OSHERTEL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    hertelbase = models.CharField(db_column='HERTELBASE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rcarotid = models.TextField(db_column='RCAROTID', blank=True, null=True)  # Field name made lowercase.
    lcarotid = models.TextField(db_column='LCAROTID', blank=True, null=True)  # Field name made lowercase.
    rtempart = models.TextField(db_column='RTEMPART', blank=True, null=True)  # Field name made lowercase.
    ltempart = models.TextField(db_column='LTEMPART', blank=True, null=True)  # Field name made lowercase.
    rcnv = models.TextField(db_column='RCNV', blank=True, null=True)  # Field name made lowercase.
    lcnv = models.TextField(db_column='LCNV', blank=True, null=True)  # Field name made lowercase.
    rcnvii = models.TextField(db_column='RCNVII', blank=True, null=True)  # Field name made lowercase.
    lcnvii = models.TextField(db_column='LCNVII', blank=True, null=True)  # Field name made lowercase.
    ext_comments = models.TextField(db_column='EXT_COMMENTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_external'
        unique_together = (('id', 'pid'),)


class FormEyeHpi(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    cc1 = models.CharField(db_column='CC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hpi1 = models.TextField(db_column='HPI1', blank=True, null=True)  # Field name made lowercase.
    quality1 = models.CharField(db_column='QUALITY1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    timing1 = models.CharField(db_column='TIMING1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    duration1 = models.CharField(db_column='DURATION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    context1 = models.CharField(db_column='CONTEXT1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    severity1 = models.CharField(db_column='SEVERITY1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    modify1 = models.CharField(db_column='MODIFY1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    associated1 = models.CharField(db_column='ASSOCIATED1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    location1 = models.CharField(db_column='LOCATION1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chronic1 = models.CharField(db_column='CHRONIC1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chronic2 = models.CharField(db_column='CHRONIC2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    chronic3 = models.CharField(db_column='CHRONIC3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cc2 = models.TextField(db_column='CC2', blank=True, null=True)  # Field name made lowercase.
    hpi2 = models.TextField(db_column='HPI2', blank=True, null=True)  # Field name made lowercase.
    quality2 = models.TextField(db_column='QUALITY2', blank=True, null=True)  # Field name made lowercase.
    timing2 = models.TextField(db_column='TIMING2', blank=True, null=True)  # Field name made lowercase.
    duration2 = models.TextField(db_column='DURATION2', blank=True, null=True)  # Field name made lowercase.
    context2 = models.TextField(db_column='CONTEXT2', blank=True, null=True)  # Field name made lowercase.
    severity2 = models.TextField(db_column='SEVERITY2', blank=True, null=True)  # Field name made lowercase.
    modify2 = models.TextField(db_column='MODIFY2', blank=True, null=True)  # Field name made lowercase.
    associated2 = models.TextField(db_column='ASSOCIATED2', blank=True, null=True)  # Field name made lowercase.
    location2 = models.TextField(db_column='LOCATION2', blank=True, null=True)  # Field name made lowercase.
    cc3 = models.TextField(db_column='CC3', blank=True, null=True)  # Field name made lowercase.
    hpi3 = models.TextField(db_column='HPI3', blank=True, null=True)  # Field name made lowercase.
    quality3 = models.TextField(db_column='QUALITY3', blank=True, null=True)  # Field name made lowercase.
    timing3 = models.TextField(db_column='TIMING3', blank=True, null=True)  # Field name made lowercase.
    duration3 = models.TextField(db_column='DURATION3', blank=True, null=True)  # Field name made lowercase.
    context3 = models.TextField(db_column='CONTEXT3', blank=True, null=True)  # Field name made lowercase.
    severity3 = models.TextField(db_column='SEVERITY3', blank=True, null=True)  # Field name made lowercase.
    modify3 = models.TextField(db_column='MODIFY3', blank=True, null=True)  # Field name made lowercase.
    associated3 = models.TextField(db_column='ASSOCIATED3', blank=True, null=True)  # Field name made lowercase.
    location3 = models.TextField(db_column='LOCATION3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_hpi'
        unique_together = (('id', 'pid'),)


class FormEyeLocking(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    imp = models.TextField(db_column='IMP', blank=True, null=True)  # Field name made lowercase.
    plan = models.TextField(db_column='PLAN', blank=True, null=True)  # Field name made lowercase.
    resource = models.CharField(db_column='Resource', max_length=50, blank=True, null=True)  # Field name made lowercase.
    technician = models.CharField(db_column='Technician', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locked = models.CharField(db_column='LOCKED', max_length=3, blank=True, null=True)  # Field name made lowercase.
    lockeddate = models.DateTimeField(db_column='LOCKEDDATE')  # Field name made lowercase.
    lockedby = models.CharField(db_column='LOCKEDBY', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_locking'
        unique_together = (('id', 'pid'),)


class FormEyeMagDispense(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField()
    encounter = models.BigIntegerField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    refdate = models.DateTimeField(db_column='REFDATE', blank=True, null=True)  # Field name made lowercase.
    reftype = models.CharField(db_column='REFTYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rxtype = models.CharField(db_column='RXTYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odsph = models.CharField(db_column='ODSPH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odcyl = models.CharField(db_column='ODCYL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odaxis = models.CharField(db_column='ODAXIS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ossph = models.CharField(db_column='OSSPH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    oscyl = models.CharField(db_column='OSCYL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osaxis = models.CharField(db_column='OSAXIS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odmidadd = models.CharField(db_column='ODMIDADD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osmidadd = models.CharField(db_column='OSMIDADD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odadd = models.CharField(db_column='ODADD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osadd = models.CharField(db_column='OSADD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odhpd = models.CharField(db_column='ODHPD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odhbase = models.CharField(db_column='ODHBASE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odvpd = models.CharField(db_column='ODVPD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odvbase = models.CharField(db_column='ODVBASE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odslaboff = models.CharField(db_column='ODSLABOFF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odvertexdist = models.CharField(db_column='ODVERTEXDIST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oshpd = models.CharField(db_column='OSHPD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oshbase = models.CharField(db_column='OSHBASE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osvpd = models.CharField(db_column='OSVPD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osvbase = models.CharField(db_column='OSVBASE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osslaboff = models.CharField(db_column='OSSLABOFF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osvertexdist = models.CharField(db_column='OSVERTEXDIST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odmpdd = models.CharField(db_column='ODMPDD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odmpdn = models.CharField(db_column='ODMPDN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osmpdd = models.CharField(db_column='OSMPDD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osmpdn = models.CharField(db_column='OSMPDN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bpdd = models.CharField(db_column='BPDD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bpdn = models.CharField(db_column='BPDN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lens_material = models.CharField(db_column='LENS_MATERIAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lens_treatments = models.CharField(db_column='LENS_TREATMENTS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ctlmanufacturerod = models.CharField(db_column='CTLMANUFACTUREROD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlmanufactureros = models.CharField(db_column='CTLMANUFACTUREROS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlsupplierod = models.CharField(db_column='CTLSUPPLIEROD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlsupplieros = models.CharField(db_column='CTLSUPPLIEROS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlbrandod = models.CharField(db_column='CTLBRANDOD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctlbrandos = models.CharField(db_column='CTLBRANDOS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctlodquantity = models.CharField(db_column='CTLODQUANTITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ctlosquantity = models.CharField(db_column='CTLOSQUANTITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    oddiam = models.CharField(db_column='ODDIAM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    odbc = models.CharField(db_column='ODBC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osdiam = models.CharField(db_column='OSDIAM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    osbc = models.CharField(db_column='OSBC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rxcomments = models.TextField(db_column='RXCOMMENTS', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='COMMENTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_mag_dispense'
        unique_together = (('pid', 'encounter', 'id'),)


class FormEyeMagImpplan(models.Model):
    form_id = models.BigIntegerField()
    pid = models.BigIntegerField()
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=50, blank=True, null=True)
    codetype = models.CharField(max_length=50, blank=True, null=True)
    codedesc = models.CharField(max_length=255, blank=True, null=True)
    codetext = models.CharField(max_length=255, blank=True, null=True)
    plan = models.CharField(max_length=3000, blank=True, null=True)
    pmsfh_link = models.CharField(db_column='PMSFH_link', max_length=50, blank=True, null=True)  # Field name made lowercase.
    impplan_order = models.IntegerField(db_column='IMPPLAN_order', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_mag_impplan'
        unique_together = (('form_id', 'pid', 'title', 'plan'),)


class FormEyeMagOrders(models.Model):
    id = models.BigAutoField(primary_key=True)
    form_id = models.IntegerField()
    pid = models.BigIntegerField()
    order_details = models.CharField(db_column='ORDER_DETAILS', max_length=255)  # Field name made lowercase.
    order_status = models.CharField(db_column='ORDER_STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    order_priority = models.CharField(db_column='ORDER_PRIORITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    order_date_placed = models.DateField(db_column='ORDER_DATE_PLACED')  # Field name made lowercase.
    order_placed_bywhom = models.CharField(db_column='ORDER_PLACED_BYWHOM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    order_date_completed = models.DateField(db_column='ORDER_DATE_COMPLETED', blank=True, null=True)  # Field name made lowercase.
    order_completed_bywhom = models.CharField(db_column='ORDER_COMPLETED_BYWHOM', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_mag_orders'
        unique_together = (('pid', 'order_details', 'order_date_placed'),)


class FormEyeMagPrefs(models.Model):
    pezone = models.CharField(db_column='PEZONE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=25, blank=True, null=True)  # Field name made lowercase.
    location_text = models.CharField(db_column='LOCATION_text', max_length=25)  # Field name made lowercase.
    id = models.BigIntegerField(blank=True, null=True)
    selection = models.CharField(max_length=255, blank=True, null=True)
    zone_order = models.IntegerField(db_column='ZONE_ORDER', blank=True, null=True)  # Field name made lowercase.
    govalue = models.CharField(db_column='GOVALUE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ordering = models.SmallIntegerField(blank=True, null=True)
    fill_action = models.CharField(db_column='FILL_ACTION', max_length=10)  # Field name made lowercase.
    goright = models.CharField(db_column='GORIGHT', max_length=50)  # Field name made lowercase.
    goleft = models.CharField(db_column='GOLEFT', max_length=50)  # Field name made lowercase.
    unspec = models.CharField(db_column='UNSPEC', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_mag_prefs'
        unique_together = (('id', 'pezone', 'location', 'selection'),)


class FormEyeMagWearing(models.Model):
    id = models.AutoField(unique=True)
    encounter = models.IntegerField(db_column='ENCOUNTER')  # Field name made lowercase.
    form_id = models.SmallIntegerField(db_column='FORM_ID')  # Field name made lowercase.
    pid = models.BigIntegerField(db_column='PID')  # Field name made lowercase.
    rx_number = models.IntegerField(db_column='RX_NUMBER')  # Field name made lowercase.
    odsph = models.CharField(db_column='ODSPH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odcyl = models.CharField(db_column='ODCYL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odaxis = models.CharField(db_column='ODAXIS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ossph = models.CharField(db_column='OSSPH', max_length=10, blank=True, null=True)  # Field name made lowercase.
    oscyl = models.CharField(db_column='OSCYL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osaxis = models.CharField(db_column='OSAXIS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odmidadd = models.CharField(db_column='ODMIDADD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osmidadd = models.CharField(db_column='OSMIDADD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odadd = models.CharField(db_column='ODADD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osadd = models.CharField(db_column='OSADD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odva = models.CharField(db_column='ODVA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osva = models.CharField(db_column='OSVA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odnearva = models.CharField(db_column='ODNEARVA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osnearva = models.CharField(db_column='OSNEARVA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odhpd = models.CharField(db_column='ODHPD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odhbase = models.CharField(db_column='ODHBASE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odvpd = models.CharField(db_column='ODVPD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odvbase = models.CharField(db_column='ODVBASE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odslaboff = models.CharField(db_column='ODSLABOFF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odvertexdist = models.CharField(db_column='ODVERTEXDIST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oshpd = models.CharField(db_column='OSHPD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    oshbase = models.CharField(db_column='OSHBASE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osvpd = models.CharField(db_column='OSVPD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osvbase = models.CharField(db_column='OSVBASE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osslaboff = models.CharField(db_column='OSSLABOFF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osvertexdist = models.CharField(db_column='OSVERTEXDIST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odmpdd = models.CharField(db_column='ODMPDD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odmpdn = models.CharField(db_column='ODMPDN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osmpdd = models.CharField(db_column='OSMPDD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osmpdn = models.CharField(db_column='OSMPDN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bpdd = models.CharField(db_column='BPDD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bpdn = models.CharField(db_column='BPDN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lens_material = models.CharField(db_column='LENS_MATERIAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lens_treatments = models.CharField(db_column='LENS_TREATMENTS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rx_type = models.CharField(db_column='RX_TYPE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='COMMENTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_mag_wearing'
        unique_together = (('form_id', 'encounter', 'pid', 'rx_number'),)


class FormEyeNeuro(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    act = models.CharField(db_column='ACT', max_length=3)  # Field name made lowercase.
    act5ccdist = models.TextField(db_column='ACT5CCDIST', blank=True, null=True)  # Field name made lowercase.
    act1ccdist = models.TextField(db_column='ACT1CCDIST', blank=True, null=True)  # Field name made lowercase.
    act2ccdist = models.TextField(db_column='ACT2CCDIST', blank=True, null=True)  # Field name made lowercase.
    act3ccdist = models.TextField(db_column='ACT3CCDIST', blank=True, null=True)  # Field name made lowercase.
    act4ccdist = models.TextField(db_column='ACT4CCDIST', blank=True, null=True)  # Field name made lowercase.
    act6ccdist = models.TextField(db_column='ACT6CCDIST', blank=True, null=True)  # Field name made lowercase.
    act7ccdist = models.TextField(db_column='ACT7CCDIST', blank=True, null=True)  # Field name made lowercase.
    act8ccdist = models.TextField(db_column='ACT8CCDIST', blank=True, null=True)  # Field name made lowercase.
    act9ccdist = models.TextField(db_column='ACT9CCDIST', blank=True, null=True)  # Field name made lowercase.
    act10ccdist = models.TextField(db_column='ACT10CCDIST', blank=True, null=True)  # Field name made lowercase.
    act11ccdist = models.TextField(db_column='ACT11CCDIST', blank=True, null=True)  # Field name made lowercase.
    act1scdist = models.TextField(db_column='ACT1SCDIST', blank=True, null=True)  # Field name made lowercase.
    act2scdist = models.TextField(db_column='ACT2SCDIST', blank=True, null=True)  # Field name made lowercase.
    act3scdist = models.TextField(db_column='ACT3SCDIST', blank=True, null=True)  # Field name made lowercase.
    act4scdist = models.TextField(db_column='ACT4SCDIST', blank=True, null=True)  # Field name made lowercase.
    act5scdist = models.TextField(db_column='ACT5SCDIST', blank=True, null=True)  # Field name made lowercase.
    act6scdist = models.TextField(db_column='ACT6SCDIST', blank=True, null=True)  # Field name made lowercase.
    act7scdist = models.TextField(db_column='ACT7SCDIST', blank=True, null=True)  # Field name made lowercase.
    act8scdist = models.TextField(db_column='ACT8SCDIST', blank=True, null=True)  # Field name made lowercase.
    act9scdist = models.TextField(db_column='ACT9SCDIST', blank=True, null=True)  # Field name made lowercase.
    act10scdist = models.TextField(db_column='ACT10SCDIST', blank=True, null=True)  # Field name made lowercase.
    act11scdist = models.TextField(db_column='ACT11SCDIST', blank=True, null=True)  # Field name made lowercase.
    act1scnear = models.TextField(db_column='ACT1SCNEAR', blank=True, null=True)  # Field name made lowercase.
    act2scnear = models.TextField(db_column='ACT2SCNEAR', blank=True, null=True)  # Field name made lowercase.
    act3scnear = models.TextField(db_column='ACT3SCNEAR', blank=True, null=True)  # Field name made lowercase.
    act4scnear = models.TextField(db_column='ACT4SCNEAR', blank=True, null=True)  # Field name made lowercase.
    act5ccnear = models.TextField(db_column='ACT5CCNEAR', blank=True, null=True)  # Field name made lowercase.
    act6ccnear = models.TextField(db_column='ACT6CCNEAR', blank=True, null=True)  # Field name made lowercase.
    act7ccnear = models.TextField(db_column='ACT7CCNEAR', blank=True, null=True)  # Field name made lowercase.
    act8ccnear = models.TextField(db_column='ACT8CCNEAR', blank=True, null=True)  # Field name made lowercase.
    act9ccnear = models.TextField(db_column='ACT9CCNEAR', blank=True, null=True)  # Field name made lowercase.
    act10ccnear = models.TextField(db_column='ACT10CCNEAR', blank=True, null=True)  # Field name made lowercase.
    act11ccnear = models.TextField(db_column='ACT11CCNEAR', blank=True, null=True)  # Field name made lowercase.
    act5scnear = models.TextField(db_column='ACT5SCNEAR', blank=True, null=True)  # Field name made lowercase.
    act6scnear = models.TextField(db_column='ACT6SCNEAR', blank=True, null=True)  # Field name made lowercase.
    act7scnear = models.TextField(db_column='ACT7SCNEAR', blank=True, null=True)  # Field name made lowercase.
    act8scnear = models.TextField(db_column='ACT8SCNEAR', blank=True, null=True)  # Field name made lowercase.
    act9scnear = models.TextField(db_column='ACT9SCNEAR', blank=True, null=True)  # Field name made lowercase.
    act10scnear = models.TextField(db_column='ACT10SCNEAR', blank=True, null=True)  # Field name made lowercase.
    act11scnear = models.TextField(db_column='ACT11SCNEAR', blank=True, null=True)  # Field name made lowercase.
    act1ccnear = models.TextField(db_column='ACT1CCNEAR', blank=True, null=True)  # Field name made lowercase.
    act2ccnear = models.TextField(db_column='ACT2CCNEAR', blank=True, null=True)  # Field name made lowercase.
    act3ccnear = models.TextField(db_column='ACT3CCNEAR', blank=True, null=True)  # Field name made lowercase.
    act4ccnear = models.TextField(db_column='ACT4CCNEAR', blank=True, null=True)  # Field name made lowercase.
    motilitynormal = models.CharField(db_column='MOTILITYNORMAL', max_length=3)  # Field name made lowercase.
    motility_rs = models.CharField(db_column='MOTILITY_RS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    motility_ri = models.CharField(db_column='MOTILITY_RI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    motility_rr = models.CharField(db_column='MOTILITY_RR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    motility_rl = models.CharField(db_column='MOTILITY_RL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    motility_ls = models.CharField(db_column='MOTILITY_LS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    motility_li = models.CharField(db_column='MOTILITY_LI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    motility_lr = models.CharField(db_column='MOTILITY_LR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    motility_ll = models.CharField(db_column='MOTILITY_LL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    motility_rrso = models.IntegerField(db_column='MOTILITY_RRSO', blank=True, null=True)  # Field name made lowercase.
    motility_rlso = models.IntegerField(db_column='MOTILITY_RLSO', blank=True, null=True)  # Field name made lowercase.
    motility_rrio = models.IntegerField(db_column='MOTILITY_RRIO', blank=True, null=True)  # Field name made lowercase.
    motility_rlio = models.IntegerField(db_column='MOTILITY_RLIO', blank=True, null=True)  # Field name made lowercase.
    motility_lrso = models.IntegerField(db_column='MOTILITY_LRSO', blank=True, null=True)  # Field name made lowercase.
    motility_llso = models.IntegerField(db_column='MOTILITY_LLSO', blank=True, null=True)  # Field name made lowercase.
    motility_lrio = models.IntegerField(db_column='MOTILITY_LRIO', blank=True, null=True)  # Field name made lowercase.
    motility_llio = models.IntegerField(db_column='MOTILITY_LLIO', blank=True, null=True)  # Field name made lowercase.
    neuro_comments = models.TextField(db_column='NEURO_COMMENTS', blank=True, null=True)  # Field name made lowercase.
    stereopsis = models.CharField(db_column='STEREOPSIS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    odnpa = models.TextField(db_column='ODNPA', blank=True, null=True)  # Field name made lowercase.
    osnpa = models.TextField(db_column='OSNPA', blank=True, null=True)  # Field name made lowercase.
    vertfusamps = models.TextField(db_column='VERTFUSAMPS', blank=True, null=True)  # Field name made lowercase.
    divergenceamps = models.TextField(db_column='DIVERGENCEAMPS', blank=True, null=True)  # Field name made lowercase.
    npc = models.CharField(db_column='NPC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    daccdist = models.CharField(db_column='DACCDIST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    daccnear = models.CharField(db_column='DACCNEAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    caccdist = models.CharField(db_column='CACCDIST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    caccnear = models.CharField(db_column='CACCNEAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    odcolor = models.TextField(db_column='ODCOLOR', blank=True, null=True)  # Field name made lowercase.
    oscolor = models.TextField(db_column='OSCOLOR', blank=True, null=True)  # Field name made lowercase.
    odcoins = models.TextField(db_column='ODCOINS', blank=True, null=True)  # Field name made lowercase.
    oscoins = models.TextField(db_column='OSCOINS', blank=True, null=True)  # Field name made lowercase.
    odreddesat = models.CharField(db_column='ODREDDESAT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    osreddesat = models.CharField(db_column='OSREDDESAT', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_neuro'
        unique_together = (('id', 'pid'),)


class FormEyePostseg(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    oddisc = models.TextField(db_column='ODDISC', blank=True, null=True)  # Field name made lowercase.
    osdisc = models.TextField(db_column='OSDISC', blank=True, null=True)  # Field name made lowercase.
    odcup = models.TextField(db_column='ODCUP', blank=True, null=True)  # Field name made lowercase.
    oscup = models.TextField(db_column='OSCUP', blank=True, null=True)  # Field name made lowercase.
    odmacula = models.TextField(db_column='ODMACULA', blank=True, null=True)  # Field name made lowercase.
    osmacula = models.TextField(db_column='OSMACULA', blank=True, null=True)  # Field name made lowercase.
    odvessels = models.TextField(db_column='ODVESSELS', blank=True, null=True)  # Field name made lowercase.
    osvessels = models.TextField(db_column='OSVESSELS', blank=True, null=True)  # Field name made lowercase.
    odvitreous = models.TextField(db_column='ODVITREOUS', blank=True, null=True)  # Field name made lowercase.
    osvitreous = models.TextField(db_column='OSVITREOUS', blank=True, null=True)  # Field name made lowercase.
    odperiph = models.TextField(db_column='ODPERIPH', blank=True, null=True)  # Field name made lowercase.
    osperiph = models.TextField(db_column='OSPERIPH', blank=True, null=True)  # Field name made lowercase.
    odcmt = models.TextField(db_column='ODCMT', blank=True, null=True)  # Field name made lowercase.
    oscmt = models.TextField(db_column='OSCMT', blank=True, null=True)  # Field name made lowercase.
    retina_comments = models.TextField(db_column='RETINA_COMMENTS', blank=True, null=True)  # Field name made lowercase.
    dil_risks = models.CharField(db_column='DIL_RISKS', max_length=2)  # Field name made lowercase.
    dil_meds = models.TextField(db_column='DIL_MEDS', blank=True, null=True)  # Field name made lowercase.
    wettype = models.CharField(db_column='WETTYPE', max_length=10)  # Field name made lowercase.
    atropine = models.CharField(db_column='ATROPINE', max_length=25)  # Field name made lowercase.
    cyclomydril = models.CharField(db_column='CYCLOMYDRIL', max_length=25)  # Field name made lowercase.
    tropicamide = models.CharField(db_column='TROPICAMIDE', max_length=25)  # Field name made lowercase.
    cyclogyl = models.CharField(db_column='CYCLOGYL', max_length=25)  # Field name made lowercase.
    neo25 = models.CharField(db_column='NEO25', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_postseg'
        unique_together = (('id', 'pid'),)


class FormEyeRefraction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    mrodsph = models.CharField(db_column='MRODSPH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrodcyl = models.CharField(db_column='MRODCYL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrodaxis = models.CharField(db_column='MRODAXIS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrodprism = models.CharField(db_column='MRODPRISM', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrodbase = models.CharField(db_column='MRODBASE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrodadd = models.CharField(db_column='MRODADD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrossph = models.CharField(db_column='MROSSPH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mroscyl = models.CharField(db_column='MROSCYL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrosaxis = models.CharField(db_column='MROSAXIS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrosprism = models.CharField(db_column='MROSPRISM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mrosbase = models.CharField(db_column='MROSBASE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mrosadd = models.CharField(db_column='MROSADD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrodnearsphere = models.CharField(db_column='MRODNEARSPHERE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrodnearcyl = models.CharField(db_column='MRODNEARCYL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrodnearaxis = models.CharField(db_column='MRODNEARAXIS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrodprismnear = models.CharField(db_column='MRODPRISMNEAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mrodbasenear = models.CharField(db_column='MRODBASENEAR', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrosnearshpere = models.CharField(db_column='MROSNEARSHPERE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrosnearcyl = models.CharField(db_column='MROSNEARCYL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mrosnearaxis = models.CharField(db_column='MROSNEARAXIS', max_length=125, blank=True, null=True)  # Field name made lowercase.
    mrosprismnear = models.CharField(db_column='MROSPRISMNEAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mrosbasenear = models.CharField(db_column='MROSBASENEAR', max_length=25, blank=True, null=True)  # Field name made lowercase.
    crodsph = models.CharField(db_column='CRODSPH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    crodcyl = models.CharField(db_column='CRODCYL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    crodaxis = models.CharField(db_column='CRODAXIS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    crossph = models.CharField(db_column='CROSSPH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    croscyl = models.CharField(db_column='CROSCYL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    crosaxis = models.CharField(db_column='CROSAXIS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    crcomments = models.CharField(db_column='CRCOMMENTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    balanced = models.CharField(db_column='BALANCED', max_length=2)  # Field name made lowercase.
    arodsph = models.CharField(db_column='ARODSPH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    arodcyl = models.CharField(db_column='ARODCYL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    arodaxis = models.CharField(db_column='ARODAXIS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    arossph = models.CharField(db_column='AROSSPH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    aroscyl = models.CharField(db_column='AROSCYL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    arosaxis = models.CharField(db_column='AROSAXIS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    arodadd = models.CharField(db_column='ARODADD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    arosadd = models.CharField(db_column='AROSADD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    arnearodva = models.CharField(db_column='ARNEARODVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    arnearosva = models.CharField(db_column='ARNEAROSVA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    arodprism = models.CharField(db_column='ARODPRISM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    arosprism = models.CharField(db_column='AROSPRISM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctlodsph = models.CharField(db_column='CTLODSPH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlodcyl = models.CharField(db_column='CTLODCYL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlodaxis = models.CharField(db_column='CTLODAXIS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlodbc = models.CharField(db_column='CTLODBC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctloddiam = models.CharField(db_column='CTLODDIAM', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlossph = models.CharField(db_column='CTLOSSPH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctloscyl = models.CharField(db_column='CTLOSCYL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlosaxis = models.CharField(db_column='CTLOSAXIS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlosbc = models.CharField(db_column='CTLOSBC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlosdiam = models.CharField(db_column='CTLOSDIAM', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctl_comments = models.TextField(db_column='CTL_COMMENTS', blank=True, null=True)  # Field name made lowercase.
    ctlmanufacturerod = models.CharField(db_column='CTLMANUFACTUREROD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctlsupplierod = models.CharField(db_column='CTLSUPPLIEROD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctlbrandod = models.CharField(db_column='CTLBRANDOD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctlmanufactureros = models.CharField(db_column='CTLMANUFACTUREROS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctlsupplieros = models.CharField(db_column='CTLSUPPLIEROS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctlbrandos = models.CharField(db_column='CTLBRANDOS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctlodadd = models.CharField(db_column='CTLODADD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ctlosadd = models.CharField(db_column='CTLOSADD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nvochecked = models.CharField(db_column='NVOCHECKED', max_length=25, blank=True, null=True)  # Field name made lowercase.
    addchecked = models.CharField(db_column='ADDCHECKED', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_refraction'
        unique_together = (('id', 'pid'),)


class FormEyeRos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    rosgeneral = models.TextField(db_column='ROSGENERAL', blank=True, null=True)  # Field name made lowercase.
    rosheent = models.TextField(db_column='ROSHEENT', blank=True, null=True)  # Field name made lowercase.
    roscv = models.TextField(db_column='ROSCV', blank=True, null=True)  # Field name made lowercase.
    rospulm = models.TextField(db_column='ROSPULM', blank=True, null=True)  # Field name made lowercase.
    rosgi = models.TextField(db_column='ROSGI', blank=True, null=True)  # Field name made lowercase.
    rosgu = models.TextField(db_column='ROSGU', blank=True, null=True)  # Field name made lowercase.
    rosderm = models.TextField(db_column='ROSDERM', blank=True, null=True)  # Field name made lowercase.
    rosneuro = models.TextField(db_column='ROSNEURO', blank=True, null=True)  # Field name made lowercase.
    rospsych = models.TextField(db_column='ROSPSYCH', blank=True, null=True)  # Field name made lowercase.
    rosmusculo = models.TextField(db_column='ROSMUSCULO', blank=True, null=True)  # Field name made lowercase.
    rosimmuno = models.TextField(db_column='ROSIMMUNO', blank=True, null=True)  # Field name made lowercase.
    rosendocrine = models.TextField(db_column='ROSENDOCRINE', blank=True, null=True)  # Field name made lowercase.
    roscomments = models.TextField(db_column='ROSCOMMENTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_ros'
        unique_together = (('id', 'pid'),)


class FormEyeVitals(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pid = models.BigIntegerField(blank=True, null=True)
    alert = models.CharField(max_length=3, blank=True, null=True)
    oriented = models.CharField(max_length=3, blank=True, null=True)
    confused = models.CharField(max_length=3, blank=True, null=True)
    odiopap = models.CharField(db_column='ODIOPAP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osiopap = models.CharField(db_column='OSIOPAP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odioptpn = models.CharField(db_column='ODIOPTPN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osioptpn = models.CharField(db_column='OSIOPTPN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    odiopftn = models.CharField(db_column='ODIOPFTN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    osiopftn = models.CharField(db_column='OSIOPFTN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ioptime = models.TimeField(db_column='IOPTIME')  # Field name made lowercase.
    odioppost = models.CharField(db_column='ODIOPPOST', max_length=10)  # Field name made lowercase.
    osioppost = models.CharField(db_column='OSIOPPOST', max_length=10)  # Field name made lowercase.
    iopposttime = models.TimeField(db_column='IOPPOSTTIME', blank=True, null=True)  # Field name made lowercase.
    odioptarget = models.CharField(db_column='ODIOPTARGET', max_length=10)  # Field name made lowercase.
    osioptarget = models.CharField(db_column='OSIOPTARGET', max_length=10)  # Field name made lowercase.
    amslerod = models.SmallIntegerField(db_column='AMSLEROD', blank=True, null=True)  # Field name made lowercase.
    amsleros = models.SmallIntegerField(db_column='AMSLEROS', blank=True, null=True)  # Field name made lowercase.
    odvf1 = models.IntegerField(db_column='ODVF1', blank=True, null=True)  # Field name made lowercase.
    odvf2 = models.IntegerField(db_column='ODVF2', blank=True, null=True)  # Field name made lowercase.
    odvf3 = models.IntegerField(db_column='ODVF3', blank=True, null=True)  # Field name made lowercase.
    odvf4 = models.IntegerField(db_column='ODVF4', blank=True, null=True)  # Field name made lowercase.
    osvf1 = models.IntegerField(db_column='OSVF1', blank=True, null=True)  # Field name made lowercase.
    osvf2 = models.IntegerField(db_column='OSVF2', blank=True, null=True)  # Field name made lowercase.
    osvf3 = models.IntegerField(db_column='OSVF3', blank=True, null=True)  # Field name made lowercase.
    osvf4 = models.IntegerField(db_column='OSVF4', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_eye_vitals'
        unique_together = (('id', 'pid'),)


class FormFunctionalCognitiveStatus(models.Model):
    id = models.BigIntegerField()
    date = models.DateField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    encounter = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    codetext = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    external_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_functional_cognitive_status'


class FormGroupAttendance(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    encounter_id = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_group_attendance'


class FormGroupsEncounter(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    facility = models.TextField(blank=True, null=True)
    facility_id = models.IntegerField()
    group_id = models.BigIntegerField(blank=True, null=True)
    encounter = models.BigIntegerField(blank=True, null=True)
    onset_date = models.DateTimeField(blank=True, null=True)
    sensitivity = models.CharField(max_length=30, blank=True, null=True)
    billing_note = models.TextField(blank=True, null=True)
    pc_catid = models.IntegerField()
    last_level_billed = models.IntegerField()
    last_level_closed = models.IntegerField()
    last_stmt_date = models.DateField(blank=True, null=True)
    stmt_count = models.IntegerField()
    provider_id = models.IntegerField(blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    invoice_refno = models.CharField(max_length=31)
    referral_source = models.CharField(max_length=31)
    billing_facility = models.IntegerField()
    external_id = models.CharField(max_length=20, blank=True, null=True)
    pos_code = models.IntegerField(blank=True, null=True)
    counselors = models.CharField(max_length=255, blank=True, null=True)
    appt_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_groups_encounter'


class FormMiscBillingOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    employment_related = models.IntegerField(blank=True, null=True)
    auto_accident = models.IntegerField(blank=True, null=True)
    accident_state = models.CharField(max_length=2, blank=True, null=True)
    other_accident = models.IntegerField(blank=True, null=True)
    medicaid_referral_code = models.CharField(max_length=2, blank=True, null=True)
    epsdt_flag = models.IntegerField(blank=True, null=True)
    provider_qualifier_code = models.CharField(max_length=2, blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    outside_lab = models.IntegerField(blank=True, null=True)
    lab_amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    is_unable_to_work = models.IntegerField(blank=True, null=True)
    onset_date = models.DateField(blank=True, null=True)
    date_initial_treatment = models.DateField(blank=True, null=True)
    off_work_from = models.DateField(blank=True, null=True)
    off_work_to = models.DateField(blank=True, null=True)
    is_hospitalized = models.IntegerField(blank=True, null=True)
    hospitalization_date_from = models.DateField(blank=True, null=True)
    hospitalization_date_to = models.DateField(blank=True, null=True)
    medicaid_resubmission_code = models.CharField(max_length=10, blank=True, null=True)
    medicaid_original_reference = models.CharField(max_length=15, blank=True, null=True)
    prior_auth_number = models.CharField(max_length=20, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    replacement_claim = models.IntegerField(blank=True, null=True)
    icn_resubmission_number = models.CharField(max_length=35, blank=True, null=True)
    box_14_date_qual = models.CharField(max_length=3, blank=True, null=True)
    box_15_date_qual = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_misc_billing_options'


class FormObservation(models.Model):
    id = models.BigIntegerField()
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    encounter = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    observation = models.CharField(max_length=255, blank=True, null=True)
    ob_value = models.CharField(max_length=255, blank=True, null=True)
    ob_unit = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    code_type = models.CharField(max_length=255, blank=True, null=True)
    table_code = models.CharField(max_length=255, blank=True, null=True)
    ob_code = models.CharField(max_length=64, blank=True, null=True)
    ob_type = models.CharField(max_length=64, blank=True, null=True)
    ob_status = models.CharField(max_length=32, blank=True, null=True)
    result_status = models.CharField(max_length=32, blank=True, null=True)
    ob_reason_status = models.CharField(max_length=32, blank=True, null=True)
    ob_reason_code = models.CharField(max_length=64, blank=True, null=True)
    ob_reason_text = models.TextField(blank=True, null=True)
    ob_documentationof_table = models.CharField(max_length=255, blank=True, null=True)
    ob_documentationof_table_id = models.BigIntegerField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_observation'


class FormReviewofs(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    fever = models.CharField(max_length=5, blank=True, null=True)
    chills = models.CharField(max_length=5, blank=True, null=True)
    night_sweats = models.CharField(max_length=5, blank=True, null=True)
    weight_loss = models.CharField(max_length=5, blank=True, null=True)
    poor_appetite = models.CharField(max_length=5, blank=True, null=True)
    insomnia = models.CharField(max_length=5, blank=True, null=True)
    fatigued = models.CharField(max_length=5, blank=True, null=True)
    depressed = models.CharField(max_length=5, blank=True, null=True)
    hyperactive = models.CharField(max_length=5, blank=True, null=True)
    exposure_to_foreign_countries = models.CharField(max_length=5, blank=True, null=True)
    cataracts = models.CharField(max_length=5, blank=True, null=True)
    cataract_surgery = models.CharField(max_length=5, blank=True, null=True)
    glaucoma = models.CharField(max_length=5, blank=True, null=True)
    double_vision = models.CharField(max_length=5, blank=True, null=True)
    blurred_vision = models.CharField(max_length=5, blank=True, null=True)
    poor_hearing = models.CharField(max_length=5, blank=True, null=True)
    headaches = models.CharField(max_length=5, blank=True, null=True)
    ringing_in_ears = models.CharField(max_length=5, blank=True, null=True)
    bloody_nose = models.CharField(max_length=5, blank=True, null=True)
    sinusitis = models.CharField(max_length=5, blank=True, null=True)
    sinus_surgery = models.CharField(max_length=5, blank=True, null=True)
    dry_mouth = models.CharField(max_length=5, blank=True, null=True)
    strep_throat = models.CharField(max_length=5, blank=True, null=True)
    tonsillectomy = models.CharField(max_length=5, blank=True, null=True)
    swollen_lymph_nodes = models.CharField(max_length=5, blank=True, null=True)
    throat_cancer = models.CharField(max_length=5, blank=True, null=True)
    throat_cancer_surgery = models.CharField(max_length=5, blank=True, null=True)
    heart_attack = models.CharField(max_length=5, blank=True, null=True)
    irregular_heart_beat = models.CharField(max_length=5, blank=True, null=True)
    chest_pains = models.CharField(max_length=5, blank=True, null=True)
    shortness_of_breath = models.CharField(max_length=5, blank=True, null=True)
    high_blood_pressure = models.CharField(max_length=5, blank=True, null=True)
    heart_failure = models.CharField(max_length=5, blank=True, null=True)
    poor_circulation = models.CharField(max_length=5, blank=True, null=True)
    vascular_surgery = models.CharField(max_length=5, blank=True, null=True)
    cardiac_catheterization = models.CharField(max_length=5, blank=True, null=True)
    coronary_artery_bypass = models.CharField(max_length=5, blank=True, null=True)
    heart_transplant = models.CharField(max_length=5, blank=True, null=True)
    stress_test = models.CharField(max_length=5, blank=True, null=True)
    emphysema = models.CharField(max_length=5, blank=True, null=True)
    chronic_bronchitis = models.CharField(max_length=5, blank=True, null=True)
    interstitial_lung_disease = models.CharField(max_length=5, blank=True, null=True)
    shortness_of_breath_2 = models.CharField(max_length=5, blank=True, null=True)
    lung_cancer = models.CharField(max_length=5, blank=True, null=True)
    lung_cancer_surgery = models.CharField(max_length=5, blank=True, null=True)
    pheumothorax = models.CharField(max_length=5, blank=True, null=True)
    stomach_pains = models.CharField(max_length=5, blank=True, null=True)
    peptic_ulcer_disease = models.CharField(max_length=5, blank=True, null=True)
    gastritis = models.CharField(max_length=5, blank=True, null=True)
    endoscopy = models.CharField(max_length=5, blank=True, null=True)
    polyps = models.CharField(max_length=5, blank=True, null=True)
    colonoscopy = models.CharField(max_length=5, blank=True, null=True)
    colon_cancer = models.CharField(max_length=5, blank=True, null=True)
    colon_cancer_surgery = models.CharField(max_length=5, blank=True, null=True)
    ulcerative_colitis = models.CharField(max_length=5, blank=True, null=True)
    crohns_disease = models.CharField(max_length=5, blank=True, null=True)
    appendectomy = models.CharField(max_length=5, blank=True, null=True)
    divirticulitis = models.CharField(max_length=5, blank=True, null=True)
    divirticulitis_surgery = models.CharField(max_length=5, blank=True, null=True)
    gall_stones = models.CharField(max_length=5, blank=True, null=True)
    cholecystectomy = models.CharField(max_length=5, blank=True, null=True)
    hepatitis = models.CharField(max_length=5, blank=True, null=True)
    cirrhosis_of_the_liver = models.CharField(max_length=5, blank=True, null=True)
    splenectomy = models.CharField(max_length=5, blank=True, null=True)
    kidney_failure = models.CharField(max_length=5, blank=True, null=True)
    kidney_stones = models.CharField(max_length=5, blank=True, null=True)
    kidney_cancer = models.CharField(max_length=5, blank=True, null=True)
    kidney_infections = models.CharField(max_length=5, blank=True, null=True)
    bladder_infections = models.CharField(max_length=5, blank=True, null=True)
    bladder_cancer = models.CharField(max_length=5, blank=True, null=True)
    prostate_problems = models.CharField(max_length=5, blank=True, null=True)
    prostate_cancer = models.CharField(max_length=5, blank=True, null=True)
    kidney_transplant = models.CharField(max_length=5, blank=True, null=True)
    sexually_transmitted_disease = models.CharField(max_length=5, blank=True, null=True)
    burning_with_urination = models.CharField(max_length=5, blank=True, null=True)
    discharge_from_urethra = models.CharField(max_length=5, blank=True, null=True)
    rashes = models.CharField(max_length=5, blank=True, null=True)
    infections = models.CharField(max_length=5, blank=True, null=True)
    ulcerations = models.CharField(max_length=5, blank=True, null=True)
    pemphigus = models.CharField(max_length=5, blank=True, null=True)
    herpes = models.CharField(max_length=5, blank=True, null=True)
    osetoarthritis = models.CharField(max_length=5, blank=True, null=True)
    rheumotoid_arthritis = models.CharField(max_length=5, blank=True, null=True)
    lupus = models.CharField(max_length=5, blank=True, null=True)
    ankylosing_sondlilitis = models.CharField(max_length=5, blank=True, null=True)
    swollen_joints = models.CharField(max_length=5, blank=True, null=True)
    stiff_joints = models.CharField(max_length=5, blank=True, null=True)
    broken_bones = models.CharField(max_length=5, blank=True, null=True)
    neck_problems = models.CharField(max_length=5, blank=True, null=True)
    back_problems = models.CharField(max_length=5, blank=True, null=True)
    back_surgery = models.CharField(max_length=5, blank=True, null=True)
    scoliosis = models.CharField(max_length=5, blank=True, null=True)
    herniated_disc = models.CharField(max_length=5, blank=True, null=True)
    shoulder_problems = models.CharField(max_length=5, blank=True, null=True)
    elbow_problems = models.CharField(max_length=5, blank=True, null=True)
    wrist_problems = models.CharField(max_length=5, blank=True, null=True)
    hand_problems = models.CharField(max_length=5, blank=True, null=True)
    hip_problems = models.CharField(max_length=5, blank=True, null=True)
    knee_problems = models.CharField(max_length=5, blank=True, null=True)
    ankle_problems = models.CharField(max_length=5, blank=True, null=True)
    foot_problems = models.CharField(max_length=5, blank=True, null=True)
    insulin_dependent_diabetes = models.CharField(max_length=5, blank=True, null=True)
    noninsulin_dependent_diabetes = models.CharField(max_length=5, blank=True, null=True)
    hypothyroidism = models.CharField(max_length=5, blank=True, null=True)
    hyperthyroidism = models.CharField(max_length=5, blank=True, null=True)
    cushing_syndrom = models.CharField(max_length=5, blank=True, null=True)
    addison_syndrom = models.CharField(max_length=5, blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_reviewofs'


class FormRos(models.Model):
    pid = models.BigIntegerField()
    activity = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)
    weight_change = models.CharField(max_length=3, blank=True, null=True)
    weakness = models.CharField(max_length=3, blank=True, null=True)
    fatigue = models.CharField(max_length=3, blank=True, null=True)
    anorexia = models.CharField(max_length=3, blank=True, null=True)
    fever = models.CharField(max_length=3, blank=True, null=True)
    chills = models.CharField(max_length=3, blank=True, null=True)
    night_sweats = models.CharField(max_length=3, blank=True, null=True)
    insomnia = models.CharField(max_length=3, blank=True, null=True)
    irritability = models.CharField(max_length=3, blank=True, null=True)
    heat_or_cold = models.CharField(max_length=3, blank=True, null=True)
    intolerance = models.CharField(max_length=3, blank=True, null=True)
    change_in_vision = models.CharField(max_length=3, blank=True, null=True)
    glaucoma_history = models.CharField(max_length=3, blank=True, null=True)
    eye_pain = models.CharField(max_length=3, blank=True, null=True)
    irritation = models.CharField(max_length=3, blank=True, null=True)
    redness = models.CharField(max_length=3, blank=True, null=True)
    excessive_tearing = models.CharField(max_length=3, blank=True, null=True)
    double_vision = models.CharField(max_length=3, blank=True, null=True)
    blind_spots = models.CharField(max_length=3, blank=True, null=True)
    photophobia = models.CharField(max_length=3, blank=True, null=True)
    hearing_loss = models.CharField(max_length=3, blank=True, null=True)
    discharge = models.CharField(max_length=3, blank=True, null=True)
    pain = models.CharField(max_length=3, blank=True, null=True)
    vertigo = models.CharField(max_length=3, blank=True, null=True)
    tinnitus = models.CharField(max_length=3, blank=True, null=True)
    frequent_colds = models.CharField(max_length=3, blank=True, null=True)
    sore_throat = models.CharField(max_length=3, blank=True, null=True)
    sinus_problems = models.CharField(max_length=3, blank=True, null=True)
    post_nasal_drip = models.CharField(max_length=3, blank=True, null=True)
    nosebleed = models.CharField(max_length=3, blank=True, null=True)
    snoring = models.CharField(max_length=3, blank=True, null=True)
    apnea = models.CharField(max_length=3, blank=True, null=True)
    breast_mass = models.CharField(max_length=3, blank=True, null=True)
    breast_discharge = models.CharField(max_length=3, blank=True, null=True)
    biopsy = models.CharField(max_length=3, blank=True, null=True)
    abnormal_mammogram = models.CharField(max_length=3, blank=True, null=True)
    cough = models.CharField(max_length=3, blank=True, null=True)
    sputum = models.CharField(max_length=3, blank=True, null=True)
    shortness_of_breath = models.CharField(max_length=3, blank=True, null=True)
    wheezing = models.CharField(max_length=3, blank=True, null=True)
    hemoptsyis = models.CharField(max_length=3, blank=True, null=True)
    asthma = models.CharField(max_length=3, blank=True, null=True)
    copd = models.CharField(max_length=3, blank=True, null=True)
    chest_pain = models.CharField(max_length=3, blank=True, null=True)
    palpitation = models.CharField(max_length=3, blank=True, null=True)
    syncope = models.CharField(max_length=3, blank=True, null=True)
    pnd = models.CharField(max_length=3, blank=True, null=True)
    doe = models.CharField(max_length=3, blank=True, null=True)
    orthopnea = models.CharField(max_length=3, blank=True, null=True)
    peripheal = models.CharField(max_length=3, blank=True, null=True)
    edema = models.CharField(max_length=3, blank=True, null=True)
    legpain_cramping = models.CharField(max_length=3, blank=True, null=True)
    history_murmur = models.CharField(max_length=3, blank=True, null=True)
    arrythmia = models.CharField(max_length=3, blank=True, null=True)
    heart_problem = models.CharField(max_length=3, blank=True, null=True)
    dysphagia = models.CharField(max_length=3, blank=True, null=True)
    heartburn = models.CharField(max_length=3, blank=True, null=True)
    bloating = models.CharField(max_length=3, blank=True, null=True)
    belching = models.CharField(max_length=3, blank=True, null=True)
    flatulence = models.CharField(max_length=3, blank=True, null=True)
    nausea = models.CharField(max_length=3, blank=True, null=True)
    vomiting = models.CharField(max_length=3, blank=True, null=True)
    hematemesis = models.CharField(max_length=3, blank=True, null=True)
    gastro_pain = models.CharField(max_length=3, blank=True, null=True)
    food_intolerance = models.CharField(max_length=3, blank=True, null=True)
    hepatitis = models.CharField(max_length=3, blank=True, null=True)
    jaundice = models.CharField(max_length=3, blank=True, null=True)
    hematochezia = models.CharField(max_length=3, blank=True, null=True)
    changed_bowel = models.CharField(max_length=3, blank=True, null=True)
    diarrhea = models.CharField(max_length=3, blank=True, null=True)
    constipation = models.CharField(max_length=3, blank=True, null=True)
    polyuria = models.CharField(max_length=3, blank=True, null=True)
    polydypsia = models.CharField(max_length=3, blank=True, null=True)
    dysuria = models.CharField(max_length=3, blank=True, null=True)
    hematuria = models.CharField(max_length=3, blank=True, null=True)
    frequency = models.CharField(max_length=3, blank=True, null=True)
    urgency = models.CharField(max_length=3, blank=True, null=True)
    incontinence = models.CharField(max_length=3, blank=True, null=True)
    renal_stones = models.CharField(max_length=3, blank=True, null=True)
    utis = models.CharField(max_length=3, blank=True, null=True)
    hesitancy = models.CharField(max_length=3, blank=True, null=True)
    dribbling = models.CharField(max_length=3, blank=True, null=True)
    stream = models.CharField(max_length=3, blank=True, null=True)
    nocturia = models.CharField(max_length=3, blank=True, null=True)
    erections = models.CharField(max_length=3, blank=True, null=True)
    ejaculations = models.CharField(max_length=3, blank=True, null=True)
    g = models.CharField(max_length=3, blank=True, null=True)
    p = models.CharField(max_length=3, blank=True, null=True)
    ap = models.CharField(max_length=3, blank=True, null=True)
    lc = models.CharField(max_length=3, blank=True, null=True)
    mearche = models.CharField(max_length=3, blank=True, null=True)
    menopause = models.CharField(max_length=3, blank=True, null=True)
    lmp = models.CharField(max_length=3, blank=True, null=True)
    f_frequency = models.CharField(max_length=3, blank=True, null=True)
    f_flow = models.CharField(max_length=3, blank=True, null=True)
    f_symptoms = models.CharField(max_length=3, blank=True, null=True)
    abnormal_hair_growth = models.CharField(max_length=3, blank=True, null=True)
    f_hirsutism = models.CharField(max_length=3, blank=True, null=True)
    joint_pain = models.CharField(max_length=3, blank=True, null=True)
    swelling = models.CharField(max_length=3, blank=True, null=True)
    m_redness = models.CharField(max_length=3, blank=True, null=True)
    m_warm = models.CharField(max_length=3, blank=True, null=True)
    m_stiffness = models.CharField(max_length=3, blank=True, null=True)
    muscle = models.CharField(max_length=3, blank=True, null=True)
    m_aches = models.CharField(max_length=3, blank=True, null=True)
    fms = models.CharField(max_length=3, blank=True, null=True)
    arthritis = models.CharField(max_length=3, blank=True, null=True)
    loc = models.CharField(max_length=3, blank=True, null=True)
    seizures = models.CharField(max_length=3, blank=True, null=True)
    stroke = models.CharField(max_length=3, blank=True, null=True)
    tia = models.CharField(max_length=3, blank=True, null=True)
    n_numbness = models.CharField(max_length=3, blank=True, null=True)
    n_weakness = models.CharField(max_length=3, blank=True, null=True)
    paralysis = models.CharField(max_length=3, blank=True, null=True)
    intellectual_decline = models.CharField(max_length=3, blank=True, null=True)
    memory_problems = models.CharField(max_length=3, blank=True, null=True)
    dementia = models.CharField(max_length=3, blank=True, null=True)
    n_headache = models.CharField(max_length=3, blank=True, null=True)
    s_cancer = models.CharField(max_length=3, blank=True, null=True)
    psoriasis = models.CharField(max_length=3, blank=True, null=True)
    s_acne = models.CharField(max_length=3, blank=True, null=True)
    s_other = models.CharField(max_length=3, blank=True, null=True)
    s_disease = models.CharField(max_length=3, blank=True, null=True)
    p_diagnosis = models.CharField(max_length=3, blank=True, null=True)
    p_medication = models.CharField(max_length=3, blank=True, null=True)
    depression = models.CharField(max_length=3, blank=True, null=True)
    anxiety = models.CharField(max_length=3, blank=True, null=True)
    social_difficulties = models.CharField(max_length=3, blank=True, null=True)
    thyroid_problems = models.CharField(max_length=3, blank=True, null=True)
    diabetes = models.CharField(max_length=3, blank=True, null=True)
    abnormal_blood = models.CharField(max_length=3, blank=True, null=True)
    anemia = models.CharField(max_length=3, blank=True, null=True)
    fh_blood_problems = models.CharField(max_length=3, blank=True, null=True)
    bleeding_problems = models.CharField(max_length=3, blank=True, null=True)
    allergies = models.CharField(max_length=3, blank=True, null=True)
    frequent_illness = models.CharField(max_length=3, blank=True, null=True)
    hiv = models.CharField(max_length=3, blank=True, null=True)
    hai_status = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_ros'


class FormSoap(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    subjective = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    assessment = models.TextField(blank=True, null=True)
    plan = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_soap'


class FormTaskman(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    req_date = models.DateTimeField(db_column='REQ_DATE')  # Field name made lowercase.
    from_id = models.BigIntegerField(db_column='FROM_ID')  # Field name made lowercase.
    to_id = models.BigIntegerField(db_column='TO_ID')  # Field name made lowercase.
    patient_id = models.BigIntegerField(db_column='PATIENT_ID')  # Field name made lowercase.
    doc_type = models.CharField(db_column='DOC_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    doc_id = models.BigIntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    enc_id = models.BigIntegerField(db_column='ENC_ID', blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(db_column='METHOD', max_length=20)  # Field name made lowercase.
    completed = models.CharField(db_column='COMPLETED', max_length=1, blank=True, null=True)  # Field name made lowercase.
    completed_date = models.DateTimeField(db_column='COMPLETED_DATE', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='COMMENT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    userfield_1 = models.CharField(db_column='USERFIELD_1', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'form_taskman'


class FormVitalDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    form_id = models.BigIntegerField()
    vitals_column = models.CharField(max_length=64)
    interpretation_list_id = models.CharField(max_length=100, blank=True, null=True)
    interpretation_option_id = models.CharField(max_length=100, blank=True, null=True)
    interpretation_codes = models.CharField(max_length=255, blank=True, null=True)
    interpretation_title = models.CharField(max_length=255, blank=True, null=True)
    reason_code = models.CharField(max_length=31, blank=True, null=True)
    reason_description = models.TextField(blank=True, null=True)
    reason_status = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_vital_details'


class FormVitals(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    bps = models.CharField(max_length=40, blank=True, null=True)
    bpd = models.CharField(max_length=40, blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    height = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    temperature = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    temp_method = models.CharField(max_length=255, blank=True, null=True)
    pulse = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    respiration = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    bmi = models.DecimalField(db_column='BMI', max_digits=12, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    bmi_status = models.CharField(db_column='BMI_status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    waist_circ = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    head_circ = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    oxygen_saturation = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    oxygen_flow_rate = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    external_id = models.CharField(max_length=20, blank=True, null=True)
    ped_weight_height = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ped_bmi = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ped_head_circ = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    inhaled_oxygen_concentration = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'form_vitals'


class Forms(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    encounter = models.BigIntegerField(blank=True, null=True)
    form_name = models.TextField(blank=True, null=True)
    form_id = models.BigIntegerField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField()
    formdir = models.TextField(blank=True, null=True)
    therapy_group_id = models.IntegerField(blank=True, null=True)
    issue_id = models.BigIntegerField()
    provider_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'forms'


class GaclAcl(models.Model):
    id = models.IntegerField(primary_key=True)
    section_value = models.CharField(max_length=150)
    allow = models.IntegerField()
    enabled = models.IntegerField()
    return_value = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    updated_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_acl'


class GaclAclSections(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(unique=True, max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=230)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_acl_sections'


class GaclAclSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_acl_seq'


class GaclAco(models.Model):
    id = models.IntegerField(primary_key=True)
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=255)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aco'
        unique_together = (('section_value', 'value'),)


class GaclAcoMap(models.Model):
    acl_id = models.IntegerField(primary_key=True)
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_aco_map'
        unique_together = (('acl_id', 'section_value', 'value'),)


class GaclAcoSections(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(unique=True, max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=230)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aco_sections'


class GaclAcoSectionsSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aco_sections_seq'


class GaclAcoSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aco_seq'


class GaclAro(models.Model):
    id = models.IntegerField(primary_key=True)
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=255)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro'
        unique_together = (('section_value', 'value'),)


class GaclAroGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_aro_groups'
        unique_together = (('id', 'value'),)


class GaclAroGroupsIdSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro_groups_id_seq'


class GaclAroGroupsMap(models.Model):
    acl_id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro_groups_map'
        unique_together = (('acl_id', 'group_id'),)


class GaclAroMap(models.Model):
    acl_id = models.IntegerField(primary_key=True)
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_aro_map'
        unique_together = (('acl_id', 'section_value', 'value'),)


class GaclAroSections(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(unique=True, max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=230)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro_sections'


class GaclAroSectionsSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro_sections_seq'


class GaclAroSeq(models.Model):
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_aro_seq'


class GaclAxo(models.Model):
    id = models.IntegerField(primary_key=True)
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=255)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_axo'
        unique_together = (('section_value', 'value'),)


class GaclAxoGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    lft = models.IntegerField()
    rgt = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_axo_groups'
        unique_together = (('id', 'value'),)


class GaclAxoGroupsMap(models.Model):
    acl_id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_axo_groups_map'
        unique_together = (('acl_id', 'group_id'),)


class GaclAxoMap(models.Model):
    acl_id = models.IntegerField(primary_key=True)
    section_value = models.CharField(max_length=150)
    value = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_axo_map'
        unique_together = (('acl_id', 'section_value', 'value'),)


class GaclAxoSections(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(unique=True, max_length=150)
    order_value = models.IntegerField()
    name = models.CharField(max_length=230)
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_axo_sections'


class GaclGroupsAroMap(models.Model):
    group_id = models.IntegerField(primary_key=True)
    aro_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_groups_aro_map'
        unique_together = (('group_id', 'aro_id'),)


class GaclGroupsAxoMap(models.Model):
    group_id = models.IntegerField(primary_key=True)
    axo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gacl_groups_axo_map'
        unique_together = (('group_id', 'axo_id'),)


class GaclPhpgacl(models.Model):
    name = models.CharField(primary_key=True, max_length=230)
    value = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'gacl_phpgacl'


class Globals(models.Model):
    gl_name = models.CharField(primary_key=True, max_length=63)
    gl_index = models.IntegerField()
    gl_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'globals'
        unique_together = (('gl_name', 'gl_index'),)


class Gprelations(models.Model):
    type1 = models.IntegerField(primary_key=True)
    id1 = models.BigIntegerField()
    type2 = models.IntegerField()
    id2 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'gprelations'
        unique_together = (('type1', 'id1', 'type2', 'id2'),)


class Groups(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    user = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class HistoryData(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    coffee = models.TextField(blank=True, null=True)
    tobacco = models.TextField(blank=True, null=True)
    alcohol = models.TextField(blank=True, null=True)
    sleep_patterns = models.TextField(blank=True, null=True)
    exercise_patterns = models.TextField(blank=True, null=True)
    seatbelt_use = models.TextField(blank=True, null=True)
    counseling = models.TextField(blank=True, null=True)
    hazardous_activities = models.TextField(blank=True, null=True)
    recreational_drugs = models.TextField(blank=True, null=True)
    last_breast_exam = models.CharField(max_length=255, blank=True, null=True)
    last_mammogram = models.CharField(max_length=255, blank=True, null=True)
    last_gynocological_exam = models.CharField(max_length=255, blank=True, null=True)
    last_rectal_exam = models.CharField(max_length=255, blank=True, null=True)
    last_prostate_exam = models.CharField(max_length=255, blank=True, null=True)
    last_physical_exam = models.CharField(max_length=255, blank=True, null=True)
    last_sigmoidoscopy_colonoscopy = models.CharField(max_length=255, blank=True, null=True)
    last_ecg = models.CharField(max_length=255, blank=True, null=True)
    last_cardiac_echo = models.CharField(max_length=255, blank=True, null=True)
    last_retinal = models.CharField(max_length=255, blank=True, null=True)
    last_fluvax = models.CharField(max_length=255, blank=True, null=True)
    last_pneuvax = models.CharField(max_length=255, blank=True, null=True)
    last_ldl = models.CharField(max_length=255, blank=True, null=True)
    last_hemoglobin = models.CharField(max_length=255, blank=True, null=True)
    last_psa = models.CharField(max_length=255, blank=True, null=True)
    last_exam_results = models.CharField(max_length=255, blank=True, null=True)
    history_mother = models.TextField(blank=True, null=True)
    dc_mother = models.TextField(blank=True, null=True)
    history_father = models.TextField(blank=True, null=True)
    dc_father = models.TextField(blank=True, null=True)
    history_siblings = models.TextField(blank=True, null=True)
    dc_siblings = models.TextField(blank=True, null=True)
    history_offspring = models.TextField(blank=True, null=True)
    dc_offspring = models.TextField(blank=True, null=True)
    history_spouse = models.TextField(blank=True, null=True)
    dc_spouse = models.TextField(blank=True, null=True)
    relatives_cancer = models.TextField(blank=True, null=True)
    relatives_tuberculosis = models.TextField(blank=True, null=True)
    relatives_diabetes = models.TextField(blank=True, null=True)
    relatives_high_blood_pressure = models.TextField(blank=True, null=True)
    relatives_heart_problems = models.TextField(blank=True, null=True)
    relatives_stroke = models.TextField(blank=True, null=True)
    relatives_epilepsy = models.TextField(blank=True, null=True)
    relatives_mental_illness = models.TextField(blank=True, null=True)
    relatives_suicide = models.TextField(blank=True, null=True)
    cataract_surgery = models.DateTimeField(blank=True, null=True)
    tonsillectomy = models.DateTimeField(blank=True, null=True)
    cholecystestomy = models.DateTimeField(blank=True, null=True)
    heart_surgery = models.DateTimeField(blank=True, null=True)
    hysterectomy = models.DateTimeField(blank=True, null=True)
    hernia_repair = models.DateTimeField(blank=True, null=True)
    hip_replacement = models.DateTimeField(blank=True, null=True)
    knee_replacement = models.DateTimeField(blank=True, null=True)
    appendectomy = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField()
    name_1 = models.CharField(max_length=255, blank=True, null=True)
    value_1 = models.CharField(max_length=255, blank=True, null=True)
    name_2 = models.CharField(max_length=255, blank=True, null=True)
    value_2 = models.CharField(max_length=255, blank=True, null=True)
    additional_history = models.TextField(blank=True, null=True)
    exams = models.TextField(blank=True, null=True)
    usertext11 = models.TextField(blank=True, null=True)
    usertext12 = models.CharField(max_length=255)
    usertext13 = models.CharField(max_length=255)
    usertext14 = models.CharField(max_length=255)
    usertext15 = models.CharField(max_length=255)
    usertext16 = models.CharField(max_length=255)
    usertext17 = models.CharField(max_length=255)
    usertext18 = models.CharField(max_length=255)
    usertext19 = models.CharField(max_length=255)
    usertext20 = models.CharField(max_length=255)
    usertext21 = models.CharField(max_length=255)
    usertext22 = models.CharField(max_length=255)
    usertext23 = models.CharField(max_length=255)
    usertext24 = models.CharField(max_length=255)
    usertext25 = models.CharField(max_length=255)
    usertext26 = models.CharField(max_length=255)
    usertext27 = models.CharField(max_length=255)
    usertext28 = models.CharField(max_length=255)
    usertext29 = models.CharField(max_length=255)
    usertext30 = models.CharField(max_length=255)
    userdate11 = models.DateField(blank=True, null=True)
    userdate12 = models.DateField(blank=True, null=True)
    userdate13 = models.DateField(blank=True, null=True)
    userdate14 = models.DateField(blank=True, null=True)
    userdate15 = models.DateField(blank=True, null=True)
    userarea11 = models.TextField(blank=True, null=True)
    userarea12 = models.TextField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'history_data'


class Icd10DxOrderCode(models.Model):
    dx_id = models.BigAutoField(unique=True)
    dx_code = models.CharField(max_length=7, blank=True, null=True)
    formatted_dx_code = models.CharField(max_length=10, blank=True, null=True)
    valid_for_coding = models.CharField(max_length=1, blank=True, null=True)
    short_desc = models.CharField(max_length=60, blank=True, null=True)
    long_desc = models.TextField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_dx_order_code'


class Icd10GemDx109(models.Model):
    map_id = models.BigAutoField(unique=True)
    dx_icd10_source = models.CharField(max_length=7, blank=True, null=True)
    dx_icd9_target = models.CharField(max_length=5, blank=True, null=True)
    flags = models.CharField(max_length=5, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_gem_dx_10_9'


class Icd10GemDx910(models.Model):
    map_id = models.BigAutoField(unique=True)
    dx_icd9_source = models.CharField(max_length=5, blank=True, null=True)
    dx_icd10_target = models.CharField(max_length=7, blank=True, null=True)
    flags = models.CharField(max_length=5, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_gem_dx_9_10'


class Icd10GemPcs109(models.Model):
    map_id = models.BigAutoField(unique=True)
    pcs_icd10_source = models.CharField(max_length=7, blank=True, null=True)
    pcs_icd9_target = models.CharField(max_length=5, blank=True, null=True)
    flags = models.CharField(max_length=5, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_gem_pcs_10_9'


class Icd10GemPcs910(models.Model):
    map_id = models.BigAutoField(unique=True)
    pcs_icd9_source = models.CharField(max_length=5, blank=True, null=True)
    pcs_icd10_target = models.CharField(max_length=7, blank=True, null=True)
    flags = models.CharField(max_length=5, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_gem_pcs_9_10'


class Icd10PcsOrderCode(models.Model):
    pcs_id = models.BigAutoField(unique=True)
    pcs_code = models.CharField(max_length=7, blank=True, null=True)
    valid_for_coding = models.CharField(max_length=1, blank=True, null=True)
    short_desc = models.CharField(max_length=60, blank=True, null=True)
    long_desc = models.TextField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_pcs_order_code'


class Icd10ReimbrDx910(models.Model):
    map_id = models.BigAutoField(unique=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    code_cnt = models.IntegerField(blank=True, null=True)
    icd9_01 = models.CharField(db_column='ICD9_01', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_02 = models.CharField(db_column='ICD9_02', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_03 = models.CharField(db_column='ICD9_03', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_04 = models.CharField(db_column='ICD9_04', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_05 = models.CharField(db_column='ICD9_05', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_06 = models.CharField(db_column='ICD9_06', max_length=5, blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_reimbr_dx_9_10'


class Icd10ReimbrPcs910(models.Model):
    map_id = models.BigAutoField(unique=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    code_cnt = models.IntegerField(blank=True, null=True)
    icd9_01 = models.CharField(db_column='ICD9_01', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_02 = models.CharField(db_column='ICD9_02', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_03 = models.CharField(db_column='ICD9_03', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_04 = models.CharField(db_column='ICD9_04', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_05 = models.CharField(db_column='ICD9_05', max_length=5, blank=True, null=True)  # Field name made lowercase.
    icd9_06 = models.CharField(db_column='ICD9_06', max_length=5, blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd10_reimbr_pcs_9_10'


class Icd9DxCode(models.Model):
    dx_id = models.BigAutoField(unique=True)
    dx_code = models.CharField(max_length=5, blank=True, null=True)
    formatted_dx_code = models.CharField(max_length=6, blank=True, null=True)
    short_desc = models.CharField(max_length=60, blank=True, null=True)
    long_desc = models.CharField(max_length=300, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd9_dx_code'


class Icd9DxLongCode(models.Model):
    dx_id = models.BigAutoField(unique=True)
    dx_code = models.CharField(max_length=5, blank=True, null=True)
    long_desc = models.CharField(max_length=300, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd9_dx_long_code'


class Icd9SgCode(models.Model):
    sg_id = models.BigAutoField(unique=True)
    sg_code = models.CharField(max_length=5, blank=True, null=True)
    formatted_sg_code = models.CharField(max_length=6, blank=True, null=True)
    short_desc = models.CharField(max_length=60, blank=True, null=True)
    long_desc = models.CharField(max_length=300, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd9_sg_code'


class Icd9SgLongCode(models.Model):
    sq_id = models.BigAutoField(unique=True)
    sg_code = models.CharField(max_length=5, blank=True, null=True)
    long_desc = models.CharField(max_length=300, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd9_sg_long_code'


class ImmunizationObservation(models.Model):
    imo_id = models.AutoField(primary_key=True)
    imo_im_id = models.IntegerField()
    imo_pid = models.IntegerField(blank=True, null=True)
    imo_criteria = models.CharField(max_length=255, blank=True, null=True)
    imo_criteria_value = models.CharField(max_length=255, blank=True, null=True)
    imo_user = models.IntegerField(blank=True, null=True)
    imo_code = models.CharField(max_length=255, blank=True, null=True)
    imo_codetext = models.CharField(max_length=255, blank=True, null=True)
    imo_codetype = models.CharField(max_length=255, blank=True, null=True)
    imo_vis_date_published = models.DateField(blank=True, null=True)
    imo_vis_date_presented = models.DateField(blank=True, null=True)
    imo_date_observation = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'immunization_observation'


class Immunizations(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)
    administered_date = models.DateTimeField(blank=True, null=True)
    immunization_id = models.IntegerField(blank=True, null=True)
    cvx_code = models.CharField(max_length=64, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    lot_number = models.CharField(max_length=50, blank=True, null=True)
    administered_by_id = models.BigIntegerField(blank=True, null=True)
    administered_by = models.CharField(max_length=255, blank=True, null=True)
    education_date = models.DateField(blank=True, null=True)
    vis_date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField()
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    amount_administered = models.FloatField(blank=True, null=True)
    amount_administered_unit = models.CharField(max_length=50, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    route = models.CharField(max_length=100, blank=True, null=True)
    administration_site = models.CharField(max_length=100, blank=True, null=True)
    added_erroneously = models.IntegerField()
    external_id = models.CharField(max_length=20, blank=True, null=True)
    completion_status = models.CharField(max_length=50, blank=True, null=True)
    information_source = models.CharField(max_length=31, blank=True, null=True)
    refusal_reason = models.CharField(max_length=31, blank=True, null=True)
    ordering_provider = models.IntegerField(blank=True, null=True)
    reason_code = models.CharField(max_length=31, blank=True, null=True)
    reason_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'immunizations'


class InsuranceCompanies(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    attn = models.CharField(max_length=255, blank=True, null=True)
    cms_id = models.CharField(max_length=15, blank=True, null=True)
    ins_type_code = models.IntegerField(blank=True, null=True)
    x12_receiver_id = models.CharField(max_length=25, blank=True, null=True)
    x12_default_partner_id = models.IntegerField(blank=True, null=True)
    alt_cms_id = models.CharField(max_length=15, blank=True, null=True)
    inactive = models.IntegerField()
    eligibility_id = models.CharField(max_length=32, blank=True, null=True)
    x12_default_eligibility_id = models.IntegerField(blank=True, null=True)
    cqm_sop = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_companies'


class InsuranceData(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    type = models.CharField(max_length=9, blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    plan_name = models.CharField(max_length=255, blank=True, null=True)
    policy_number = models.CharField(max_length=255, blank=True, null=True)
    group_number = models.CharField(max_length=255, blank=True, null=True)
    subscriber_lname = models.CharField(max_length=255, blank=True, null=True)
    subscriber_mname = models.CharField(max_length=255, blank=True, null=True)
    subscriber_fname = models.CharField(max_length=255, blank=True, null=True)
    subscriber_relationship = models.CharField(max_length=255, blank=True, null=True)
    subscriber_ss = models.CharField(max_length=255, blank=True, null=True)
    subscriber_dob = models.DateField(db_column='subscriber_DOB', blank=True, null=True)  # Field name made lowercase.
    subscriber_street = models.CharField(max_length=255, blank=True, null=True)
    subscriber_postal_code = models.CharField(max_length=255, blank=True, null=True)
    subscriber_city = models.CharField(max_length=255, blank=True, null=True)
    subscriber_state = models.CharField(max_length=255, blank=True, null=True)
    subscriber_country = models.CharField(max_length=255, blank=True, null=True)
    subscriber_phone = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer_street = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer_postal_code = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer_state = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer_country = models.CharField(max_length=255, blank=True, null=True)
    subscriber_employer_city = models.CharField(max_length=255, blank=True, null=True)
    copay = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    pid = models.BigIntegerField()
    subscriber_sex = models.CharField(max_length=25, blank=True, null=True)
    accept_assignment = models.CharField(max_length=5)
    policy_type = models.CharField(max_length=25)
    subscriber_street_line_2 = models.TextField(blank=True, null=True)
    subscriber_employer_street_line_2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_data'
        unique_together = (('pid', 'type', 'date'),)


class InsuranceNumbers(models.Model):
    id = models.IntegerField(primary_key=True)
    provider_id = models.IntegerField()
    insurance_company_id = models.IntegerField(blank=True, null=True)
    provider_number = models.CharField(max_length=20, blank=True, null=True)
    rendering_provider_number = models.CharField(max_length=20, blank=True, null=True)
    group_number = models.CharField(max_length=20, blank=True, null=True)
    provider_number_type = models.CharField(max_length=4, blank=True, null=True)
    rendering_provider_number_type = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_numbers'


class InsuranceTypeCodes(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=60)
    claim_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_type_codes'


class IssueEncounter(models.Model):
    pid = models.BigIntegerField(primary_key=True)
    list_id = models.IntegerField()
    encounter = models.IntegerField()
    resolved = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'issue_encounter'
        unique_together = (('pid', 'list_id', 'encounter'),)


class IssueTypes(models.Model):
    active = models.IntegerField()
    category = models.CharField(primary_key=True, max_length=75)
    type = models.CharField(max_length=75)
    plural = models.CharField(max_length=75)
    singular = models.CharField(max_length=75)
    abbreviation = models.CharField(max_length=75)
    style = models.SmallIntegerField()
    force_show = models.SmallIntegerField()
    ordering = models.IntegerField()
    aco_spec = models.CharField(max_length=63)

    class Meta:
        managed = False
        db_table = 'issue_types'
        unique_together = (('category', 'type'),)


class JwtGrantHistory(models.Model):
    jti = models.CharField(max_length=100)
    client_id = models.CharField(max_length=80)
    jti_exp = models.DateTimeField(blank=True, null=True)
    creation_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jwt_grant_history'


class Keys(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=20)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keys'


class LangConstants(models.Model):
    cons_id = models.AutoField(unique=True)
    constant_name = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lang_constants'


class LangCustom(models.Model):
    lang_description = models.CharField(max_length=100)
    lang_code = models.CharField(max_length=2)
    constant_name = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lang_custom'


class LangDefinitions(models.Model):
    def_id = models.AutoField(unique=True)
    cons_id = models.IntegerField()
    lang_id = models.IntegerField()
    definition = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lang_definitions'


class LangLanguages(models.Model):
    lang_id = models.AutoField(unique=True)
    lang_code = models.CharField(max_length=2)
    lang_description = models.CharField(max_length=100, blank=True, null=True)
    lang_is_rtl = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lang_languages'


class LayoutGroupProperties(models.Model):
    grp_form_id = models.CharField(primary_key=True, max_length=31)
    grp_group_id = models.CharField(max_length=31)
    grp_title = models.CharField(max_length=63)
    grp_subtitle = models.CharField(max_length=63)
    grp_mapping = models.CharField(max_length=31)
    grp_seq = models.IntegerField()
    grp_activity = models.IntegerField()
    grp_repeats = models.IntegerField()
    grp_columns = models.IntegerField()
    grp_size = models.IntegerField()
    grp_issue_type = models.CharField(max_length=75)
    grp_aco_spec = models.CharField(max_length=63)
    grp_save_close = models.IntegerField()
    grp_init_open = models.IntegerField()
    grp_referrals = models.IntegerField()
    grp_services = models.CharField(max_length=4095)
    grp_products = models.CharField(max_length=4095)
    grp_diags = models.CharField(max_length=4095)
    grp_last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layout_group_properties'
        unique_together = (('grp_form_id', 'grp_group_id'),)


class LayoutOptions(models.Model):
    form_id = models.CharField(primary_key=True, max_length=31)
    field_id = models.CharField(max_length=31)
    group_id = models.CharField(max_length=31)
    title = models.TextField(blank=True, null=True)
    seq = models.IntegerField()
    data_type = models.IntegerField()
    uor = models.IntegerField()
    fld_length = models.IntegerField()
    max_length = models.IntegerField()
    list_id = models.CharField(max_length=100)
    titlecols = models.IntegerField()
    datacols = models.IntegerField()
    default_value = models.CharField(max_length=255)
    edit_options = models.CharField(max_length=36)
    description = models.TextField(blank=True, null=True)
    fld_rows = models.IntegerField()
    list_backup_id = models.CharField(max_length=100)
    source = models.CharField(max_length=1)
    conditions = models.TextField(blank=True, null=True)
    validation = models.CharField(max_length=100, blank=True, null=True)
    codes = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'layout_options'
        unique_together = (('form_id', 'field_id', 'seq'),)


class LbfData(models.Model):
    form_id = models.AutoField(primary_key=True)
    field_id = models.CharField(max_length=31)
    field_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lbf_data'
        unique_together = (('form_id', 'field_id'),)


class LbtData(models.Model):
    form_id = models.BigIntegerField(primary_key=True)
    field_id = models.CharField(max_length=31)
    field_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lbt_data'
        unique_together = (('form_id', 'field_id'),)


class ListOptions(models.Model):
    list_id = models.CharField(primary_key=True, max_length=100)
    option_id = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    seq = models.IntegerField()
    is_default = models.IntegerField()
    option_value = models.FloatField()
    mapping = models.CharField(max_length=31)
    notes = models.TextField(blank=True, null=True)
    codes = models.CharField(max_length=255)
    toggle_setting_1 = models.IntegerField()
    toggle_setting_2 = models.IntegerField()
    activity = models.IntegerField()
    subtype = models.CharField(max_length=31)
    edit_options = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'list_options'
        unique_together = (('list_id', 'option_id'),)


class Lists(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    subtype = models.CharField(max_length=31)
    title = models.CharField(max_length=255, blank=True, null=True)
    udi = models.CharField(max_length=255, blank=True, null=True)
    udi_data = models.TextField(blank=True, null=True)
    begdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    returndate = models.DateField(blank=True, null=True)
    occurrence = models.IntegerField(blank=True, null=True)
    classification = models.IntegerField(blank=True, null=True)
    referredby = models.CharField(max_length=255, blank=True, null=True)
    extrainfo = models.CharField(max_length=255, blank=True, null=True)
    diagnosis = models.CharField(max_length=255, blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    outcome = models.IntegerField()
    destination = models.CharField(max_length=255, blank=True, null=True)
    reinjury_id = models.BigIntegerField()
    injury_part = models.CharField(max_length=31)
    injury_type = models.CharField(max_length=31)
    injury_grade = models.CharField(max_length=31)
    reaction = models.CharField(max_length=255)
    verification = models.CharField(max_length=36)
    external_allergyid = models.IntegerField(blank=True, null=True)
    erx_source = models.CharField(max_length=1)
    erx_uploaded = models.CharField(max_length=1)
    modifydate = models.DateTimeField()
    severity_al = models.CharField(max_length=50, blank=True, null=True)
    external_id = models.CharField(max_length=20, blank=True, null=True)
    list_option_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lists'


class ListsMedication(models.Model):
    id = models.BigAutoField(primary_key=True)
    list_id = models.BigIntegerField(blank=True, null=True)
    drug_dosage_instructions = models.TextField(blank=True, null=True)
    usage_category = models.CharField(max_length=100, blank=True, null=True)
    usage_category_title = models.CharField(max_length=255)
    request_intent = models.CharField(max_length=100, blank=True, null=True)
    request_intent_title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lists_medication'


class ListsTouch(models.Model):
    pid = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=255)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lists_touch'
        unique_together = (('pid', 'type'),)


class Log(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    user_notes = models.TextField(blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    checksum = models.TextField(blank=True, null=True)
    crt_user = models.CharField(max_length=255, blank=True, null=True)
    log_from = models.CharField(max_length=20, blank=True, null=True)
    menu_item_id = models.IntegerField(blank=True, null=True)
    ccda_doc_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class LogCommentEncrypt(models.Model):
    log_id = models.IntegerField()
    encrypt = models.CharField(max_length=3)
    checksum = models.TextField(blank=True, null=True)
    checksum_api = models.TextField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'log_comment_encrypt'


class LoginMfaRegistrations(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    last_challenge = models.DateTimeField(blank=True, null=True)
    method = models.CharField(max_length=31)
    var1 = models.CharField(max_length=4096)
    var2 = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'login_mfa_registrations'
        unique_together = (('user_id', 'name'),)


class MedexIcons(models.Model):
    i_uid = models.AutoField(db_column='i_UID', primary_key=True)  # Field name made lowercase.
    msg_type = models.CharField(max_length=50)
    msg_status = models.CharField(max_length=10)
    i_description = models.CharField(max_length=255, blank=True, null=True)
    i_html = models.TextField(blank=True, null=True)
    i_blob = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medex_icons'


class MedexOutgoing(models.Model):
    msg_uid = models.AutoField(primary_key=True)
    msg_pid = models.IntegerField()
    msg_pc_eid = models.CharField(max_length=11)
    campaign_uid = models.IntegerField()
    msg_date = models.DateTimeField()
    msg_type = models.CharField(max_length=50)
    msg_reply = models.CharField(max_length=50, blank=True, null=True)
    msg_extra_text = models.TextField(blank=True, null=True)
    medex_uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medex_outgoing'
        unique_together = (('msg_uid', 'msg_pc_eid', 'medex_uid'),)


class MedexPrefs(models.Model):
    medex_id = models.IntegerField(db_column='MedEx_id', blank=True, null=True)  # Field name made lowercase.
    me_username = models.CharField(db_column='ME_username', unique=True, max_length=100, blank=True, null=True)  # Field name made lowercase.
    me_api_key = models.TextField(db_column='ME_api_key', blank=True, null=True)  # Field name made lowercase.
    me_facilities = models.CharField(db_column='ME_facilities', max_length=50, blank=True, null=True)  # Field name made lowercase.
    me_providers = models.CharField(db_column='ME_providers', max_length=100, blank=True, null=True)  # Field name made lowercase.
    me_hipaa_default_override = models.CharField(db_column='ME_hipaa_default_override', max_length=3, blank=True, null=True)  # Field name made lowercase.
    phone_country_code = models.IntegerField(db_column='PHONE_country_code')  # Field name made lowercase.
    msgs_default_yes = models.CharField(db_column='MSGS_default_yes', max_length=3, blank=True, null=True)  # Field name made lowercase.
    postcards_local = models.CharField(db_column='POSTCARDS_local', max_length=3, blank=True, null=True)  # Field name made lowercase.
    postcards_remote = models.CharField(db_column='POSTCARDS_remote', max_length=3, blank=True, null=True)  # Field name made lowercase.
    labels_local = models.CharField(db_column='LABELS_local', max_length=3, blank=True, null=True)  # Field name made lowercase.
    labels_choice = models.CharField(db_column='LABELS_choice', max_length=50, blank=True, null=True)  # Field name made lowercase.
    combine_time = models.IntegerField(blank=True, null=True)
    postcard_top = models.CharField(max_length=255, blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    medex_lastupdated = models.DateTimeField(db_column='MedEx_lastupdated')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medex_prefs'


class MedexRecalls(models.Model):
    r_id = models.AutoField(db_column='r_ID', primary_key=True)  # Field name made lowercase.
    r_practid = models.IntegerField(db_column='r_PRACTID')  # Field name made lowercase.
    r_pid = models.IntegerField()
    r_eventdate = models.DateField(db_column='r_eventDate')  # Field name made lowercase.
    r_facility = models.IntegerField()
    r_provider = models.IntegerField()
    r_reason = models.CharField(max_length=255, blank=True, null=True)
    r_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'medex_recalls'
        unique_together = (('r_practid', 'r_pid'),)


class MiscAddressBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    fname = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'misc_address_book'


class ModuleAclGroupSettings(models.Model):
    module_id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    section_id = models.IntegerField()
    allowed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_acl_group_settings'
        unique_together = (('module_id', 'group_id', 'section_id'),)


class ModuleAclSections(models.Model):
    section_id = models.IntegerField(blank=True, null=True)
    section_name = models.CharField(max_length=255, blank=True, null=True)
    parent_section = models.IntegerField(blank=True, null=True)
    section_identifier = models.CharField(max_length=50, blank=True, null=True)
    module_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_acl_sections'


class ModuleAclUserSettings(models.Model):
    module_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    section_id = models.IntegerField()
    allowed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_acl_user_settings'
        unique_together = (('module_id', 'user_id', 'section_id'),)


class ModuleConfiguration(models.Model):
    module_config_id = models.AutoField(primary_key=True)
    module_id = models.PositiveIntegerField()
    field_name = models.CharField(max_length=45)
    field_value = models.CharField(max_length=255)
    created_by = models.BigIntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module_configuration'


class Modules(models.Model):
    mod_id = models.AutoField(primary_key=True)
    mod_name = models.CharField(max_length=64)
    mod_directory = models.CharField(max_length=64)
    mod_parent = models.CharField(max_length=64)
    mod_type = models.CharField(max_length=64)
    mod_active = models.PositiveIntegerField()
    mod_ui_name = models.CharField(max_length=64)
    mod_relative_link = models.CharField(max_length=64)
    mod_ui_order = models.IntegerField()
    mod_ui_active = models.PositiveIntegerField()
    mod_description = models.CharField(max_length=255)
    mod_nick_name = models.CharField(max_length=25)
    mod_enc_menu = models.CharField(max_length=10)
    permissions_item_table = models.CharField(max_length=100, blank=True, null=True)
    directory = models.CharField(max_length=255)
    date = models.DateTimeField()
    sql_run = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sql_version = models.CharField(max_length=150)
    acl_version = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'modules'
        unique_together = (('mod_id', 'mod_directory'),)


class ModulesHooksSettings(models.Model):
    mod_id = models.IntegerField(blank=True, null=True)
    enabled_hooks = models.CharField(max_length=255, blank=True, null=True)
    attached_to = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modules_hooks_settings'


class ModulesSettings(models.Model):
    mod_id = models.IntegerField(blank=True, null=True)
    fld_type = models.SmallIntegerField(blank=True, null=True)
    obj_name = models.CharField(max_length=255, blank=True, null=True)
    menu_name = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modules_settings'


class MultipleDb(models.Model):
    namespace = models.CharField(unique=True, max_length=255)
    username = models.CharField(max_length=255)
    password = models.TextField(blank=True, null=True)
    dbname = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    port = models.SmallIntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'multiple_db'


class Notes(models.Model):
    id = models.IntegerField(primary_key=True)
    foreign_id = models.IntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)
    owner = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    revision = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notes'


class NotificationLog(models.Model):
    ilogid = models.AutoField(db_column='iLogId', primary_key=True)  # Field name made lowercase.
    pid = models.BigIntegerField()
    pc_eid = models.PositiveIntegerField(blank=True, null=True)
    sms_gateway_type = models.CharField(max_length=50)
    smsgateway_info = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    email_sender = models.CharField(max_length=255)
    email_subject = models.CharField(max_length=255)
    type = models.CharField(max_length=5)
    patient_info = models.TextField(blank=True, null=True)
    pc_eventdate = models.DateField(db_column='pc_eventDate')  # Field name made lowercase.
    pc_enddate = models.DateField(db_column='pc_endDate')  # Field name made lowercase.
    pc_starttime = models.TimeField(db_column='pc_startTime')  # Field name made lowercase.
    pc_endtime = models.TimeField(db_column='pc_endTime')  # Field name made lowercase.
    dsentdatetime = models.DateTimeField(db_column='dSentDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notification_log'


class NotificationSettings(models.Model):
    settingsid = models.AutoField(db_column='SettingsId', primary_key=True)  # Field name made lowercase.
    send_sms_before_hours = models.IntegerField(db_column='Send_SMS_Before_Hours')  # Field name made lowercase.
    send_email_before_hours = models.IntegerField(db_column='Send_Email_Before_Hours')  # Field name made lowercase.
    sms_gateway_username = models.CharField(db_column='SMS_gateway_username', max_length=100)  # Field name made lowercase.
    sms_gateway_password = models.CharField(db_column='SMS_gateway_password', max_length=100)  # Field name made lowercase.
    sms_gateway_apikey = models.CharField(db_column='SMS_gateway_apikey', max_length=100)  # Field name made lowercase.
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'notification_settings'


class OauthClients(models.Model):
    client_id = models.CharField(primary_key=True, max_length=80)
    client_role = models.CharField(max_length=20, blank=True, null=True)
    client_name = models.CharField(max_length=80)
    client_secret = models.TextField(blank=True, null=True)
    registration_token = models.CharField(max_length=80, blank=True, null=True)
    registration_uri_path = models.CharField(max_length=40, blank=True, null=True)
    register_date = models.DateTimeField(blank=True, null=True)
    revoke_date = models.DateTimeField(blank=True, null=True)
    contacts = models.TextField(blank=True, null=True)
    redirect_uri = models.TextField(blank=True, null=True)
    grant_types = models.CharField(max_length=80, blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
    user_id = models.CharField(max_length=40, blank=True, null=True)
    site_id = models.CharField(max_length=64, blank=True, null=True)
    is_confidential = models.IntegerField()
    logout_redirect_uris = models.TextField(blank=True, null=True)
    jwks_uri = models.TextField(blank=True, null=True)
    jwks = models.TextField(blank=True, null=True)
    initiate_login_uri = models.TextField(blank=True, null=True)
    endorsements = models.TextField(blank=True, null=True)
    policy_uri = models.TextField(blank=True, null=True)
    tos_uri = models.TextField(blank=True, null=True)
    is_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthTrustedUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=80, blank=True, null=True)
    client_id = models.CharField(max_length=80, blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
    persist_login = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    session_cache = models.TextField(blank=True, null=True)
    grant_type = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_trusted_user'


class Onotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onotes'


class OnsiteDocuments(models.Model):
    pid = models.PositiveBigIntegerField(blank=True, null=True)
    facility = models.PositiveIntegerField(blank=True, null=True)
    provider = models.PositiveIntegerField(blank=True, null=True)
    encounter = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField()
    doc_type = models.CharField(max_length=255)
    patient_signed_status = models.PositiveSmallIntegerField()
    patient_signed_time = models.DateTimeField(blank=True, null=True)
    authorize_signed_time = models.DateTimeField(blank=True, null=True)
    accept_signed_status = models.SmallIntegerField()
    authorizing_signator = models.CharField(max_length=50)
    review_date = models.DateTimeField(blank=True, null=True)
    denial_reason = models.CharField(max_length=255)
    authorized_signature = models.TextField(blank=True, null=True)
    patient_signature = models.TextField(blank=True, null=True)
    full_document = models.TextField(blank=True, null=True)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'onsite_documents'


class OnsiteMail(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    owner = models.CharField(max_length=128, blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    header = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    recipient_id = models.CharField(max_length=128, blank=True, null=True)
    recipient_name = models.CharField(max_length=255, blank=True, null=True)
    sender_id = models.CharField(max_length=128, blank=True, null=True)
    sender_name = models.CharField(max_length=255, blank=True, null=True)
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    mtype = models.CharField(max_length=128, blank=True, null=True)
    message_status = models.CharField(max_length=20)
    mail_chain = models.IntegerField(blank=True, null=True)
    reply_mail_chain = models.IntegerField(blank=True, null=True)
    is_msg_encrypted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onsite_mail'


class OnsiteMessages(models.Model):
    username = models.CharField(max_length=64)
    message = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=15)
    date = models.DateTimeField()
    sender_id = models.CharField(max_length=64, blank=True, null=True)
    recip_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'onsite_messages'


class OnsiteOnline(models.Model):
    hash = models.CharField(primary_key=True, max_length=32)
    ip = models.CharField(max_length=15)
    last_update = models.DateTimeField()
    username = models.CharField(max_length=64)
    userid = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onsite_online'


class OnsitePortalActivity(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)
    activity = models.CharField(max_length=255, blank=True, null=True)
    require_audit = models.IntegerField(blank=True, null=True)
    pending_action = models.CharField(max_length=255, blank=True, null=True)
    action_taken = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    narrative = models.TextField(blank=True, null=True)
    table_action = models.TextField(blank=True, null=True)
    table_args = models.TextField(blank=True, null=True)
    action_user = models.IntegerField(blank=True, null=True)
    action_taken_time = models.DateTimeField(blank=True, null=True)
    checksum = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onsite_portal_activity'


class OnsiteSignatures(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    created = models.IntegerField()
    lastmod = models.DateTimeField()
    pid = models.BigIntegerField(blank=True, null=True)
    encounter = models.IntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    activity = models.IntegerField()
    authorized = models.IntegerField(blank=True, null=True)
    signator = models.CharField(max_length=255)
    sig_image = models.TextField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    sig_hash = models.CharField(max_length=255)
    ip = models.CharField(max_length=46)

    class Meta:
        managed = False
        db_table = 'onsite_signatures'
        unique_together = (('pid', 'user'),)


class OpenemrModuleVars(models.Model):
    pn_id = models.AutoField(primary_key=True)
    pn_modname = models.CharField(max_length=64, blank=True, null=True)
    pn_name = models.CharField(max_length=64, blank=True, null=True)
    pn_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'openemr_module_vars'


class OpenemrModules(models.Model):
    pn_id = models.AutoField(primary_key=True)
    pn_name = models.CharField(max_length=64, blank=True, null=True)
    pn_type = models.IntegerField()
    pn_displayname = models.CharField(max_length=64, blank=True, null=True)
    pn_description = models.CharField(max_length=255, blank=True, null=True)
    pn_regid = models.PositiveIntegerField()
    pn_directory = models.CharField(max_length=64, blank=True, null=True)
    pn_version = models.CharField(max_length=10, blank=True, null=True)
    pn_admin_capable = models.IntegerField()
    pn_user_capable = models.IntegerField()
    pn_state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'openemr_modules'


class OpenemrPostcalendarCategories(models.Model):
    pc_catid = models.AutoField(primary_key=True)
    pc_constant_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    pc_catname = models.CharField(max_length=100, blank=True, null=True)
    pc_catcolor = models.CharField(max_length=50, blank=True, null=True)
    pc_catdesc = models.TextField(blank=True, null=True)
    pc_recurrtype = models.IntegerField()
    pc_enddate = models.DateField(blank=True, null=True)
    pc_recurrspec = models.TextField(blank=True, null=True)
    pc_recurrfreq = models.IntegerField()
    pc_duration = models.BigIntegerField()
    pc_end_date_flag = models.IntegerField()
    pc_end_date_type = models.IntegerField(blank=True, null=True)
    pc_end_date_freq = models.IntegerField()
    pc_end_all_day = models.IntegerField()
    pc_dailylimit = models.IntegerField()
    pc_cattype = models.IntegerField()
    pc_active = models.IntegerField()
    pc_seq = models.IntegerField()
    aco_spec = models.CharField(max_length=63)

    class Meta:
        managed = False
        db_table = 'openemr_postcalendar_categories'


class OpenemrPostcalendarEvents(models.Model):
    pc_eid = models.AutoField(primary_key=True)
    pc_catid = models.IntegerField()
    pc_multiple = models.PositiveIntegerField()
    pc_aid = models.CharField(max_length=30, blank=True, null=True)
    pc_pid = models.CharField(max_length=11, blank=True, null=True)
    pc_gid = models.IntegerField(blank=True, null=True)
    pc_title = models.CharField(max_length=150, blank=True, null=True)
    pc_time = models.DateTimeField(blank=True, null=True)
    pc_hometext = models.TextField(blank=True, null=True)
    pc_comments = models.IntegerField(blank=True, null=True)
    pc_counter = models.PositiveIntegerField(blank=True, null=True)
    pc_topic = models.IntegerField()
    pc_informant = models.CharField(max_length=20, blank=True, null=True)
    pc_eventdate = models.DateField(db_column='pc_eventDate')  # Field name made lowercase.
    pc_enddate = models.DateField(db_column='pc_endDate')  # Field name made lowercase.
    pc_duration = models.BigIntegerField()
    pc_recurrtype = models.IntegerField()
    pc_recurrspec = models.TextField(blank=True, null=True)
    pc_recurrfreq = models.IntegerField()
    pc_starttime = models.TimeField(db_column='pc_startTime', blank=True, null=True)  # Field name made lowercase.
    pc_endtime = models.TimeField(db_column='pc_endTime', blank=True, null=True)  # Field name made lowercase.
    pc_alldayevent = models.IntegerField()
    pc_location = models.TextField(blank=True, null=True)
    pc_conttel = models.CharField(max_length=50, blank=True, null=True)
    pc_contname = models.CharField(max_length=50, blank=True, null=True)
    pc_contemail = models.CharField(max_length=255, blank=True, null=True)
    pc_website = models.CharField(max_length=255, blank=True, null=True)
    pc_fee = models.CharField(max_length=50, blank=True, null=True)
    pc_eventstatus = models.IntegerField()
    pc_sharing = models.IntegerField()
    pc_language = models.CharField(max_length=30, blank=True, null=True)
    pc_apptstatus = models.CharField(max_length=15)
    pc_prefcatid = models.IntegerField()
    pc_facility = models.IntegerField()
    pc_sendalertsms = models.CharField(max_length=3)
    pc_sendalertemail = models.CharField(max_length=3)
    pc_billing_location = models.SmallIntegerField()
    pc_room = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'openemr_postcalendar_events'


class PatientAccessOnsite(models.Model):
    pid = models.BigIntegerField(unique=True, blank=True, null=True)
    portal_username = models.CharField(max_length=100, blank=True, null=True)
    portal_pwd = models.CharField(max_length=255, blank=True, null=True)
    portal_pwd_status = models.IntegerField(blank=True, null=True)
    portal_login_username = models.CharField(max_length=100, blank=True, null=True)
    portal_onetime = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'patient_access_onsite'


class PatientBirthdayAlert(models.Model):
    pid = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    turned_off_on = models.DateField()

    class Meta:
        managed = False
        db_table = 'patient_birthday_alert'
        unique_together = (('pid', 'user_id'),)


class PatientData(models.Model):
    id = models.BigAutoField()
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    financial = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country_code = models.CharField(max_length=255)
    drivers_license = models.CharField(max_length=255)
    ss = models.CharField(max_length=255)
    occupation = models.TextField(blank=True, null=True)
    phone_home = models.CharField(max_length=255)
    phone_biz = models.CharField(max_length=255)
    phone_contact = models.CharField(max_length=255)
    phone_cell = models.CharField(max_length=255)
    pharmacy_id = models.IntegerField()
    status = models.CharField(max_length=255)
    contact_relationship = models.CharField(max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    sex = models.CharField(max_length=255)
    referrer = models.CharField(max_length=255)
    referrerid = models.CharField(db_column='referrerID', max_length=255)  # Field name made lowercase.
    providerid = models.IntegerField(db_column='providerID', blank=True, null=True)  # Field name made lowercase.
    ref_providerid = models.IntegerField(db_column='ref_providerID', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    email_direct = models.CharField(max_length=255)
    ethnoracial = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    ethnicity = models.CharField(max_length=255)
    religion = models.CharField(max_length=40)
    interpretter = models.CharField(max_length=255)
    migrantseasonal = models.CharField(max_length=255)
    family_size = models.CharField(max_length=255)
    monthly_income = models.CharField(max_length=255)
    billing_note = models.TextField(blank=True, null=True)
    homeless = models.CharField(max_length=255)
    financial_review = models.DateTimeField(blank=True, null=True)
    pubpid = models.CharField(max_length=255)
    pid = models.BigIntegerField(unique=True)
    genericname1 = models.CharField(max_length=255)
    genericval1 = models.CharField(max_length=255)
    genericname2 = models.CharField(max_length=255)
    genericval2 = models.CharField(max_length=255)
    hipaa_mail = models.CharField(max_length=3)
    hipaa_voice = models.CharField(max_length=3)
    hipaa_notice = models.CharField(max_length=3)
    hipaa_message = models.CharField(max_length=20)
    hipaa_allowsms = models.CharField(max_length=3)
    hipaa_allowemail = models.CharField(max_length=3)
    squad = models.CharField(max_length=32)
    fitness = models.IntegerField()
    referral_source = models.CharField(max_length=30)
    usertext1 = models.CharField(max_length=255)
    usertext2 = models.CharField(max_length=255)
    usertext3 = models.CharField(max_length=255)
    usertext4 = models.CharField(max_length=255)
    usertext5 = models.CharField(max_length=255)
    usertext6 = models.CharField(max_length=255)
    usertext7 = models.CharField(max_length=255)
    usertext8 = models.CharField(max_length=255)
    userlist1 = models.CharField(max_length=255)
    userlist2 = models.CharField(max_length=255)
    userlist3 = models.CharField(max_length=255)
    userlist4 = models.CharField(max_length=255)
    userlist5 = models.CharField(max_length=255)
    userlist6 = models.CharField(max_length=255)
    userlist7 = models.CharField(max_length=255)
    pricelevel = models.CharField(max_length=255)
    regdate = models.DateTimeField(blank=True, null=True)
    contrastart = models.DateField(blank=True, null=True)
    completed_ad = models.CharField(max_length=3)
    ad_reviewed = models.DateField(blank=True, null=True)
    vfc = models.CharField(max_length=255)
    mothersname = models.CharField(max_length=255)
    guardiansname = models.TextField(blank=True, null=True)
    allow_imm_reg_use = models.CharField(max_length=255)
    allow_imm_info_share = models.CharField(max_length=255)
    allow_health_info_ex = models.CharField(max_length=255)
    allow_patient_portal = models.CharField(max_length=31)
    deceased_date = models.DateTimeField(blank=True, null=True)
    deceased_reason = models.CharField(max_length=255)
    soap_import_status = models.IntegerField(blank=True, null=True)
    cmsportal_login = models.CharField(max_length=60)
    care_team_provider = models.TextField(blank=True, null=True)
    care_team_facility = models.TextField(blank=True, null=True)
    care_team_status = models.TextField(blank=True, null=True)
    county = models.CharField(max_length=40)
    industry = models.TextField(blank=True, null=True)
    imm_reg_status = models.TextField(blank=True, null=True)
    imm_reg_stat_effdate = models.TextField(blank=True, null=True)
    publicity_code = models.TextField(blank=True, null=True)
    publ_code_eff_date = models.TextField(blank=True, null=True)
    protect_indicator = models.TextField(blank=True, null=True)
    prot_indi_effdate = models.TextField(blank=True, null=True)
    guardianrelationship = models.TextField(blank=True, null=True)
    guardiansex = models.TextField(blank=True, null=True)
    guardianaddress = models.TextField(blank=True, null=True)
    guardiancity = models.TextField(blank=True, null=True)
    guardianstate = models.TextField(blank=True, null=True)
    guardianpostalcode = models.TextField(blank=True, null=True)
    guardiancountry = models.TextField(blank=True, null=True)
    guardianphone = models.TextField(blank=True, null=True)
    guardianworkphone = models.TextField(blank=True, null=True)
    guardianemail = models.TextField(blank=True, null=True)
    sexual_orientation = models.TextField(blank=True, null=True)
    gender_identity = models.TextField(blank=True, null=True)
    birth_fname = models.TextField(blank=True, null=True)
    birth_lname = models.TextField(blank=True, null=True)
    birth_mname = models.TextField(blank=True, null=True)
    dupscore = models.IntegerField()
    name_history = models.TextField(blank=True, null=True)
    suffix = models.TextField(blank=True, null=True)
    street_line_2 = models.TextField(blank=True, null=True)
    patient_groups = models.TextField(blank=True, null=True)
    prevent_portal_apps = models.TextField(blank=True, null=True)
    provider_since_date = models.TextField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_data'


class PatientHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    date = models.DateTimeField()
    care_team_provider = models.TextField(blank=True, null=True)
    care_team_facility = models.TextField(blank=True, null=True)
    pid = models.BigIntegerField()
    history_type_key = models.CharField(max_length=36, blank=True, null=True)
    previous_name_prefix = models.TextField(blank=True, null=True)
    previous_name_first = models.TextField(blank=True, null=True)
    previous_name_middle = models.TextField(blank=True, null=True)
    previous_name_last = models.TextField(blank=True, null=True)
    previous_name_suffix = models.TextField(blank=True, null=True)
    previous_name_enddate = models.DateField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_history'


class PatientPortalMenu(models.Model):
    patient_portal_menu_id = models.AutoField(primary_key=True)
    patient_portal_menu_group_id = models.IntegerField(blank=True, null=True)
    menu_name = models.CharField(max_length=40, blank=True, null=True)
    menu_order = models.SmallIntegerField(blank=True, null=True)
    menu_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_portal_menu'


class PatientReminders(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.IntegerField()
    date_inactivated = models.DateTimeField(blank=True, null=True)
    reason_inactivated = models.CharField(max_length=31)
    due_status = models.CharField(max_length=31)
    pid = models.BigIntegerField()
    category = models.CharField(max_length=31)
    item = models.CharField(max_length=31)
    date_created = models.DateTimeField(blank=True, null=True)
    date_sent = models.DateTimeField(blank=True, null=True)
    voice_status = models.IntegerField()
    sms_status = models.IntegerField()
    email_status = models.IntegerField()
    mail_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient_reminders'


class PatientTracker(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    apptdate = models.DateField(blank=True, null=True)
    appttime = models.TimeField(blank=True, null=True)
    eid = models.BigIntegerField()
    pid = models.BigIntegerField()
    original_user = models.CharField(max_length=255)
    encounter = models.BigIntegerField()
    lastseq = models.CharField(max_length=4)
    random_drug_test = models.IntegerField(blank=True, null=True)
    drug_screen_completed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient_tracker'


class PatientTrackerElement(models.Model):
    pt_tracker_id = models.BigIntegerField()
    start_datetime = models.DateTimeField(blank=True, null=True)
    room = models.CharField(max_length=20)
    status = models.CharField(max_length=31)
    seq = models.CharField(max_length=4)
    user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'patient_tracker_element'


class PaymentGatewayDetails(models.Model):
    service_name = models.CharField(max_length=100, blank=True, null=True)
    login_id = models.CharField(max_length=255, blank=True, null=True)
    transaction_key = models.CharField(max_length=255, blank=True, null=True)
    md5 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_gateway_details'


class PaymentProcessingAudit(models.Model):
    uuid = models.CharField(primary_key=True, max_length=16)
    service = models.CharField(max_length=50, blank=True, null=True)
    pid = models.BigIntegerField()
    success = models.IntegerField(blank=True, null=True)
    action_name = models.CharField(max_length=50, blank=True, null=True)
    amount = models.CharField(max_length=20, blank=True, null=True)
    ticket = models.CharField(max_length=100, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    audit_data = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    map_uuid = models.CharField(max_length=16, blank=True, null=True)
    map_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    reverted = models.IntegerField(blank=True, null=True)
    revert_action_name = models.CharField(max_length=50, blank=True, null=True)
    revert_transaction_id = models.CharField(max_length=100, blank=True, null=True)
    revert_audit_data = models.TextField(blank=True, null=True)
    revert_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_processing_audit'


class Payments(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid = models.BigIntegerField()
    dtime = models.DateTimeField()
    encounter = models.BigIntegerField()
    user = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    amount1 = models.DecimalField(max_digits=12, decimal_places=2)
    amount2 = models.DecimalField(max_digits=12, decimal_places=2)
    posted1 = models.DecimalField(max_digits=12, decimal_places=2)
    posted2 = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'payments'


class Pharmacies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    transmit_method = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    ncpdp = models.IntegerField(blank=True, null=True)
    npi = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmacies'


class PhoneNumbers(models.Model):
    id = models.IntegerField(primary_key=True)
    country_code = models.CharField(max_length=5, blank=True, null=True)
    area_code = models.CharField(max_length=3, blank=True, null=True)
    prefix = models.CharField(max_length=3, blank=True, null=True)
    number = models.CharField(max_length=4, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    foreign_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_numbers'


class Pnotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255, blank=True, null=True)
    groupname = models.CharField(max_length=255, blank=True, null=True)
    activity = models.IntegerField(blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    assigned_to = models.CharField(max_length=255, blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    message_status = models.CharField(max_length=20)
    portal_relation = models.CharField(max_length=100, blank=True, null=True)
    is_msg_encrypted = models.IntegerField(blank=True, null=True)
    update_by = models.BigIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pnotes'


class Prescriptions(models.Model):
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    patient_id = models.BigIntegerField(blank=True, null=True)
    filled_by_id = models.IntegerField(blank=True, null=True)
    pharmacy_id = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    encounter = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    drug = models.CharField(max_length=150, blank=True, null=True)
    drug_id = models.IntegerField()
    rxnorm_drugcode = models.CharField(max_length=25, blank=True, null=True)
    form = models.IntegerField(blank=True, null=True)
    dosage = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.CharField(max_length=31, blank=True, null=True)
    size = models.CharField(max_length=25, blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    route = models.IntegerField(blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    substitute = models.IntegerField(blank=True, null=True)
    refills = models.IntegerField(blank=True, null=True)
    per_refill = models.IntegerField(blank=True, null=True)
    filled_date = models.DateField(blank=True, null=True)
    medication = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    datetime = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    site = models.CharField(max_length=50, blank=True, null=True)
    prescriptionguid = models.CharField(max_length=50, blank=True, null=True)
    erx_source = models.IntegerField()
    erx_uploaded = models.IntegerField()
    drug_info_erx = models.TextField(blank=True, null=True)
    external_id = models.CharField(max_length=20, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    indication = models.TextField(blank=True, null=True)
    prn = models.CharField(max_length=30, blank=True, null=True)
    ntx = models.IntegerField(blank=True, null=True)
    rtx = models.IntegerField(blank=True, null=True)
    txdate = models.DateField(db_column='txDate')  # Field name made lowercase.
    usage_category = models.CharField(max_length=100, blank=True, null=True)
    usage_category_title = models.CharField(max_length=255)
    request_intent = models.CharField(max_length=100, blank=True, null=True)
    request_intent_title = models.CharField(max_length=255)
    drug_dosage_instructions = models.TextField(blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)
    updated_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescriptions'


class Prices(models.Model):
    pr_id = models.CharField(primary_key=True, max_length=11)
    pr_selector = models.CharField(max_length=255)
    pr_level = models.CharField(max_length=31)
    pr_price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'prices'
        unique_together = (('pr_id', 'pr_selector', 'pr_level'),)


class ProAssessments(models.Model):
    form_oid = models.CharField(max_length=255)
    form_name = models.CharField(max_length=255)
    user_id = models.IntegerField()
    deadline = models.DateTimeField()
    patient_id = models.IntegerField()
    assessment_oid = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    score = models.FloatField()
    error = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pro_assessments'


class ProcedureAnswers(models.Model):
    procedure_order_id = models.BigIntegerField(primary_key=True)
    procedure_order_seq = models.IntegerField()
    question_code = models.CharField(max_length=31)
    answer_seq = models.IntegerField()
    answer = models.CharField(max_length=255)
    procedure_code = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedure_answers'
        unique_together = (('procedure_order_id', 'procedure_order_seq', 'question_code', 'answer_seq'),)


class ProcedureOrder(models.Model):
    procedure_order_id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    provider_id = models.BigIntegerField()
    patient_id = models.BigIntegerField()
    encounter_id = models.BigIntegerField()
    date_collected = models.DateTimeField(blank=True, null=True)
    date_ordered = models.DateTimeField(blank=True, null=True)
    order_priority = models.CharField(max_length=31)
    order_status = models.CharField(max_length=31)
    patient_instructions = models.TextField(blank=True, null=True)
    activity = models.IntegerField()
    control_id = models.CharField(max_length=255)
    lab_id = models.BigIntegerField()
    specimen_type = models.CharField(max_length=31)
    specimen_location = models.CharField(max_length=31)
    specimen_volume = models.CharField(max_length=30)
    date_transmitted = models.DateTimeField(blank=True, null=True)
    clinical_hx = models.CharField(max_length=255)
    external_id = models.CharField(max_length=20, blank=True, null=True)
    history_order = models.CharField(max_length=1, blank=True, null=True)
    order_diagnosis = models.CharField(max_length=255, blank=True, null=True)
    billing_type = models.CharField(max_length=4, blank=True, null=True)
    specimen_fasting = models.CharField(max_length=31, blank=True, null=True)
    order_psc = models.IntegerField(blank=True, null=True)
    order_abn = models.CharField(max_length=31)
    collector_id = models.BigIntegerField()
    account = models.CharField(max_length=60, blank=True, null=True)
    account_facility = models.IntegerField(blank=True, null=True)
    provider_number = models.CharField(max_length=30, blank=True, null=True)
    procedure_order_type = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'procedure_order'


class ProcedureOrderCode(models.Model):
    procedure_order_id = models.BigIntegerField(primary_key=True)
    procedure_order_seq = models.IntegerField()
    procedure_code = models.CharField(max_length=64)
    procedure_name = models.CharField(max_length=255)
    procedure_source = models.CharField(max_length=1)
    diagnoses = models.TextField(blank=True, null=True)
    do_not_send = models.IntegerField()
    procedure_order_title = models.CharField(max_length=255, blank=True, null=True)
    procedure_type = models.CharField(max_length=31, blank=True, null=True)
    transport = models.CharField(max_length=31, blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    reason_code = models.CharField(max_length=31, blank=True, null=True)
    reason_description = models.TextField(blank=True, null=True)
    reason_date_low = models.DateTimeField(blank=True, null=True)
    reason_date_high = models.DateTimeField(blank=True, null=True)
    reason_status = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedure_order_code'
        unique_together = (('procedure_order_id', 'procedure_order_seq'),)


class ProcedureProviders(models.Model):
    ppid = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    name = models.CharField(max_length=255)
    npi = models.CharField(max_length=15)
    send_app_id = models.CharField(max_length=255)
    send_fac_id = models.CharField(max_length=255)
    recv_app_id = models.CharField(max_length=255)
    recv_fac_id = models.CharField(max_length=255)
    dorp = models.CharField(db_column='DorP', max_length=1)  # Field name made lowercase.
    direction = models.CharField(max_length=1)
    protocol = models.CharField(max_length=15)
    remote_host = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    orders_path = models.CharField(max_length=255)
    results_path = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    lab_director = models.BigIntegerField()
    active = models.IntegerField()
    type = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedure_providers'


class ProcedureQuestions(models.Model):
    lab_id = models.BigIntegerField(primary_key=True)
    procedure_code = models.CharField(max_length=31)
    question_code = models.CharField(max_length=31)
    seq = models.IntegerField()
    question_text = models.CharField(max_length=255)
    required = models.IntegerField()
    maxsize = models.IntegerField()
    fldtype = models.CharField(max_length=1)
    options = models.TextField(blank=True, null=True)
    tips = models.CharField(max_length=255)
    activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'procedure_questions'
        unique_together = (('lab_id', 'procedure_code', 'question_code'),)


class ProcedureReport(models.Model):
    procedure_report_id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    procedure_order_id = models.BigIntegerField(blank=True, null=True)
    procedure_order_seq = models.IntegerField()
    date_collected = models.DateTimeField(blank=True, null=True)
    date_collected_tz = models.CharField(max_length=5, blank=True, null=True)
    date_report = models.DateTimeField(blank=True, null=True)
    date_report_tz = models.CharField(max_length=5, blank=True, null=True)
    source = models.BigIntegerField()
    specimen_num = models.CharField(max_length=63)
    report_status = models.CharField(max_length=31)
    review_status = models.CharField(max_length=31)
    report_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedure_report'


class ProcedureResult(models.Model):
    procedure_result_id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    procedure_report_id = models.BigIntegerField()
    result_data_type = models.CharField(max_length=1)
    result_code = models.CharField(max_length=31)
    result_text = models.CharField(max_length=255)
    date = models.DateTimeField(blank=True, null=True)
    facility = models.CharField(max_length=255)
    units = models.CharField(max_length=31)
    result = models.CharField(max_length=255)
    range = models.CharField(max_length=255)
    abnormal = models.CharField(max_length=31)
    comments = models.TextField(blank=True, null=True)
    document_id = models.BigIntegerField()
    result_status = models.CharField(max_length=31)
    date_end = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedure_result'


class ProcedureType(models.Model):
    procedure_type_id = models.BigAutoField(primary_key=True)
    parent = models.BigIntegerField()
    name = models.CharField(max_length=63)
    lab_id = models.BigIntegerField()
    procedure_code = models.CharField(max_length=64)
    procedure_type = models.CharField(max_length=31)
    body_site = models.CharField(max_length=31)
    specimen = models.CharField(max_length=31)
    route_admin = models.CharField(max_length=31)
    laterality = models.CharField(max_length=31)
    description = models.CharField(max_length=255)
    standard_code = models.CharField(max_length=255)
    related_code = models.CharField(max_length=255)
    units = models.CharField(max_length=31)
    range = models.CharField(max_length=255)
    seq = models.IntegerField()
    activity = models.IntegerField()
    notes = models.CharField(max_length=255)
    transport = models.CharField(max_length=31, blank=True, null=True)
    procedure_type_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procedure_type'


class ProductRegistration(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    opt_out = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_registration'


class ProductWarehouse(models.Model):
    pw_drug_id = models.IntegerField(primary_key=True)
    pw_warehouse = models.CharField(max_length=31)
    pw_min_level = models.FloatField(blank=True, null=True)
    pw_max_level = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_warehouse'
        unique_together = (('pw_drug_id', 'pw_warehouse'),)


class Registry(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    directory = models.CharField(max_length=255, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    sql_run = models.IntegerField(blank=True, null=True)
    unpackaged = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    patient_encounter = models.IntegerField()
    therapy_group_encounter = models.IntegerField()
    aco_spec = models.CharField(max_length=63)

    class Meta:
        managed = False
        db_table = 'registry'


class ReportItemized(models.Model):
    report_id = models.BigIntegerField()
    itemized_test_id = models.SmallIntegerField()
    numerator_label = models.CharField(max_length=25)
    pass_field = models.IntegerField(db_column='pass')  # Field renamed because it was a Python reserved word.
    pid = models.BigIntegerField()
    rule_id = models.CharField(max_length=31, blank=True, null=True)
    item_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_itemized'


class ReportResults(models.Model):
    report_id = models.BigIntegerField(primary_key=True)
    field_id = models.CharField(max_length=31)
    field_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_results'
        unique_together = (('report_id', 'field_id'),)


class RuleAction(models.Model):
    id = models.CharField(max_length=31)
    group_id = models.BigIntegerField()
    category = models.CharField(max_length=31)
    item = models.CharField(max_length=31)

    class Meta:
        managed = False
        db_table = 'rule_action'


class RuleActionItem(models.Model):
    category = models.CharField(primary_key=True, max_length=31)
    item = models.CharField(max_length=31)
    clin_rem_link = models.CharField(max_length=255)
    reminder_message = models.TextField(blank=True, null=True)
    custom_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rule_action_item'
        unique_together = (('category', 'item'),)


class RuleFilter(models.Model):
    id = models.CharField(max_length=31)
    include_flag = models.IntegerField()
    required_flag = models.IntegerField()
    method = models.CharField(max_length=31)
    method_detail = models.CharField(max_length=31)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rule_filter'


class RulePatientData(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pid = models.BigIntegerField()
    category = models.CharField(max_length=31)
    item = models.CharField(max_length=31)
    complete = models.CharField(max_length=31)
    result = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rule_patient_data'


class RuleReminder(models.Model):
    id = models.CharField(max_length=31)
    method = models.CharField(max_length=31)
    method_detail = models.CharField(max_length=31)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rule_reminder'


class RuleTarget(models.Model):
    id = models.CharField(max_length=31)
    group_id = models.BigIntegerField()
    include_flag = models.IntegerField()
    required_flag = models.IntegerField()
    method = models.CharField(max_length=31)
    value = models.CharField(max_length=255)
    interval = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'rule_target'


class Sequences(models.Model):
    id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'sequences'


class SessionTracker(models.Model):
    uuid = models.CharField(primary_key=True, max_length=16)
    created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_tracker'


class SharedAttributes(models.Model):
    pid = models.BigIntegerField(primary_key=True)
    encounter = models.BigIntegerField()
    field_id = models.CharField(max_length=31)
    last_update = models.DateTimeField()
    user_id = models.BigIntegerField()
    field_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shared_attributes'
        unique_together = (('pid', 'encounter', 'field_id'),)


class StandardizedTablesTrack(models.Model):
    imported_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    revision_version = models.CharField(max_length=255)
    revision_date = models.DateTimeField(blank=True, null=True)
    file_checksum = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'standardized_tables_track'


class SupportedExternalDataloads(models.Model):
    load_id = models.BigAutoField(unique=True)
    load_type = models.CharField(max_length=24)
    load_source = models.CharField(max_length=24)
    load_release_date = models.DateField()
    load_filename = models.CharField(max_length=256)
    load_checksum = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'supported_external_dataloads'


class SyndromicSurveillance(models.Model):
    id = models.BigAutoField(primary_key=True)
    lists_id = models.BigIntegerField()
    submission_date = models.DateTimeField()
    filename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'syndromic_surveillance'


class TemplateUsers(models.Model):
    tu_id = models.AutoField(primary_key=True)
    tu_user_id = models.IntegerField(blank=True, null=True)
    tu_facility_id = models.IntegerField(blank=True, null=True)
    tu_template_id = models.IntegerField(blank=True, null=True)
    tu_template_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_users'
        unique_together = (('tu_user_id', 'tu_template_id'),)


class TherapyGroups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255)
    group_start_date = models.DateField()
    group_end_date = models.DateField(blank=True, null=True)
    group_type = models.IntegerField()
    group_participation = models.IntegerField()
    group_status = models.IntegerField()
    group_notes = models.TextField(blank=True, null=True)
    group_guest_counselors = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'therapy_groups'


class TherapyGroupsCounselors(models.Model):
    group_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'therapy_groups_counselors'
        unique_together = (('group_id', 'user_id'),)


class TherapyGroupsParticipantAttendance(models.Model):
    form_id = models.IntegerField(primary_key=True)
    pid = models.BigIntegerField()
    meeting_patient_comment = models.TextField(blank=True, null=True)
    meeting_patient_status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'therapy_groups_participant_attendance'
        unique_together = (('form_id', 'pid'),)


class TherapyGroupsParticipants(models.Model):
    group_id = models.IntegerField(primary_key=True)
    pid = models.BigIntegerField()
    group_patient_status = models.IntegerField()
    group_patient_start = models.DateField()
    group_patient_end = models.DateField(blank=True, null=True)
    group_patient_comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'therapy_groups_participants'
        unique_together = (('group_id', 'pid'),)


class Transactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255)
    pid = models.BigIntegerField(blank=True, null=True)
    user = models.CharField(max_length=255)
    groupname = models.CharField(max_length=255)
    authorized = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class UserSettings(models.Model):
    setting_user = models.BigIntegerField(primary_key=True)
    setting_label = models.CharField(max_length=100)
    setting_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_settings'
        unique_together = (('setting_user', 'setting_label'),)


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    authorized = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    fname = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    federaltaxid = models.CharField(max_length=255, blank=True, null=True)
    federaldrugid = models.CharField(max_length=255, blank=True, null=True)
    upin = models.CharField(max_length=255, blank=True, null=True)
    facility = models.CharField(max_length=255, blank=True, null=True)
    facility_id = models.IntegerField()
    see_auth = models.IntegerField()
    active = models.IntegerField()
    npi = models.CharField(max_length=15, blank=True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    specialty = models.CharField(max_length=255, blank=True, null=True)
    billname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    email_direct = models.CharField(max_length=255)
    google_signin_email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    assistant = models.CharField(max_length=255, blank=True, null=True)
    organization = models.CharField(max_length=255, blank=True, null=True)
    valedictory = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=60, blank=True, null=True)
    streetb = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    street2 = models.CharField(max_length=60, blank=True, null=True)
    streetb2 = models.CharField(max_length=60, blank=True, null=True)
    city2 = models.CharField(max_length=30, blank=True, null=True)
    state2 = models.CharField(max_length=30, blank=True, null=True)
    zip2 = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    phonew1 = models.CharField(max_length=30, blank=True, null=True)
    phonew2 = models.CharField(max_length=30, blank=True, null=True)
    phonecell = models.CharField(max_length=30, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    cal_ui = models.IntegerField()
    taxonomy = models.CharField(max_length=30)
    calendar = models.IntegerField()
    abook_type = models.CharField(max_length=31)
    default_warehouse = models.CharField(max_length=31)
    irnpool = models.CharField(max_length=31)
    state_license_number = models.CharField(max_length=25, blank=True, null=True)
    weno_prov_id = models.CharField(max_length=15, blank=True, null=True)
    newcrop_user_role = models.CharField(max_length=30, blank=True, null=True)
    cpoe = models.IntegerField(blank=True, null=True)
    physician_type = models.CharField(max_length=50, blank=True, null=True)
    main_menu_role = models.CharField(max_length=50)
    patient_menu_role = models.CharField(max_length=50)
    portal_user = models.IntegerField()
    supervisor_id = models.IntegerField()
    billing_facility = models.TextField(blank=True, null=True)
    billing_facility_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class UsersFacility(models.Model):
    tablename = models.CharField(primary_key=True, max_length=64)
    table_id = models.IntegerField()
    facility_id = models.IntegerField()
    warehouse_id = models.CharField(max_length=31)

    class Meta:
        managed = False
        db_table = 'users_facility'
        unique_together = (('tablename', 'table_id', 'facility_id', 'warehouse_id'),)


class UsersSecure(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    last_update_password = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField()
    password_history1 = models.CharField(max_length=255, blank=True, null=True)
    password_history2 = models.CharField(max_length=255, blank=True, null=True)
    password_history3 = models.CharField(max_length=255, blank=True, null=True)
    password_history4 = models.CharField(max_length=255, blank=True, null=True)
    last_challenge_response = models.DateTimeField(blank=True, null=True)
    login_work_area = models.TextField(blank=True, null=True)
    login_fail_counter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_secure'
        unique_together = (('id', 'username'),)


class UuidMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(max_length=16)
    resource = models.CharField(max_length=255)
    resource_path = models.CharField(max_length=255, blank=True, null=True)
    table = models.CharField(max_length=255)
    target_uuid = models.CharField(max_length=16)
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uuid_mapping'


class UuidRegistry(models.Model):
    uuid = models.CharField(primary_key=True, max_length=16)
    table_name = models.CharField(max_length=255)
    table_id = models.CharField(max_length=255)
    table_vertical = models.CharField(max_length=255)
    couchdb = models.CharField(max_length=255)
    document_drive = models.IntegerField()
    mapped = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uuid_registry'


class Valueset(models.Model):
    nqf_code = models.CharField(primary_key=True, max_length=255)
    code = models.CharField(max_length=255)
    code_system = models.CharField(max_length=255)
    code_type = models.CharField(max_length=255, blank=True, null=True)
    valueset = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    valueset_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valueset'
        unique_together = (('nqf_code', 'code', 'valueset'),)


class ValuesetOid(models.Model):
    nqf_code = models.CharField(primary_key=True, max_length=255)
    code = models.CharField(max_length=255)
    code_system = models.CharField(max_length=255)
    code_type = models.CharField(max_length=255, blank=True, null=True)
    valueset = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    valueset_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'valueset_oid'
        unique_together = (('nqf_code', 'code', 'valueset'),)


class VerifyEmail(models.Model):
    id = models.BigAutoField(primary_key=True)
    pid_holder = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    fname = models.CharField(max_length=255, blank=True, null=True)
    mname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    token_onetime = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'verify_email'


class Version(models.Model):
    v_major = models.IntegerField()
    v_minor = models.IntegerField()
    v_patch = models.IntegerField()
    v_realpatch = models.IntegerField()
    v_tag = models.CharField(max_length=31)
    v_database = models.IntegerField()
    v_acl = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'version'


class Voids(models.Model):
    void_id = models.BigAutoField(primary_key=True)
    patient_id = models.BigIntegerField()
    encounter_id = models.BigIntegerField()
    what_voided = models.CharField(max_length=31)
    date_original = models.DateTimeField(blank=True, null=True)
    date_voided = models.DateTimeField()
    user_id = models.BigIntegerField()
    amount1 = models.DecimalField(max_digits=12, decimal_places=2)
    amount2 = models.DecimalField(max_digits=12, decimal_places=2)
    other_info = models.TextField(blank=True, null=True)
    reason = models.CharField(max_length=31, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voids'


class X12Partners(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    id_number = models.CharField(max_length=255, blank=True, null=True)
    x12_sender_id = models.CharField(max_length=255, blank=True, null=True)
    x12_receiver_id = models.CharField(max_length=255, blank=True, null=True)
    processing_format = models.CharField(max_length=20, blank=True, null=True)
    x12_isa01 = models.CharField(max_length=2)
    x12_isa02 = models.CharField(max_length=10)
    x12_isa03 = models.CharField(max_length=2)
    x12_isa04 = models.CharField(max_length=10)
    x12_isa05 = models.CharField(max_length=2)
    x12_isa07 = models.CharField(max_length=2)
    x12_isa14 = models.CharField(max_length=1)
    x12_isa15 = models.CharField(max_length=1)
    x12_gs02 = models.CharField(max_length=15)
    x12_per06 = models.CharField(max_length=80)
    x12_dtp03 = models.CharField(max_length=1)
    x12_gs03 = models.CharField(max_length=15, blank=True, null=True)
    x12_submitter_name = models.CharField(max_length=255, blank=True, null=True)
    x12_sftp_login = models.CharField(max_length=255, blank=True, null=True)
    x12_sftp_pass = models.CharField(max_length=255, blank=True, null=True)
    x12_sftp_host = models.CharField(max_length=255, blank=True, null=True)
    x12_sftp_port = models.CharField(max_length=255, blank=True, null=True)
    x12_sftp_local_dir = models.CharField(max_length=255, blank=True, null=True)
    x12_sftp_remote_dir = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'x12_partners'


class X12RemoteTracker(models.Model):
    id = models.BigAutoField(primary_key=True)
    x12_partner_id = models.IntegerField()
    x12_filename = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    claims = models.TextField(blank=True, null=True)
    messages = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'x12_remote_tracker'
