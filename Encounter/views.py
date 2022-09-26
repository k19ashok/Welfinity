import re
from django.http import HttpResponse
from random import random
from django.shortcuts import render,redirect
from django.http import request
from django.contrib import messages
import random

from Encounter.models import *
# Create your views here.

def emr(request):
    if request.method=='POST':
        searchid=request.POST.get('searchid')
        print(searchid)
        if searchid:
            try:
                pt=PatientData.objects.get(pid=searchid)
            except:
                messages.info(request,"No Patient Exists with the ID "+searchid)
                return redirect('emr')
            return redirect('dash',pt.pid)

        print(request)
        title = request.POST.get('title')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dob = request.POST.get('dob') or None
        if not dob:
            dob=None
        sex = request.POST.get('sex')
        extid = request.POST.get('extid')
        licid = request.POST.get('licid')
        prevnames = request.POST.get('prevnames')
        address = request.POST.get('address')
        addressline2 = request.POST.get('addressline2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        altphone = request.POST.get('altphone')
        careteam = request.POST.get('careteam')
        carefacility = request.POST.get('carefacility')
        hipaa = request.POST.get('hipaa')
        allowvoice = request.POST.get('allowvoice')
        allowmail = request.POST.get('allowmail')
        leavemsg = request.POST.get('leavemsg')
        allowimmreg = request.POST.get('allowimmreg')
        allowimmshare = request.POST.get('allowimmshare')
        allowhie = request.POST.get('allowhie')
        allowpp = request.POST.get('allowpp')
        imstatus = request.POST.get('immstatus')
        imstatusdt = request.POST.get('immstatusdt')
        if not imstatusdt:
            imstatusdt=None
        pubcode = request.POST.get('pubcode')
        pubcodedate = request.POST.get('pubcodedate') or None
        if not pubcodedate:
            pubcodedate=None
        protind = request.POST.get('protind')
        protinddate = request.POST.get('protinddate') or None
        if not protinddate:
            protinddate=None
        carestatus = request.POST.get('carestatus')
        ptcat = request.POST.get('ptcat')
        occupation = request.POST.get('occupation')
        industry = request.POST.get('industry')
        empname = request.POST.get('empname')
        empaddress = request.POST.get('empaddress')
        language = request.POST.get('language')
        ethnicity = request.POST.get('ethnicity')
        famsize = request.POST.get('famsize')
        finreview = request.POST.get('finreview')
        if not finreview:
            finreview=None
        income = request.POST.get('income')
        homeless = request.POST.get('homeless')
        migrant = request.POST.get('migrant')
        religion = request.POST.get('religion')
        vfc = request.POST.get('vfc')
        deceased = request.POST.get('deceased') or None
        if not deceased:
            deceased=None
        reasondeceased = request.POST.get('reasondeceased')
        guardian = request.POST.get('guardian')
        guardianrelation = request.POST.get('guardianrelation')
        guardiansex = request.POST.get('guardiansex')
        guardaddress = request.POST.get('guardaddress')
        guardaddressline2 = request.POST.get('guardaddressline2')
        guardcity = request.POST.get('guardcity')
        guardstate = request.POST.get('guardstate')
        guardpin = request.POST.get('guardpin')
        guardcountry = request.POST.get('guardcountry')
        guardphone = request.POST.get('guardphone')
        guardemail = request.POST.get('guardemail')

        
        nums=list(range(10))
        
        
        while True:
            id=random.choices(nums,k=8)
            id=''.join(list(map(str,id)))
            try:
                PatientData.objects.get(pid=id)
            except:
                break



        pt=PatientData(id=id,pid=id,title = title, fname = firstname, lname = lastname, dob = dob, sex = sex, extid = extid, licid = licid, prevnames = prevnames, address = address, addressline2 = addressline2, city = city, state = state, pin = pin, country = country, phone = phone, email = email, altphone = altphone, careteam = careteam, carefacility = carefacility, hipaa = hipaa, allowvoice = allowvoice, allowmail = allowmail, leavemsg = leavemsg, allowimmreg = allowimmreg, allowimmshare = allowimmshare, allowhie = allowhie, allowpp = allowpp, immstatus = imstatus, immstatusdt = imstatusdt, pubcode = pubcode, pubcodedate = pubcodedate, protind = protind, protinddate = protinddate, carestatus = carestatus, ptcat = ptcat, occupation = occupation, industry = industry, empname = empname, empaddress = empaddress, language = language, ethnicity = ethnicity, famsize = famsize, finreview = finreview, income = income, homeless = homeless, migrant = migrant, religion = religion, vfc = vfc, deceased = deceased, reasondeceased = reasondeceased, guardian = guardian, guardianrelation = guardianrelation, guardiansex = guardiansex, guardianaddress = guardaddress, guardianaddressline2 = guardaddressline2, guardiancity = guardcity, guardianstate = guardstate, guardianpin = guardpin, guardiancountry = guardcountry, guardianphone = guardphone, guardianemail = guardemail)
        print(pt)
        pt.save()

        
        return redirect('dash',pt.pid)
    else:
        return render(request,'emr.html')

def dash(request,pid=None):
    if pid:
        x=PatientData.objects.all()
        print(x)
        pt=PatientData.objects.get(pid=pid)
        enc=Encounter.objects.filter(pid=pid)
        print(enc)

        try:
            mp=MedicalProblems.objects.filter(pid=pid)
            try:
                p=Prescription.objects.filter(pid=pid)
                return render(request,'dashboard.html',{'pt':pt,'enc':enc,'p':p,'mp':mp})
            except:
                return render(request,'dashboard.html',{'pt':pt,'enc':enc,'mp':mp})
        except:
            return render(request,'dashboard.html',{'pt':pt,'enc':enc})
    
    return render(request,'dashboard.html')

import datetime

def encounter(request,pid):
    if request.method=='POST':
        encid=''
        x = datetime.datetime.now()
        x=str(x)
        for i in x:
            if i in '1234567890':
                encid+=i
         
        pid = pid

        visitcat = request.POST.get('visitcat')
        pclass = request.POST.get('pclass')
        ptype = request.POST.get('ptype')
        sensitivity = request.POST.get('sensitivity')
        dos = request.POST.get('dos')
        onsetdt = request.POST.get('onsetdt')
        encprovider = request.POST.get('encprovider')
        referprovider = request.POST.get('referprovider')
        facility = request.POST.get('facility')
        dischargedisposition = request.POST.get('dischargedisposition')
        visitreason = request.POST.get('visitreason')

        ec=Encounter(encid=encid,pid=pid,visitcat=visitcat,pclass=pclass,ptype=ptype,sensitivity=sensitivity,dos=dos,onsetdt=onsetdt,encprovider=encprovider,referprovider=referprovider,facility=facility,dischargedisposition=dischargedisposition,visitreason=visitreason)
        vitals=Vitals(pid=pid,encid=encid)
        soap=SOAP(pid=pid,encid=encid)
        notes=ClinicalNotes(pid=pid,encid=encid)
        ros=ROS(pid=pid,encid=encid)
        vitals.save()
        soap.save()
        notes.save()
        ros.save()
        ec.save()

        return redirect('encSummary',pid,encid)
    else:
        return redirect('dash',pid)



def encSummary(request,pid,encid):
    pt=PatientData.objects.get(pid=pid)
    enc=Encounter.objects.get(encid=encid)
    vitals=Vitals.objects.get(encid=encid)
    notes=ClinicalNotes.objects.get(encid=encid)
    ros=ROS.objects.get(encid=encid)
    soap=SOAP.objects.get(encid=encid)
    return render(request,'encounter.html',{'enc':enc,'pt':pt,'vitals':vitals,'notes':notes,'ros':ros,'soap':soap})


def getEnc(request,pid):
    if request.method=='POST':
        encid=request.POST.get('encval')
        enc=Encounter.objects.get(encid=encid)
        return redirect('encSummary',pid,encid)
    return redirect('dash',pid)


def form(request):
    return render(request,'Forms.html')


def saveros(request,encid,pid):
    if request.method=='POST':
        chestpain = request.POST.get('chestpain')
        pnd = request.POST.get('pnd')
        historyofheartmurmur = request.POST.get('historyofheartmurmur')
        peripheral = request.POST.get('peripheral')
        palpitation = request.POST.get('palpitation')
        doe = request.POST.get('doe')
        edema = request.POST.get('edema')
        arrythmia = request.POST.get('arrythmia')
        syncope = request.POST.get('syncope')
        orthopnea = request.POST.get('orthopnea')
        legpain = request.POST.get('legpain')
        heartproblem = request.POST.get('heartproblem')
        cough = request.POST.get('cough')
        wheezing = request.POST.get('wheezing')
        copd = request.POST.get('copd')
        sputum = request.POST.get('sputum')
        hemoptysis = request.POST.get('hemoptysis')
        shortnessofbreath = request.POST.get('shortnessofbreath')
        asthma = request.POST.get('asthma')
        breastmass = request.POST.get('breastmass')
        abnormalmammogram = request.POST.get('abnormalmammogram')
        discharge = request.POST.get('discharge')
        biopsy = request.POST.get('biopsy')
        hearingloss = request.POST.get('hearingloss')
        vertigo = request.POST.get('vertigo')
        sorethroat = request.POST.get('sorethroat')
        nosebleed = request.POST.get('nosebleed')
        discharge = request.POST.get('discharge')
        tinnitus = request.POST.get('tinnitus')
        sinusproblem = request.POST.get('sinusproblem')
        snoring = request.POST.get('snoring')
        pain = request.POST.get('pain')
        frequentcolds = request.POST.get('frequentcolds')
        postnasaldrip = request.POST.get('postnasaldrip')
        apnea = request.POST.get('apnea')
        changeinvision = request.POST.get('changeinvision')
        irritation = request.POST.get('irritation')
        doublevision = request.POST.get('doublevision')
        familyhistoryofglaucoma = request.POST.get('familyhistoryofglaucoma')
        redness = request.POST.get('redness')
        blindspots = request.POST.get('blindspots')
        eyepain = request.POST.get('eyepain')
        excessivetearing = request.POST.get('excessivetearing')
        photophobia = request.POST.get('photophobia')
        weightchange = request.POST.get('weightchange')
        anorexia = request.POST.get('anorexia')
        nightsweats = request.POST.get('nightsweats')
        heatorcold = request.POST.get('heatorcold')
        weakness = request.POST.get('weakness')
        fever = request.POST.get('fever')
        insomnia = request.POST.get('insomnia')
        intolerence = request.POST.get('intolerence')
        fatigue = request.POST.get('fatigue')
        chills = request.POST.get('chills')
        irritability = request.POST.get('irritability')




        

        try:
            ros=ROS.objects.filter(encid=encid)
            ros.update(chestpain=chestpain,pnd=pnd,historyofheartmurmur=historyofheartmurmur,peripheral=peripheral,palpitation=palpitation,doe=doe,edema=edema,arrythmia=arrythmia,syncope=syncope,orthopnea=orthopnea,legpain=legpain,heartproblem=heartproblem,cough=cough,wheezing=wheezing,copd=copd,sputum=sputum,hemoptysis=hemoptysis,shortnessofbreath=shortnessofbreath,asthma=asthma,breastmass=breastmass,abnormalmammogram=abnormalmammogram,discharge=discharge,biopsy=biopsy,hearingloss=hearingloss,vertigo=vertigo,sorethroat=sorethroat,nosebleed=nosebleed,tinnitus=tinnitus,sinusproblem=sinusproblem,snoring=snoring,pain=pain,frequentcolds=frequentcolds,postnasaldrip=postnasaldrip,apnea=apnea,changeinvision=changeinvision,irritation=irritation,doublevision=doublevision,familyhistoryofglaucoma=familyhistoryofglaucoma,redness=redness,blindspots=blindspots,eyepain=eyepain,excessivetearing=excessivetearing,photophobia=photophobia,weightchange=weightchange,anorexia=anorexia,nightsweats=nightsweats,heatorcold=heatorcold,weakness=weakness,fever=fever,insomnia=insomnia,intolerence=intolerence,fatigue=fatigue,chills=chills,irritability=irritability)

        except:
            ros=ROS(encid=encid,pid=pid,chestpain=chestpain,pnd=pnd,historyofheartmurmur=historyofheartmurmur,peripheral=peripheral,palpitation=palpitation,doe=doe,edema=edema,arrythmia=arrythmia,syncope=syncope,orthopnea=orthopnea,legpain=legpain,heartproblem=heartproblem,cough=cough,wheezing=wheezing,copd=copd,sputum=sputum,hemoptysis=hemoptysis,shortnessofbreath=shortnessofbreath,asthma=asthma,breastmass=breastmass,abnormalmammogram=abnormalmammogram,biopsy=biopsy,hearingloss=hearingloss,vertigo=vertigo,sorethroat=sorethroat,nosebleed=nosebleed,discharge=discharge,tinnitus=tinnitus,sinusproblem=sinusproblem,snoring=snoring,pain=pain,frequentcolds=frequentcolds,postnasaldrip=postnasaldrip,apnea=apnea,changeinvision=changeinvision,irritation=irritation,doublevision=doublevision,familyhistoryofglaucoma=familyhistoryofglaucoma,redness=redness,blindspots=blindspots,eyepain=eyepain,excessivetearing=excessivetearing,photophobia=photophobia,weightchange=weightchange,anorexia=anorexia,nightsweats=nightsweats,heatorcold=heatorcold,weakness=weakness,fever=fever,insomnia=insomnia,intolerence=intolerence,fatigue=fatigue,chills=chills,irritability=irritability)
            ros.save()
        

    return redirect('encSummary',pid,encid)


def savesoap(request,pid,encid):

    if request.method=='POST':

        subjective = request.POST.get('subjective')
        objective = request.POST.get('objective')
        assesment = request.POST.get('assesment')
        plan = request.POST.get('plan')
        try:
            sp=SOAP.objects.filter(encid=encid)
            sp.update(subjective=subjective,objective=objective,assesment=assesment,plan=plan)
        except:
            sp=SOAP(pid=pid,encid=encid,subjective=subjective,objective=objective,assesment=assesment,plan=plan)

            sp.save()

    return redirect('encSummary',pid,encid)


def savevitals(request,pid,encid):

    if request.method=='POST':
        weightabn = request.POST.get('weightabn')
        heightabn = request.POST.get('heightabn')
        bpsystolicabn = request.POST.get('bpsystolicabn')
        bpdiastolicabn = request.POST.get('bpdiastolicabn')
        pulseabn = request.POST.get('pulseabn')
        respirationabn = request.POST.get('respirationabn')
        temperatureabn = request.POST.get('temperatureabn')
        oxygensaturationabn = request.POST.get('oxygensaturationabn')
        oxygenflowrateabn = request.POST.get('oxygenflowrateabn')
        inhaledoxygenconcabn = request.POST.get('inhaledoxygenconcabn')
        headcircumferenceabn = request.POST.get('headcircumferenceabn')
        waistcircumferenceabn = request.POST.get('waistcircumferenceabn')
        bmiabn = request.POST.get('bmiabn')
        pediatricbmipercentileabn = request.POST.get('pediatricbmipercentileabn')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        bpsystolic = request.POST.get('bpsystolic')
        bpdiastolic = request.POST.get('bpdiastolic')
        pulse = request.POST.get('pulse')
        respiration = request.POST.get('respiration')
        temperature = request.POST.get('temperature')
        oxygensaturation = request.POST.get('oxygensaturation')
        oxygenflowrate = request.POST.get('oxygenflowrate')
        inhaledoxygenconc = request.POST.get('inhaledoxygenconc')
        headcircumference = request.POST.get('headcircumference')
        waistcircumference = request.POST.get('waistcircumference')
        bmi = request.POST.get('bmi')
        pediatricbmipercentile = request.POST.get('pediatricbmipercentile')

        l=[weightabn, heightabn, bpsystolicabn, bpdiastolicabn, pulseabn, respirationabn, temperatureabn, oxygensaturationabn, oxygenflowrateabn, inhaledoxygenconcabn, headcircumferenceabn, waistcircumferenceabn, bmiabn, pediatricbmipercentileabn, weight, height, bpsystolic, bpdiastolic, pulse, respiration, temperature, oxygensaturation, oxygenflowrate, inhaledoxygenconc, headcircumference, waistcircumference, bmi, pediatricbmipercentile]

        ll=['weightabn', 'heightabn', 'bpsystolicabn', 'bpdiastolicabn', 'pulseabn', 'respirationabn', 'temperatureabn', 'oxygensaturationabn', 'oxygenflowrateabn', 'inhaledoxygenconcabn', 'headcircumferenceabn', 'waistcircumferenceabn', 'bmiabn', 'pediatricbmipercentileabn', 'weight', 'height', 'bpsystolic', 'bpdiastolic', 'pulse', 'respiration', 'temperature', 'oxygensaturation', 'oxygenflowrate', 'inhaledoxygenconc', 'headcircumference', 'waistcircumference', 'bmi', 'pediatricbmipercentile']


        try:
            v=Vitals.objects.filter(encid=encid)
            v.update(encid=encid,pid=pid,weightabn=weightabn,heightabn=heightabn,bpsystolicabn=bpsystolicabn,bpdiastolicabn=bpdiastolicabn,pulseabn=pulseabn,respirationabn=respirationabn,temperatureabn=temperatureabn,oxygensaturationabn=oxygensaturationabn,oxygenflowrateabn=oxygenflowrateabn,inhaledoxygenconcabn=inhaledoxygenconcabn,headcircumferenceabn=headcircumferenceabn,waistcircumferenceabn=waistcircumferenceabn,bmiabn=bmiabn,pediatricbmipercentileabn=pediatricbmipercentileabn,weight=weight,height=height,bpsystolic=bpsystolic,bpdiastolic=bpdiastolic,pulse=pulse,respiration=respiration,temperature=temperature,oxygensaturation=oxygensaturation,oxygenflowrate=oxygenflowrate,inhaledoxygenconc=inhaledoxygenconc,headcircumference=headcircumference,waistcircumference=waistcircumference,bmi=bmi,pediatricbmipercentile=pediatricbmipercentile)
        except:
            v=Vitals(encid=encid,pid=pid,weightabn=weightabn,heightabn=heightabn,bpsystolicabn=bpsystolicabn,bpdiastolicabn=bpdiastolicabn,pulseabn=pulseabn,respirationabn=respirationabn,temperatureabn=temperatureabn,oxygensaturationabn=oxygensaturationabn,oxygenflowrateabn=oxygenflowrateabn,inhaledoxygenconcabn=inhaledoxygenconcabn,headcircumferenceabn=headcircumferenceabn,waistcircumferenceabn=waistcircumferenceabn,bmiabn=bmiabn,pediatricbmipercentileabn=pediatricbmipercentileabn,weight=weight,height=height,bpsystolic=bpsystolic,bpdiastolic=bpdiastolic,pulse=pulse,respiration=respiration,temperature=temperature,oxygensaturation=oxygensaturation,oxygenflowrate=oxygenflowrate,inhaledoxygenconc=inhaledoxygenconc,headcircumference=headcircumference,waistcircumference=waistcircumference,bmi=bmi,pediatricbmipercentile=pediatricbmipercentile)
            v.save()
    return redirect('encSummary',pid,encid)



def savenotes(request,pid,encid):
    if request.method=='POST':

        date = request.POST.get('date')
        type = request.POST.get('type')
        category = request.POST.get('category')
        narrative=request.POST.get('narrative')

        try:
            note=ClinicalNotes.objects.filter(encid=encid)
            note.update(date=date,type=type,category=category,narrative=narrative)
        except:
            note=ClinicalNotes(pid=pid,encid=encid,date=date,type=type,category=category,narrative=narrative)
            note.save()

    return redirect('encSummary',pid,encid)


def addMedicalProblem(request,pid):
    if request.method=='POST':
        nums=list(range(10))
        while True:
            id=random.choices(nums,k=8)
            id=''.join(list(map(str,id)))
            try:
                MedicalProblems.objects.get(problemid=id)
            except:
                break
        problem=request.POST.get('problem')
        other=request.POST.get('other')
        coding=request.POST.get('coding')
        begindate=request.POST.get('begindate') or None
        enddate=request.POST.get('enddate') or None
        clstype=request.POST.get('clstype')
        occurence=request.POST.get('occurence')
        verificationstatus=request.POST.get('verificationstatus')
        referredby=request.POST.get('referredby')
        comments=request.POST.get('comments')
        outcome=request.POST.get('ooutcome')


        mp=MedicalProblems(pid=pid,problemid=id,problem=problem,other=other,coding=coding,begindate=begindate,enddate=enddate,clstype=clstype,occurence=occurence,verificationstatus=verificationstatus,referredby=referredby,comments=comments,outcome=outcome)
        mp.save()

    return redirect('dash',pid)

def addPrescription(request,pid):
    if request.method=='POST':
        nums=list(range(10))
        while True:
            id=random.choices(nums,k=8)
            id=''.join(list(map(str,id)))
            try:
                Prescription.objects.get(prescid=id)
            except:
                break
        startdate=request.POST.get('startdate')
        provider=request.POST.get('provider')
        drug=request.POST.get('drug')
        quantity=request.POST.get('quantity')
        notes=request.POST.get('notes')

        p=Prescription(pid=pid,prescid=id,startdate=startdate,provider=provider,drug=drug,quantity=quantity,notes=notes)

        p.save()
    return redirect('dash',pid)

        


