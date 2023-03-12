#include <iostream>
#include <vector>
#define MAX(a, b) ((a) > (b) ? (a) : b)
#define MIN(a, b) ((a) < (b) ? (a) : b)
namespace polinom{
    class Polinom {
		int pow;
		std::vector<double> polinom;
	public:
		Polinom(std::vector<double> polinom1, int pow1): polinom(polinom1), pow(pow1) {}
		Polinom() :pow(0) {}
		Polinom(int pow1) :pow(pow1) {
			polinom.resize(pow + 1);
		}
		//float get_polinoms() { return *polinom; }
		Polinom operator+(Polinom p2);
		Polinom operator*(Polinom& p2);
		Polinom operator-(Polinom& p2);
		Polinom operator=(const Polinom& p2);
		friend std::ostream& operator << (std::ostream& stream,const Polinom& p) {
			stream << "(";
			for (int i = 0; i < p.pow + 1; i++) {
				stream << p.polinom[i] << "x^" << i;
				if (i != p.pow) {
					stream << " +";
				}
			}
			stream << ")\n";
			return stream;
		}
		friend std::istream& operator >> (std::istream& stream, Polinom& p) {
			std::cout << "ввведите стпепень:\n";
			stream >> p.pow;
			p.polinom.resize(p.pow+1);
			std::cout << "введите коэффициенты:\n";
			for (int i = 0; i < p.pow + 1; i++) {
				std::cout << "x^" << i << ": ";
				
				stream >> p.polinom[i];

			}
			return stream;
		}
	};
}