#include <vector>
#include <iostream>
using namespace std;
namespace matrix {
	template <typename T>class Matrix {
	private:
		int sizex, sizey;
		vector<vector<T>> matrix;
		int flag = 1;
		vector<vector<T>> inverse_matrix;

	public:
		Matrix(int x = 0, int y = 0) : sizex(x), sizey(y) {
			matrix.resize(y);
			for (int i = 0; i < y; i++) {
				matrix[i].resize(x);
			}
		}
		Matrix(vector<vector<T>> matrixa, int x, int y) : matrix(matrixa), sizex(x), sizey(y) {}
		Matrix(vector<vector<T>> matrixa) : matrix(matrixa), sizex(matrixa[0].size()), sizey(matrixa.size()) {}

		vector<vector<T>> get_matrix(){
			return matrix;
		}
		
		vector <vector <T>> inverse_Matrix();


		T determinant(vector <vector < T >> matrixa1);

		vector<vector<T>> to_Triangle_Form(vector <vector < T >> matrixa);

		Matrix operator +(const Matrix& m);

		Matrix operator *(Matrix& m);

		Matrix operator -(Matrix& m);

		Matrix& operator =(const Matrix& m);

		friend std::ostream& operator << (std::ostream& stream, Matrix& m) {
			cout << "вывод: " << endl;
			if (m.flag == 1) {
				for (int i = 0; i < m.sizey; i++) {
					for (int i1 = 0; i1 < m.sizex; i1++) {
						stream << m.matrix[i][i1] << " ";
					}
					stream << endl;
				}
			}
			else
			{
				for (int i = 0; i < m.inverse_matrix.size(); i++) {
					for (int i1 = 0; i1 < m.inverse_matrix[0].size(); i1++) {
						stream << m.inverse_matrix[i][i1] << " ";
					}
					stream << endl;
				}
			}
			m.flag = 1;
			return stream;
		}

		friend std::istream& operator >> (std::istream& stream, Matrix& m) {
			cout << "введите данные для матрицы:\n";
			for (register int i = 0; i < m.sizey; i++)
				for (register int i1 = 0; i1 < m.sizex; i1++)
					stream >> m.matrix[i][i1];

			cout << endl;
			return stream;
		}
	};
}