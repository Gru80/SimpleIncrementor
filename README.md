# SimpleIncrementor
Simple Incrementor Plugin for Sublime Text 3

# Quick Start
1. Select a text part
2. Execute Simple Incrementor by one of the following options
  * Command - commands start with "Simple Incrementor:"
  * Context Menu - select one option of the "Simple Incrementor" sub-menu
  * Shortcut Key - <Ctrl+i> <Ctrl+i> will execute the default increment command
3. All occurances of the selected text will be replaced with chosen incrementation

# Expert Mode
In expert mode, several options can be combined by use of key:value pairs.
* Keys and values are separated by a : character
* Key:value pairs are separated by a blank character

## Implemented keys
* digits - fill up the value with leading 0s to the specified number of digits
* offset - start with an offset instead of 0
* prectext - preceding text to be used before the increment-value
* step - use other step-count instead of 1

## Example
`Simple Incrementor - Expert Mode: ` `digits:4 prectext:TEST_ offset:10`

This will replace all occurances of the selected text part starting with `TEST_0010`
