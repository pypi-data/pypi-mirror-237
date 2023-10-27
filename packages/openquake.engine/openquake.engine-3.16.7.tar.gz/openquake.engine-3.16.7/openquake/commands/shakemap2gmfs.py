
import os
import logging
from openquake.hazardlib.shakemap.maps import get_sitecol_shakemap
from openquake.commonlib import logs, logictree
from openquake.commonlib.readinput import get_site_collection
from openquake.calculators.base import calculators, save_shakemap


def main(id, site_model, *, num_gmfs: int = 0, random_seed: int = 42,
         site_effects: bool = 0, trunclevel: float = 3,
         spatialcorr='yes', crosscorr='yes', cholesky_limit: int = 10_000):
    """
    Example of usage: oq shakemap2gmfs us2000ar20 site_model.csv -n 10
    """
    fname = '%s.npy' % id
    if os.path.exists(fname):
        dic = {'kind': 'file_npy', 'fname': fname}
    else:
        dic = {'kind': 'usgs_id', 'id': id}
    imts = ['PGA', 'SA(0.3)', 'SA(1.0)']
    param = dict(number_of_ground_motion_fields=str(num_gmfs),
                 description='Converting ShakeMap->GMFs',
                 truncation_level=str(trunclevel),
                 calculation_mode='scenario',
                 random_seed=str(random_seed),
                 inputs={'site_model': [os.path.abspath(site_model)]})
    with logs.init("job", param) as log:
        oq = log.get_oqparam()
        calc = calculators(oq, log.calc_id)
        sitecol, shakemap, discarded = get_sitecol_shakemap(
            dic, imts, get_site_collection(oq))
        if len(discarded):
            logging.warning('%d sites discarded', len(discarded))
        calc.datastore['sitecol'] = sitecol
        calc.datastore['full_lt'] = logictree.FullLogicTree.fake()
        if num_gmfs:
            gmfdic = {'kind': 'Silva&Horspool',
                      'spatialcorr': spatialcorr,
                      'crosscorr': crosscorr,
                      'cholesky_limit': cholesky_limit}
            save_shakemap(calc, sitecol, shakemap, gmfdic)
    print('See the output with silx view %s' % calc.datastore.filename)


main.id = 'ShakeMap ID for the USGS'
main.site_model = 'Path to site model file'
main.num_gmfs = 'Number of GMFs to generate'
main.random_seed = 'Random seed to use'
main.site_effects = 'Wether to apply site effects or not'
main.trunclevel = 'Truncation level'
main.spatialcorr = 'Spatial correlation'
main.crosscorr = 'Cross correlation among IMTs'
main.cholesky_limit = 'Cholesky Limit'
