# 557. Reverse Words in a String III

## https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

## Problem Description
Given a string `s`, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

### Examples:
**Example 1:**
```
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```

**Example 2:**
```
Input: s = "Mr Ding"
Output: "rM gniD"
```

### Constraints:
* `1 <= s.length <= 5 * 10^4`
* `s` contains printable ASCII characters.
* `s` does not contain any leading or trailing spaces.
* There is at least one word in `s`.
* All the words in `s` are separated by a single space.

## Solution Approach
This problem can be solved using the following steps:
1. Split the input string by spaces to get individual words
2. Reverse each word's characters 
3. Join the reversed words back together with spaces

## Time & Space Complexity
- **Time Complexity**: O(n) where n is the length of the string
- **Space Complexity**: O(n) for storing the split words and the result


## Test Cases
- `"Let's take LeetCode contest"` → `"s'teL ekat edoCteeL tsetnoc"`
- `"Mr Ding"` → `"rM gniD"`
- `"hello world"` → `"olleh dlrow"`