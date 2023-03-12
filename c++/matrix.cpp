#include "matrix.h"
#include "polinom.h"
#include "complex.h"
using namespace matrix;
using namespace complex;
using namespace polinom;
template Matrix<int>;
template Matrix<double>;
template Matrix<Complex>;
template Matrix<Polinom>;


template<class T> matrix::Matrix<T> matrix::Matrix<T>::operator +(const matrix::Matrix<T> &m) {
	vector<vector<T>> answer_matrix(this->sizey, vector<T>(this->sizex));
	for (register int i = 0; i < this->sizey; i++) {
		for (register int i1 = 0; i1 < this->sizex; i1++) {
			answer_matrix[i][i1] = matrix[i][i1] + m.matrix[i][i1];
		}
	}
	return Matrix<T>(answer_matrix, sizex, sizey);
}

template<class T> matrix::Matrix<T> matrix::Matrix<T>::operator *(matrix::Matrix<T>& m) {
	vector<vector<T>> answer_matrix(this->sizey, vector<T>(m.sizex));
	for (int row = 0; row < this->sizey; row++) {
		for (int col = 0; col < this->sizex; col++) {
			for (int inner = 0; inner < m.sizey; inner++) {
				answer_matrix[row][col] = answer_matrix[row][col] + this->matrix[row][inner] * m.matrix[inner][col];
			}
		}
	}
	return Matrix(answer_matrix, m.sizex, sizey);
}

template<class T> matrix::Matrix<T> matrix::Matrix<T>:: operator -(matrix::Matrix<T>& m) {
	vector<vector<T>> answer_matrix(this->sizey, vector<T>(this->sizex));
	for (register int i = 0; i < this->sizey; i++) {
		for (register int i1 = 0; i1 < this->sizex; i1++) {
			answer_matrix[i][i1] = matrix[i][i1] - m.matrix[i][i1];
		}
	}
	return Matrix<T>(answer_matrix, sizex, sizey);
}

template<class T> matrix::Matrix<T>& matrix::Matrix<T>::operator =(const matrix::Matrix<T>& m) {
	matrix = m.matrix;
	sizex = m.sizex;
	sizey = m.sizey;
	return *this;
}
