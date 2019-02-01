__author__ = 'mike'
import helper
from table_definitions import Group, Meteorite, Sample


def new_meteorite(name, group, subgroup=None,
                  magnetic_carriers=None, iron_content=None,
                  fall=False, fall_date=None,
                  shock_stage=None,
                  comment='', notes=''):
    session = helper.connect_db()
    res = session.query(Group).filter(Group.name == group).first()
    if not res:
        res = session.query(Group).filter(Group.full_name == group).first()
    if res:
        check = session.query(Meteorite).filter(Meteorite.name == name).first()

        if check:
            print '%s already in database' % check.name
            return check
        else:
            met = Meteorite(name=name.lower(), group_id=res.id,
                            magnetic_carriers=None, iron_content=iron_content,
                            shock_stage=shock_stage,
                            fall=True, fall_date=fall_date,
                            comment=comment, notes=notes
            )
            session.add(met)
            session.commit()
            session.close()
            return res
    else:
        print '%s not found' % group


def new_sample(name, meteorite,
               intensity, unit, determination_type,
               citekey,
               intensity_error=None, lab_field=None,
               fit_t_min=None, fit_t_max=None,
               vacuum=None, vac_unit='', inert_gas=None,
               comment='', notes=''):
    session = helper.connect_db()

    conversion = {'Oe': 0.0001,  #to Tesla
                  'mT': 1e-3,
                  'muT': 1e-6,
                  'torr': 133.322368,  #pascal
                  '': 1}

    if isinstance(meteorite, Meteorite):
        met_id = meteorite.id
    else:
        res = session.query(Meteorite).filter(Meteorite.name == meteorite).first()
        if res:
            met_id = res.id
    check = session.query(Sample).filter(Sample.name == name).first()
    # try:
    #     Pint_T = intensity*conversion[unit]

    if not check:
        sample = Sample(name=name, meteorite_id=met_id,
                        intensity=intensity * conversion[unit], intensity_error=intensity_error * conversion[unit],
                        determination_type=determination_type,
                        citekey=citekey,
                        vacuum=vacuum * conversion[vac_unit], inert_gas=inert_gas,
                        fit_t_min=fit_t_min, fit_t_max=fit_t_max, lab_field=lab_field * conversion[unit],
                        comment=comment, notes=notes)
        session.add(sample)
        session.commit()
        session.close()
        return sample

if __name__ == '__main__':
    import import_from_pub

    import_from_pub.Butler1972()
    import_from_pub.Banerjee1972()
