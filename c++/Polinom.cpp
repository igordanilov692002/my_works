#include<iostream>
#include"polinom.h"

using namespace polinom;

Polinom Polinom::operator+(Polinom& p2) {
	int maxpow = MAX(this->pow, p2.pow);
	int minpow = MIN(this->pow, p2.pow);
	Polinom temp(maxpow);
	for (int i = 0; i < maxpow + 1; i++) {
		if (i > minpow) {
			if (this->pow > p2.pow) {
				temp.polinom[i] = polinom[i];
			}
			else {
				temp.polinom[i] = p2.polinom[i];
			}
		}
		else {
			temp.polinom[i] = polinom[i] + p2.polinom[i];
		}
	}
	return temp;
}

Polinom Polinom::operator-(Polinom& p2) {
	int maxpow = MAX(this->pow, p2.pow);
	int minpow = MIN(this->pow, p2.pow);
	Polinom temp(maxpow);
	for (int i = 0; i < maxpow + 1; i++) {
		if (i > minpow) {
			if (this->pow > p2.pow) {
				temp.polinom[i] = polinom[i];
			}
			else {
				temp.polinom[i] = -p2.polinom[i];
			}
		}
		else {
			temp.polinom[i] = polinom[i] - p2.polinom[i];
		}
	}
	return temp;
}

Polinom Polinom::operator=(const Polinom& p2) {
	pow = p2.pow;
	polinom = p2.polinom;
	return *this;
}

Polinom Polinom::operator/(Polinom& p2) {

}

Polinom Polinom::operator*(Polinom& p2) { // this->pow > p2.pow
	int maxpow = MAX(this->pow, p2.pow);
	int minpow = MIN(this->pow, p2.pow);
	Polinom temp(pow + p2.pow);
	for (int i = 0; i < pow + p2.pow + 1; i++) {
		temp.polinom[i] = 0.0;
	}
	for (int i = 0; i < this->pow + 1; i++) {
		for (int i1 = 0; i1 < p2.pow + 1; i1++) {
			temp.polinom[i + i1] += this->polinom[i] * p2.polinom[i1];
		}
	}
	return temp;
}