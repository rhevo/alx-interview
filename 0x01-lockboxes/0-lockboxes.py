def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    keys = boxes[0]  # Keys from the first box

    while keys:
        key = keys.pop()  # Take a key from our list
        
        # If the key opens a new box that hasn't been unlocked yet
        if key < n and key not in unlocked:
            unlocked.add(key)  # Mark this box as unlocked
            keys.extend(boxes[key])  # Add new keys from this newly unlocked box
    
    # Check if the number of unlocked boxes equals the total number of boxes
    return len(unlocked) == n
