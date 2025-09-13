# Prefix Sum 专题

前缀和 (Prefix Sum) 是数组类题目的高频技巧。
核心思想：用一个辅助数组 / 哈希表存储「前缀信息」，
将区间和、子数组统计问题的时间复杂度从 O(n²) 降到 O(n) 或 O(1)。

---

## 📂 目录结构

- **01-basic-range-sum**
  - 303. Range Sum Query - Immutable
  - 304. Range Sum Query 2D - Immutable

- **02-subarray-sum-hashmap**
  - 560. Subarray Sum Equals K
  - 325. Maximum Size Subarray Sum Equals k
  - 930. Binary Subarrays With Sum

- **03-subarray-sum-mod**
  - 523. Continuous Subarray Sum
  - 974. Subarray Sums Divisible by K
  - 1590. Make Sum Divisible by P

- **04-prefix-sum-variants**
  - 1248. Count Number of Nice Subarrays
  - 238. Product of Array Except Self
  - 152. Maximum Product Subarray

---

## 📝 学习顺序

1. **入门**：303 → 304 （理解前缀和定义）
2. **子数组统计**：560 → 325 → 930 （前缀和 + 哈希表）
3. **取模技巧**：523 → 974 → 1590 （前缀和 + 取模）
4. **扩展变体**：1248 / 238 / 152 （把前缀和思想迁移到奇偶 / 乘积）

---

## 🎯 总结

- **303/304** → 基础前缀和
- **560/325/930** → 前缀和 + 哈希表（统计子数组）
- **523/974/1590** → 前缀和 + 取模（整除问题）
- **1248/238/152** → 前缀和思想迁移（计数、积、奇偶）

前缀和是数组题的必备基础，后续还能扩展到二维、动态规划和哈希表结合的复杂题目。
