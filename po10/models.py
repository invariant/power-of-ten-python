

class Model(object):
    pass

class Athlete(Model):
    name = None
    coach = None
    clubs = None
    gender = None
    age_group = None
    county = None
    region = None
    nation = None
    date_of_birth = None
    
    def __repr__(self):
        return "< Athlete: %s >" % self.name
    
    