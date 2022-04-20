#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
/*void graph(){
	srand((unsigned)time(NULL));

	int width_index = 0;
	int width_index_tmp[4] = { 0 };
	int Weight = 0;
	int count1 = 0;
	int count2 = 0;
	for (int i = 0; i < Max; i++) {
		while (true) {
			if ((Max - i - 1) > 4) {
				count1 = 0;
				count2 = 0;
				for (int j = 0; j < Max; j++) {
					if (xy[j][i] != 0)
						count1++;
				}

				if (count1 > 3)
					break;

				else {
					for (int k = 0; k < 4 - count1; k++) {
						width_index = (rand() % (Max - i - 1)) + i + 1;

						for (int l = 0; l < Max; l++) {
							if (xy[width_index][l] != 0)
								count2++;
						}

						if (count2 > 3)
							break;

						Weight = (rand() % 9) + 1;
						width_index_tmp[k] = width_index;
						xy[i][width_index_tmp[k]] = Weight;
						xy[width_index_tmp[k]][i] = Weight;
					}
				}
			}
			break;
		}

		while (true) {
			if (Max - i - 1 <= 4 && Max - i - 1 > 0) {
				count1 = 0;
				count2 = 0;
				for (int j = 0; j < Max; j++) {
					if (xy[i][j] != 0 || xy[j][i] != 0)
						count1++;
				}
				if (count1 > Max - i - 1)
					break;
				else {
					for (int k = 0; k < Max - i - 1 - count1; k++) {
						width_index = (rand() % (Max - i - 1)) + i + 1;

						for (int l = 0; l < Max; l++) {
							if (xy[width_index][l] != 0)
								count2++;
						}

						if (count2 > 3)
							break;
						for (int l = 0; l < Max; l++) {
							if (xy[width_index][l] != 0)
								count1++;
						}

						if (count1 > Max - i - 1)
							break;
						Weight = (rand() % 9) + 1;
						width_index_tmp[k] = width_index;
						xy[i][width_index_tmp[k]] = Weight;
						xy[width_index_tmp[k]][i] = Weight;
					}
				}
			}
			break;
		}
	}
	for (int ab = 0; ab < Max; ab++) {
		for (int j = 0; j < 26; j++) {
			printf("%d  ", xy[ab][j]);
		}
		printf("\n");
	}
}

int Out(int dist[], int start) {  //3
	int best=0; 
	int min = 10;

	for (int i = 0; i < Max; i++) {
		if (dist[i] != 0 && dist[i] < min) {
			min = dist[i];
			best = i;
		}
	}
	dist[best] = 0; 

	return best;
}
void PrimMST(int start)
{
	cout << "시작점: " << start << "-" << start << endl;
	
	for (int i = 0; i < Max; i++)
		dist[i] = xy[start-1][i];

	int a = start-1;
	for (int i = 0; i < Max-1; i++) {
		int b = Out(dist, a); // dist 1 / 3
		cout << "간선" << i+1 << ": " << a + 1 << "-" << b + 1 << endl; //1,1 1,4 4,


		for (int j = 0; j < Max; j++) {// 058042  118013 = 018012
			if (b != j || a != j) {
				if (dist[j] == 0 && 0 < xy[b][j]) // 10 15 88 00 14 32
					dist[j] = xy[b][j];
				else if()
			}
		}
	
		a = b;  //4
	}

	cout << endl;

}

void main()
{
	int start;
	cout << "시작 정점을 정하시오:";
	cin >> start;
	graph();
    PrimMST(start);
}*/

#define MAX 26
#define INF 10000L
int Matrix[MAX][MAX] = { 0 };
int dist[MAX];
int from[MAX];

void grap() {
	srand((unsigned)time(NULL));

	int Tindex = 0;
	int Weight = 0;

	int count1 = 0;										//세로줄 가중치 개수 저장
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
				for (int j = 0; j < MAX; j++) {			//가로열에 대한 가중치 개수 검사.
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

						Weight = (rand() % 29) + 1;
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
				if (count1 > MAX - i - 1)
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

						Weight = (rand() % 29) + 1;
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
				cout << "INF ";
			else
				printf("%3d ", Matrix[i][j]);
		}
		cout << endl;
	}
	cout << endl;
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
void PrimMST(int start)
{
	
	int Temp = start;
	int T[2][MAX] = { 0 };

	T[0][0] = start;
	T[1][0] = start;

	for (int i = 0; i < MAX; i++) {				//처음
		dist[i] = Matrix[start - 1][i];
		from[i] = start;
	}

	for (int i = 0; i < MAX - 1; i++) {
		int best = OutMin();
		if (best == INF)return;

		T[0][i + 1] = from[best];
		T[1][i + 1] = best+1;
		dist[best] = 0;

		for (int j = 0; j < MAX; j++) {
			if (Matrix[best][j] != 0) {
				if (dist[j] > Matrix[best][j]) {
					dist[j] = Matrix[best][j];
					from[j] = best+1;
				}
			}
		}
	}

	for (int i = 0; i < MAX; i++) {
		if (i == 0)
			cout << "시작점: " << T[0][i] << '-' << T[1][i] << endl;
		else
			cout << "간선" << i << ": " << T[0][i] << '-' << T[1][i] << endl;
	}

}
int main()
{
	int start;
	cout << "시작점을 입력하세요: ";
	cin >> start;

	grap();
	PrimMST(start);

	return 0;
}