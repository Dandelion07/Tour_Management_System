--
-- File generated with SQLiteStudio v3.3.3 on Mon Jul 25 14:01:23 2022
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: AccessTBL
DROP TABLE IF EXISTS AccessTBL;

CREATE TABLE AccessTBL (
    Id                 INTEGER PRIMARY KEY AUTOINCREMENT
                               UNIQUE
                               NOT NULL,
    CreateTour         BOOLEAN NOT NULL,
    DeleteTour         BOOLEAN NOT NULL,
    ConfirmTour        BOOLEAN NOT NULL,
    RegisterPassenger  BOOLEAN NOT NULL,
    ModifyPassenger    BOOLEAN NOT NULL,
    CancelRegistration BOOLEAN NOT NULL,
    ReserveCars        BOOLEAN NOT NULL,
    AddUser            BOOLEAN NOT NULL,
    DeleteUser         BOOLEAN NOT NULL
);

INSERT INTO AccessTBL (
                          Id,
                          CreateTour,
                          DeleteTour,
                          ConfirmTour,
                          RegisterPassenger,
                          ModifyPassenger,
                          CancelRegistration,
                          ReserveCars,
                          AddUser,
                          DeleteUser
                      )
                      VALUES (
                          1,
                          1,
                          1,
                          1,
                          0,
                          0,
                          0,
                          0,
                          1,
                          1
                      );

INSERT INTO AccessTBL (
                          Id,
                          CreateTour,
                          DeleteTour,
                          ConfirmTour,
                          RegisterPassenger,
                          ModifyPassenger,
                          CancelRegistration,
                          ReserveCars,
                          AddUser,
                          DeleteUser
                      )
                      VALUES (
                          2,
                          1,
                          1,
                          0,
                          1,
                          1,
                          1,
                          1,
                          0,
                          0
                      );


-- Table: CarTBL
DROP TABLE IF EXISTS CarTBL;

