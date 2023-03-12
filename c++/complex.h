#include <vector>
#include <iostream>
namespace complex {
	class Complex {
	    double real;
		double mnim;
	public:
		Complex(double x = 0.0, double  y = 0.0) {
			real = x;
			mnim = y;
		}
		double get_real() { return real; }
		double get_mnim() { return mnim; }
		Complex operator+(Complex z2);
		bool operator==(const double &z2);
		Complex operator*(Complex z2);
		Complex operator/(Complex z2);
		Complex operator-(Complex z2);
		Complex operator=(Complex z2);
		Complex operator=(double &d);
		friend std::ostream& operator << (std::ostream& stream, Complex& z) {
			stream << "(" <<z.real << ", " << z.mnim << ")";
			return stream;
		}
		friend std::istream& operator >> (std::istream& stream, Complex& z) {
			std::cout << "(a,i): ";
			stream >> z.real;
			stream >> z.mnim;
			return stream;
		}
	};
}