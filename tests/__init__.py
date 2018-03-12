"""
tests module - 

    A package defining the api tests. Tests are partitioned according to their type.
    All tests in this api use the pytest package (asked for in the requirements).
    Package test types: 
        unit tests - located in 'tests.unit_tests' sub-pack. This are the tests
        that check the integrity of functions and code that does NOT require
        connection do outside sources, such as Redis servers and databases.
        integration tests - located in 'tests.integration_tests' sub-pack. This are
        the tests that check the integrity of functions and code that REQUIRE
        connection do outside sources, such as Redis servers and databases.
"""