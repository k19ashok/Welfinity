from operator import mod
from statistics import mode
from django.db import models




class PatientData(models.Model):


    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    pid = models.BigIntegerField(unique=True)


    title = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)


    sex = models.CharField(max_length=255)
    licid = models.CharField(max_length=255)
    extid = models.CharField(max_length=255)
    prevnames = models.TextField(blank=True, null=True)


    address = models.CharField(max_length=255)
    addressline2 = models.CharField(max_length=255)
    pin = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    altphone = models.CharField(max_length=255)

    careteam = models.CharField(max_length=255,null=True)
    carefacility = models.CharField(max_length=255,null=True)

    allowvoice = models.CharField(max_length=3,null=True)
    hipaa = models.CharField(max_length=3,null=True)
    allowmail = models.CharField(max_length=3,null=True)
    leavemsg = models.CharField(max_length=20,null=True)
    allowimmreg = models.CharField(max_length=255,null=True)
    allowimmshare = models.CharField(max_length=255,null=True)
    allowhie = models.CharField(max_length=255,null=True)
    allowpp = models.CharField(max_length=31,null=True)
    immstatus = models.TextField(blank=True, null=True)
    immstatusdt = models.DateField(blank=True, null=True)
    pubcode = models.TextField(blank=True, null=True)
    pubcodedate = models.DateField(blank=True, null=True)
    protind = models.TextField(blank=True, null=True)
    protinddate = models.DateField(blank=True, null=True)
    carestatus = models.TextField(blank=True, null=True)
    ptcat = models.TextField(blank=True, null=True)


    industry = models.TextField(blank=True, null=True)
    occupation = models.TextField(blank=True, null=True)
    empname = models.TextField(blank=True, null=True)
    empaddress = models.TextField(blank=True, null=True)



    ethnicity = models.CharField(max_length=255,null=True)
    religion = models.CharField(max_length=40,null=True)
    migrant = models.CharField(max_length=255,null=True)
    famsize = models.CharField(max_length=255,null=True)
    income = models.CharField(max_length=255,null=True)
    homeless = models.CharField(max_length=255,null=True)
    finreview = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=255,null=True)
    vfc = models.CharField(max_length=255,null=True)


    deceased = models.DateField(blank=True, null=True)
    reasondeceased = models.CharField(max_length=255,null=True)


    guardian = models.CharField(blank=True, null=True, max_length=255)
    guardianrelation = models.TextField(blank=True, null=True)
    guardiansex = models.TextField(blank=True, null=True)
    guardianaddress = models.TextField(blank=True, null=True)
    guardianaddressline2 = models.TextField(blank=True, null=True)
    guardiancity = models.TextField(blank=True, null=True)
    guardianstate = models.TextField(blank=True, null=True)
    guardianpin = models.TextField(blank=True, null=True)
    guardiancountry = models.TextField(blank=True, null=True)
    guardianphone = models.TextField(blank=True, null=True)
    guardianemail = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'patient_data'


class Encounter(models.Model):
    encid = models.CharField(max_length=100,primary_key=True) 
    pid = models.BigIntegerField()

    visitcat = models.CharField(max_length=30,null=True)
    pclass = models.CharField(max_length=30,null=True)
    ptype = models.CharField(max_length=30,null=True)
    sensitivity = models.CharField(max_length=30,null=True)
    dos = models.CharField(max_length=100,null=True)
    onsetdt = models.CharField(max_length=30,null=True)
    encprovider = models.CharField(max_length=30,null=True)
    referprovider = models.CharField(max_length=30,null=True)
    facility = models.CharField(max_length=30,null=True)
    dischargedisposition = models.CharField(max_length=50,null=True)
    visitreason = models.TextField(null=True,blank=True)


class ROS(models.Model):
    encid = models.CharField(max_length=100,primary_key=True) 
    pid = models.BigIntegerField()


    chestpain = models.CharField(max_length=3,null=True)
    pnd = models.CharField(max_length=3,null=True)
    historyofheartmurmur = models.CharField(max_length=3,null=True)
    peripheral = models.CharField(max_length=3,null=True)
    palpitation = models.CharField(max_length=3,null=True)
    doe = models.CharField(max_length=3,null=True)
    edema = models.CharField(max_length=3,null=True)
    arrythmia = models.CharField(max_length=3,null=True)
    syncope = models.CharField(max_length=3,null=True)
    orthopnea = models.CharField(max_length=3,null=True)
    legpain = models.CharField(max_length=3,null=True)
    heartproblem = models.CharField(max_length=3,null=True)
    cough = models.CharField(max_length=3,null=True)
    wheezing = models.CharField(max_length=3,null=True)
    copd = models.CharField(max_length=3,null=True)
    sputum = models.CharField(max_length=3,null=True)
    hemoptysis = models.CharField(max_length=3,null=True)
    shortnessofbreath = models.CharField(max_length=3,null=True)
    asthma = models.CharField(max_length=3,null=True)
    breastmass = models.CharField(max_length=3,null=True)
    abnormalmammogram = models.CharField(max_length=3,null=True)
    discharge = models.CharField(max_length=3,null=True)
    biopsy = models.CharField(max_length=3,null=True)
    hearingloss = models.CharField(max_length=3,null=True)
    vertigo = models.CharField(max_length=3,null=True)
    sorethroat = models.CharField(max_length=3,null=True)
    nosebleed = models.CharField(max_length=3,null=True)
    discharge = models.CharField(max_length=3,null=True)
    tinnitus = models.CharField(max_length=3,null=True)
    sinusproblem = models.CharField(max_length=3,null=True)
    snoring = models.CharField(max_length=3,null=True)
    pain = models.CharField(max_length=3,null=True)
    frequentcolds = models.CharField(max_length=3,null=True)
    postnasaldrip = models.CharField(max_length=3,null=True)
    apnea = models.CharField(max_length=3,null=True)
    changeinvision = models.CharField(max_length=3,null=True)
    irritation = models.CharField(max_length=3,null=True)
    doublevision = models.CharField(max_length=3,null=True)
    familyhistoryofglaucoma = models.CharField(max_length=3,null=True)
    redness = models.CharField(max_length=3,null=True)
    blindspots = models.CharField(max_length=3,null=True)
    eyepain = models.CharField(max_length=3,null=True)
    excessivetearing = models.CharField(max_length=3,null=True)
    photophobia = models.CharField(max_length=3,null=True)
    weightchange = models.CharField(max_length=3,null=True)
    anorexia = models.CharField(max_length=3,null=True)
    nightsweats = models.CharField(max_length=3,null=True)
    heatorcold = models.CharField(max_length=3,null=True)
    weakness = models.CharField(max_length=3,null=True)
    fever = models.CharField(max_length=3,null=True)
    insomnia = models.CharField(max_length=3,null=True)
    intolerence = models.CharField(max_length=3,null=True)
    fatigue = models.CharField(max_length=3,null=True)
    chills = models.CharField(max_length=3,null=True)
    irritability = models.CharField(max_length=3,null=True)





   
