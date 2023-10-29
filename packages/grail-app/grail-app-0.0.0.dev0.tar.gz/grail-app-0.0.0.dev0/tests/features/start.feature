Feature: As a website owner,
    I want to configure my website

    Scenario: Update configuration
        Given A app is created
        When I set NEWCONFIG to newvalue
        Then The value of NEWCONFIG is newvalue
