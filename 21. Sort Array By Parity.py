class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        list1 = []
        list2 = []
        for i in A:
            if(i%2 == 0):
                list1.append(i)
            else:
                list2.append(i)
        return list1+list2
