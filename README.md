# Shoe Inventory Manager (L1T30)
This script is a basic implementation of an inventory manager from my L1T30 task. It is desgined to take in an inventory from a text file and display the current info in the console.
This is a command line interface script. Everything to manage the inventory is done in the console running it.

## Table of Contents:
* [Installation](https://github.com/BotEthan/L3T06/#installation)

* [Usage](https://github.com/BotEthan/L3T06/#usage)


## Installation
To install, all that needs to be done is to download the files and edit the **inventory.txt** to contain the stock of the shoes you currently house.

## Usage
In order to use this script please make sure that the **inventory.txt** file is following the set the layout. This layout consists of data separated by a comma (,).The order of the data follows this pattern:
Country of Origin,Shoe Code,Shoe Name,Shoe Price,Shoe Quantity

Upon running the script you'll be greeted by an interface in the console detailing the options in which you can enter to complete specific tasks. These tasks consist of:
1. Reload shoes inventory
    * Reloads the current stored inventory in the script with the inventory.txt file in case it has been changed.
2. Add a shoe to the invetory
    * Allows you to add shoes to the the inventory.txt file. Will require a reload to view changes.
3. View all shoes in the inventory
    * Allows you to view all the shoes currently in the inventory. This is useful to get a specific shoe's code.
4. Restock a shoe
    * Allows you to add stockt to a specific shoe.
5. Search for a shoe
    * Allows you to search for a specific shoe using its code.
6. Total stock value for all shoes
    * Shows the total combined value for all the shoes currently in stock in your inventory.
7. Show the shoe with the highest amount of stock
    * Shows all the details on the shoe with the most amount of stock.

In order to make a selection all one has to do is input the number referencing the choice and hit enter to follow the next set of prompts should there be any.