class Vitals(models.Model):
    encid = models.CharField(max_length=100,primary_key=True) 
    pid = models.BigIntegerField()


    weight = models.CharField(max_length=3,null=True,blank=True)
    height = models.CharField(max_length=3,null=True,blank=True)
    bpsystolic = models.CharField(max_length=3,null=True,blank=True)
    bpdiastolic = models.CharField(max_length=3,null=True,blank=True)
    pulse = models.CharField(max_length=3,null=True,blank=True)
    respiration = models.CharField(max_length=3,null=True,blank=True)
    temperature = models.CharField(max_length=3,null=True,blank=True)
    oxygensaturation = models.CharField(max_length=3,null=True,blank=True)
    oxygenflowrate = models.CharField(max_length=3,null=True,blank=True)
    inhaledoxygenconc = models.CharField(max_length=3,null=True,blank=True)
    headcircumference = models.CharField(max_length=3,null=True,blank=True)
    waistcircumference = models.CharField(max_length=3,null=True,blank=True)
    bmi = models.CharField(max_length=3,null=True,blank=True)
    pediatricbmipercentile = models.CharField(max_length=3,null=True,blank=True)



    weightabn = models.CharField(max_length=20,null=True)
    heightabn = models.CharField(max_length=20,null=True)
    bpsystolicabn = models.CharField(max_length=20,null=True)
    bpdiastolicabn = models.CharField(max_length=20,null=True)
    pulseabn = models.CharField(max_length=20,null=True)
    respirationabn = models.CharField(max_length=20,null=True)
    temperatureabn = models.CharField(max_length=20,null=True)
    oxygensaturationabn = models.CharField(max_length=20,null=True)
    oxygenflowrateabn = models.CharField(max_length=20,null=True)
    inhaledoxygenconcabn = models.CharField(max_length=20,null=True)
    headcircumferenceabn = models.CharField(max_length=20,null=True)
    waistcircumferenceabn = models.CharField(max_length=20,null=True)
    bmiabn = models.CharField(max_length=20,null=True)
    pediatricbmipercentileabn = models.CharField(max_length=20,null=True)




class SOAP(models.Model):
    encid = models.CharField(max_length=100,primary_key=True) 
    pid = models.BigIntegerField()

    subjective=models.TextField(max_length=500,blank=True,null=True)
    objective=models.TextField(max_length=500,blank=True,null=True)
    assesment=models.TextField(max_length=500,blank=True,null=True)
    plan=models.TextField(max_length=500,blank=True,null=True)




class ClinicalNotes(models.Model):
    encid = models.CharField(max_length=100,primary_key=True) 
    pid = models.BigIntegerField()


    date = models.DateField(null=True,blank=True)
    type = models.CharField(max_length=30,blank=True,null=True)
    category= models.CharField(max_length=30,blank=True,null=True)
    narrative = models.TextField(max_length=500,blank=True,null=True)



class MedicalProblems(models.Model):
    problemid=models.CharField(max_length=100,primary_key=True)
    pid = models.BigIntegerField()

    problem =models.CharField(max_length=30,null=True,blank=True)
    other = models.CharField(max_length=30,null=True,blank=True)
    coding = models.CharField(max_length=50,null=True,blank=True)
    begindate = models.DateField(null=True,blank=True)
    enddate= models.DateField(null=True,blank=True)
    clstype = models.CharField(max_length=30,null=True,blank=True)
    occurence = models.CharField(max_length=30,null=True,blank=True)
    verificationstatus = models.CharField(max_length=30,null=True,blank=True)
    referredby = models.CharField(max_length=30,null=True,blank=True)
    comments = models.TextField(max_length=200,null=True,blank=True)
    outcome = models.CharField(max_length=30,null=True,blank=True)

class Prescription(models.Model):
    pid = models.BigIntegerField()
    prescid=models.CharField(max_length=100,primary_key=True)

    startdate = models.DateField(null=True,blank=True)
    provider = models.CharField(max_length=30,null=True,blank=True)
    drug = models.CharField(max_length=30,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    notes = models.TextField(max_length=200,null=True,blank=True)














class PatientHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=16, blank=True, null=True)
    date = models.DateField(null=True,blank=True)
    careteam = models.TextField(blank=True, null=True)
    carefacility = models.TextField(blank=True, null=True)
    pid = models.BigIntegerField()
    history_type = models.CharField(max_length=36, blank=True, null=True)
    created_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'patient_history'









