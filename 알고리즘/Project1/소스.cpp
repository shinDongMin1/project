#include <stdio.h>

/*
void CoinchangeA(int change) {
	int Coin[] = { 500,100,50,10,1 };
	int Count[] = { 0,0,0,0,0,0,0 };

	while (change >= 500) {
		change = change - 500;
		Count[0]++;
	}
	while (change >= 100) {
		change = change - 100;
		Count[1]++;
	}
	while (change >= 50) {
		change = change - 50;
		Count[2]++;
	}
	while (change >= 10) {
		change = change - 10;
		Count[3]++;
	}
	while (change >= 1) {
		change = change - 1;
		Count[4]++;
	}

	printf("규정 A: ");
	for (int i = 0; i < 5; i++) {
		printf("%d원:%d개 ", Coin[i], Count[i]);
	}
	printf("\n");
}
void CoinchangeB(int change) {
	int Coin[] = { 500,130,100,50,10,5,1 };
	int Count[] = { 0,0,0,0,0,0,0 };

	while (change >= 500) {
		change = change - 500;
		Count[0]++;
	}
	while (change >= 130) {
		change = change - 130;
		Count[1]++;
	}
	while (change >= 100) {
		change = change - 100;
		Count[2]++;
	}
	while (change >= 50) {
		change = change - 50;
		Count[3]++;
	}
	while (change >= 10) {
		change = change - 10;
		Count[4]++;
	}
	while (change >= 5) {
		change = change - 5;
		Count[5]++;
	}
	while (change >= 1) {
		change = change - 1;
		Count[6]++;
	}

	printf("규정 B: ");
	for (int i = 0; i < 7; i++) {
		printf("%d원:%d개 ", Coin[i], Count[i]);
	}
	printf("\n");
}
void main() {
	int change;

	printf("거스름돈 액수를 입력하시오:");
	scanf_s("%d", &change);

	CoinchangeA(change);
	CoinchangeB(change);
	
	
}*/

#include <stdlib.h>
#include <time.h>
#define MAX 26
#define INF 1000L

int Matrix[MAX][MAX] = { 0 };
int dist[MAX];
int from[MAX];