CREATE TABLE CarTBL (
    Id          INTEGER       PRIMARY KEY AUTOINCREMENT
                              NOT NULL,
    Type        NVARCHAR (15) NOT NULL,
    Capacity    INT           NOT NULL,
    CarTag      NVARCHAR (9)  NOT NULL,
    DriverName  NVARCHAR (70),
    DriverID    CHAR (10),
    DriverPhone CHAR (11) 
);

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       1,
                       'مینی بوس',
                       20,
                       '57ه373-67',
                       'ابراهیم ابراهیمی',
                       '1273419663',
                       '09137646856'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       2,
                       'مینی بوس',
                       20,
                       '92ع550-67',
                       'حسین احمدی',
                       '1273369743',
                       '09139430862'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       3,
                       'مینی بوس',
                       20,
                       '69ط572-13',
                       'مصطفی اسدی',
                       '1290634397',
                       '09134026587'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       4,
                       'مینی بوس',
                       20,
                       '32ف924-67',
                       'رامین اسکندری',
                       '1288269675',
                       '09133005083'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       5,
                       'اتوبوس',
                       40,
                       '17ه642-53',
                       'حبیب الله اسلامی',
                       '1275875850',
                       '09132448673'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       6,
                       'ون',
                       14,
                       '17ج283-53',
                       'حامد اسماعیلی',
                       '1280747724',
                       '09135500493'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       7,
                       'اتوبوس',
                       40,
                       '89ه231-67',
                       'بهرام افشار',
                       '1284864076',
                       '09132063214'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       8,
                       'ون',
                       14,
                       '77د290-13',
                       'حمید اکبری',
                       '1299686370',
                       '09133186778'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       9,
                       'ون',
                       14,
                       '38ج365-53',
                       'نادر امامی',
                       '1286416771',
                       '09136664432'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       10,
                       'ون',
                       14,
                       '12ع236-53',
                       'غلامرضا امیری',
                       '1288978016',
                       '09137384743'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       11,
                       'اتوبوس',
                       40,
                       '41د959-53',
                       'یعقوب امین',
                       '1287368025',
                       '09139469511'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       12,
                       'مینی بوس',
                       20,
                       '76ط685-53',
                       'جواد امینی',
                       '1295759201',
                       '09133415323'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       13,
                       'اتوبوس',
                       40,
                       '82ز895-67',
                       'احسان انصاری',
                       '1288934606',
                       '09133215441'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       14,
                       'ون',
                       14,
                       '89م629-67',
                       'غلام بابایی',
                       '1287572543',
                       '09136109648'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       15,
                       'اتوبوس',
                       40,
                       '28ج878-53',
                       'علی اکبر باقری',
                       '1291778622',
                       '09133419910'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       16,
                       'ون',
                       14,
                       '80و445-67',
                       'امید بهرامی',
                       '1286330420',
                       '09131728649'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       17,
                       'ون',
                       14,
                       '39ط259-53',
                       'بهزاد بیات',
                       '1292241830',
                       '09131496865'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       18,
                       'اتوبوس',
                       40,
                       '88چ370-67',
                       'سیدعلی ترابی',
                       '1298388675',
                       '09139144480'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       19,
                       'ون',
                       14,
                       '34ب278-13',
                       'ایمان تهرانی',
                       '1279286378',
                       '09134786925'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       20,
                       'اتوبوس',
                       40,
                       '26م151-53',
                       'فرهاد توکلی',
                       '1292070073',
                       '09131374650'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       21,
                       'اتوبوس',
                       40,
                       '26س605-67',
                       'احمد جعفری',
                       '1275520204',
                       '09139486152'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       22,
                       'مینی بوس',
                       20,
                       '87ص721-53',
                       'میلاد جلالی',
                       '1284870220',
                       '09131605134'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       23,
                       'مینی بوس',
                       20,
                       '59ل925-13',
                       'امیرحسین جمشیدی',
                       '1296826483',
                       '09136129681'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       24,
                       'مینی بوس',
                       20,
                       '45ز464-67',
                       'عزیز جوادی',
                       '1291840066',
                       '09136680298'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       25,
                       'ون',
                       14,
                       '16ک783-67',
                       'بهروز حبیبی',
                       '1289251839',
                       '09135733450'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       26,
                       'مینی بوس',
                       20,
                       '35چ982-13',
                       'رسول حسنی',
                       '1279464679',
                       '09136911909'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       27,
                       'ون',
                       14,
                       '87ف257-13',
                       'علی حسینی',
                       '1277569283',
                       '09137344224'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       28,
                       'اتوبوس',
                       40,
                       '19ف812-13',
                       'سیدحسین حمیدی',
                       '1287356505',
                       '09135722245'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       29,
                       'مینی بوس',
                       20,
                       '31ج464-13',
                       'عباس حیدری',
                       '1284186036',
                       '09132117715'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       30,
                       'اتوبوس',
                       40,
                       '77ج767-13',
                       'غلامحسین خسروی',
                       '1290319925',
                       '09132799851'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       31,
                       'اتوبوس',
                       40,
                       '43ق931-67',
                       'کریم خلیلی',
                       '1281751485',
                       '09139634589'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       32,
                       'اتوبوس',
                       40,
                       '71ق611-67',
                       'بهمن دهقان',
                       '1278632086',
                       '09132326625'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       33,
                       'مینی بوس',
                       20,
                       '42س753-13',
                       'حیدر دهقانی',
                       '1275694163',
                       '09132528348'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       34,
                       'ون',
                       14,
                       '15ل677-53',
                       'پرویز راد',
                       '1294657710',
                       '09131715851'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       35,
                       'مینی بوس',
                       20,
                       '30ک910-53',
                       'اسدالله رجبی',
                       '1276898108',
                       '09131820808'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       36,
                       'ون',
                       14,
                       '40ه169-13',
                       'داوود رحمانی',
                       '1280432659',
                       '09134451988'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       37,
                       'اتوبوس',
                       40,
                       '79ق797-13',
                       'سعید رحیمی',
                       '1275343436',
                       '09137716745'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       38,
                       'اتوبوس',
                       40,
                       '73د874-53',
                       'منصور رستمی',
                       '1280316929',
                       '09132023269'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       39,
                       'اتوبوس',
                       40,
                       '29ن218-67',
                       'محمدتقی رشیدی',
                       '1275626995',
                       '09134888799'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       40,
                       'مینی بوس',
                       20,
                       '35ذ719-67',
                       'مهدی رضایی',
                       '1285774388',
                       '09135308984'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       41,
                       'ون',
                       14,
                       '35ج741-13',
                       'خلیل رضوی',
                       '1280186505',
                       '09136714151'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       42,
                       'مینی بوس',
                       20,
                       '30ذ372-67',
                       'روح الله رمضانی',
                       '1284600706',
                       '09131272951'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       43,
                       'مینی بوس',
                       20,
                       '45ن638-53',
                       'حسینعلی رنجبر',
                       '1274547740',
                       '09133048452'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       44,
                       'ون',
                       14,
                       '35ج330-67',
                       'اسماعیل زارع',
                       '1272711362',
                       '09138088683'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       45,
                       'اتوبوس',
                       40,
                       '16ص876-13',
                       'عیسی زارعی',
                       '1278326244',
                       '09131728494'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       46,
                       'مینی بوس',
                       20,
                       '99ک855-53',
                       'ناصر زمانی',
                       '1275801735',
                       '09137889006'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       47,
                       'اتوبوس',
                       40,
                       '29ل544-67',
                       'مسعود سلطانی',
                       '1295682410',
                       '09133286255'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       48,
                       'مینی بوس',
                       20,
                       '78ل995-67',
                       'وحید سلیمانی',
                       '1296833934',
                       '09139426737'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       49,
                       'ون',
                       14,
                       '24ز228-53',
                       'محمدحسن سلیمی',
                       '1287049235',
                       '09137866046'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       50,
                       'ون',
                       14,
                       '96س961-53',
                       'محمدحسین شریفی',
                       '1275344239',
                       '09136939050'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       51,
                       'مینی بوس',
                       20,
                       '30د604-67',
                       'عباسعلی شفیعی',
                       '1282477906',
                       '09133065931'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       52,
                       'مینی بوس',
                       20,
                       '49ب196-67',
                       'مهرداد شمس',
                       '1290663224',
                       '09139930589'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       53,
                       'ون',
                       14,
                       '48ع666-67',
                       'محمدرضا صادقی',
                       '1283076385',
                       '09131816053'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       54,
                       'مینی بوس',
                       20,
                       '33ع817-67',
                       'محمدعلی صالحی',
                       '1299002190',
                       '09132129260'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       55,
                       'مینی بوس',
                       20,
                       '95ج562-13',
                       'عبدالحسین طالبی',
                       '1281354031',
                       '09132021936'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       56,
                       'ون',
                       14,
                       '96ک746-67',
                       'اکبر طاهری',
                       '1281009086',
                       '09136681397'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       57,
                       'مینی بوس',
                       20,
                       '61ک862-13',
                       'اسماعیل عابدی',
                       '1281414301',
                       '09133645808'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       58,
                       'اتوبوس',
                       40,
                       '58ب174-53',
                       'مرتضی عباسی',
                       '1281117809',
                       '09137273258'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       59,
                       'ون',
                       14,
                       '16ک649-13',
                       'بهنام عبدالهی',
                       '1283433567',
                       '09135066655'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       60,
                       'اتوبوس',
                       40,
                       '43س565-13',
                       'جمشید عبدی',
                       '1273249214',
                       '09134393304'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       61,
                       'مینی بوس',
                       20,
                       '19ن961-67',
                       'قاسم عزیزی',
                       '1286286759',
                       '09137727244'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       62,
                       'مینی بوس',
                       20,
                       '77ن978-53',
                       'ابوالقاسم عسگری',
                       '1296224040',
                       '09135418054'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       63,
                       'ون',
                       14,
                       '77ف607-67',
                       'میثم عظیمی',
                       '1298208713',
                       '09132508959'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       64,
                       'مینی بوس',
                       20,
                       '48ن134-67',
                       'مسلم علوی',
                       '1274281888',
                       '09136240135'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       65,
                       'مینی بوس',
                       20,
                       '64ذ937-53',
                       'عبدالرضا علیپور',
                       '1276854118',
                       '09132589442'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       66,
                       'مینی بوس',
                       20,
                       '41م722-13',
                       'عبدالله علیزاده',
                       '1281968442',
                       '09133064948'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       67,
                       'اتوبوس',
                       40,
                       '86ن695-53',
                       'رحیم غفاری',
                       '1286967768',
                       '09139658934'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       68,
                       'ون',
                       14,
                       '80ز997-13',
                       'جعفر غلامی',
                       '1286263201',
                       '09138757508'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       69,
                       'ون',
                       14,
                       '80د776-13',
                       'غلامعلی فتحی',
                       '1275751617',
                       '09139938659'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       70,
                       'اتوبوس',
                       40,
                       '44ر172-67',
                       'رمضان فراهانی',
                       '1284721723',
                       '09135831099'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       71,
                       'مینی بوس',
                       20,
                       '74ل415-67',
                       'حبیب فلاح',
                       '1285261305',
                       '09131714100'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       72,
                       'مینی بوس',
                       20,
                       '59ط795-53',
                       'محمود قاسمی',
                       '1283342511',
                       '09132423807'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       73,
                       'اتوبوس',
                       40,
                       '16ل471-53',
                       'یوسف قربانی',
                       '1274582549',
                       '09135501715'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       74,
                       'مینی بوس',
                       20,
                       '58ص622-53',
                       'علی محمد قنبری',
                       '1281510817',
                       '09136932285'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       75,
                       'مینی بوس',
                       20,
                       '77ب555-67',
                       'مجید کاظمی',
                       '1287616850',
                       '09137291234'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       76,
                       'اتوبوس',
                       40,
                       '14چ604-53',
                       'امین کرمی',
                       '1282738042',
                       '09135472849'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       77,
                       'مینی بوس',
                       20,
                       '37ه299-13',
                       'حسن کریمی',
                       '1292042363',
                       '09135226947'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       78,
                       'مینی بوس',
                       20,
                       '88ج789-53',
                       'محمدجواد کمالی',
                       '1294512953',
                       '09135396820'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       79,
                       'مینی بوس',
                       20,
                       '38ن999-53',
                       'علی رضا کیانی',
                       '1280662624',
                       '09139375288'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       80,
                       'اتوبوس',
                       40,
                       '87ز720-67',
                       'جلال لطفی',
                       '1275576190',
                       '09131090754'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       81,
                       'اتوبوس',
                       40,
                       '21ص980-67',
                       'سیدمحمد محسنی',
                       '1272308127',
                       '09135048216'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       82,
                       'مینی بوس',
                       20,
                       '60ب617-67',
                       'محمد محمدی',
                       '1274116330',
                       '09133353846'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       83,
                       'مینی بوس',
                       20,
                       '40ل364-53',
                       'مجتبی محمودی',
                       '1288818436',
                       '09132270966'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       84,
                       'مینی بوس',
                       20,
                       '97ق396-67',
                       'مهران مختاری',
                       '1283448647',
                       '09136895953'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       85,
                       'ون',
                       14,
                       '15ع807-53',
                       'علیرضا مرادی',
                       '1274227057',
                       '09137659657'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       86,
                       'اتوبوس',
                       40,
                       '35چ865-67',
                       'سجاد مقدم',
                       '1290176406',
                       '09132289604'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       87,
                       'ون',
                       14,
                       '28ف975-53',
                       'اصغر ملکی',
                       '1293595971',
                       '09137926102'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       88,
                       'ون',
                       14,
                       '47ه585-53',
                       'شهرام منصوری',
                       '1289968616',
                       '09137257813'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       89,
                       'اتوبوس',
                       40,
                       '86ج401-53',
                       'کاظم مهدوی',
                       '1274510093',
                       '09134864303'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       90,
                       'مینی بوس',
                       20,
                       '97ک849-13',
                       'رضا موسوی',
                       '1276812904',
                       '09131064225'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       91,
                       'مینی بوس',
                       20,
                       '86چ361-67',
                       'ابوالفضل میرزایی',
                       '1296982863',
                       '09136640172'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       92,
                       'ون',
                       14,
                       '25ک489-53',
                       'قربانعلی نادری',
                       '1275331167',
                       '09133861472'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       93,
                       'ون',
                       14,
                       '18ر882-67',
                       'هادی نجفی',
                       '1285469985',
                       '09136848213'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       94,
                       'اتوبوس',
                       40,
                       '86ک732-13',
                       'موسی نصیری',
                       '1284702057',
                       '09135824225'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       95,
                       'ون',
                       14,
                       '95ه498-67',
                       'حمیدرضا نظری',
                       '1294248488',
                       '09136074017'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       96,
                       'مینی بوس',
                       20,
                       '45م689-67',
                       'صادق نوروزی',
                       '1278539320',
                       '09136402064'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       97,
                       'مینی بوس',
                       20,
                       '50ز330-53',
                       'امیر نوری',
                       '1296338848',
                       '09137237103'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       98,
                       'اتوبوس',
                       40,
                       '71س651-13',
                       'محسن هاشمی',
                       '1282404011',
                       '09137113234'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       99,
                       'اتوبوس',
                       40,
                       '65ذ406-67',
                       'یدالله یزدانی',
                       '1295893209',
                       '09137782224'
                   );

