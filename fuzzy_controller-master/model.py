# Ухвалення рішення про розмір чайових у ресторані.
# Розмір чайових повинен залежати від якості обслуговування та якості страв.

input_lvs = [
    {
        'X': (0, 101, 1),
        'name': 'Quality_of_service',
        'terms': {
            'low': ('trapmf', 0, 10, 20, 30),
            'medium': ('trapmf', 20, 30, 45, 60),
            'high': ('trapmf', 50, 60, 75, 87),
            'extremely high': ('trapmf', 78, 80, 90, 100),
        }
    },

    {
        'X': (0, 101, 1),
        'name': 'Quality_of_dishes',
        'terms': {
            'low': ('trapmf', 0, 10, 20, 30),
            'medium': ('trapmf', 20, 30, 45, 60),
            'high': ('trapmf', 50, 60, 75, 87),
            'extremely high': ('trapmf', 78, 80, 90, 100),
        }
    }

    # {
    #     'X': (0, 5001, 1),
    #     'name': 'Payment',
    #     'terms': {
    #         'low': ('trapmf', 0, 50, 200, 300),
    #         'medium': ('trapmf', 200, 300, 500, 700),
    #         'high': ('trapmf', 550, 700, 1000, 1800),
    #         'extremely high': ('trapmf', 1000, 1500, 2000, 3000),
    #     }
    # }
]

output_lv = {
    # what percent of price to pay as a tip
    'X': (0, 26, 1),
    'name': 'Tip',
    'terms': {
        'none to very little': ('trapmf', 0, 1, 2, 4),
        'low': ('trapmf', 3, 5, 6, 8),
        'medium': ('trimf', 7, 10, 14),
        'high': ('trapmf', 12, 16, 18, 22),
        'extremely high': ('trapmf', 17, 20, 22, 25),
    }
}


rule_base = [
    (('low', 'low'), 'none to very little'),
    (('low', 'medium'), 'none to very little'), 
    (('low', 'medium'), 'low'), 
    (('low', 'high'), 'low'), 
    (('low', 'high'), 'medium'), 
    (('low', 'extremely high'), 'low'),
    (('low', 'extremely high'), 'medium'),
    (('low', 'extremely high'), 'high'), 
    (('medium', 'low'), 'none to very little'), 
    (('medium', 'low'), 'low'),
    (('medium', 'low'), 'medium'),
    (('medium', 'medium'), 'low'), 
    (('medium', 'medium'), 'medium'),
    (('medium', 'high'), 'medium'), 
    (('medium', 'high'), 'high'),
    (('medium', 'extremely high'), 'medium'), 
    (('medium', 'extremely high'), 'high'),
    (('high', 'low'), 'low'), 
    (('high', 'low'), 'medium'),
    (('high', 'medium'), 'medium'), 
    (('high', 'medium'), 'high'),
    (('high', 'high'), 'high'), 
    (('high', 'extremely high'), 'high'), 
    (('high', 'extremely high'), 'extremely high'),
    (('extremely high', 'low'), 'low'), 
    (('extremely high', 'low'), 'medium'),
    (('extremely high', 'low'), 'high'),
    (('extremely high', 'medium'), 'medium'), 
    (('extremely high', 'medium'), 'high'), 
    (('extremely high', 'high'), 'high'), 
    (('extremely high', 'high'), 'extremely high'),
    (('extremely high', 'extremely high'), 'extremely high')
]