void GraphMaker() {
	srand((unsigned)time(NULL));

	int Tindex = 0;
	int Weight = 0;

	int count1 = 0;
	int count2 = 0;

	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++)
			if (i != j)
				Matrix[j][i] = INF;
	}

	for (int i = 0; i < MAX; i++) {
		while (true) {
			if ((MAX - i - 1) > 4) {
				count1 = 0;
				count2 = 0;
				for (int j = 0; j < MAX; j++) {
					if (Matrix[i][j] != INF && Matrix[i][j] != 0)
						count1++;
				}

				if (count1 > 3)
					break;

				else {
					for (int j = 0; j < 4 - count1; j++) {
						Tindex = (rand() % (MAX - i - 1)) + i + 1;

						for (int k = 0; k < MAX; k++) {
							if (Matrix[k][Tindex] != INF && Matrix[k][Tindex] != 0)
								count2++;
						}

						if (count2 > 3)
							break;

						Weight = (rand() % 99) + 1;
						Matrix[i][Tindex] = Weight;
						Matrix[Tindex][i] = Weight;
					}
				}
			}

			else {
				count1 = 0;
				count2 = 0;
				for (int j = 0; j < MAX; j++) {
					if (Matrix[i][j] != INF && Matrix[i][j] != 0)
						count1++;
				}
				if (count1 > 3)
					break;
				else {
					for (int j = 0; j < MAX - i - 1 - count1; j++) {
						Tindex = (rand() % (MAX - i - 1)) + i + 1;

						for (int k = 0; k < MAX; k++) {
							if (Matrix[Tindex][k] != INF && Matrix[Tindex][k] != 0)
								count2++;
						}

						if (count2 > 3)
							break;

						Weight = (rand() % 99) + 1;
						Matrix[i][Tindex] = Weight;
						Matrix[Tindex][i] = Weight;
					}
				}
			}
			break;
		}
	}

	for (int i = 0; i < MAX; i++) {
		for (int j = 0; j < MAX; j++) {
			if (Matrix[i][j] == INF)
				printf("INF ");
			else
				printf("%3d ", Matrix[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}
int OutMin() {
	int min = INF;
	int best = INF;

	for (int i = 0; i < MAX; i++) {
		if (dist[i] != 0 && dist[i] < min) {
			min = dist[i];
			best = i;
		}
	}

	return best;
}
void PrimMST(int start){

	int T[2][MAX] = { 0 };

	T[0][0] = start;
	T[1][0] = start;

	for (int i = 0; i < MAX; i++) {
		dist[i] = Matrix[start - 1][i];
		from[i] = start;
	}

	for (int i = 0; i < MAX - 1; i++) {
		int best = OutMin();
		if (best == INF)return;

		T[0][i + 1] = from[best];
		T[1][i + 1] = best + 1;
		dist[best] = 0;

		for (int j = 0; j < MAX; j++) {
			if (Matrix[best][j] != 0 && Matrix[best][j] < dist[j]) {
				dist[j] = Matrix[best][j];
				from[j] = best + 1;
			}
		}
	}

	for (int i = 0; i < MAX; i++) {
		if (i == 0)
			printf("시작점: %d-%d\n", T[0][i], T[1][i]);
		else
			printf("간선%d: %d-%d\n", i, T[0][i], T[1][i]);
	}

}
int main()
{
	int start;
	printf("시작점을 입력하세요: ");
	scanf_s("%d", &start);

	GraphMaker();
	PrimMST(start);

	return 0;
}

/*void MakeGraph(int Apex)
{
	srand((unsigned)time(NULL));
	int line;
	int Weight;

	for (int i = 0; i < Apex; i++) {
		int Tindex = 0;
		int Temp[4] = {0,0,0,0 };
		while (true) {
			line = rand() % Apex+1;

			if (i == line)
				continue;
			else if (Temp[0] == line)
				continue;
			else if (Temp[1] == line)
				continue;
			else if (Temp[2] == line)
				continue;
			else if (Temp[3] == line)
				continue;
			else
				Temp[Tindex++] = line;

			if (Tindex == 4)
				break;

		}

		for (int j = 0; j < 4; j++) {
			Weight = rand() % 9 + 1;
			Matrix[i][Temp[j]] = Weight;
			Matrix[Temp[j]][i] = Weight;
		}
	}

	cout << endl;

	for (int i = 1; i <= Apex; i++) {
		for (int j = 1; j <= Apex; j++) {
			cout << Matrix[i][j] << ' ';
		}
		cout << endl;
	}
}*/
/*const int MAX = 10000; //필요한 배열의 수를 MAX로 정의한다.
int Temp[MAX];

void Merge(int data[], int start, int mid, int start2, int end) {
	int Tindex = start;
	int k = start;


	while (start <= mid && start2 <= end) { //두개의 배열 영역 중 하나라도 영역을 넘으면 중단하고
		if (data[start] <= data[start2])     //비교하고 값이 작은 쪽을 Temp에 저장한다.
			Temp[Tindex++] = data[start++];
		else
			Temp[Tindex++] = data[start2++];
	}

	if (start > mid) {                            //while에서 한 쪽이 Temp에 다 넣어지면 다른 쪽에 남은
		for (int i = start2; i <= end; i++)       //값들을 Temp에 저장한다.
			Temp[Tindex++] = data[i];
	}
	else {
		for (int i = start; i <= mid; i++)
			Temp[Tindex++] = data[i];
	}

	for (int i = k; i <= end; i++)           //임시로 값을 저장한 Temp에서 data로 넣어준다.
		data[i] = Temp[i];
}
void Mergesort(int data[], int start, int end) {
	int mid;
	if (start < end)                                    // 배열의 원소의 수가 2개 이상이면 실행한다
	{
		mid = (start + end) / 2;		                // mid=반으로 나누기 위한 중간 원소의 인덱스이다.
		Mergesort(data, start, mid);  	        // 앞부분 재귀 호출한다.
		Mergesort(data, mid + 1, end);    	    // 뒷부분 재귀 호출한다.
		Merge(data, start, mid, mid + 1, end);    // 합병 함수 호출한다.
	}
}
void location(int data[], int low, int high, int a) {
	int mid;

	if (low > high) {
		cout << "찾는 값이 없습니다." << endl; //찾지 못하면 출력한다.
	}
	else {
		mid = (low + high) / 2;
		if (a == data[mid]) {
			cout << mid + 1 << "번째에 있습니다." << endl;
		}
		else if (a < data[mid])
			location(data, low, mid - 1, a);

		else
			location(data, mid + 1, high, a);
	}
}

int main() {
	srand((unsigned)time(NULL));

	int* Array = new int[MAX];                  //동적할당으로 랜덤값을 10000개를 받는 배열과       //합병할 때에 필요한 공간을 배열 및 변수선언한다.
	int a;

	for (int i = 0; i < MAX; i++) {              // 0~49999의 값을 랜덤으로 Array에 넣어준다.
		Array[i] = (int)(((long)rand() << 15) | rand()) % 50000;
	}
	for (int i = 0; i < 10; i++)
		cout << Array[i] << " ";
	cout << "찾을 값을 입력하시오.(0~49999)";   //찾는 값을 입력받아 변수a에 넣는다.
	cin >> a;

	Mergesort(Array, 0, MAX-1);           //합병정렬의 함수 호출한다,
	for (int i = 0; i < 10; i++)
		cout << Array[i] << " ";
	location(Array, 0, MAX-1, a);               //이진탐색의 함수 호출한다.


	delete[] Array;
}



/*int main() {
	srand((unsigned)time(NULL));

	int* Array = new int[MAX];  //랜덤값을 10000개를 받는 배열과 변수선언
	int index = 0;
	int a;

	for (int i = 0; i < MAX; i++) {         // 0~49999의 값을 랜덤으로 Array에 넣어준다.
		Array[i] = rand() % 50000;
	}

	cout << "찾을 값을 입력하시오.(0~49999)"; //찾는 값을 입력받아 변수a에 넣는다.
	cin >> a;

	for (int i = 0; i < MAX; i++)   //선행탐색을 하는 for문
	{
		if (Array[i] == a)
		{
			cout << i << "번째에 있습니다." << endl;
			++index;
		}
		if (index == 1)               // 1개라도 찾으면 중단
			break;

	}
	if (index == 0)                      //찾지 못하면 출력
		cout << "찾는 값이 없습니다." << endl;

	delete[] Array;
}
while (start <= mid && start2 <= end) {       //두개의 배열 영역 중 하나라도 영역을 넘으면 중단하고
	if (data[start] <= data[start2]) {          //조건문으로 비교하고 값이 작은 쪽을 Temp에 저장한다.
		Temp[Tindex++] = data[start++];
	}
	else {
		Temp[Tindex++] = data[start2++];
	}

	for (int i = start; i < mid; i++) {
		for (int j = start2; j < end; j++) {
			if (data[i] < data[j]) {
				Temp[Tindex++] = data[i];
				start++;
			}
			else {
				Temp[Tindex++] = data[j];
				start2++;
			}
		}
	}
}*/