def tim_cuc_tri(file):
    with open(file, 'r') as f:
        nums = list(map(int, f.read().split()))

    cuc_tri = []
    for i in range(1, len(nums) - 1):
        if (nums[i] > nums[i-1] and nums[i] > nums[i+1]) or \
           (nums[i] < nums[i-1] and nums[i] < nums[i+1]):
            cuc_tri.append(nums[i])

    with open('f_out.dat', 'w') as f:
        f.write(f"{len(cuc_tri)}\n")
        f.write(' '.join(map(str, cuc_tri)))
file = input('Nhập đường dẫn đến file= ')

tim_cuc_tri(file)