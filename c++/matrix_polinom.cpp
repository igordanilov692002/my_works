#include "matrix.h"
#include "complex.h"
using namespace matrix;
using namespace complex;
template Matrix<int>;
template Matrix<double>;
template Matrix<Complex>;



template<class T>  std::vector <std::vector <T>> matrix::Matrix<T>::inverse_Matrix() {
	T det = determinant(matrix);
	if (det == 0.0) {
		cout << "обратной матрицы нет";
	}
	vector <vector < T >> matrix_alg_dop(sizey, vector<T>(sizex));
	for (int ix = 0; ix < sizey; ix++) {
		for (int iy = 0; iy < sizex; iy++) {
			vector <vector < T >> alg_dop(sizey - 1, vector<T>(sizex - 1));
			for (int i = 0; i < sizey - 1; i++) {
				int flagx = 0, flagy = 0;
				for (int i1 = 0; i1 < sizex - 1; i1++) {
					if (i == ix) {
						flagx = 1;
					}
					if (i1 == iy) {
						flagy = 1;
					}
					if (i + flagx < sizex && i1 + flagy < sizey) {
						alg_dop[i][i1] = matrix[i + flagx][i1 + flagy];
					}
				}
			}
			matrix_alg_dop[ix][iy] = determinant(alg_dop);
		}
	}
	for (int i = 0; i < sizey; i++) {
		for (int i1 = 0; i1 < sizex; i1++) {
			T val = matrix_alg_dop[i][i1];
			matrix_alg_dop[i1][i] = matrix_alg_dop[i][i1] / det;
			matrix_alg_dop[i][i1] = val / det;
		}
	}
	inverse_matrix = matrix_alg_dop;
	flag = 0;
	return matrix_alg_dop;
}


template<class T> T matrix::Matrix<T>::determinant(std::vector <std::vector < T >> matrixa1) {
	T d = 1;
	vector <vector < T >> matrixa = to_Triangle_Form(matrixa1);
	for (int i = 0; i < matrixa.size(); i++)
		d = d * matrixa[i][i];
	return d;
}
template<class T>  std::vector <std::vector <T>> matrix::Matrix<T>::to_Triangle_Form(std::vector <std::vector < T >> matrixa) {
	T mult = 0.0, d = 1.0;
	for (int i = 0; i < matrixa.size(); i++) {
		for (int j = i + 1; j < matrixa[0].size(); j++)
		{
			mult = matrixa[j][i] / matrixa[i][i];
			for (int k = i; k < matrixa.size(); k++) {
				matrixa[j][k] = matrixa[j][k] - matrixa[i][k] * mult;
			}
		}
	}
	return matrixa;
}
