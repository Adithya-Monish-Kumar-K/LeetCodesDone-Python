class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        if k == 1:
            return nums[0]
        if k == 2:
            return nums[0] + min(nums[1:])
        need = k - 2
        small: List[tuple[int, int]] = []
        large: List[tuple[int, int]] = []
        in_small = [False] * n
        removed = [False] * n
        small_size = 0
        small_sum = 0
        def prune(heap: List[tuple[int, int]]) -> None:
            while heap and removed[heap[0][1]]:
                heapq.heappop(heap)
        def balance() -> None:
            nonlocal small_size, small_sum
            prune(small)
            prune(large)
            while small_size < need and large:
                val, idx = heapq.heappop(large)
                heapq.heappush(small, (-val, idx))
                in_small[idx] = True
                small_size += 1
                small_sum += val
            while small_size > need:
                prune(small)
                if not small:
                    break
                neg_val, idx = heapq.heappop(small)
                val = -neg_val
                heapq.heappush(large, (val, idx))
                in_small[idx] = False
                small_size -= 1
                small_sum -= val
            prune(small)
            prune(large)
            while small and large and -small[0][0] > large[0][0]:
                neg_val, idx_s = heapq.heappop(small)
                val_s = -neg_val
                val_l, idx_l = heapq.heappop(large)
                heapq.heappush(small, (-val_l, idx_l))
                heapq.heappush(large, (val_s, idx_s))
                in_small[idx_s] = False
                in_small[idx_l] = True
                small_sum += val_l - val_s
        def add(idx: int) -> None:
            nonlocal small_size, small_sum
            heapq.heappush(large, (nums[idx], idx))
            balance()
        def remove(idx: int) -> None:
            nonlocal small_size, small_sum
            removed[idx] = True
            if in_small[idx]:
                in_small[idx] = False
                small_size -= 1
                small_sum -= nums[idx]

        for pos in range(2, min(n, dist + 2)):
            add(pos)
        balance()
        best = float("inf")
        for i in range(1, n - k + 2):
            balance()
            if small_size == need:
                best = min(best, nums[i] + small_sum)
            out_idx = i + 1
            if out_idx < n:
                remove(out_idx)
            new_idx = i + dist + 1
            if new_idx < n:
                add(new_idx)
        return -1 if best == float("inf") else nums[0] + best