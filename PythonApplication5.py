nums = [1,1,1,1,2.2,5,6,9,1,1]
major = nums [1]
count = 0
for each in nums:
    if count == 0 :
        major = each
    if major == each:
        count =+1
    else:
        count =-1
if nums.count(major)>=len(nums)/2:
    print(major,"vactor")
else :
    print("no have")