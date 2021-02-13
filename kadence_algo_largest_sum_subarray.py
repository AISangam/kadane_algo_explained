class KadenceAlgo:
    """
    Initial value of current best and overall best
    We are interested in getting the overall best
    """

    def __init__(self, arr):

        self.current_best = arr[0]
        self.overall_best = arr[0]
        self.n = len(arr)

    def kadence_cal(self):
        """
        Returns the largest sum of the subarray
        using kadence algorithm
        Time complexity is O(n). Process takes place using
        single for loop
        """
        for i in range(1, self.n):

            if self.current_best >= 0:

                self.current_best += arr[i]
            else:

                self.current_best = arr[i]

            if self.current_best > self.overall_best:
                self.overall_best = self.current_best

        return self.overall_best

    def largest_sum_contagious_arr(self):
        """
        Based on the largest sum calculated in the
        previous function this function returns that
        subarray which contains such result

        For finding the largest subarray two loops are
        needed hence the time complexity is O(n^2)

        Overall to find the laargest sum of the subarray
        time complexity is O(n) and to find the indexes
        of that subarray which contributes to that sum
        time complexity is O(n**2)

        Overall process is executed in O(n) + O(n**2)

        Applying the formula of droping the less significant term

        overall complexity of kadence algorithm and finding the
        subarray corresponding to largest sum is O(n**2)

        """
        for i in range(self.n):
            current_sum = arr[i]
            for j in range(i + 1, self.n + 1):

                if current_sum == self.overall_best:
                    indexes = [i, j - 1]

                if current_sum > self.overall_best or j == self.n:
                    break

                current_sum += arr[j]
                j += 1

        range_lower = indexes[0]
        range_higher = indexes[1]

        largest_sub_array = arr[
                            range_lower:(range_higher + 1)
                            ]
        return largest_sub_array


arr = [
    -2, -3, 4, -1, -2, 1, 5, -3
]
object_kadence = KadenceAlgo(arr)
best_value = object_kadence.kadence_cal()
largest_sub_array = object_kadence.largest_sum_contagious_arr()
print("Largest subarray is:", largest_sub_array)