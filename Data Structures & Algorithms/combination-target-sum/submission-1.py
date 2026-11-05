class Solution:
    def combinationExist(self, C :  List[List[int]], comb :  List[int]):
        for C_comb in C:
            if sorted(C_comb) == sorted(comb):
                return True
        return False

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
            Backtracking problem

            strategy 1 
             - write a func to see if a given target is multiple of a number, return list if it is
             - run main func to see if first number is multiple of THE target using func
                    - if yes, we got our first combination
                    - if no, we move on
             - keep track of combinations. As soon as we have a combination, 
            we make all possible comb. out of this comb and give sum of each comb. as target
            for each number in the list. each time we hit a yes, we add a comb to our combinations
            with appropriate data. we iterate this until we're exhausted of combinations
            - we continue with second number until we're exhausted


            [2,5,6,9] - target 9 
            check if 9 is multiple of 2. no 
            check if 9 is multiple of 5. no 
            check if 9 is multiple of 6. no 
            check if 9 is mulitle of 9. yes
        
            strategy 2
            - write a recursive func, that finds combination of given sum 
            - pass in TARGET, list. 
            - Create a combo list C= [].
            - loop thru elements in the list.
                - sublist = SL  
                - if TARGET is smaller than N, skip to next number
                - else 
                    - see if completely divisible. 
                    - save divisor, remainder as D, R
                    - if R == 0
                        - make a combination, save in C. 
                    - else
                        - D_new = D
                        - run a loop until D_new > 0
                            - R_new = TARGET % N*D_new 
                            - pass R_new and sublist to same func. 
                            - if output []
                                - pass. 
                            - else
                                - concatenate (N, N .. D_new times) with each list in list
                                - save each new list in C. 
                            - Decrement D_new.
            - return C    
        """
        C = []
        for i in range(0, len(nums)): 
            current = nums[i]
            sublist = nums[i:]
            print(sublist)
            if target < current: 
                continue
            else:
                div, rem = target // current, target % current
                if rem == 0: 
                    possible_comb = [current]*div
                    if not self.combinationExist(C, possible_comb):
                        C.append(possible_comb)

                div_temp = div
                while div_temp > 0:
                    balance = target - (current*div_temp)
                    temp_combs = self.combinationSum(sublist, balance)
                    if len(temp_combs) > 0:
                        for comb in temp_combs:
                            possible_comb = [current]*div_temp + comb
                            if not self.combinationExist(C, possible_comb): 
                                C.append(possible_comb) 
                    div_temp -= 1

        return C
