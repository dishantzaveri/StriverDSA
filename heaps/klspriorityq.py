"""
COMPLEX HEAP PROBLEMS — Priority Queue Masterclass
====================================================
Problems covered:
  1. Sliding Window Median           (two-heap technique)
  2. K-Way Merge of Sorted Arrays    (min-heap with index tracking)
  3. IPO – Maximize Capital          (greedy + two heaps)
  4. Task Scheduler with Cooldown    (max-heap + simulation)
  5. Find Median from Data Stream    (classic two-heap design)
  6. Reorganize String               (max-heap greedy)
"""

import heapq
from collections import Counter, defaultdict
from typing import List, Optional
import math


# ─────────────────────────────────────────────────────────────────────────────
# 1. SLIDING WINDOW MEDIAN
#    Given array nums and window size k, return median of every window.
#    TC: O(n * k)  SC: O(k)
# ─────────────────────────────────────────────────────────────────────────────

class SlidingWindowMedian:
    """
    Uses two heaps:
      • max_heap (left half)  — stores negatives to simulate max-heap
      • min_heap (right half) — normal min-heap
    Invariant: len(max_heap) == len(min_heap)  OR  len(max_heap) == len(min_heap) + 1
    Lazy deletion via a 'to_remove' counter to avoid O(k) removal.
    """

    def __init__(self):
        self.max_heap: List[int] = []   # left  (negated)
        self.min_heap: List[int] = []   # right
        self.to_remove: dict = defaultdict(int)
        self.max_size = 0               # effective size of max_heap
        self.min_size = 0               # effective size of min_heap

    def _balance(self):
        # max_heap should have equal or one more element than min_heap
        while self.max_size > self.min_size + 1:
            val = -heapq.heappop(self.max_heap)
            self.max_size -= 1
            heapq.heappush(self.min_heap, val)
            self.min_size += 1
            self._prune(self.max_heap, is_max=True)

        while self.min_size > self.max_size:
            val = heapq.heappop(self.min_heap)
            self.min_size -= 1
            heapq.heappush(self.max_heap, -val)
            self.max_size += 1
            self._prune(self.min_heap, is_max=False)

    def _prune(self, heap, is_max: bool):
        """Lazily remove stale top elements."""
        while heap:
            top = -heap[0] if is_max else heap[0]
            if self.to_remove[top] > 0:
                self.to_remove[top] -= 1
                heapq.heappop(heap)
            else:
                break

    def add(self, num: int):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
            self.max_size += 1
        else:
            heapq.heappush(self.min_heap, num)
            self.min_size += 1
        self._balance()

    def remove(self, num: int):
        self.to_remove[num] += 1
        if self.max_heap and num <= -self.max_heap[0]:
            self.max_size -= 1
            self._prune(self.max_heap, is_max=True)
        else:
            self.min_size -= 1
            self._prune(self.min_heap, is_max=False)
        self._balance()

    def get_median(self, k: int) -> float:
        if k % 2 == 1:
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0

    @staticmethod
    def median_sliding_window(nums: List[int], k: int) -> List[float]:
        swm = SlidingWindowMedian()
        result = []
        for i, num in enumerate(nums):
            swm.add(num)
            if i >= k:
                swm.remove(nums[i - k])
            if i >= k - 1:
                result.append(swm.get_median(k))
        return result


# ─────────────────────────────────────────────────────────────────────────────
# 2. K-WAY MERGE OF SORTED ARRAYS
#    Merge k sorted arrays into one sorted list.
#    TC: O(N log k)  where N = total elements   SC: O(k)
# ─────────────────────────────────────────────────────────────────────────────

def k_way_merge(arrays: List[List[int]]) -> List[int]:
    """
    Push (value, array_index, element_index) into a min-heap.
    Each pop extracts the global minimum; push the next element from the same array.
    """
    min_heap = []
    for arr_idx, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], arr_idx, 0))

    result = []
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        next_idx = elem_idx + 1
        if next_idx < len(arrays[arr_idx]):
            heapq.heappush(min_heap, (arrays[arr_idx][next_idx], arr_idx, next_idx))

    return result


