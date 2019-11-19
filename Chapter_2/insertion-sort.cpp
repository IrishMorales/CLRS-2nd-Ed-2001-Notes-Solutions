#include <iostream>

void printArray(int array_size, int array[]) {
	for (int i = 0; i < array_size; ++i) {
		std::cout << array[i] << " ";
	}
	std::cout << "\n";
}

void insertionSort(int array_size, int array[]) {
	
	//j - index of the element to be inserted
	for (int j = 1; j < array_size; ++j) {
		
		int current_element = array[j];
		
		//i - index of the element to be compared to array[j]
		int i = j - 1;
		
		//compare element[i] to element[j], going down the array
		while (array[i] > current_element && i >= 0) {
			//shift the element to the right
			array[i+1] = array[i];
			--i;
		}
		
		array[i+1] = current_element;
	}
}


//driver function
int main() {
	int array_size = 7;
	int array[array_size] = {3, -6, 2, 7, 1, 99, -5};
	
	insertionSort(array_size, array);

	std::cout << "SORTED ARRAY: ";
	printArray(array_size, array);
}
