#include "complex.h"
using namespace complex;

Complex Complex::operator-(Complex z2) {
	Complex temp;
	temp.real = this->real - z2.real;
	temp.mnim = mnim - z2.mnim;
	return temp;
}

Complex Complex::operator*(Complex z2) {
	Complex temp;
	temp.real = this->real * z2.real + mnim * z2.mnim;
	temp.mnim = real * z2.mnim + mnim * z2.real;
	return temp;
}

Complex Complex::operator=(Complex z2) {
	real = z2.real;
	mnim = z2.mnim;
	return *this;
}

Complex Complex::operator=(double &d) {
	real = d;
	mnim = 0.0;
	return *this;
}

bool Complex::operator==(const double& d) { // Complex operator==(double z2)
	if (real == d && mnim == 0.0) {
		return true;
	}
	else {
		return false;
	}
}

Complex Complex::operator/(Complex z2) {
	Complex temp;
	temp.real = (real * z2.real + mnim * z2.mnim) / (z2.real * z2.real + z2.mnim * z2.mnim);
	temp.mnim = (mnim * z2.real - real * z2.mnim) / (z2.real * z2.real + z2.mnim * z2.mnim);
	return temp;
}

Complex Complex::operator+(Complex z2) {
	Complex temp;
	temp.real = this->real + z2.real;
	temp.mnim = mnim + z2.mnim;
	return temp;
}
	