# ─────────────────────────────────────────────────────────────────────────────
# 3. IPO — MAXIMIZE CAPITAL  (LeetCode 502)
#    You have 'w' initial capital.
#    Each project has a 'profit' and 'capital' (minimum capital required).
#    Pick at most k projects to maximize final capital.
#    TC: O(n log n + k log n)  SC: O(n)
# ─────────────────────────────────────────────────────────────────────────────

def find_maximized_capital(k: int, w: int,
                           profits: List[int],
                           capital: List[int]) -> int:
    """
    Strategy:
      • Sort projects by capital requirement (min-heap by capital).
      • At each step, unlock all affordable projects and push profits
        into a max-heap (negate for Python).
      • Always pick the project with the highest profit from the max-heap.
    """
    n = len(profits)
    projects = sorted(zip(capital, profits))     # sort by capital
    available: List[int] = []                    # max-heap (negated profits)
    ptr = 0

    for _ in range(k):
        # Unlock all projects we can now afford
        while ptr < n and projects[ptr][0] <= w:
            heapq.heappush(available, -projects[ptr][1])
            ptr += 1

        if not available:
            break  # cannot proceed further

        w += -heapq.heappop(available)

    return w


# ─────────────────────────────────────────────────────────────────────────────
# 4. TASK SCHEDULER WITH COOLDOWN  (LeetCode 621)
#    Given tasks and cooldown n, find minimum intervals needed.
#    TC: O(m log 26) ≈ O(m)   SC: O(26) = O(1)
# ─────────────────────────────────────────────────────────────────────────────

def least_interval(tasks: List[str], n: int) -> int:
    """
    Use a max-heap of frequencies + a queue to simulate cooldown.
    Each round:
      1. Pop the task with the highest frequency and execute it.
      2. Decrement frequency; push to cooldown queue (time_available, freq-1).
      3. When a task's cooldown expires, push it back to the heap.
    """
    freq = Counter(tasks)
    max_heap = [-f for f in freq.values()]
    heapq.heapify(max_heap)

    time = 0
    cooldown_queue: List[tuple] = []   # (time_when_available, neg_freq)

    while max_heap or cooldown_queue:
        time += 1

        if max_heap:
            neg_freq = heapq.heappop(max_heap)
            remaining = neg_freq + 1       # reduce frequency by 1
            if remaining < 0:              # still has tasks left
                cooldown_queue.append((time + n, remaining))
        else:
            # CPU is idle; jump time forward
            time = cooldown_queue[0][0]

        # Re-enable tasks whose cooldown has expired
        while cooldown_queue and cooldown_queue[0][0] <= time:
            _, rem = heapq.heappop(cooldown_queue)
            heapq.heappush(max_heap, rem)

    return time


# ─────────────────────────────────────────────────────────────────────────────
# 5. FIND MEDIAN FROM DATA STREAM  (LeetCode 295)
#    Support two operations: addNum(int), findMedian() → float
#    TC: O(log n) per add,  O(1) per median query    SC: O(n)
# ─────────────────────────────────────────────────────────────────────────────

class MedianFinder:
    """
    Two heaps:
      • small → max-heap (left  half, store negated)
      • large → min-heap (right half)
    Invariant: |small| - |large| ∈ {0, 1}
    """

    def __init__(self):
        self.small: List[int] = []   # max-heap (negated)
        self.large: List[int] = []   # min-heap

    def addNum(self, num: int) -> None:
        # Push to small first, then rebalance
        heapq.heappush(self.small, -num)

        # Ensure all of small ≤ all of large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


# ─────────────────────────────────────────────────────────────────────────────
# 6. REORGANIZE STRING  (LeetCode 767)
#    Rearrange string so no two adjacent chars are the same.
#    Return "" if impossible.
#    TC: O(n log 26) ≈ O(n)   SC: O(26) = O(1)
# ─────────────────────────────────────────────────────────────────────────────

