# Created by Amrita at 20-08-2019
Feature: SKF application test
  # Enter feature description here

  Scenario Outline: Launch SKF application and fetch the drop down options test
    Given User is on "https://www.skfbearingselect.com"
    When Click on "Accept & continue" button if displayed
    Then Click on Single Bearing image
    Then Click on Select bearing type dropdown
    Then validate that <Bearings_Options> are displayed
    Then Close the dropdown without selecting any option

    Examples:

      |Bearings_Options|
      |['Insert bearing (Y-bearing)', 'Angular contact ball bearings', 'Self-aligning ball bearings', 'Cylindrical roller bearings','Needle roller bearings', 'Tapered roller bearings', 'Spherical roller bearings', 'CARB toroidal roller bearings', 'Thrust ball bearings', 'Cylindrical roller thrust bearings', 'Needle roller thrust bearings', 'Spherical roller thrust bearings', 'Track roller', 'Deep groove ball bearings']|