__author__ = 'mike'


def Butler1972():
    '''
    data from:

    Butler, R. F. (1972). Natural remanent magnetization and thermomagnetic properties of the Allende meteorite.
    Earth and Planetary Science Letters, 17(1), 120–128. doi:10.1016/0012-821X(72)90266-X
    '''

    allende = new_meteorite(name='allende', group='CV', subgroup='CV3', iron_content='23.85e-2',
                            magnetic_carriers='95 wt% taenite (67% Ni), 5 wt% taenite (36% Ni)'
    fall = True, fall_date = '1969 February 08', shock_stage = 'S1')
    Butler1972a = new_sample(name='a', meteorite=allende,
                             intensity=1.31, intensity_error=0.42, unit='Oe',
                             determination_type='TT',
                             citekey='Butler1972',
                             vacuum=1e-5, vac_unit='torr', fit_t_min=30, fit_t_max=150, lab_field=0.59)
    Butler1972b = new_sample(name='b', meteorite=allende,
                             intensity=1.08, intensity_error=0.15, unit='Oe',
                             determination_type='TT',
                             citekey='Butler1972',
                             vacuum=1e-5, vac_unit='torr', fit_t_min=30, fit_t_max=150, lab_field=0.59)
    Butler1972c = new_sample(name='c', meteorite=allende,
                             intensity=0.93, intensity_error=0.20, unit='Oe',
                             determination_type='TT',
                             citekey='Butler1972',
                             vacuum=1e-5, vac_unit='torr', fit_t_min=30, fit_t_max=150, lab_field=0.59)


def Banerjee1972():
    '''
    data from:
    Banerjee, S. K., & Hargraves, R. B. (1972). Natural remanent magnetizations of carbonaceous chondrites and the
    magnetic field in the early solar system. Earth and Planetary Science Letters, 17(1), 110–119.
    doi:10.1016/0012-821X(72)90265-8
    '''
    allende = new_meteorite(name='allende', group='CV', subgroup='CV3', iron_content='23.85e-2',
                            magnetic_carriers='95 wt% taenite (67% Ni), 5 wt% taenite (36% Ni)'
    fall = True, fall_date = '1969 February 08', shock_stage = 'S1')
    murchison = new_meteorite(name='murchison', group='CM', subgroup='CM2', iron_content='22.13e-2',
                              fall=True, fall_date='1969 September 28', shock_stage='S1-S2')
    Banerjee1972_allende_1a = new_sample(name='allende(a)', meteorite=allende,
                                         intensity=1.23, unit='Oe',
                                         determination_type='TT',
                                         citekey='Banerjee1972',
                                         vacuum=2e-5, vac_unit='torr', fit_t_min=20, fit_t_max=110, lab_field=0.52)
    Banerjee1972_allende_1b = new_sample(name='allende1(b)', meteorite=allende,
                                         intensity=0.96, unit='Oe',
                                         determination_type='TT-modified',
                                         citekey='Banerjee1972',
                                         vacuum=2e-5, vac_unit='torr', fit_t_min=20, fit_t_max=110, lab_field=0.52)
    Banerjee1972_allende_2a = new_sample(name='allende2(a)', meteorite=allende,
                                         intensity=0.96, unit='Oe',
                                         determination_type='TT-modified',
                                         citekey='Banerjee1972',
                                         vacuum=2e-5, vac_unit='torr', fit_t_min=20, fit_t_max=110, lab_field=0.52)
