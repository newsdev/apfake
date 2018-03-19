import argparse
import os
import re

import ujson as json

from apfake import utils

def main():

    # get the arguments we need
    final_results_path, racedate, number, data_directory = setup()
    
    # prepare the filesystem
    # remove old files
    os.system('mkdir -p %s%s' % (data_directory, racedate))
    os.system('rm -rf %s%s/*.apf.json' % ((data_directory, racedate)))

    print("======================================================")
    print("\tWriting %s files to %s%s" % (number, data_directory, racedate))
    print("======================================================")

    # read in the final results to use as a template
    with open(final_results_path, 'r') as readfile:
        final_results = dict(json.loads(readfile.read()))

    # write the 0th file, e.g., zeroes
    with open('%s%s/%s-%s.apf.json' % (data_directory, racedate, racedate, str(0).zfill(5)), 'w') as writefile:
        writefile.write(json.dumps(utils.generate_zeros(final_results)))
        print("0, ", end='', flush=True)

    # loop over the steps, writing intermediate files
    for step in range(1, number):
        results = utils.generate_stepping(final_results, step, number)

        with open('%s%s/%s-%s.apf.json' % (data_directory, racedate, racedate, str(step).zfill(5)), 'w') as writefile:
            writefile.write(json.dumps(results))

        print_step = "%s, " % step
        if step == number-1:
            print_step = "%s" % print_step
        print(print_step, end='', flush=True)

    # write the last file
    with open('%s%s/%s-%s.apf.json' % (data_directory, racedate, racedate, str(number).zfill(5)), 'w') as writefile:
        writefile.write(json.dumps(final_results))
        print(number, end='\n', flush=True)

def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-directory', '-d', dest='data_directory')
    parser.add_argument('--final-results-path', '-f', dest='final_results_path')
    parser.add_argument('--racedate', '-r', dest='racedate')
    parser.add_argument('--number', '-n', dest='number')
    args = parser.parse_args()

    if not args.data_directory:
        data_directory = "/tmp/"
    else:
        data_directory = args.data_directory

    if not data_directory.endswith('/'):
        if not data_directory == "":
            data_directory = "%s/" % data_directory

    if not args.final_results_path:
        raise ValueError("Must have the last file from an AP test.")
    else:
        final_results_path = args.final_results_path

    if not args.racedate:
        match = re.match('([0-9]{4}-[0-9]{2}-[0-9]{2})', final_results_path)
        if match:
            racedate = match.group(1)
        else:
            raise ValueError("You must pass in a racedate if one cannot be found in the final results filename.")
    else:
        racedate = args.racedate


    if not args.number:
        number = 120
    else:
        number = int(args.number)

    return final_results_path, racedate, number, data_directory

if __name__ == "__main__":
    main()