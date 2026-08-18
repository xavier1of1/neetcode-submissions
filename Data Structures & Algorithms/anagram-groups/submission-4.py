class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Maps each character-count signature to its anagram group.
        groups = {}

        for string in strs:
            # Each position represents the frequency of one letter:
            # index 0 = 'a', index 1 = 'b', ..., index 25 = 'z'
            counts = [0] * 26

            for char in string:
                # Convert the character to an index from 0 to 25.
                # For example:
                # ord('a') - ord('a') = 0
                # ord('c') - ord('a') = 2
                index = ord(char) - ord('a')
                counts[index] += 1

            # Lists cannot be dictionary keys because they are mutable.
            # Convert the counts list into an immutable tuple.
            signature = tuple(counts)

            # Create a new group when this signature is first encountered.
            if signature not in groups:
                groups[signature] = []

            # Store the original string in its corresponding group.
            groups[signature].append(string)

        # We only need the grouped strings, not their signatures.
        return list(groups.values())