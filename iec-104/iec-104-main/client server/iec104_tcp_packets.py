# u frame types
STARTDT_ACT=0x07
STARTDT_CON=0x0b
STOPDT_ACT=0x13
STOPDT_CON=0x23
TESTFR_ACT=0x43
TESTFR_CON=0x83

#Sending Reasons
Cause_Act=0x06
Cause_Deact=0x08

#Control values
SCO_Off_Np_Ex=0x00
SCO_On_Np_Ex=0x01
SCO_Off_Sp_Ex=0x04
SCO_On_Sp_Ex=0x05
SCO_Off_Np_Se=0x80
SCO_On_Np_Se=0x81

DCO_Off_Np_Se=0x81
DCO_On_Np_Se=0x82

RCO_Down_Np_Se=0x81
RCO_Up_Np_Se=0x82

plist=[
    ('START','auto','if',[45,1,Cause_Act,4,3,(45000,SCO_Off_Np_Se)]),
    ('START','auto','if',[58,1,Cause_Act,4,3,(45200,SCO_Off_Np_Se)]),
    ('START','auto','if',[61,1,Cause_Deact,4,3,(48250,10,0x80)]),
    ('START','auto','if',[61,1,Cause_Deact,4,3,(48300,101,0x80)]),
    ('START','auto','if',[101,1,Cause_Deact,4,4,(0,0x05)]),
    ('START','auto','if',[103,1,Cause_Deact,4,4,(0,0x05)]),
    ('START','auto','sf'),
    ('START','auto','uf',STARTDT_ACT),
    ('START','auto','uf',TESTFR_ACT),
    ('START','auto','uf',TESTFR_CON)
]