INSERT INTO CarTBL (
                       Id,
                       Type,
                       Capacity,
                       CarTag,
                       DriverName,
                       DriverID,
                       DriverPhone
                   )
                   VALUES (
                       100,
                       'ون',
                       14,
                       '24ط429-53',
                       'علی اصغر یوسفی',
                       '1297031179',
                       '09136922285'
                   );


-- Table: PassengerTBL
DROP TABLE IF EXISTS PassengerTBL;

CREATE TABLE PassengerTBL (
    Id         CHAR (10)     PRIMARY KEY
                             NOT NULL,
    Name       NVARCHAR (30) NOT NULL,
    Family     NVARCHAR (50) NOT NULL,
    FatherName NVARCHAR (30) NOT NULL,
    Phone      CHAR (11) 
);

-- Table: TourCarsTBL
DROP TABLE IF EXISTS TourCarsTBL;

CREATE TABLE TourCarsTBL (
    Id     INTEGER PRIMARY KEY AUTOINCREMENT
                   UNIQUE
                   NOT NULL,
    TourId INTEGER REFERENCES TourTBL (Id) 
                   NOT NULL,
    CarId  INTEGER REFERENCES CarTBL (Id) 
                   NOT NULL
);

-- Table: TourPassengersTBL
DROP TABLE IF EXISTS TourPassengersTBL;

