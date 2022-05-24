#!/usr/bin/python3
"""Calculates the multiplication of two given matrix"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Lazy matrix multiplication by numpy method: matmul"""
    return np.matmul(m_a, m_b)
