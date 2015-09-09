# -*- coding: utf-8 -*-

class OrdinalValueError(Exception):
    def __init__(self, info=None):
        self.msg = info
        
    def __str__(self):
        return repr(self.msg)
    

class OrdinalTemplate(object):
    num_name = {}
    name_num = {}
    
    @classmethod
    def add_num_name(cls, num_name_dict):
        cls.num_name.update(num_name_dict)
        cls.name_num = {v:k for k,v in cls.num_name.items()}
    
    @classmethod    
    def set_num_name(cls, num_name_dict):
        cls.num_name = num_name_dict
        cls.name_num = {v:k for k,v in cls.num_name.items()}
    
    def __init__(self, value):
        if value in type(self).num_name:
            self.num = value
            self.name = type(self).num_name[value]
        elif value in type(self).name_num:
            self.name = value
            self.num = type(self).name_num[value]
        else:
            raise OrdinalValueError("Valid numbers are %s" % type(self).num_name)
    
    def __str__(self):
        return str(self.name)
      
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, self.num)
    
    def __cmp__(self, another_ord):
        return cmp(self.num, another_ord.num)
        
    
def create_ordinal_class(class_name, num_name={}):
     globals()[class_name] = type(class_name, (OrdinalTemplate,), dict(num_name=num_name))


        