CREATE TABLE TourPassengersTBL (
    Id          INTEGER   PRIMARY KEY AUTOINCREMENT
                          UNIQUE
                          NOT NULL,
    TourId      INTEGER   REFERENCES TourTBL (Id) 
                          NOT NULL,
    PassengerId CHAR (10) REFERENCES PassengerTBL (Id) 
                          NOT NULL
);

-- Table: TourTBL
DROP TABLE IF EXISTS TourTBL;

CREATE TABLE TourTBL (
    Id          INTEGER       PRIMARY KEY AUTOINCREMENT
                              NOT NULL,
    Destination NVARCHAR (50) NOT NULL,
    Origin      NVARCHAR (50) NOT NULL,
    Capacity    INTEGER       NOT NULL,
    DepartTime  DATETIME      NOT NULL,
    ReturnTime  DATETIME      NOT NULL,
    Status      NVARCHAR (20) NOT NULL
);


-- Table: UserTBL
DROP TABLE IF EXISTS UserTBL;

CREATE TABLE UserTBL (
    Username    VARCHAR (50) PRIMARY KEY
                             NOT NULL,
    Password    CHAR (64)    NOT NULL,
    AccessLevel INTEGER      NOT NULL
);

INSERT INTO UserTBL (
                        Username,
                        Password,
                        AccessLevel
                    )
                    VALUES (
                        'user',
                        '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb',
                        2
                    );

INSERT INTO UserTBL (
                        Username,
                        Password,
                        AccessLevel
                    )
                    VALUES (
                        'admin',
                        '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',
                        1
                    );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
