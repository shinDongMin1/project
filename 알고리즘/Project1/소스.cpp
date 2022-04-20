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

	printf("���� A: ");
	for (int i = 0; i < 5; i++) {
		printf("%d��:%d�� ", Coin[i], Count[i]);
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

	printf("���� B: ");
	for (int i = 0; i < 7; i++) {
		printf("%d��:%d�� ", Coin[i], Count[i]);
	}
	printf("\n");
}
void main() {
	int change;

	printf("�Ž����� �׼��� �Է��Ͻÿ�:");
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
			printf("������: %d-%d\n", T[0][i], T[1][i]);
		else
			printf("����%d: %d-%d\n", i, T[0][i], T[1][i]);
	}

}
int main()
{
	int start;
	printf("�������� �Է��ϼ���: ");
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
/*const int MAX = 10000; //�ʿ��� �迭�� ���� MAX�� �����Ѵ�.
int Temp[MAX];

void Merge(int data[], int start, int mid, int start2, int end) {
	int Tindex = start;
	int k = start;


	while (start <= mid && start2 <= end) { //�ΰ��� �迭 ���� �� �ϳ��� ������ ������ �ߴ��ϰ�
		if (data[start] <= data[start2])     //���ϰ� ���� ���� ���� Temp�� �����Ѵ�.
			Temp[Tindex++] = data[start++];
		else
			Temp[Tindex++] = data[start2++];
	}

	if (start > mid) {                            //while���� �� ���� Temp�� �� �־����� �ٸ� �ʿ� ����
		for (int i = start2; i <= end; i++)       //������ Temp�� �����Ѵ�.
			Temp[Tindex++] = data[i];
	}
	else {
		for (int i = start; i <= mid; i++)
			Temp[Tindex++] = data[i];
	}

	for (int i = k; i <= end; i++)           //�ӽ÷� ���� ������ Temp���� data�� �־��ش�.
		data[i] = Temp[i];
}
void Mergesort(int data[], int start, int end) {
	int mid;
	if (start < end)                                    // �迭�� ������ ���� 2�� �̻��̸� �����Ѵ�
	{
		mid = (start + end) / 2;		                // mid=������ ������ ���� �߰� ������ �ε����̴�.
		Mergesort(data, start, mid);  	        // �պκ� ��� ȣ���Ѵ�.
		Mergesort(data, mid + 1, end);    	    // �޺κ� ��� ȣ���Ѵ�.
		Merge(data, start, mid, mid + 1, end);    // �պ� �Լ� ȣ���Ѵ�.
	}
}
void location(int data[], int low, int high, int a) {
	int mid;

	if (low > high) {
		cout << "ã�� ���� �����ϴ�." << endl; //ã�� ���ϸ� ����Ѵ�.
	}
	else {
		mid = (low + high) / 2;
		if (a == data[mid]) {
			cout << mid + 1 << "��°�� �ֽ��ϴ�." << endl;
		}
		else if (a < data[mid])
			location(data, low, mid - 1, a);

		else
			location(data, mid + 1, high, a);
	}
}

int main() {
	srand((unsigned)time(NULL));

	int* Array = new int[MAX];                  //�����Ҵ����� �������� 10000���� �޴� �迭��       //�պ��� ���� �ʿ��� ������ �迭 �� ���������Ѵ�.
	int a;

	for (int i = 0; i < MAX; i++) {              // 0~49999�� ���� �������� Array�� �־��ش�.
		Array[i] = (int)(((long)rand() << 15) | rand()) % 50000;
	}
	for (int i = 0; i < 10; i++)
		cout << Array[i] << " ";
	cout << "ã�� ���� �Է��Ͻÿ�.(0~49999)";   //ã�� ���� �Է¹޾� ����a�� �ִ´�.
	cin >> a;

	Mergesort(Array, 0, MAX-1);           //�պ������� �Լ� ȣ���Ѵ�,
	for (int i = 0; i < 10; i++)
		cout << Array[i] << " ";
	location(Array, 0, MAX-1, a);               //����Ž���� �Լ� ȣ���Ѵ�.


	delete[] Array;
}



/*int main() {
	srand((unsigned)time(NULL));

	int* Array = new int[MAX];  //�������� 10000���� �޴� �迭�� ��������
	int index = 0;
	int a;

	for (int i = 0; i < MAX; i++) {         // 0~49999�� ���� �������� Array�� �־��ش�.
		Array[i] = rand() % 50000;
	}

	cout << "ã�� ���� �Է��Ͻÿ�.(0~49999)"; //ã�� ���� �Է¹޾� ����a�� �ִ´�.
	cin >> a;

	for (int i = 0; i < MAX; i++)   //����Ž���� �ϴ� for��
	{
		if (Array[i] == a)
		{
			cout << i << "��°�� �ֽ��ϴ�." << endl;
			++index;
		}
		if (index == 1)               // 1���� ã���� �ߴ�
			break;

	}
	if (index == 0)                      //ã�� ���ϸ� ���
		cout << "ã�� ���� �����ϴ�." << endl;

	delete[] Array;
}
while (start <= mid && start2 <= end) {       //�ΰ��� �迭 ���� �� �ϳ��� ������ ������ �ߴ��ϰ�
	if (data[start] <= data[start2]) {          //���ǹ����� ���ϰ� ���� ���� ���� Temp�� �����Ѵ�.
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