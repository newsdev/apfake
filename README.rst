APFAKE
======

.. figure:: https://user-images.githubusercontent.com/109988/37601020-67598cd4-2b5f-11e8-9bfc-be939317eb46.png
   :alt: screen shot 2018-03-19 at 10 21 06 am

   screen shot 2018-03-19 at 10 21 06 am

Have you ever thought “I should record the AP API test that’s coming in
a half hour” only to find out that it actually concluded a half hour
AGO? I’ve done this several times. And if I’ve done it before, I have to
assume others have done it as well.

Taking the FINAL JSON state file of an AP API election test (e.g., what
happens if you hit the test URL after a test has run but before it’s
zeroed out in the moments before a new test or a live election),
``apfake`` will generate a file of zeros and then ``n`` intermediate
states between the zeros and the final file with a smoothly incrementing
set of votes.

In short: If you give it the last file of a test, ``apfake`` will
generate all the missing files for you.

CAVEATS
-------

-  ``apfake`` does not call races.
-  ``apfake`` votes do not properly match actual election night spikes
   when ballots are counted.
-  ``apfake`` precincts reporting and precincts reporting percentages
   are probably wrong.
-  ``apfake`` does not work on zeros or initialization data. It needs
   the format ``&results=ru`` from the AP API.

USAGE
-----

::

    apfake -f 2018-03-20-final.json -n 10 -d /tmp/foo/ -r 2018-03-20

``apfake`` accepts four command-line options, two are required.

-  ``-f, --final-results-path`` **REQUIRED** The path to the final
   results JSON file.
-  ``-n, --number`` **REQUIRED** The number of files to generate.
-  ``-r, --racedate`` *OPTIONAL* The ``YYYY-MM-DD`` racedate of the
   election. If the file specified in ``final-results-path`` has a
   racedate in the filename, this will be used. Otherwise, ``apfake``
   will raise a ``ValueError``.
-  ``-d, --data-directory`` *OPTIONAL* A directory or set of directories
   to write the data to. ``apfake`` will create these directories if
   they do not exist, and will also create a directory named for the
   ``racedate`` to hold the output files. Defaults to ``/tmp/``.

DEBUGGING WITCHERY
------------------

This is the shape that ``apfake`` expects your JSON to have. If you use
the format ``&results=ru`` it will probably work. If you use a different
format, it might work, though YMMV.

::

    """
    results.keys()
    dict_keys(['electionDate', 'timestamp', 'races', 'nextrequest'])

    results['races'][0].keys()
    dict_keys(['test', 'raceID', 'raceType', 'raceTypeID', 'officeID', 'officeName', 'party', 'seatName', 'reportingUnits'])

    result['races][0]['reportingUnits'][0].keys()
    dict_keys(['statePostal', 'stateName', 'level', 'lastUpdated', 'precinctsReporting', 'precinctsTotal', 'precinctsReportingPct', 'candidates'])

    results['races'][0]['reportingUnits'][0]['candidates'][0].keys()
    dict_keys(['first', 'last', 'party', 'incumbent', 'candidateID', 'polID', 'ballotOrder', 'polNum', 'voteCount'])
    """