def reorganize_string(s: str) -> str:
    """
    Greedy: always place the most frequent remaining character.
    Use a max-heap to track (frequency, char).
    After placing a char, hold it out for one step (cooldown of 1).
    """
    freq = Counter(s)
    max_heap = [(-cnt, ch) for ch, cnt in freq.items()]
    heapq.heapify(max_heap)

    result = []
    prev_cnt, prev_ch = 0, ""

    while max_heap:
        cnt, ch = heapq.heappop(max_heap)

        result.append(ch)

        # Re-insert the previously held character
        if prev_cnt < 0:
            heapq.heappush(max_heap, (prev_cnt, prev_ch))

        prev_cnt, prev_ch = cnt + 1, ch   # decrement frequency (cnt is negative)

    if prev_cnt < 0:
        return ""   # leftover character couldn't be placed

    return "".join(result)


# ─────────────────────────────────────────────────────────────────────────────
#  DRIVER — run all problems with test cases
# ─────────────────────────────────────────────────────────────────────────────

def separator(title: str):
    print(f"\n{'═' * 60}")
    print(f"  {title}")
    print('═' * 60)


if __name__ == "__main__":

    # ── 1. Sliding Window Median ──────────────────────────────────
    separator("1. Sliding Window Median")
    cases_swm = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3),
        ([1, 2, 3, 4, 2, 3, 1, 4, 2], 5),
        ([2147483647, 2147483647], 2),
    ]
    for nums, k in cases_swm:
        res = SlidingWindowMedian.median_sliding_window(nums, k)
        print(f"  nums={nums}, k={k}")
        print(f"  medians → {res}\n")

    # ── 2. K-Way Merge ────────────────────────────────────────────
    separator("2. K-Way Merge of Sorted Arrays")
    arrays_set = [
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]],
        [[10, 20], [5, 15, 25], [1, 12]],
        [[100], [], [50, 75], [10, 20, 30]],
    ]
    for arrays in arrays_set:
        merged = k_way_merge(arrays)
        print(f"  Input : {arrays}")
        print(f"  Merged: {merged}\n")

    # ── 3. IPO — Maximize Capital ─────────────────────────────────
    separator("3. IPO — Maximize Capital")
    ipo_cases = [
        (2, 0, [1, 2, 3], [0, 1, 1]),
        (3, 0, [1, 2, 3], [0, 1, 2]),
        (1, 2, [1, 2, 3], [1, 1, 2]),
    ]
    for k, w, profits, capital in ipo_cases:
        final = find_maximized_capital(k, w, profits, capital)
        print(f"  k={k}, w={w}, profits={profits}, capital={capital}")
        print(f"  Max capital → {final}\n")

    # ── 4. Task Scheduler ─────────────────────────────────────────
    separator("4. Task Scheduler with Cooldown")
    ts_cases = [
        (["A","A","A","B","B","B"], 2),
        (["A","A","A","B","B","B"], 0),
        (["A","A","A","A","A","A","B","C","D","E","F","G"], 2),
    ]
    for tasks, n in ts_cases:
        intervals = least_interval(tasks, n)
        print(f"  tasks={tasks}, n={n}")
        print(f"  Min intervals → {intervals}\n")

    # ── 5. Median from Data Stream ────────────────────────────────
    separator("5. Median from Data Stream")
    mf = MedianFinder()
    stream = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    for num in stream:
        mf.addNum(num)
        print(f"  Added {num:3d}  →  median = {mf.findMedian()}")

    # ── 6. Reorganize String ──────────────────────────────────────
    separator("6. Reorganize String")
    strings = ["aab", "aaab", "aaabbbccc", "vvvlo", "zzz"]
    for s in strings:
        res = reorganize_string(s)
        valid = all(res[i] != res[i+1] for i in range(len(res)-1)) if res else True
        status = "VALID  ✓" if (res and valid) else ("IMPOSSIBLE" if not res else "INVALID ✗")
        print(f"  Input: {s!r:15s}  Output: {res!r:20s}  [{status}]")
