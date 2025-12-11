#trace the prefix value for each dry run step in LC:525

def trace(nums):
    mapping = {0: -1, 1: 1}
    prefix = 0
    first_seen = {0: -1}
    best = 0

    print(f"{'i':>3} {'num':>5} {'mapped':>7} {'prefix':>7} {'first_seen(before)':>22} {'best(before)':>12} {'action/first_seen(after)':>30}")
    for i, num in enumerate(nums):
        mapped = mapping[num]
        prefix += mapped
        fs_before = dict(first_seen)  # snapshot

        action = "no"
        if prefix in first_seen:
            best = max(best, i - first_seen[prefix])
            action = f"update best={best}"
        else:
            first_seen[prefix] = i
            action = f"first_seen[{prefix}]={i}"

        print(f"{i:3} {num:5} {mapped:7} {prefix:7} {str(fs_before):22} {str(best):12} {action:30}")

    print("\nfinal best:", best)
    print("final first_seen:", first_seen)

if __name__ == "__main__":
    # example 1: the one you used
    trace([0,1,0,1,1,0])
    # try another case to test yourself:
    print("\n---\n")
    trace([1,0,1,1,0,0])