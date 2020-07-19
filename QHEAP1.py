# Enter your code here. Read input from STDIN. Print output to STDOUT
def add_element(heap,ele):
    n = len(heap)
    if not n:
        return [ele]

    heap.append(ele)
    i=n
    n+=1
    while i>0 and heap[i]<=heap[(i-1)//2]:
        heap[i],heap[(i-1)//2] = heap[(i-1)//2],heap[i]
        i = (i-1)//2
    
    return heap

def min_heapify(arr,n,i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2

    if l<n and arr[l]<arr[smallest]:
        smallest = l

    if r<n and arr[r]<arr[smallest]:
        smallest = r

    if smallest!=i:
        arr[i],arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr,n,smallest)

def remove_element(heap,ele):
    idx = heap.index(ele)
    n = len(heap)
    heap[idx],heap[n-1] = heap[n-1],heap[idx]
    heap = heap[:-1]
    min_heapify(heap,n-1,idx)
    return heap


if __name__=="__main__":
    q = int(input())
    heap = []
    # print('aeifh')
    for i in range(q):
        # print(heap)
        inp = input().split()
        if len(inp)==1:
            print(heap[0])

        else:
            if inp[0]=='1':
                heap = add_element(heap,int(inp[1]))
            else:
                heap = remove_element(heap,int(inp[1]))
