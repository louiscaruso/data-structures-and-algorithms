# Data Structure Implementation: Array Shift
---

## insertShiftArray

*Authors: Louis Caruso and Robert Carter*
*Got some information from stack overflow @ https://stackoverflow.com/questions/48561673/adding-items-in-the-middle-of-a-list-in-python*

---

## Description

A Python implementation of an "`Array Shift`. Array shifts are utilized to manipulate data within an array to insert numbers, strings, or other forms of data into particular parts of the list.


---

## Functions

| Function | Summary | Big O Time | Big O Space | Example | 
| :----------- | :----------- | :-------------: | :-------------: | :----------- |
| insertShiftArray | Inserts a number into a particular spot in an array and returns a new array | O(1) | O(1) | insertShiftArray[10, 11, 12, 13], 7 => [13, 12, 7, 11, 10] |




---
### Approach

#### insertShiftArray()
1. Create variable for array of numbers
2. Create variable for number to insert
3. Iterate through array to find length
4. Slice array at strictly found middle position
5. Create new blank array
6. Push first half of old array into new array
7. Push number variable into array
8. Push second half of old array into new array
9. Return new array

### Efficiency
* Methods that have Big O efficiency O(1) for time
  * insertShiftArray(). Because we are adding one or more nubmers at a time in a single array, it gets longer to do at a set rate
  
* Methods that have Big O efficiency O(1) for space
  * insertShiftArray(). Because it is only a single array with numbers, each added takes up the same amount of space, thus adding space at a linear rate
  
  
## Visuals
![Whiteboard Image](../../assets/code_challenge_02_401whiteboard.png)



---

## Change Log
1.1 Finished Challenge 1 - 10 December 2020