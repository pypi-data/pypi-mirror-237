.. _reporting:
Reporting
=========

After validating metadata against a schema, a report can be generated with a tabulation of validation details, including all errors encountered.

Reports are generated with the ``-r`` argument to the ``axiom validate`` command during command-line usage, or via Python.

.. code-block:: python

    from axiom.report import generate_report

    generate_report(
        validator, # A validator object that has been used.
        input_filepath, # The path to the original input file.
        report_filepath # The path to which to write the report
    )


The report will be a plain text file in the following format:

.. code-block:: text

    Axiom Validator 0.1.0
    Report generated: 2021-06-04 13:36:10.227704
    schema_filepath: specifications/mrd-0.1.0.json
    input_filepath: test.json
    Status: FAILED
    +------------+-----------------------+----------------------+
    | Variable   | Attribute             | Error                |
    +============+=======================+======================+
    | _global    | averaging_horizontal  | Attribute is missing |
    +------------+-----------------------+----------------------+
    | _global    | averaging_temporal    | Attribute is missing |
    +------------+-----------------------+----------------------+
    | _global    | averaging_vertical    | Attribute is missing |
    +------------+-----------------------+----------------------+
    | _global    | citation              | Attribute is missing |
    +------------+-----------------------+----------------------+
    | _global    | created               | Attribute is missing |
    +------------+-----------------------+----------------------+
    | _global    | history               | Attribute is missing |
    +------------+-----------------------+----------------------+