'''
Duplication Detection:

Detect whether a given sequence contains only unique elements

PSEUDO
```

```
FUNCTION duplication_detection(array):
    
    seen_values = empty set 

    FOR each value IN array:
        IF value IN seen_values:
            RETURN FALSE
        ELSE:
            ADD value TO seen_values
    
    RETURN TRUE
'''

# Alis response

'''
Hi everyone,
For this task, I decided to use a nested loop to check whether all the elements in a sequence are unique. The algorithm checks each element against the elements that follow it. If the same value appears again, it returns False. If it reaches the end without finding any duplicate value, it returns True.
Pseudocode:
FUNCTION allUnique(sequence)
FOR i = 0 TO length(sequence) - 2
 FOR j = i + 1 TO length(sequence) - 1
  IF sequence[i] = sequence[j]
   RETURN False
RETURN True
The best-case scenario is when the first comparison finds a duplicate, for example [4, 4, 7, 9]. The algorithm returns False straight away, so the running time is O(1).
The worst-case scenario is when all the elements are unique, or when the duplicate is only found at the end of the sequence. In this case, the algorithm must compare almost every pair of elements before it returns a result, so the worst-case complexity is O(n²).
Thank you, and I look forward to reading everyone else's approaches.
'''

array = [4 ,4.0,7,9]

def all_unique(sequence):
    for i in range(0, len(sequence) - 1):
        for j in range(i + 1, len(sequence)):
            if sequence[i] == sequence[j]:
                return False
    return True
    

if __name__ == "__main__":
    all_unique(array)