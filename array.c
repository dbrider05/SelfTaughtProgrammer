#include <stdio.h>

int main()
{
	int mid, n, ele;
	printf("Enter the size of the array:");
    scanf("%d", &n);
    int arr[100];
	for (int i = 0; i < n; i++)
		scanf("%d",&arr[i]);
    for(int i=0; i<n; i++)
        printf("%d ",arr[i]);
    printf("Enter the element to be inserted:");
    scanf("%d",&ele);
    mid = n/2;
	n++;
	for (int i = n-1; i >= mid; i--)
		arr[i] = arr[i - 1];
	arr[mid] = ele;
	for (int i = 0; i < n; i++)
		printf("%d ", arr[i]);
	printf("\n");

	return 0;
}
