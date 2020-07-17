import numpy as np
#emerlin_lovell_config
num_dishes = 7
diameters=[25., 32., 25., 25., 25., 76., 25.]
diameters_25=[25., 25., 25., 25., 25., 25., 25.]
emerlin_diam = np.zeros((num_dishes,), np.float64) + diameters
diam_25 = np.zeros((num_dishes,), np.float64) + diameters_25
emerlin_xx=[3923069.1710, 3919982.7520, 3859711.5030, 3828714.5130, 3822473.3650, 3822252.6430, 3817176.5610]
emerlin_yy=[146804.3680, -2651.9820, 201995.0770, 169458.9950, 153692.3180, 153995.6830, 162921.1790]
emerlin_zz=[5009320.5280, 5013849.8260, 5056134.2510, 5080647.7490, 5085851.3030, 5086051.4430, 5089462.0570]