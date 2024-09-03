# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Apilogs(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    level = models.CharField(max_length=10, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apilogs'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Logrecords(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    level = models.CharField(max_length=10, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logrecords'


class Lookup(models.Model):
    lookupkey = models.TextField(db_column='LookupKey', primary_key=True)  # Field name made lowercase.
    lookupname = models.TextField(db_column='LookupName', blank=True, null=True)  # Field name made lowercase.
    lookupvalue = models.TextField(db_column='LookupValue', blank=True, null=True)  # Field name made lowercase.
    mlgcanuse = models.TextField(db_column='MlgCanUse', blank=True, null=True)  # Field name made lowercase.
    mlgcanview = models.IntegerField(db_column='MlgCanView', blank=True, null=True)  # Field name made lowercase.
    modificationtimestamp = models.DateTimeField(db_column='ModificationTimestamp', blank=True, null=True)  # Field name made lowercase.
    originatingsystemname = models.TextField(db_column='OriginatingSystemName', blank=True, null=True)  # Field name made lowercase.
    standardlookupvalue = models.TextField(db_column='StandardLookupValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lookup'


class Media(models.Model):
    imageheight = models.BigIntegerField(db_column='ImageHeight', blank=True, null=True)  # Field name made lowercase.
    imagesizedescription = models.TextField(db_column='ImageSizeDescription', blank=True, null=True)  # Field name made lowercase.
    imagewidth = models.BigIntegerField(db_column='ImageWidth', blank=True, null=True)  # Field name made lowercase.
    longdescription = models.TextField(db_column='LongDescription', blank=True, null=True)  # Field name made lowercase.
    mediakey = models.TextField(db_column='MediaKey', primary_key=True)  # Field name made lowercase.
    mediamodificationtimestamp = models.DateTimeField(db_column='MediaModificationTimestamp', blank=True, null=True)  # Field name made lowercase.
    mediaobjectid = models.TextField(db_column='MediaObjectID', blank=True, null=True)  # Field name made lowercase.
    mediatype = models.TextField(db_column='MediaType', blank=True, null=True)  # Field name made lowercase.
    mediaurl = models.TextField(db_column='MediaURL', blank=True, null=True)  # Field name made lowercase.
    order = models.SmallIntegerField(db_column='Order', blank=True, null=True)  # Field name made lowercase.
    preferredphotoyn = models.IntegerField(db_column='PreferredPhotoYN', blank=True, null=True)  # Field name made lowercase.
    resourcerecordkey = models.TextField(db_column='ResourceRecordKey', blank=True, null=True)  # Field name made lowercase.
    listingid = models.TextField(db_column='ListingId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'media'


class Member(models.Model):
    memberaddress1 = models.TextField(db_column='MemberAddress1', blank=True, null=True)  # Field name made lowercase.
    memberaddress2 = models.TextField(db_column='MemberAddress2', blank=True, null=True)  # Field name made lowercase.
    memberaor = models.TextField(db_column='MemberAOR', blank=True, null=True)  # Field name made lowercase.
    membercity = models.TextField(db_column='MemberCity', blank=True, null=True)  # Field name made lowercase.
    memberdesignation = models.TextField(db_column='MemberDesignation', blank=True, null=True)  # Field name made lowercase.
    memberdirectphone = models.CharField(db_column='MemberDirectPhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    memberemail = models.TextField(db_column='MemberEmail', blank=True, null=True)  # Field name made lowercase.
    memberfax = models.CharField(db_column='MemberFax', max_length=16, blank=True, null=True)  # Field name made lowercase.
    memberfirstname = models.TextField(db_column='MemberFirstName', blank=True, null=True)  # Field name made lowercase.
    memberfullname = models.TextField(db_column='MemberFullName', blank=True, null=True)  # Field name made lowercase.
    memberhomephone = models.CharField(db_column='MemberHomePhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    memberkey = models.TextField(db_column='MemberKey', blank=True, null=True)  # Field name made lowercase.
    memberlastname = models.TextField(db_column='MemberLastName', blank=True, null=True)  # Field name made lowercase.
    membermiddlename = models.TextField(db_column='MemberMiddleName', blank=True, null=True)  # Field name made lowercase.
    membermlsid = models.CharField(db_column='MemberMlsId', primary_key=True, max_length=25)  # Field name made lowercase.
    membermobilephone = models.CharField(db_column='MemberMobilePhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    membernationalassociationid = models.CharField(db_column='MemberNationalAssociationId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    membernickname = models.TextField(db_column='MemberNickname', blank=True, null=True)  # Field name made lowercase.
    memberpostalcode = models.CharField(db_column='MemberPostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    memberstatelicense = models.TextField(db_column='MemberStateLicense', blank=True, null=True)  # Field name made lowercase.
    memberstateorprovince = models.CharField(db_column='MemberStateOrProvince', max_length=2, blank=True, null=True)  # Field name made lowercase.
    memberstatus = models.CharField(db_column='MemberStatus', max_length=25, blank=True, null=True)  # Field name made lowercase.
    membertype = models.TextField(db_column='MemberType', blank=True, null=True)  # Field name made lowercase.
    mfr_memberrosterflagyn = models.TextField(db_column='MFR_MemberRosterFlagYN', blank=True, null=True)  # Field name made lowercase.
    mfr_officeaor = models.TextField(db_column='MFR_OfficeAOR', blank=True, null=True)  # Field name made lowercase.
    mfr_thompsonbrokeryn = models.TextField(db_column='MFR_ThompsonBrokerYN', blank=True, null=True)  # Field name made lowercase.
    mlgcanuse = models.TextField(db_column='MlgCanUse', blank=True, null=True)  # Field name made lowercase.
    mlgcanview = models.IntegerField(db_column='MlgCanView', blank=True, null=True)  # Field name made lowercase.
    modificationtimestamp = models.DateTimeField(db_column='ModificationTimestamp', blank=True, null=True)  # Field name made lowercase.
    officekey = models.TextField(db_column='OfficeKey', blank=True, null=True)  # Field name made lowercase.
    officemlsid = models.CharField(db_column='OfficeMlsId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    originatingsystemmemberkey = models.TextField(db_column='OriginatingSystemMemberKey', blank=True, null=True)  # Field name made lowercase.
    originatingsystemmodificationtimestamp = models.DateTimeField(db_column='OriginatingSystemModificationTimestamp', blank=True, null=True)  # Field name made lowercase.
    originatingsystemname = models.TextField(db_column='OriginatingSystemName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member'


class Office(models.Model):
    idxofficeparticipationyn = models.IntegerField(db_column='IDXOfficeParticipationYN', blank=True, null=True)  # Field name made lowercase.
    mainofficekey = models.TextField(db_column='MainOfficeKey', blank=True, null=True)  # Field name made lowercase.
    mainofficemlsid = models.CharField(db_column='MainOfficeMlsId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    mfr_officecontactpreferred = models.TextField(db_column='MFR_OfficeContactPreferred', blank=True, null=True)  # Field name made lowercase.
    mfr_officelongname = models.TextField(db_column='MFR_OfficeLongName', blank=True, null=True)  # Field name made lowercase.
    mfr_officerosterflagyn = models.TextField(db_column='MFR_OfficeRosterFlagYN', blank=True, null=True)  # Field name made lowercase.
    mlgcanuse = models.TextField(db_column='MlgCanUse', blank=True, null=True)  # Field name made lowercase.
    mlgcanview = models.IntegerField(db_column='MlgCanView', blank=True, null=True)  # Field name made lowercase.
    modificationtimestamp = models.DateTimeField(db_column='ModificationTimestamp', blank=True, null=True)  # Field name made lowercase.
    officeaddress1 = models.TextField(db_column='OfficeAddress1', blank=True, null=True)  # Field name made lowercase.
    officeaddress2 = models.TextField(db_column='OfficeAddress2', blank=True, null=True)  # Field name made lowercase.
    officeaor = models.TextField(db_column='OfficeAOR', blank=True, null=True)  # Field name made lowercase.
    officebrokerkey = models.TextField(db_column='OfficeBrokerKey', blank=True, null=True)  # Field name made lowercase.
    officecity = models.TextField(db_column='OfficeCity', blank=True, null=True)  # Field name made lowercase.
    officeemail = models.TextField(db_column='OfficeEmail', blank=True, null=True)  # Field name made lowercase.
    officefax = models.CharField(db_column='OfficeFax', max_length=16, blank=True, null=True)  # Field name made lowercase.
    officekey = models.TextField(db_column='OfficeKey', blank=True, null=True)  # Field name made lowercase.
    officemanagerkey = models.TextField(db_column='OfficeManagerKey', blank=True, null=True)  # Field name made lowercase.
    officemanagermlsid = models.CharField(db_column='OfficeManagerMlsId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    officemlsid = models.CharField(db_column='OfficeMlsId', primary_key=True, max_length=25)  # Field name made lowercase.
    officename = models.TextField(db_column='OfficeName', blank=True, null=True)  # Field name made lowercase.
    officenationalassociationid = models.CharField(db_column='OfficeNationalAssociationId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    officephone = models.CharField(db_column='OfficePhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    officepostalcode = models.CharField(db_column='OfficePostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    officestateorprovince = models.CharField(db_column='OfficeStateOrProvince', max_length=2, blank=True, null=True)  # Field name made lowercase.
    officestatus = models.CharField(db_column='OfficeStatus', max_length=25, blank=True, null=True)  # Field name made lowercase.
    officetype = models.TextField(db_column='OfficeType', blank=True, null=True)  # Field name made lowercase.
    originalentrytimestamp = models.DateTimeField(db_column='OriginalEntryTimestamp', blank=True, null=True)  # Field name made lowercase.
    originatingsystemname = models.TextField(db_column='OriginatingSystemName', blank=True, null=True)  # Field name made lowercase.
    originatingsystemofficekey = models.TextField(db_column='OriginatingSystemOfficeKey', blank=True, null=True)  # Field name made lowercase.
    photoschangetimestamp = models.DateTimeField(db_column='PhotosChangeTimestamp', blank=True, null=True)  # Field name made lowercase.
    syndicateto = models.TextField(db_column='SyndicateTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'office'


class Openhouse(models.Model):
    listingid = models.TextField(db_column='ListingId', blank=True, null=True)  # Field name made lowercase.
    listingkey = models.TextField(db_column='ListingKey', blank=True, null=True)  # Field name made lowercase.
    mfr_virtualopenhouseurl = models.TextField(db_column='MFR_VirtualOpenHouseURL', blank=True, null=True)  # Field name made lowercase.
    mlgcanuse = models.TextField(db_column='MlgCanUse', blank=True, null=True)  # Field name made lowercase.
    mlgcanview = models.IntegerField(db_column='MlgCanView', blank=True, null=True)  # Field name made lowercase.
    modificationtimestamp = models.DateTimeField(db_column='ModificationTimestamp', blank=True, null=True)  # Field name made lowercase.
    openhousedate = models.DateField(db_column='OpenHouseDate', blank=True, null=True)  # Field name made lowercase.
    openhouseendtime = models.DateTimeField(db_column='OpenHouseEndTime', blank=True, null=True)  # Field name made lowercase.
    openhousekey = models.TextField(db_column='OpenHouseKey', primary_key=True)  # Field name made lowercase.
    openhouseremarks = models.TextField(db_column='OpenHouseRemarks', blank=True, null=True)  # Field name made lowercase.
    openhousestarttime = models.DateTimeField(db_column='OpenHouseStartTime', blank=True, null=True)  # Field name made lowercase.
    openhousestatus = models.CharField(db_column='OpenHouseStatus', max_length=25, blank=True, null=True)  # Field name made lowercase.
    openhousetype = models.CharField(db_column='OpenHouseType', max_length=25, blank=True, null=True)  # Field name made lowercase.
    originatingsystemname = models.TextField(db_column='OriginatingSystemName', blank=True, null=True)  # Field name made lowercase.
    refreshments = models.TextField(db_column='Refreshments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'openhouse'


class Property(models.Model):
    accessibilityfeatures = models.TextField(db_column='AccessibilityFeatures', blank=True, null=True)  # Field name made lowercase.
    additionalparcelsdescription = models.TextField(db_column='AdditionalParcelsDescription', blank=True, null=True)  # Field name made lowercase.
    additionalparcelsyn = models.IntegerField(db_column='AdditionalParcelsYN', blank=True, null=True)  # Field name made lowercase.
    appliances = models.TextField(db_column='Appliances', blank=True, null=True)  # Field name made lowercase.
    architecturalstyle = models.TextField(db_column='ArchitecturalStyle', blank=True, null=True)  # Field name made lowercase.
    associationamenities = models.TextField(db_column='AssociationAmenities', blank=True, null=True)  # Field name made lowercase.
    associationfee = models.DecimalField(db_column='AssociationFee', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    associationfee2 = models.DecimalField(db_column='AssociationFee2', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    associationfee2frequency = models.CharField(db_column='AssociationFee2Frequency', max_length=25, blank=True, null=True)  # Field name made lowercase.
    associationfeefrequency = models.CharField(db_column='AssociationFeeFrequency', max_length=25, blank=True, null=True)  # Field name made lowercase.
    associationfeeincludes = models.TextField(db_column='AssociationFeeIncludes', blank=True, null=True)  # Field name made lowercase.
    associationname = models.TextField(db_column='AssociationName', blank=True, null=True)  # Field name made lowercase.
    associationname2 = models.TextField(db_column='AssociationName2', blank=True, null=True)  # Field name made lowercase.
    associationphone = models.CharField(db_column='AssociationPhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    associationphone2 = models.CharField(db_column='AssociationPhone2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    associationyn = models.IntegerField(db_column='AssociationYN', blank=True, null=True)  # Field name made lowercase.
    attachedgarageyn = models.IntegerField(db_column='AttachedGarageYN', blank=True, null=True)  # Field name made lowercase.
    availabilitydate = models.DateField(db_column='AvailabilityDate', blank=True, null=True)  # Field name made lowercase.
    basement = models.TextField(db_column='Basement', blank=True, null=True)  # Field name made lowercase.
    bathroomsfull = models.SmallIntegerField(db_column='BathroomsFull', blank=True, null=True)  # Field name made lowercase.
    bathroomshalf = models.SmallIntegerField(db_column='BathroomsHalf', blank=True, null=True)  # Field name made lowercase.
    bathroomstotalinteger = models.SmallIntegerField(db_column='BathroomsTotalInteger', blank=True, null=True)  # Field name made lowercase.
    bedroomstotal = models.SmallIntegerField(db_column='BedroomsTotal', blank=True, null=True)  # Field name made lowercase.
    bodytype = models.TextField(db_column='BodyType', blank=True, null=True)  # Field name made lowercase.
    buildermodel = models.TextField(db_column='BuilderModel', blank=True, null=True)  # Field name made lowercase.
    buildername = models.TextField(db_column='BuilderName', blank=True, null=True)  # Field name made lowercase.
    buildingareasource = models.TextField(db_column='BuildingAreaSource', blank=True, null=True)  # Field name made lowercase.
    buildingareatotal = models.DecimalField(db_column='BuildingAreaTotal', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    buildingareaunits = models.CharField(db_column='BuildingAreaUnits', max_length=25, blank=True, null=True)  # Field name made lowercase.
    buildingfeatures = models.TextField(db_column='BuildingFeatures', blank=True, null=True)  # Field name made lowercase.
    businessname = models.TextField(db_column='BusinessName', blank=True, null=True)  # Field name made lowercase.
    businesstype = models.TextField(db_column='BusinessType', blank=True, null=True)  # Field name made lowercase.
    buyeragencycompensation = models.CharField(db_column='BuyerAgencyCompensation', max_length=25, blank=True, null=True)  # Field name made lowercase.
    buyeragentaor = models.TextField(db_column='BuyerAgentAOR', blank=True, null=True)  # Field name made lowercase.
    buyeragentdirectphone = models.CharField(db_column='BuyerAgentDirectPhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    buyeragentfullname = models.TextField(db_column='BuyerAgentFullName', blank=True, null=True)  # Field name made lowercase.
    buyeragentkey = models.TextField(db_column='BuyerAgentKey', blank=True, null=True)  # Field name made lowercase.
    buyeragentmlsid = models.CharField(db_column='BuyerAgentMlsId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    buyerfinancing = models.TextField(db_column='BuyerFinancing', blank=True, null=True)  # Field name made lowercase.
    buyerofficekey = models.TextField(db_column='BuyerOfficeKey', blank=True, null=True)  # Field name made lowercase.
    buyerofficemlsid = models.CharField(db_column='BuyerOfficeMlsId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    buyerofficename = models.TextField(db_column='BuyerOfficeName', blank=True, null=True)  # Field name made lowercase.
    buyerofficephone = models.CharField(db_column='BuyerOfficePhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    buyerteamkey = models.TextField(db_column='BuyerTeamKey', blank=True, null=True)  # Field name made lowercase.
    buyerteamkeynumeric = models.BigIntegerField(db_column='BuyerTeamKeyNumeric', blank=True, null=True)  # Field name made lowercase.
    buyerteamname = models.TextField(db_column='BuyerTeamName', blank=True, null=True)  # Field name made lowercase.
    carportspaces = models.DecimalField(db_column='CarportSpaces', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    carportyn = models.IntegerField(db_column='CarportYN', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    closedate = models.DateField(db_column='CloseDate', blank=True, null=True)  # Field name made lowercase.
    closeprice = models.DecimalField(db_column='ClosePrice', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cobuyeragentdirectphone = models.CharField(db_column='CoBuyerAgentDirectPhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cobuyeragentemail = models.TextField(db_column='CoBuyerAgentEmail', blank=True, null=True)  # Field name made lowercase.
    cobuyeragentfullname = models.TextField(db_column='CoBuyerAgentFullName', blank=True, null=True)  # Field name made lowercase.
    cobuyeragentkey = models.TextField(db_column='CoBuyerAgentKey', blank=True, null=True)  # Field name made lowercase.
    cobuyeragentmlsid = models.CharField(db_column='CoBuyerAgentMlsId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cobuyerofficekey = models.TextField(db_column='CoBuyerOfficeKey', blank=True, null=True)  # Field name made lowercase.
    cobuyerofficemlsid = models.CharField(db_column='CoBuyerOfficeMlsId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cobuyerofficename = models.TextField(db_column='CoBuyerOfficeName', blank=True, null=True)  # Field name made lowercase.
    cobuyerofficephone = models.CharField(db_column='CoBuyerOfficePhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    colistagentdirectphone = models.CharField(db_column='CoListAgentDirectPhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    colistagentemail = models.TextField(db_column='CoListAgentEmail', blank=True, null=True)  # Field name made lowercase.
    colistagentfullname = models.TextField(db_column='CoListAgentFullName', blank=True, null=True)  # Field name made lowercase.
    colistagentkey = models.TextField(db_column='CoListAgentKey', blank=True, null=True)  # Field name made lowercase.
    colistagentmlsid = models.CharField(db_column='CoListAgentMlsId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    colistofficekey = models.TextField(db_column='CoListOfficeKey', blank=True, null=True)  # Field name made lowercase.
    colistofficemlsid = models.CharField(db_column='CoListOfficeMlsId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    colistofficename = models.TextField(db_column='CoListOfficeName', blank=True, null=True)  # Field name made lowercase.
    colistofficephone = models.CharField(db_column='CoListOfficePhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    communityfeatures = models.TextField(db_column='CommunityFeatures', blank=True, null=True)  # Field name made lowercase.
    concessions = models.CharField(db_column='Concessions', max_length=25, blank=True, null=True)  # Field name made lowercase.
    concessionsamount = models.BigIntegerField(db_column='ConcessionsAmount', blank=True, null=True)  # Field name made lowercase.
    constructionmaterials = models.TextField(db_column='ConstructionMaterials', blank=True, null=True)  # Field name made lowercase.
    cooling = models.TextField(db_column='Cooling', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=2, blank=True, null=True)  # Field name made lowercase.
    countyorparish = models.TextField(db_column='CountyOrParish', blank=True, null=True)  # Field name made lowercase.
    cumulativedaysonmarket = models.SmallIntegerField(db_column='CumulativeDaysOnMarket', blank=True, null=True)  # Field name made lowercase.
    currentuse = models.TextField(db_column='CurrentUse', blank=True, null=True)  # Field name made lowercase.
    daysonmarket = models.SmallIntegerField(db_column='DaysOnMarket', blank=True, null=True)  # Field name made lowercase.
    directionfaces = models.CharField(db_column='DirectionFaces', max_length=25, blank=True, null=True)  # Field name made lowercase.
    directions = models.TextField(db_column='Directions', blank=True, null=True)  # Field name made lowercase.
    disclosures = models.TextField(db_column='Disclosures', blank=True, null=True)  # Field name made lowercase.
    dualvariablecompensationyn = models.IntegerField(db_column='DualVariableCompensationYN', blank=True, null=True)  # Field name made lowercase.
    electric = models.TextField(db_column='Electric', blank=True, null=True)  # Field name made lowercase.
    elementaryschool = models.TextField(db_column='ElementarySchool', blank=True, null=True)  # Field name made lowercase.
    expirationdate = models.DateField(db_column='ExpirationDate', blank=True, null=True)  # Field name made lowercase.
    exteriorfeatures = models.TextField(db_column='ExteriorFeatures', blank=True, null=True)  # Field name made lowercase.
    fencing = models.TextField(db_column='Fencing', blank=True, null=True)  # Field name made lowercase.
    financialdatasource = models.TextField(db_column='FinancialDataSource', blank=True, null=True)  # Field name made lowercase.
    fireplacefeatures = models.TextField(db_column='FireplaceFeatures', blank=True, null=True)  # Field name made lowercase.
    fireplaceyn = models.IntegerField(db_column='FireplaceYN', blank=True, null=True)  # Field name made lowercase.
    flooring = models.TextField(db_column='Flooring', blank=True, null=True)  # Field name made lowercase.
    foundationdetails = models.TextField(db_column='FoundationDetails', blank=True, null=True)  # Field name made lowercase.
    furnished = models.TextField(db_column='Furnished', blank=True, null=True)  # Field name made lowercase.
    garagespaces = models.DecimalField(db_column='GarageSpaces', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    garageyn = models.IntegerField(db_column='GarageYN', blank=True, null=True)  # Field name made lowercase.
    greenbuildingverificationtype = models.TextField(db_column='GreenBuildingVerificationType', blank=True, null=True)  # Field name made lowercase.
    greenenergyefficient = models.TextField(db_column='GreenEnergyEfficient', blank=True, null=True)  # Field name made lowercase.
    greenenergygeneration = models.TextField(db_column='GreenEnergyGeneration', blank=True, null=True)  # Field name made lowercase.
    greenindoorairquality = models.TextField(db_column='GreenIndoorAirQuality', blank=True, null=True)  # Field name made lowercase.
    greensustainability = models.TextField(db_column='GreenSustainability', blank=True, null=True)  # Field name made lowercase.
    greenwaterconservation = models.TextField(db_column='GreenWaterConservation', blank=True, null=True)  # Field name made lowercase.
    grossincome = models.DecimalField(db_column='GrossIncome', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    grossscheduledincome = models.DecimalField(db_column='GrossScheduledIncome', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    heating = models.TextField(db_column='Heating', blank=True, null=True)  # Field name made lowercase.
    highschool = models.TextField(db_column='HighSchool', blank=True, null=True)  # Field name made lowercase.
    homewarrantyyn = models.IntegerField(db_column='HomeWarrantyYN', blank=True, null=True)  # Field name made lowercase.
    horseamenities = models.TextField(db_column='HorseAmenities', blank=True, null=True)  # Field name made lowercase.
    interiorfeatures = models.TextField(db_column='InteriorFeatures', blank=True, null=True)  # Field name made lowercase.
    internetaddressdisplayyn = models.IntegerField(db_column='InternetAddressDisplayYN', blank=True, null=True)  # Field name made lowercase.
    internetautomatedvaluationdisplayyn = models.IntegerField(db_column='InternetAutomatedValuationDisplayYN', blank=True, null=True)  # Field name made lowercase.
    internetconsumercommentyn = models.IntegerField(db_column='InternetConsumerCommentYN', blank=True, null=True)  # Field name made lowercase.
    internetentirelistingdisplayyn = models.IntegerField(db_column='InternetEntireListingDisplayYN', blank=True, null=True)  # Field name made lowercase.
    landleaseamount = models.DecimalField(db_column='LandLeaseAmount', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='Latitude', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    laundryfeatures = models.TextField(db_column='LaundryFeatures', blank=True, null=True)  # Field name made lowercase.
    leasablearea = models.DecimalField(db_column='LeasableArea', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    leasableareaunits = models.CharField(db_column='LeasableAreaUnits', max_length=25, blank=True, null=True)  # Field name made lowercase.
    leaseamountfrequency = models.CharField(db_column='LeaseAmountFrequency', max_length=25, blank=True, null=True)  # Field name made lowercase.
    leaseterm = models.CharField(db_column='LeaseTerm', max_length=25, blank=True, null=True)  # Field name made lowercase.
    levels = models.TextField(db_column='Levels', blank=True, null=True)  # Field name made lowercase.
    listagentaor = models.TextField(db_column='ListAgentAOR', blank=True, null=True)  # Field name made lowercase.
    listagentdirectphone = models.CharField(db_column='ListAgentDirectPhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    listagentemail = models.TextField(db_column='ListAgentEmail', blank=True, null=True)  # Field name made lowercase.
    listagentfax = models.CharField(db_column='ListAgentFax', max_length=16, blank=True, null=True)  # Field name made lowercase.
    listagentfullname = models.TextField(db_column='ListAgentFullName', blank=True, null=True)  # Field name made lowercase.
    listagentkey = models.TextField(db_column='ListAgentKey', blank=True, null=True)  # Field name made lowercase.
    listagentmlsid = models.CharField(db_column='ListAgentMlsId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    listagentofficephoneext = models.CharField(db_column='ListAgentOfficePhoneExt', max_length=10, blank=True, null=True)  # Field name made lowercase.
    listagentpager = models.CharField(db_column='ListAgentPager', max_length=16, blank=True, null=True)  # Field name made lowercase.
    listagenturl = models.TextField(db_column='ListAgentURL', blank=True, null=True)  # Field name made lowercase.
    listaor = models.TextField(db_column='ListAOR', blank=True, null=True)  # Field name made lowercase.
    listingagreement = models.TextField(db_column='ListingAgreement', blank=True, null=True)  # Field name made lowercase.
    listingcontractdate = models.DateField(db_column='ListingContractDate', blank=True, null=True)  # Field name made lowercase.
    listingid = models.TextField(db_column='ListingId', primary_key=True)  # Field name made lowercase.
    listingkey = models.TextField(db_column='ListingKey', blank=True, null=True)  # Field name made lowercase.
    listingservice = models.CharField(db_column='ListingService', max_length=25, blank=True, null=True)  # Field name made lowercase.
    listingterms = models.TextField(db_column='ListingTerms', blank=True, null=True)  # Field name made lowercase.
    listofficefax = models.CharField(db_column='ListOfficeFax', max_length=16, blank=True, null=True)  # Field name made lowercase.
    listofficekey = models.TextField(db_column='ListOfficeKey', blank=True, null=True)  # Field name made lowercase.
    listofficemlsid = models.CharField(db_column='ListOfficeMlsId', max_length=25, blank=True, null=True)  # Field name made lowercase.
    listofficename = models.TextField(db_column='ListOfficeName', blank=True, null=True)  # Field name made lowercase.
    listofficephone = models.CharField(db_column='ListOfficePhone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    listofficeurl = models.TextField(db_column='ListOfficeURL', blank=True, null=True)  # Field name made lowercase.
    listprice = models.DecimalField(db_column='ListPrice', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    listteamkey = models.TextField(db_column='ListTeamKey', blank=True, null=True)  # Field name made lowercase.
    listteamkeynumeric = models.BigIntegerField(db_column='ListTeamKeyNumeric', blank=True, null=True)  # Field name made lowercase.
    listteamname = models.TextField(db_column='ListTeamName', blank=True, null=True)  # Field name made lowercase.
    livingarea = models.DecimalField(db_column='LivingArea', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    livingareasource = models.TextField(db_column='LivingAreaSource', blank=True, null=True)  # Field name made lowercase.
    livingareaunits = models.CharField(db_column='LivingAreaUnits', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lockboxlocation = models.TextField(db_column='LockBoxLocation', blank=True, null=True)  # Field name made lowercase.
    lockboxserialnumber = models.CharField(db_column='LockBoxSerialNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lockboxtype = models.TextField(db_column='LockBoxType', blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='Longitude', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lotfeatures = models.TextField(db_column='LotFeatures', blank=True, null=True)  # Field name made lowercase.
    lotsizeacres = models.DecimalField(db_column='LotSizeAcres', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lotsizedimensions = models.TextField(db_column='LotSizeDimensions', blank=True, null=True)  # Field name made lowercase.
    lotsizesquarefeet = models.DecimalField(db_column='LotSizeSquareFeet', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    majorchangetimestamp = models.DateTimeField(db_column='MajorChangeTimestamp', blank=True, null=True)  # Field name made lowercase.
    majorchangetype = models.TextField(db_column='MajorChangeType', blank=True, null=True)  # Field name made lowercase.
    make = models.TextField(db_column='Make', blank=True, null=True)  # Field name made lowercase.
    mfr_additionalapplicantfee = models.TextField(db_column='MFR_AdditionalApplicantFee', blank=True, null=True)  # Field name made lowercase.
    mfr_additionalleaserestrictions = models.TextField(db_column='MFR_AdditionalLeaseRestrictions', blank=True, null=True)  # Field name made lowercase.
    mfr_additionalmembershipavailableyn = models.TextField(db_column='MFR_AdditionalMembershipAvailableYN', blank=True, null=True)  # Field name made lowercase.
    mfr_additionalpetfees = models.TextField(db_column='MFR_AdditionalPetFees', blank=True, null=True)  # Field name made lowercase.
    mfr_additionalrooms = models.TextField(db_column='MFR_AdditionalRooms', blank=True, null=True)  # Field name made lowercase.
    mfr_additionalwaterinformation = models.TextField(db_column='MFR_AdditionalWaterInformation', blank=True, null=True)  # Field name made lowercase.
    mfr_adjoiningproperty = models.TextField(db_column='MFR_AdjoiningProperty', blank=True, null=True)  # Field name made lowercase.
    mfr_affidavityn = models.TextField(db_column='MFR_AffidavitYN', blank=True, null=True)  # Field name made lowercase.
    mfr_agexemptionyn = models.TextField(db_column='MFR_AGExemptionYN', blank=True, null=True)  # Field name made lowercase.
    mfr_alternatekeyfolionum = models.TextField(db_column='MFR_AlternateKeyFolioNum', blank=True, null=True)  # Field name made lowercase.
    mfr_amenitiesadditionalfees = models.TextField(db_column='MFR_AmenitiesAdditionalFees', blank=True, null=True)  # Field name made lowercase.
    mfr_annualexpenses = models.TextField(db_column='MFR_AnnualExpenses', blank=True, null=True)  # Field name made lowercase.
    mfr_annualincometype = models.TextField(db_column='MFR_AnnualIncomeType', blank=True, null=True)  # Field name made lowercase.
    mfr_annualnetincome = models.TextField(db_column='MFR_AnnualNetIncome', blank=True, null=True)  # Field name made lowercase.
    mfr_annualrent = models.TextField(db_column='MFR_AnnualRent', blank=True, null=True)  # Field name made lowercase.
    mfr_applicationfee = models.TextField(db_column='MFR_ApplicationFee', blank=True, null=True)  # Field name made lowercase.
    mfr_approvalprocess = models.TextField(db_column='MFR_ApprovalProcess', blank=True, null=True)  # Field name made lowercase.
    mfr_assocfeestenants = models.TextField(db_column='MFR_AssocFeesTenants', blank=True, null=True)  # Field name made lowercase.
    mfr_association2yn = models.TextField(db_column='MFR_Association2YN', blank=True, null=True)  # Field name made lowercase.
    mfr_associationapplicationfee = models.TextField(db_column='MFR_AssociationApplicationFee', blank=True, null=True)  # Field name made lowercase.
    mfr_associationapprovalfee = models.TextField(db_column='MFR_AssociationApprovalFee', blank=True, null=True)  # Field name made lowercase.
    mfr_associationapprovalrequiredyn = models.TextField(db_column='MFR_AssociationApprovalRequiredYN', blank=True, null=True)  # Field name made lowercase.
    mfr_associationemail = models.TextField(db_column='MFR_AssociationEmail', blank=True, null=True)  # Field name made lowercase.
    mfr_associationfeerequirement = models.TextField(db_column='MFR_AssociationFeeRequirement', blank=True, null=True)  # Field name made lowercase.
    mfr_associationurl = models.TextField(db_column='MFR_AssociationURL', blank=True, null=True)  # Field name made lowercase.
    mfr_assocsecdeposittenants = models.TextField(db_column='MFR_AssocSecDepositTenants', blank=True, null=True)  # Field name made lowercase.
    mfr_attributioncontact = models.TextField(db_column='MFR_AttributionContact', blank=True, null=True)  # Field name made lowercase.
    mfr_auctionfirmurl = models.TextField(db_column='MFR_AuctionFirmURL', blank=True, null=True)  # Field name made lowercase.
    mfr_auctionpropaccessyn = models.TextField(db_column='MFR_AuctionPropAccessYN', blank=True, null=True)  # Field name made lowercase.
    mfr_auctiontype = models.TextField(db_column='MFR_AuctionType', blank=True, null=True)  # Field name made lowercase.
    mfr_audiosurveillancenoticeyn = models.TextField(db_column='MFR_AudioSurveillanceNoticeYN', blank=True, null=True)  # Field name made lowercase.
    mfr_availableforleaseyn = models.TextField(db_column='MFR_AvailableForLeaseYN', blank=True, null=True)  # Field name made lowercase.
    mfr_backupsrequestedyn = models.TextField(db_column='MFR_BackupsRequestedYN', blank=True, null=True)  # Field name made lowercase.
    mfr_barnfeatures = models.TextField(db_column='MFR_BarnFeatures', blank=True, null=True)  # Field name made lowercase.
    mfr_betweenus1riveryn = models.TextField(db_column='MFR_BetweenUS1RiverYN', blank=True, null=True)  # Field name made lowercase.
    mfr_bomdate = models.TextField(db_column='MFR_BOMDate', blank=True, null=True)  # Field name made lowercase.
    mfr_bonusamount = models.TextField(db_column='MFR_BonusAmount', blank=True, null=True)  # Field name made lowercase.
    mfr_bonusexpirationdate = models.TextField(db_column='MFR_BonusExpirationDate', blank=True, null=True)  # Field name made lowercase.
    mfr_bonusyn = models.TextField(db_column='MFR_BonusYN', blank=True, null=True)  # Field name made lowercase.
    mfr_builderlicensenumber = models.TextField(db_column='MFR_BuilderLicenseNumber', blank=True, null=True)  # Field name made lowercase.
    mfr_buildingareatotalsrchsqm = models.TextField(db_column='MFR_BuildingAreaTotalSrchSqM', blank=True, null=True)  # Field name made lowercase.
    mfr_buildingelevatoryn = models.TextField(db_column='MFR_BuildingElevatorYN', blank=True, null=True)  # Field name made lowercase.
    mfr_buildingnamenumber = models.TextField(db_column='MFR_BuildingNameNumber', blank=True, null=True)  # Field name made lowercase.
    mfr_businessopportunitywithrealestateyn = models.TextField(db_column='MFR_BusinessOpportunityWithRealEstateYN', blank=True, null=True)  # Field name made lowercase.
    mfr_buyerspremium = models.TextField(db_column='MFR_BuyersPremium', blank=True, null=True)  # Field name made lowercase.
    mfr_calculatedlistpricebycalculatedsqft = models.TextField(db_column='MFR_CalculatedListPriceByCalculatedSqFt', blank=True, null=True)  # Field name made lowercase.
    mfr_callcenterphonenumber = models.TextField(db_column='MFR_CallCenterPhoneNumber', blank=True, null=True)  # Field name made lowercase.
    mfr_cddyn = models.TextField(db_column='MFR_CDDYN', blank=True, null=True)  # Field name made lowercase.
    mfr_ceilingheight = models.TextField(db_column='MFR_CeilingHeight', blank=True, null=True)  # Field name made lowercase.
    mfr_ceilingtype = models.TextField(db_column='MFR_CeilingType', blank=True, null=True)  # Field name made lowercase.
    mfr_classofspace = models.TextField(db_column='MFR_ClassofSpace', blank=True, null=True)  # Field name made lowercase.
    mfr_closepricebycalculatedlistpriceratio = models.TextField(db_column='MFR_ClosePriceByCalculatedListPriceRatio', blank=True, null=True)  # Field name made lowercase.
    mfr_closepricebycalculatedsqft = models.TextField(db_column='MFR_ClosePriceByCalculatedSqFt', blank=True, null=True)  # Field name made lowercase.
    mfr_cobuyerteamkey = models.TextField(db_column='MFR_CoBuyerTeamKey', blank=True, null=True)  # Field name made lowercase.
    mfr_cobuyerteamkeynumeric = models.TextField(db_column='MFR_CoBuyerTeamKeyNumeric', blank=True, null=True)  # Field name made lowercase.
    mfr_cobuyerteamname = models.TextField(db_column='MFR_CoBuyerTeamName', blank=True, null=True)  # Field name made lowercase.
    mfr_colistteamkey = models.TextField(db_column='MFR_CoListTeamKey', blank=True, null=True)  # Field name made lowercase.
    mfr_colistteamkeynumeric = models.TextField(db_column='MFR_CoListTeamKeyNumeric', blank=True, null=True)  # Field name made lowercase.
    mfr_colistteamname = models.TextField(db_column='MFR_CoListTeamName', blank=True, null=True)  # Field name made lowercase.
    mfr_communityassociationwaterfeatures = models.TextField(db_column='MFR_CommunityAssociationWaterFeatures', blank=True, null=True)  # Field name made lowercase.
    mfr_complexcommunitynamenccb = models.TextField(db_column='MFR_ComplexCommunityNameNCCB', blank=True, null=True)  # Field name made lowercase.
    mfr_complexdevelopmentname = models.TextField(db_column='MFR_ComplexDevelopmentName', blank=True, null=True)  # Field name made lowercase.
    mfr_comtransactionterms = models.TextField(db_column='MFR_ComTransactionTerms', blank=True, null=True)  # Field name made lowercase.
    mfr_comtransactiontype = models.TextField(db_column='MFR_ComTransactionType', blank=True, null=True)  # Field name made lowercase.
    mfr_conditionexpdate = models.TextField(db_column='MFR_ConditionExpDate', blank=True, null=True)  # Field name made lowercase.
    mfr_condoenvironmentyn = models.TextField(db_column='MFR_CondoEnvironmentYN', blank=True, null=True)  # Field name made lowercase.
    mfr_condofees = models.TextField(db_column='MFR_CondoFees', blank=True, null=True)  # Field name made lowercase.
    mfr_condofeesterm = models.TextField(db_column='MFR_CondoFeesTerm', blank=True, null=True)  # Field name made lowercase.
    mfr_condolandincludedyn = models.TextField(db_column='MFR_CondoLandIncludedYN', blank=True, null=True)  # Field name made lowercase.
    mfr_contractstatus = models.TextField(db_column='MFR_ContractStatus', blank=True, null=True)  # Field name made lowercase.
    mfr_convertedresidenceyn = models.TextField(db_column='MFR_ConvertedResidenceYN', blank=True, null=True)  # Field name made lowercase.
    mfr_countylandusecode = models.TextField(db_column='MFR_CountyLandUseCode', blank=True, null=True)  # Field name made lowercase.
    mfr_countypropertyusecode = models.TextField(db_column='MFR_CountyPropertyUseCode', blank=True, null=True)  # Field name made lowercase.
    mfr_crmnumber = models.TextField(db_column='MFR_CRMNumber', blank=True, null=True)  # Field name made lowercase.
    mfr_currencymonthlyrentamt = models.TextField(db_column='MFR_CurrencyMonthlyRentAmt', blank=True, null=True)  # Field name made lowercase.
    mfr_currentadjacentuse = models.TextField(db_column='MFR_CurrentAdjacentUse', blank=True, null=True)  # Field name made lowercase.
    mfr_currentprice = models.TextField(db_column='MFR_CurrentPrice', blank=True, null=True)  # Field name made lowercase.
    mfr_daysnoticetotenantifnotrenew = models.TextField(db_column='MFR_DaysNoticeToTenantIfNotRenew', blank=True, null=True)  # Field name made lowercase.
    mfr_daystoclosed = models.TextField(db_column='MFR_DaysToClosed', blank=True, null=True)  # Field name made lowercase.
    mfr_daystocontract = models.TextField(db_column='MFR_DaystoContract', blank=True, null=True)  # Field name made lowercase.
    mfr_depositsyn = models.TextField(db_column='MFR_DepositsYN', blank=True, null=True)  # Field name made lowercase.
    mfr_development = models.TextField(db_column='MFR_Development', blank=True, null=True)  # Field name made lowercase.
    mfr_disastermitigation = models.TextField(db_column='MFR_DisasterMitigation', blank=True, null=True)  # Field name made lowercase.
    mfr_dockdescription = models.TextField(db_column='MFR_DockDescription', blank=True, null=True)  # Field name made lowercase.
    mfr_dockdimensions = models.TextField(db_column='MFR_DockDimensions', blank=True, null=True)  # Field name made lowercase.
    mfr_dockliftcapacity = models.TextField(db_column='MFR_DockLiftCapacity', blank=True, null=True)  # Field name made lowercase.
    mfr_dockmaintenancefee = models.TextField(db_column='MFR_DockMaintenanceFee', blank=True, null=True)  # Field name made lowercase.
    mfr_dockmaintenancefeefrequency = models.TextField(db_column='MFR_DockMaintenanceFeeFrequency', blank=True, null=True)  # Field name made lowercase.
    mfr_dockyearbuilt = models.TextField(db_column='MFR_DockYearBuilt', blank=True, null=True)  # Field name made lowercase.
    mfr_dockyn = models.TextField(db_column='MFR_DockYN', blank=True, null=True)  # Field name made lowercase.
    mfr_doorheight = models.TextField(db_column='MFR_DoorHeight', blank=True, null=True)  # Field name made lowercase.
    mfr_doorwidth = models.TextField(db_column='MFR_DoorWidth', blank=True, null=True)  # Field name made lowercase.
    mfr_dprurl = models.TextField(db_column='MFR_DPRURL', blank=True, null=True)  # Field name made lowercase.
    mfr_dprurl2 = models.TextField(db_column='MFR_DPRURL2', blank=True, null=True)  # Field name made lowercase.
    mfr_dpryn = models.TextField(db_column='MFR_DPRYN', blank=True, null=True)  # Field name made lowercase.
    mfr_easements = models.TextField(db_column='MFR_Easements', blank=True, null=True)  # Field name made lowercase.
    mfr_eavesheight = models.TextField(db_column='MFR_EavesHeight', blank=True, null=True)  # Field name made lowercase.
    mfr_enddateoflease = models.TextField(db_column='MFR_EndDateofLease', blank=True, null=True)  # Field name made lowercase.
    mfr_escrowagentemail = models.TextField(db_column='MFR_EscrowAgentEmail', blank=True, null=True)  # Field name made lowercase.
    mfr_escrowagentfax = models.TextField(db_column='MFR_EscrowAgentFax', blank=True, null=True)  # Field name made lowercase.
    mfr_escrowagentname = models.TextField(db_column='MFR_EscrowAgentName', blank=True, null=True)  # Field name made lowercase.
    mfr_escrowagentphone = models.TextField(db_column='MFR_EscrowAgentPhone', blank=True, null=True)  # Field name made lowercase.
    mfr_escrowcity = models.TextField(db_column='MFR_EscrowCity', blank=True, null=True)  # Field name made lowercase.
    mfr_escrowcompany = models.TextField(db_column='MFR_EscrowCompany', blank=True, null=True)  # Field name made lowercase.
    mfr_escrowpostalcode = models.TextField(db_column='MFR_EscrowPostalCode', blank=True, null=True)  # Field name made lowercase.
    mfr_escrowstate = models.TextField(db_column='MFR_EscrowState', blank=True, null=True)  # Field name made lowercase.
    mfr_escrowstreetname = models.TextField(db_column='MFR_EscrowStreetName', blank=True, null=True)  # Field name made lowercase.
    mfr_escrowstreetnumber = models.TextField(db_column='MFR_EscrowStreetNumber', blank=True, null=True)  # Field name made lowercase.
    mfr_estannualmarketincome = models.TextField(db_column='MFR_EstAnnualMarketIncome', blank=True, null=True)  # Field name made lowercase.
    mfr_existlsetenantyn = models.TextField(db_column='MFR_ExistLseTenantYN', blank=True, null=True)  # Field name made lowercase.
    mfr_expectedclosingdate = models.TextField(db_column='MFR_ExpectedClosingDate', blank=True, null=True)  # Field name made lowercase.
    mfr_expectedleasedate = models.TextField(db_column='MFR_ExpectedLeaseDate', blank=True, null=True)  # Field name made lowercase.
    mfr_expirerenewaldate = models.TextField(db_column='MFR_ExpireRenewalDate', blank=True, null=True)  # Field name made lowercase.
    mfr_farmtype = models.TextField(db_column='MFR_FarmType', blank=True, null=True)  # Field name made lowercase.
    mfr_fchrurlyn = models.TextField(db_column='MFR_FCHRURLYN', blank=True, null=True)  # Field name made lowercase.
    mfr_financialpackageyn = models.TextField(db_column='MFR_FinancialPackageYN', blank=True, null=True)  # Field name made lowercase.
    mfr_financingterms = models.TextField(db_column='MFR_FinancingTerms', blank=True, null=True)  # Field name made lowercase.
    mfr_flexspacesqft = models.TextField(db_column='MFR_FlexSpaceSqFt', blank=True, null=True)  # Field name made lowercase.
    mfr_floodzonecode = models.TextField(db_column='MFR_FloodZoneCode', blank=True, null=True)  # Field name made lowercase.
    mfr_floodzonedate = models.TextField(db_column='MFR_FloodZoneDate', blank=True, null=True)  # Field name made lowercase.
    mfr_floodzonepanel = models.TextField(db_column='MFR_FloodZonePanel', blank=True, null=True)  # Field name made lowercase.
    mfr_floornumber = models.TextField(db_column='MFR_FloorNumber', blank=True, null=True)  # Field name made lowercase.
    mfr_forleaseyn = models.TextField(db_column='MFR_ForLeaseYN', blank=True, null=True)  # Field name made lowercase.
    mfr_freestandingyn = models.TextField(db_column='MFR_FreestandingYN', blank=True, null=True)  # Field name made lowercase.
    mfr_freezerspaceyn = models.TextField(db_column='MFR_FreezerSpaceYN', blank=True, null=True)  # Field name made lowercase.
    mfr_frontfootage = models.TextField(db_column='MFR_FrontFootage', blank=True, null=True)  # Field name made lowercase.
    mfr_futurelanduse = models.TextField(db_column='MFR_FutureLandUse', blank=True, null=True)  # Field name made lowercase.
    mfr_garagedimensions = models.TextField(db_column='MFR_GarageDimensions', blank=True, null=True)  # Field name made lowercase.
    mfr_garagedoorheight = models.TextField(db_column='MFR_GarageDoorHeight', blank=True, null=True)  # Field name made lowercase.
    mfr_geolocation = models.TextField(db_column='MFR_Geolocation', blank=True, null=True)  # Field name made lowercase.
    mfr_greenlandscaping = models.TextField(db_column='MFR_GreenLandscaping', blank=True, null=True)  # Field name made lowercase.
    mfr_greenverificationcount = models.TextField(db_column='MFR_GreenVerificationCount', blank=True, null=True)  # Field name made lowercase.
    mfr_hersindex = models.TextField(db_column='MFR_HERSIndex', blank=True, null=True)  # Field name made lowercase.
    mfr_homesteadyn = models.TextField(db_column='MFR_HomesteadYN', blank=True, null=True)  # Field name made lowercase.
    mfr_individuallymetered = models.TextField(db_column='MFR_IndividuallyMetered', blank=True, null=True)  # Field name made lowercase.
    mfr_inlawsuitedescription = models.TextField(db_column='MFR_InLawSuiteDescription', blank=True, null=True)  # Field name made lowercase.
    mfr_inlawsuitetotalsqft = models.TextField(db_column='MFR_InLawSuiteTotalSqFt', blank=True, null=True)  # Field name made lowercase.
    mfr_inlawsuiteunderairsqft = models.TextField(db_column='MFR_InLawSuiteUnderAirSqFt', blank=True, null=True)  # Field name made lowercase.
    mfr_inlawsuiteyn = models.TextField(db_column='MFR_InLawSuiteYN', blank=True, null=True)  # Field name made lowercase.
    mfr_lastdateavailable = models.TextField(db_column='MFR_LastDateAvailable', blank=True, null=True)  # Field name made lowercase.
    mfr_lastmonthsrent = models.TextField(db_column='MFR_LastMonthsRent', blank=True, null=True)  # Field name made lowercase.
    mfr_leasefee = models.TextField(db_column='MFR_LeaseFee', blank=True, null=True)  # Field name made lowercase.
    mfr_leaseprice = models.TextField(db_column='MFR_LeasePrice', blank=True, null=True)  # Field name made lowercase.
    mfr_leasepriceperacre = models.TextField(db_column='MFR_LeasePricePerAcre', blank=True, null=True)  # Field name made lowercase.
    mfr_leasepricepersqft = models.TextField(db_column='MFR_LeasePricePerSqFt', blank=True, null=True)  # Field name made lowercase.
    mfr_leasepriceunit = models.TextField(db_column='MFR_LeasePriceUnit', blank=True, null=True)  # Field name made lowercase.
    mfr_leasereferralfeecomments = models.TextField(db_column='MFR_LeaseReferralFeeComments', blank=True, null=True)  # Field name made lowercase.
    mfr_leaserestrictionsyn = models.TextField(db_column='MFR_LeaseRestrictionsYN', blank=True, null=True)  # Field name made lowercase.
    mfr_licenses = models.TextField(db_column='MFR_Licenses', blank=True, null=True)  # Field name made lowercase.
    mfr_listingexclusionyn = models.TextField(db_column='MFR_ListingExclusionYN', blank=True, null=True)  # Field name made lowercase.
    mfr_listofficecontactpreferred = models.TextField(db_column='MFR_ListOfficeContactPreferred', blank=True, null=True)  # Field name made lowercase.
    mfr_listofficeheadofficekeynumeric = models.TextField(db_column='MFR_ListOfficeHeadOfficeKeyNumeric', blank=True, null=True)  # Field name made lowercase.
    mfr_livingareameters = models.TextField(db_column='MFR_LivingAreaMeters', blank=True, null=True)  # Field name made lowercase.
    mfr_longtermyn = models.TextField(db_column='MFR_LongTermYN', blank=True, null=True)  # Field name made lowercase.
    mfr_lotsizesquaremeters = models.TextField(db_column='MFR_LotSizeSquareMeters', blank=True, null=True)  # Field name made lowercase.
    mfr_management = models.TextField(db_column='MFR_Management', blank=True, null=True)  # Field name made lowercase.
    mfr_manufacturingspaceheated = models.TextField(db_column='MFR_ManufacturingSpaceHeated', blank=True, null=True)  # Field name made lowercase.
    mfr_manufacturingspacetotal = models.TextField(db_column='MFR_ManufacturingSpaceTotal', blank=True, null=True)  # Field name made lowercase.
    mfr_masterbedsize = models.TextField(db_column='MFR_MasterBedSize', blank=True, null=True)  # Field name made lowercase.
    mfr_maxpetweight = models.TextField(db_column='MFR_MaxPetWeight', blank=True, null=True)  # Field name made lowercase.
    mfr_millagerate = models.TextField(db_column='MFR_MillageRate', blank=True, null=True)  # Field name made lowercase.
    mfr_minimumlease = models.TextField(db_column='MFR_MinimumLease', blank=True, null=True)  # Field name made lowercase.
    mfr_mlsmajorchangetype = models.TextField(db_column='MFR_MlsMajorChangeType', blank=True, null=True)  # Field name made lowercase.
    mfr_monthlycondofeeamount = models.TextField(db_column='MFR_MonthlyCondoFeeAmount', blank=True, null=True)  # Field name made lowercase.
    mfr_monthlyhoaamount = models.TextField(db_column='MFR_MonthlyHOAAmount', blank=True, null=True)  # Field name made lowercase.
    mfr_monthsavailable = models.TextField(db_column='MFR_MonthsAvailable', blank=True, null=True)  # Field name made lowercase.
    mfr_monthtomonthorweeklyyn = models.TextField(db_column='MFR_MonthToMonthOrWeeklyYN', blank=True, null=True)  # Field name made lowercase.
    mfr_montlymaintamtadditiontohoa = models.TextField(db_column='MFR_MontlyMaintAmtAdditionToHOA', blank=True, null=True)  # Field name made lowercase.
    mfr_nodrivebeach = models.TextField(db_column='MFR_NoDriveBeach', blank=True, null=True)  # Field name made lowercase.
    mfr_nonrepcompensation = models.TextField(db_column='MFR_NonRepCompensation', blank=True, null=True)  # Field name made lowercase.
    mfr_numassignedparkingspaces = models.TextField(db_column='MFR_NumAssignedParkingSpaces', blank=True, null=True)  # Field name made lowercase.
    mfr_numberofpaddockspastures = models.TextField(db_column='MFR_NumberOfPaddocksPastures', blank=True, null=True)  # Field name made lowercase.
    mfr_numberofpets = models.TextField(db_column='MFR_NumberOfPets', blank=True, null=True)  # Field name made lowercase.
    mfr_numberofseptics = models.TextField(db_column='MFR_NumberOfSeptics', blank=True, null=True)  # Field name made lowercase.
    mfr_numberofstalls = models.TextField(db_column='MFR_NumberOfStalls', blank=True, null=True)  # Field name made lowercase.
    mfr_numberofwells = models.TextField(db_column='MFR_NumberOfWells', blank=True, null=True)  # Field name made lowercase.
    mfr_numofbays = models.TextField(db_column='MFR_NumofBays', blank=True, null=True)  # Field name made lowercase.
    mfr_numofbaysdockhigh = models.TextField(db_column='MFR_NumofBaysDockHigh', blank=True, null=True)  # Field name made lowercase.
    mfr_numofbaysgradelevel = models.TextField(db_column='MFR_NumofBaysGradeLevel', blank=True, null=True)  # Field name made lowercase.
    mfr_numofconferencemeetingrooms = models.TextField(db_column='MFR_NumofConferenceMeetingRooms', blank=True, null=True)  # Field name made lowercase.
    mfr_numofhotelmotelrms = models.TextField(db_column='MFR_NumofHotelMotelRms', blank=True, null=True)  # Field name made lowercase.
    mfr_numofoffices = models.TextField(db_column='MFR_NumofOffices', blank=True, null=True)  # Field name made lowercase.
    mfr_numofownyearspriortolse = models.TextField(db_column='MFR_NumOfOwnYearsPriorToLse', blank=True, null=True)  # Field name made lowercase.
    mfr_numofrestrooms = models.TextField(db_column='MFR_NumofRestrooms', blank=True, null=True)  # Field name made lowercase.
    mfr_numtimesperyear = models.TextField(db_column='MFR_NumTimesperYear', blank=True, null=True)  # Field name made lowercase.
    mfr_officeretailspacesqft = models.TextField(db_column='MFR_OfficeRetailSpaceSqFt', blank=True, null=True)  # Field name made lowercase.
    mfr_offseasonrent = models.TextField(db_column='MFR_OffSeasonRent', blank=True, null=True)  # Field name made lowercase.
    mfr_originatingsystemname_field = models.TextField(db_column='MFR_OriginatingSystemName_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    mfr_originatingsystemtimestamp = models.TextField(db_column='MFR_OriginatingSystemTimestamp', blank=True, null=True)  # Field name made lowercase.
    mfr_otherassocfeestenants = models.TextField(db_column='MFR_OtherAssocFeesTenants', blank=True, null=True)  # Field name made lowercase.
    mfr_otherassocfeestenantsfrequency = models.TextField(db_column='MFR_OtherAssocFeesTenantsFrequency', blank=True, null=True)  # Field name made lowercase.
    mfr_otherexemptionsyn = models.TextField(db_column='MFR_OtherExemptionsYN', blank=True, null=True)  # Field name made lowercase.
    mfr_otherfeesamount = models.TextField(db_column='MFR_OtherFeesAmount', blank=True, null=True)  # Field name made lowercase.
    mfr_otherfeesdescription = models.TextField(db_column='MFR_OtherFeesDescription', blank=True, null=True)  # Field name made lowercase.
    mfr_otherfeesterm = models.TextField(db_column='MFR_OtherFeesTerm', blank=True, null=True)  # Field name made lowercase.
    mfr_parkingfeetenants = models.TextField(db_column='MFR_ParkingFeeTenants', blank=True, null=True)  # Field name made lowercase.
    mfr_parkingfeetenantsfrequency = models.TextField(db_column='MFR_ParkingFeeTenantsFrequency', blank=True, null=True)  # Field name made lowercase.
    mfr_permitnumber = models.TextField(db_column='MFR_PermitNumber', blank=True, null=True)  # Field name made lowercase.
    mfr_petdepositfee = models.TextField(db_column='MFR_PetDepositFee', blank=True, null=True)  # Field name made lowercase.
    mfr_petfeenonrefundable = models.TextField(db_column='MFR_PetFeeNonRefundable', blank=True, null=True)  # Field name made lowercase.
    mfr_petmonthlyfee = models.TextField(db_column='MFR_PetMonthlyFee', blank=True, null=True)  # Field name made lowercase.
    mfr_petrestrictions = models.TextField(db_column='MFR_PetRestrictions', blank=True, null=True)  # Field name made lowercase.
    mfr_petrestrictionssource = models.TextField(db_column='MFR_PetRestrictionsSource', blank=True, null=True)  # Field name made lowercase.
    mfr_petsize = models.TextField(db_column='MFR_PetSize', blank=True, null=True)  # Field name made lowercase.
    mfr_plannedunitdevelopmentyn = models.TextField(db_column='MFR_PlannedUnitDevelopmentYN', blank=True, null=True)  # Field name made lowercase.
    mfr_pooldimensions = models.TextField(db_column='MFR_PoolDimensions', blank=True, null=True)  # Field name made lowercase.
    mfr_previousstatus = models.TextField(db_column='MFR_PreviousStatus', blank=True, null=True)  # Field name made lowercase.
    mfr_priceperacre = models.TextField(db_column='MFR_PricePerAcre', blank=True, null=True)  # Field name made lowercase.
    mfr_projectedcompletiondate = models.TextField(db_column='MFR_ProjectedCompletionDate', blank=True, null=True)  # Field name made lowercase.
    mfr_propertydescription = models.TextField(db_column='MFR_PropertyDescription', blank=True, null=True)  # Field name made lowercase.
    mfr_propertymanager = models.TextField(db_column='MFR_PropertyManager', blank=True, null=True)  # Field name made lowercase.
    mfr_propertymanagerphone = models.TextField(db_column='MFR_PropertyManagerPhone', blank=True, null=True)  # Field name made lowercase.
    mfr_publicremarksagent = models.TextField(db_column='MFR_PublicRemarksAgent', blank=True, null=True)  # Field name made lowercase.
    mfr_publicremarksagentspanish = models.TextField(db_column='MFR_PublicRemarksAgentSpanish', blank=True, null=True)  # Field name made lowercase.
    mfr_ratio_closeprice_by_listprice = models.TextField(db_column='MFR_RATIO_ClosePrice_By_ListPrice', blank=True, null=True)  # Field name made lowercase.
    mfr_ratio_closeprice_by_originallistprice = models.TextField(db_column='MFR_RATIO_ClosePrice_By_OriginalListPrice', blank=True, null=True)  # Field name made lowercase.
    mfr_ratio_currentprice_by_calculatedsqft = models.TextField(db_column='MFR_RATIO_CurrentPrice_By_CalculatedSqFt', blank=True, null=True)  # Field name made lowercase.
    mfr_realtorinfo = models.TextField(db_column='MFR_RealtorInfo', blank=True, null=True)  # Field name made lowercase.
    mfr_realtorinfoconfidential = models.TextField(db_column='MFR_RealtorInfoConfidential', blank=True, null=True)  # Field name made lowercase.
    mfr_referralfee = models.TextField(db_column='MFR_ReferralFee', blank=True, null=True)  # Field name made lowercase.
    mfr_rentspreeurl = models.TextField(db_column='MFR_RentSpreeURL', blank=True, null=True)  # Field name made lowercase.
    mfr_rentspreeyn = models.TextField(db_column='MFR_RentSpreeYN', blank=True, null=True)  # Field name made lowercase.
    mfr_representation = models.TextField(db_column='MFR_Representation', blank=True, null=True)  # Field name made lowercase.
    mfr_roadfrontageft = models.TextField(db_column='MFR_RoadFrontageFt', blank=True, null=True)  # Field name made lowercase.
    mfr_roomcount = models.TextField(db_column='MFR_RoomCount', blank=True, null=True)  # Field name made lowercase.
    mfr_saleincludes = models.TextField(db_column='MFR_SaleIncludes', blank=True, null=True)  # Field name made lowercase.
    mfr_sdeoyn = models.TextField(db_column='MFR_SDEOYN', blank=True, null=True)  # Field name made lowercase.
    mfr_seasonalrent = models.TextField(db_column='MFR_SeasonalRent', blank=True, null=True)  # Field name made lowercase.
    mfr_securitydeposit = models.TextField(db_column='MFR_SecurityDeposit', blank=True, null=True)  # Field name made lowercase.
    mfr_securitydepositterms = models.TextField(db_column='MFR_SecurityDepositTerms', blank=True, null=True)  # Field name made lowercase.
    mfr_showingconsiderations = models.TextField(db_column='MFR_ShowingConsiderations', blank=True, null=True)  # Field name made lowercase.
    mfr_showingtime = models.TextField(db_column='MFR_ShowingTime', blank=True, null=True)  # Field name made lowercase.
    mfr_signage = models.TextField(db_column='MFR_Signage', blank=True, null=True)  # Field name made lowercase.
    mfr_solarpanelownership = models.TextField(db_column='MFR_SolarPanelOwnership', blank=True, null=True)  # Field name made lowercase.
    mfr_soldremarks = models.TextField(db_column='MFR_SoldRemarks', blank=True, null=True)  # Field name made lowercase.
    mfr_spacetype = models.TextField(db_column='MFR_SpaceType', blank=True, null=True)  # Field name made lowercase.
    mfr_statelandusecode = models.TextField(db_column='MFR_StateLandUseCode', blank=True, null=True)  # Field name made lowercase.
    mfr_statepropertyusecode = models.TextField(db_column='MFR_StatePropertyUseCode', blank=True, null=True)  # Field name made lowercase.
    mfr_statuscontractualsearchdate = models.TextField(db_column='MFR_StatusContractualSearchDate', blank=True, null=True)  # Field name made lowercase.
    mfr_subdivisionnum = models.TextField(db_column='MFR_SubdivisionNum', blank=True, null=True)  # Field name made lowercase.
    mfr_subdivisionsectionnumber = models.TextField(db_column='MFR_SubdivisionSectionNumber', blank=True, null=True)  # Field name made lowercase.
    mfr_swsubdivcommunityname = models.TextField(db_column='MFR_SWSubdivCommunityName', blank=True, null=True)  # Field name made lowercase.
    mfr_swsubdivcondonum = models.TextField(db_column='MFR_SWSubdivCondoNum', blank=True, null=True)  # Field name made lowercase.
    mfr_tempoffmarketdate = models.TextField(db_column='MFR_TempOffMarketDate', blank=True, null=True)  # Field name made lowercase.
    mfr_termsoflease = models.TextField(db_column='MFR_TermsOfLease', blank=True, null=True)  # Field name made lowercase.
    mfr_thirdpartyyn = models.TextField(db_column='MFR_ThirdPartyYN', blank=True, null=True)  # Field name made lowercase.
    mfr_totalacreage = models.TextField(db_column='MFR_TotalAcreage', blank=True, null=True)  # Field name made lowercase.
    mfr_totalannualfees = models.TextField(db_column='MFR_TotalAnnualFees', blank=True, null=True)  # Field name made lowercase.
    mfr_totalmonthlyexpenses = models.TextField(db_column='MFR_TotalMonthlyExpenses', blank=True, null=True)  # Field name made lowercase.
    mfr_totalmonthlyfees = models.TextField(db_column='MFR_TotalMonthlyFees', blank=True, null=True)  # Field name made lowercase.
    mfr_totalnumbuildings = models.TextField(db_column='MFR_TotalNumBuildings', blank=True, null=True)  # Field name made lowercase.
    mfr_transportationaccess = models.TextField(db_column='MFR_TransportationAccess', blank=True, null=True)  # Field name made lowercase.
    mfr_unitcount = models.TextField(db_column='MFR_UnitCount', blank=True, null=True)  # Field name made lowercase.
    mfr_unitnumberyn = models.TextField(db_column='MFR_UnitNumberYN', blank=True, null=True)  # Field name made lowercase.
    mfr_usecode = models.TextField(db_column='MFR_UseCode', blank=True, null=True)  # Field name made lowercase.
    mfr_virtualtoururlbranded2 = models.TextField(db_column='MFR_VirtualTourURLBranded2', blank=True, null=True)  # Field name made lowercase.
    mfr_virtualtoururlunbranded2 = models.TextField(db_column='MFR_VirtualTourURLUnbranded2', blank=True, null=True)  # Field name made lowercase.
    mfr_warehousespaceheated = models.TextField(db_column='MFR_WarehouseSpaceHeated', blank=True, null=True)  # Field name made lowercase.
    mfr_warehousespacetotal = models.TextField(db_column='MFR_WarehouseSpaceTotal', blank=True, null=True)  # Field name made lowercase.
    mfr_wateraccess = models.TextField(db_column='MFR_WaterAccess', blank=True, null=True)  # Field name made lowercase.
    mfr_wateraccessyn = models.TextField(db_column='MFR_WaterAccessYN', blank=True, null=True)  # Field name made lowercase.
    mfr_waterextras = models.TextField(db_column='MFR_WaterExtras', blank=True, null=True)  # Field name made lowercase.
    mfr_waterextrasyn = models.TextField(db_column='MFR_WaterExtrasYN', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetbayharbor = models.TextField(db_column='MFR_WaterFrontageFeetBayHarbor', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetbayou = models.TextField(db_column='MFR_WaterFrontageFeetBayou', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetbeach = models.TextField(db_column='MFR_WaterFrontageFeetBeach', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetbeachprvt = models.TextField(db_column='MFR_WaterFrontageFeetBeachPrvt', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetbeachpub = models.TextField(db_column='MFR_WaterFrontageFeetBeachPub', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetbrackishwater = models.TextField(db_column='MFR_WaterFrontageFeetBrackishWater', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetcanalbrackish = models.TextField(db_column='MFR_WaterFrontageFeetCanalBrackish', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetcanalfresh = models.TextField(db_column='MFR_WaterFrontageFeetCanalFresh', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetcanalfront = models.TextField(db_column='MFR_WaterFrontageFeetCanalFront', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetcanalsalt = models.TextField(db_column='MFR_WaterFrontageFeetCanalSalt', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetcreek = models.TextField(db_column='MFR_WaterFrontageFeetCreek', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetfcwlsc = models.TextField(db_column='MFR_WaterFrontageFeetFCWLSC', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetgulfocean = models.TextField(db_column='MFR_WaterFrontageFeetGulfOcean', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeeticw = models.TextField(db_column='MFR_WaterFrontageFeetICW', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetlagoon = models.TextField(db_column='MFR_WaterFrontageFeetLagoon', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetlake = models.TextField(db_column='MFR_WaterFrontageFeetLake', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetlakechain = models.TextField(db_column='MFR_WaterFrontageFeetLakeChain', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetmarina = models.TextField(db_column='MFR_WaterFrontageFeetMarina', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetocean2bay = models.TextField(db_column='MFR_WaterFrontageFeetOcean2Bay', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetpond = models.TextField(db_column='MFR_WaterFrontageFeetPond', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetriparianrights = models.TextField(db_column='MFR_WaterFrontageFeetRiparianRights', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontagefeetriver = models.TextField(db_column='MFR_WaterFrontageFeetRiver', blank=True, null=True)  # Field name made lowercase.
    mfr_waterfrontfeettotal = models.TextField(db_column='MFR_WaterfrontFeetTotal', blank=True, null=True)  # Field name made lowercase.
    mfr_waterview = models.TextField(db_column='MFR_WaterView', blank=True, null=True)  # Field name made lowercase.
    mfr_waterviewyn = models.TextField(db_column='MFR_WaterViewYN', blank=True, null=True)  # Field name made lowercase.
    mfr_weeklyrent = models.TextField(db_column='MFR_WeeklyRent', blank=True, null=True)  # Field name made lowercase.
    mfr_weeksavailable = models.TextField(db_column='MFR_WeeksAvailable', blank=True, null=True)  # Field name made lowercase.
    mfr_yrsofownerpriortoleasingreqyn = models.TextField(db_column='MFR_YrsOfOwnerPriorToLeasingReqYN', blank=True, null=True)  # Field name made lowercase.
    mfr_zoningcompatibleyn = models.TextField(db_column='MFR_ZoningCompatibleYN', blank=True, null=True)  # Field name made lowercase.
    middleorjuniorschool = models.TextField(db_column='MiddleOrJuniorSchool', blank=True, null=True)  # Field name made lowercase.
    mlgcanuse = models.TextField(db_column='MlgCanUse', blank=True, null=True)  # Field name made lowercase.
    mlgcanview = models.IntegerField(db_column='MlgCanView', blank=True, null=True)  # Field name made lowercase.
    mlsareamajor = models.TextField(db_column='MLSAreaMajor', blank=True, null=True)  # Field name made lowercase.
    mlsstatus = models.TextField(db_column='MlsStatus', blank=True, null=True)  # Field name made lowercase.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase.
    modificationtimestamp = models.DateTimeField(db_column='ModificationTimestamp', blank=True, null=True)  # Field name made lowercase.
    netoperatingincome = models.DecimalField(db_column='NetOperatingIncome', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    newconstructionyn = models.IntegerField(db_column='NewConstructionYN', blank=True, null=True)  # Field name made lowercase.
    numberoflots = models.SmallIntegerField(db_column='NumberOfLots', blank=True, null=True)  # Field name made lowercase.
    numberofseparateelectricmeters = models.SmallIntegerField(db_column='NumberOfSeparateElectricMeters', blank=True, null=True)  # Field name made lowercase.
    numberofseparategasmeters = models.SmallIntegerField(db_column='NumberOfSeparateGasMeters', blank=True, null=True)  # Field name made lowercase.
    numberofseparatewatermeters = models.SmallIntegerField(db_column='NumberOfSeparateWaterMeters', blank=True, null=True)  # Field name made lowercase.
    numberofunitstotal = models.SmallIntegerField(db_column='NumberOfUnitsTotal', blank=True, null=True)  # Field name made lowercase.
    occupanttype = models.TextField(db_column='OccupantType', blank=True, null=True)  # Field name made lowercase.
    offmarketdate = models.DateField(db_column='OffMarketDate', blank=True, null=True)  # Field name made lowercase.
    onmarketdate = models.DateField(db_column='OnMarketDate', blank=True, null=True)  # Field name made lowercase.
    originalentrytimestamp = models.DateTimeField(db_column='OriginalEntryTimestamp', blank=True, null=True)  # Field name made lowercase.
    originallistprice = models.DecimalField(db_column='OriginalListPrice', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    originatingsystemkey = models.TextField(db_column='OriginatingSystemKey', blank=True, null=True)  # Field name made lowercase.
    originatingsystemname = models.TextField(db_column='OriginatingSystemName', blank=True, null=True)  # Field name made lowercase.
    otherequipment = models.TextField(db_column='OtherEquipment', blank=True, null=True)  # Field name made lowercase.
    otherstructures = models.TextField(db_column='OtherStructures', blank=True, null=True)  # Field name made lowercase.
    ownerpays = models.TextField(db_column='OwnerPays', blank=True, null=True)  # Field name made lowercase.
    ownership = models.TextField(db_column='Ownership', blank=True, null=True)  # Field name made lowercase.
    parcelnumber = models.TextField(db_column='ParcelNumber', blank=True, null=True)  # Field name made lowercase.
    parkingfeatures = models.TextField(db_column='ParkingFeatures', blank=True, null=True)  # Field name made lowercase.
    patioandporchfeatures = models.TextField(db_column='PatioAndPorchFeatures', blank=True, null=True)  # Field name made lowercase.
    petsallowed = models.TextField(db_column='PetsAllowed', blank=True, null=True)  # Field name made lowercase.
    photoschangetimestamp = models.DateTimeField(db_column='PhotosChangeTimestamp', blank=True, null=True)  # Field name made lowercase.
    photoscount = models.SmallIntegerField(db_column='PhotosCount', blank=True, null=True)  # Field name made lowercase.
    poolfeatures = models.TextField(db_column='PoolFeatures', blank=True, null=True)  # Field name made lowercase.
    poolprivateyn = models.IntegerField(db_column='PoolPrivateYN', blank=True, null=True)  # Field name made lowercase.
    possession = models.TextField(db_column='Possession', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    postalcodeplus4 = models.CharField(db_column='PostalCodePlus4', max_length=4, blank=True, null=True)  # Field name made lowercase.
    previouslistprice = models.DecimalField(db_column='PreviousListPrice', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pricechangetimestamp = models.DateTimeField(db_column='PriceChangeTimestamp', blank=True, null=True)  # Field name made lowercase.
    privateofficeremarks = models.TextField(db_column='PrivateOfficeRemarks', blank=True, null=True)  # Field name made lowercase.
    privateremarks = models.TextField(db_column='PrivateRemarks', blank=True, null=True)  # Field name made lowercase.
    propertyattachedyn = models.IntegerField(db_column='PropertyAttachedYN', blank=True, null=True)  # Field name made lowercase.
    propertycondition = models.TextField(db_column='PropertyCondition', blank=True, null=True)  # Field name made lowercase.
    propertysubtype = models.TextField(db_column='PropertySubType', blank=True, null=True)  # Field name made lowercase.
    propertytype = models.TextField(db_column='PropertyType', blank=True, null=True)  # Field name made lowercase.
    publicremarks = models.TextField(db_column='PublicRemarks', blank=True, null=True)  # Field name made lowercase.
    publicsurveyrange = models.CharField(db_column='PublicSurveyRange', max_length=20, blank=True, null=True)  # Field name made lowercase.
    publicsurveysection = models.CharField(db_column='PublicSurveySection', max_length=20, blank=True, null=True)  # Field name made lowercase.
    purchasecontractdate = models.DateField(db_column='PurchaseContractDate', blank=True, null=True)  # Field name made lowercase.
    roadfrontagetype = models.TextField(db_column='RoadFrontageType', blank=True, null=True)  # Field name made lowercase.
    roadresponsibility = models.TextField(db_column='RoadResponsibility', blank=True, null=True)  # Field name made lowercase.
    roadsurfacetype = models.TextField(db_column='RoadSurfaceType', blank=True, null=True)  # Field name made lowercase.
    roof = models.TextField(db_column='Roof', blank=True, null=True)  # Field name made lowercase.
    securityfeatures = models.TextField(db_column='SecurityFeatures', blank=True, null=True)  # Field name made lowercase.
    seniorcommunityyn = models.IntegerField(db_column='SeniorCommunityYN', blank=True, null=True)  # Field name made lowercase.
    sewer = models.TextField(db_column='Sewer', blank=True, null=True)  # Field name made lowercase.
    showinginstructions = models.TextField(db_column='ShowingInstructions', blank=True, null=True)  # Field name made lowercase.
    showingrequirements = models.TextField(db_column='ShowingRequirements', blank=True, null=True)  # Field name made lowercase.
    spafeatures = models.TextField(db_column='SpaFeatures', blank=True, null=True)  # Field name made lowercase.
    spayn = models.IntegerField(db_column='SpaYN', blank=True, null=True)  # Field name made lowercase.
    speciallistingconditions = models.TextField(db_column='SpecialListingConditions', blank=True, null=True)  # Field name made lowercase.
    standardstatus = models.CharField(db_column='StandardStatus', max_length=25, blank=True, null=True)  # Field name made lowercase.
    stateorprovince = models.CharField(db_column='StateOrProvince', max_length=2, blank=True, null=True)  # Field name made lowercase.
    statuschangetimestamp = models.DateTimeField(db_column='StatusChangeTimestamp', blank=True, null=True)  # Field name made lowercase.
    storiestotal = models.SmallIntegerField(db_column='StoriesTotal', blank=True, null=True)  # Field name made lowercase.
    streetdirprefix = models.CharField(db_column='StreetDirPrefix', max_length=15, blank=True, null=True)  # Field name made lowercase.
    streetdirsuffix = models.CharField(db_column='StreetDirSuffix', max_length=15, blank=True, null=True)  # Field name made lowercase.
    streetname = models.TextField(db_column='StreetName', blank=True, null=True)  # Field name made lowercase.
    streetnumber = models.CharField(db_column='StreetNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    streetnumbernumeric = models.IntegerField(db_column='StreetNumberNumeric', blank=True, null=True)  # Field name made lowercase.
    streetsuffix = models.CharField(db_column='StreetSuffix', max_length=25, blank=True, null=True)  # Field name made lowercase.
    subdivisionname = models.TextField(db_column='SubdivisionName', blank=True, null=True)  # Field name made lowercase.
    syndicateto = models.TextField(db_column='SyndicateTo', blank=True, null=True)  # Field name made lowercase.
    taxannualamount = models.DecimalField(db_column='TaxAnnualAmount', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taxblock = models.CharField(db_column='TaxBlock', max_length=25, blank=True, null=True)  # Field name made lowercase.
    taxbooknumber = models.CharField(db_column='TaxBookNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    taxlegaldescription = models.TextField(db_column='TaxLegalDescription', blank=True, null=True)  # Field name made lowercase.
    taxlot = models.CharField(db_column='TaxLot', max_length=25, blank=True, null=True)  # Field name made lowercase.
    taxotherannualassessmentamount = models.DecimalField(db_column='TaxOtherAnnualAssessmentAmount', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taxyear = models.SmallIntegerField(db_column='TaxYear', blank=True, null=True)  # Field name made lowercase.
    tenantpays = models.TextField(db_column='TenantPays', blank=True, null=True)  # Field name made lowercase.
    totalactualrent = models.DecimalField(db_column='TotalActualRent', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    township = models.TextField(db_column='Township', blank=True, null=True)  # Field name made lowercase.
    transactionbrokercompensation = models.CharField(db_column='TransactionBrokerCompensation', max_length=25, blank=True, null=True)  # Field name made lowercase.
    unitnumber = models.CharField(db_column='UnitNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    universalpropertyid = models.TextField(db_column='UniversalPropertyId', blank=True, null=True)  # Field name made lowercase.
    unparsedaddress = models.TextField(db_column='UnparsedAddress', blank=True, null=True)  # Field name made lowercase.
    utilities = models.TextField(db_column='Utilities', blank=True, null=True)  # Field name made lowercase.
    vegetation = models.TextField(db_column='Vegetation', blank=True, null=True)  # Field name made lowercase.
    view = models.TextField(db_column='View', blank=True, null=True)  # Field name made lowercase.
    virtualtoururlbranded = models.TextField(db_column='VirtualTourURLBranded', blank=True, null=True)  # Field name made lowercase.
    virtualtoururlunbranded = models.TextField(db_column='VirtualTourURLUnbranded', blank=True, null=True)  # Field name made lowercase.
    waterbodyname = models.TextField(db_column='WaterBodyName', blank=True, null=True)  # Field name made lowercase.
    waterfrontfeatures = models.TextField(db_column='WaterfrontFeatures', blank=True, null=True)  # Field name made lowercase.
    waterfrontyn = models.IntegerField(db_column='WaterfrontYN', blank=True, null=True)  # Field name made lowercase.
    watersource = models.TextField(db_column='WaterSource', blank=True, null=True)  # Field name made lowercase.
    windowfeatures = models.TextField(db_column='WindowFeatures', blank=True, null=True)  # Field name made lowercase.
    withdrawndate = models.DateField(db_column='WithdrawnDate', blank=True, null=True)  # Field name made lowercase.
    yearbuilt = models.SmallIntegerField(db_column='YearBuilt', blank=True, null=True)  # Field name made lowercase.
    yearestablished = models.SmallIntegerField(db_column='YearEstablished', blank=True, null=True)  # Field name made lowercase.
    zoning = models.CharField(db_column='Zoning', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'property'


class Propertygreenverification(models.Model):
    greenbuildingverificationkey = models.TextField(db_column='GreenBuildingVerificationKey', primary_key=True)  # Field name made lowercase.
    greenbuildingverificationtype = models.TextField(db_column='GreenBuildingVerificationType', blank=True, null=True)  # Field name made lowercase.
    greenverificationbody = models.TextField(db_column='GreenVerificationBody', blank=True, null=True)  # Field name made lowercase.
    greenverificationmetric = models.SmallIntegerField(db_column='GreenVerificationMetric', blank=True, null=True)  # Field name made lowercase.
    greenverificationrating = models.TextField(db_column='GreenVerificationRating', blank=True, null=True)  # Field name made lowercase.
    greenverificationsource = models.CharField(db_column='GreenVerificationSource', max_length=25, blank=True, null=True)  # Field name made lowercase.
    greenverificationstatus = models.CharField(db_column='GreenVerificationStatus', max_length=25, blank=True, null=True)  # Field name made lowercase.
    greenverificationurl = models.TextField(db_column='GreenVerificationURL', blank=True, null=True)  # Field name made lowercase.
    greenverificationversion = models.CharField(db_column='GreenVerificationVersion', max_length=25, blank=True, null=True)  # Field name made lowercase.
    greenverificationyear = models.SmallIntegerField(db_column='GreenVerificationYear', blank=True, null=True)  # Field name made lowercase.
    mfr_inputentryorder = models.TextField(db_column='MFR_InputEntryOrder', blank=True, null=True)  # Field name made lowercase.
    mfr_isdeleted = models.TextField(db_column='MFR_IsDeleted', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propertygreenverification'


class Propertyrooms(models.Model):
    mfr_bedroomclosettype = models.TextField(db_column='MFR_BedroomClosetType', blank=True, null=True)  # Field name made lowercase.
    mfr_roomflooring = models.TextField(db_column='MFR_RoomFlooring', blank=True, null=True)  # Field name made lowercase.
    roomarea = models.DecimalField(db_column='RoomArea', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    roomareasource = models.TextField(db_column='RoomAreaSource', blank=True, null=True)  # Field name made lowercase.
    roomareaunits = models.CharField(db_column='RoomAreaUnits', max_length=25, blank=True, null=True)  # Field name made lowercase.
    roomdescription = models.TextField(db_column='RoomDescription', blank=True, null=True)  # Field name made lowercase.
    roomdimensions = models.TextField(db_column='RoomDimensions', blank=True, null=True)  # Field name made lowercase.
    roomfeatures = models.TextField(db_column='RoomFeatures', blank=True, null=True)  # Field name made lowercase.
    roomkey = models.TextField(db_column='RoomKey', primary_key=True)  # Field name made lowercase.
    roomlength = models.DecimalField(db_column='RoomLength', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    roomlengthwidthsource = models.TextField(db_column='RoomLengthWidthSource', blank=True, null=True)  # Field name made lowercase.
    roomlengthwidthunits = models.CharField(db_column='RoomLengthWidthUnits', max_length=25, blank=True, null=True)  # Field name made lowercase.
    roomlevel = models.CharField(db_column='RoomLevel', max_length=25, blank=True, null=True)  # Field name made lowercase.
    roomtype = models.TextField(db_column='RoomType', blank=True, null=True)  # Field name made lowercase.
    roomwidth = models.DecimalField(db_column='RoomWidth', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    listingid = models.TextField(db_column='ListingId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propertyrooms'


class Propertyunittypes(models.Model):
    mfr_unittypeheatedsqft = models.TextField(db_column='MFR_UnitTypeHeatedSqFt', blank=True, null=True)  # Field name made lowercase.
    mfr_unittypenumberofunitsoccupied = models.TextField(db_column='MFR_UnitTypeNumberOfUnitsOccupied', blank=True, null=True)  # Field name made lowercase.
    unittypeactualrent = models.DecimalField(db_column='UnitTypeActualRent', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unittypebathstotal = models.SmallIntegerField(db_column='UnitTypeBathsTotal', blank=True, null=True)  # Field name made lowercase.
    unittypebedstotal = models.SmallIntegerField(db_column='UnitTypeBedsTotal', blank=True, null=True)  # Field name made lowercase.
    unittypedescription = models.TextField(db_column='UnitTypeDescription', blank=True, null=True)  # Field name made lowercase.
    unittypegarageattachedyn = models.IntegerField(db_column='UnitTypeGarageAttachedYN', blank=True, null=True)  # Field name made lowercase.
    unittypegaragespaces = models.DecimalField(db_column='UnitTypeGarageSpaces', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unittypekey = models.TextField(db_column='UnitTypeKey', primary_key=True)  # Field name made lowercase.
    unittypeproforma = models.IntegerField(db_column='UnitTypeProForma', blank=True, null=True)  # Field name made lowercase.
    unittypetotalrent = models.DecimalField(db_column='UnitTypeTotalRent', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unittypetype = models.TextField(db_column='UnitTypeType', blank=True, null=True)  # Field name made lowercase.
    unittypeunitstotal = models.SmallIntegerField(db_column='UnitTypeUnitsTotal', blank=True, null=True)  # Field name made lowercase.
    listingid = models.TextField(db_column='ListingId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propertyunittypes'
