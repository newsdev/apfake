from copy import deepcopy

def generate_stepping(final_results, step, number):
    """
    Requires an AP API JSON file from &results=ru
    Does not work on initialization data.d
    """
    results = deepcopy(final_results)

    for r in results['races']:
        for ru in r['reportingUnits']:
            if int(ru['precinctsTotal']) > 0:
                ru['precinctsReporting'] = do_stepping_math(step, number, ru['precinctsReporting'])
                ru['precinctsReportingPct'] = ru['precinctsReporting'] / ru['precinctsTotal']
            for c in ru['candidates']:
                c['voteCount'] = do_stepping_math(step, number, c['voteCount'])

    return results


def generate_zeros(final_results):
    """
    Requires an AP API JSON file from &results=ru
    Does not work on initialization data.
    """
    results = deepcopy(final_results)

    for race in results['races']:
        for reporting_unit in race['reportingUnits']:
            reporting_unit['precinctsReporting'] = 0
            reporting_unit['precinctsReportingPct'] = 0.0
            for candidate in reporting_unit['candidates']:
                candidate['voteCount'] = 0

    return results

def do_stepping_math(step, number, max_votes):
    
    # applies the appropriate math
    # thanks to matt apuzzo for the inspiration
    return int(step/number * max_votes)