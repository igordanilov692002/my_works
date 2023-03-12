#include <iostream>
#include <vector>
#include "complex.h"
#include "matrix.h"
#include "polinom.h"


using namespace matrix;
using namespace std;
using namespace complex;
using namespace polinom;


int menu();
template<class T> void choise();
void choise2();

int main() {
	setlocale(LC_ALL, "Russian");
	cout << "�������� � ����� ����� ������ ����� ��������: 1 - �����������, 2 -  ��������, 3 - ������������:\n";
	int regim;
	cin >> regim;
	if (regim == 1) {
		choise<Complex>();
	}
	else if(regim == 2)
	{
		choise2();
	}
	else
	{
		choise<double>();
	}
}


int menu() {
	cout << "\t ����:\n";
	cout << "1 - �������� ���� ������\n";
	cout << "2 - ��������� ���� ������\n";
	cout << "3 - ��������� ���� ������\n";
	cout << "4 - ����� �������� ������\n";
	cout << "5 - �����\n";
	int a;
	cin >> a;
	return a;
}

void choise2() {
	cout << "������� ������ ������  �������(x*y): ";
	int a1, b1, a2, b2;
	cin >> a1 >> b1;
	cout << "������� ������ ������ �������(x*y): ";
	cin >> a2 >> b2;
	cout << endl;
	Matrix<Polinom> ob1(a1, b1), ob2(a2, b2), ob3;
	cin >> ob1;
	cin >> ob2;
	int choice = menu();
	while (choice != 5) {
		switch (choice)
		{
		case 1:
			ob3 = ob1 + ob2;
			cout << ob3;
			break;
		case 2:
			ob3 = ob1 - ob2;
			cout << ob3;
			break;
		case 3:
			ob3 = ob1 * ob2;
			cout << ob3;
			break;
		case 5:
			exit;
		default:
			cout << "�������� �� ����������!\n";
		}
		choice = menu();
	}
}


template<typename T> void choise() {
	cout << "������� ������ ������  �������(x*y): ";
	int a1, b1, a2, b2;
	cin >> a1 >> b1;
	cout << "������� ������ ������ �������(x*y): ";
	cin >> a2 >> b2;
	cout << endl; 
	Matrix<T> ob1(a1, b1), ob2(a2, b2), ob3;
	cin >> ob1;
	cin >> ob2;
	int choice = menu();
	while (choice != 5) {
		switch (choice)
		{
		case 1:
			ob3 = ob1 + ob2;
			cout << ob3;
			break;
		case 2:
			ob3 = ob1 - ob2;
			cout << ob3;
			break;
		case 3:
			ob3 = ob1 * ob2;
			cout << ob3;
			break;
		case 4:
			
			ob1.inverse_Matrix();
			ob2.inverse_Matrix();
			cout << ob1 << ob2;*/
			break;
		case 5:
			exit;
		default:
			cout << "�������� �� ����������!\n";
		}
		choice = menu();
	}
}