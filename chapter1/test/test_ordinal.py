# -*- coding: utf-8 -*-
import ordinal

if __name__ == '__main__':
    #定义学历序数
    ordinal.create_ordinal_class('EduDegree',
                                 {0:'Undereducated',
                                  1:'Primary-school',
                                  2:'Junior-high',
                                  3:'Senior-high',
                                  4:'Bachelor',
                                  5:'Master',
                                  6:'Doctor'})

    edu1 = ordinal.EduDegree(1)
    print edu1
    
    edu2 = ordinal.EduDegree(3)
    edu3 = ordinal.EduDegree(5)
    print edu1 < edu2
    print edu2 > edu3

    #edu4 = ordinal.EduDegree(7)                                     
    #OrdinalValueError: Valid numbers are {0: 'Undereducated', 1: 'Primary-school', 2: u'Junior-high', 3: 'Senior-high', 4: 'Bachelor', 5: 'Master', 6: 'Doctor'}
                                
    #定义年纪序数
    ordinal.create_ordinal_class('Age',
                                 {1:'Child',
                                  2:'Youth',
                                  3:'Middle-aged',
                                  4:'Elderly'})
                                  
    age1 = ordinal.Age(1)
    age2 = ordinal.Age(2)
    print age1, age2, age1 < age2
    
    #age5 = ordinal.Age(5)
    #OrdinalValueError: Valid numbers are {1: 'Child', 2: 'Youth', 3: 'Middle-aged', 4: 'Elderly'}

                              
                            

