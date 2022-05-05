#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import torch


#  Part I tensors (张量)
def test_torch():

    #  create one 5X3 matrix without initialize
    x = torch.empty(5, 3)
    print(x)

    #  output:
    """
      tensor([[ 0.0000e+00, -3.6893e+19,  6.2537e+01],
            [ 4.6577e-10,  1.8361e+25,  1.4603e-19],
            [ 6.4069e+02,  2.7489e+20,  1.5444e+25],
            [ 1.6217e-19,  7.0062e+22,  1.6795e+08],
            [ 4.7423e+30,  4.7393e+30,  9.5461e-01]])
    
    Process finished with exit code 0
    
    """

    #  create one random initialized matrix
    y = torch.rand(5, 3)
    print(y)

    #  output
    """
        tensor([[0.0460, 0.7391, 0.1205],
            [0.4279, 0.7832, 0.6240],
            [0.6860, 0.7386, 0.2701],
            [0.9278, 0.4698, 0.7551],
            [0.9167, 0.7668, 0.8985]])
    """

    # create one matrix filled all of 0 and with long dtype
    z = torch.zeros(5, 3, dtype=torch.long)
    print(z)

    # output
    """
        tensor([[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]])
    """

    #  create one tensor use data_science
    x = torch.tensor([5.5, 3])
    print(x)
    # output
    #  tensor([5.5000, 3.0000])


def tensor_based_on_tensor():
    x = torch.tensor([5.5, 3])
    x = x.new_ones(5, 3, dtype=torch.double)
    # new_* methods take in sizes
    print(x)
    x = torch.randn_like(x, dtype=torch.float)

    # override dtype!
    print(x)

    # result has the same size

    # dimension info
    print(x.size())
    # torch.Size([5, 3])

    return x


# Part II Operator （操作）
def add_in_torch():
    """
    !!! Attention: any operator which will make tensor changed has a prefix ''
    e.g. x.copy()   (y)     x.t_()  will change x.
    U can use standard NumPy index operator
    print(x[:, 1])
    :return:
    """
    # way 1
    x = tensor_based_on_tensor()
    y = torch.rand(5, 3)

    print('X: ', x)
    print('Y: ', y)

    print('way 1: ', x + y)

    # way 2
    # print(torch.add(x, y))
    print('way 2: ', torch.add(x, y))

    # method: offer an output tensor as parameter
    result = torch.empty(5, 3)
    torch.add(x, y, out=result)
    print('result:', result)

    # add: in-place
    y.add_(x)
    print('in-place: ', y)

    print('x[:, 1]', x[:, 1])

    # change size: if U want to change the size or the shape of a tensor,
    # U can use torch.view
    x1 = torch.rand(4, 4)
    y1 = x1.view(16)
    z1 = x1.view(-1, 8) # the size -1 is inferred from other dimensions
    print('change size here: \n', x1.size(), y1.size(), z1.size())


def get_tensor_value():
    x = torch.rand(1)
    print(x)
    print(x.item())


if __name__ == '__main__':

    # tensor_based_on_tensor()
    """
        tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]], dtype=torch.float64)
tensor([[-1.7472, -0.7479,  0.2762],
        [-2.2536,  0.7806,  0.7572],
        [-1.0355, -0.0416,  0.4884],
        [-1.5578,  0.2680, -1.1111],
        [-0.8064,  0.3391,  1.9606]])

Process finished with exit code 0

    """

    # add_in_torch()
    get_tensor_value()

    # all results:
    """
tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]], dtype=torch.float64)
tensor([[-1.1333, -0.5950,  0.8910],
        [ 1.5214,  1.0200, -0.7105],
        [-0.1769,  0.2270, -1.3278],
        [-1.3065, -0.6226, -0.0460],
        [ 1.5617,  0.4823, -0.0475]])
torch.Size([5, 3])
X:  tensor([[-1.1333, -0.5950,  0.8910],
        [ 1.5214,  1.0200, -0.7105],
        [-0.1769,  0.2270, -1.3278],
        [-1.3065, -0.6226, -0.0460],
        [ 1.5617,  0.4823, -0.0475]])
Y:  tensor([[0.1271, 0.8103, 0.2531],
        [0.7382, 0.7552, 0.3193],
        [0.4353, 0.7741, 0.1194],
        [0.4561, 0.1034, 0.2586],
        [0.9760, 0.9182, 0.5962]])
way 1:  tensor([[-1.0062,  0.2153,  1.1441],
        [ 2.2596,  1.7752, -0.3913],
        [ 0.2584,  1.0012, -1.2084],
        [-0.8504, -0.5192,  0.2126],
        [ 2.5377,  1.4004,  0.5487]])
way 2:  tensor([[-1.0062,  0.2153,  1.1441],
        [ 2.2596,  1.7752, -0.3913],
        [ 0.2584,  1.0012, -1.2084],
        [-0.8504, -0.5192,  0.2126],
        [ 2.5377,  1.4004,  0.5487]])
result: tensor([[-1.0062,  0.2153,  1.1441],
        [ 2.2596,  1.7752, -0.3913],
        [ 0.2584,  1.0012, -1.2084],
        [-0.8504, -0.5192,  0.2126],
        [ 2.5377,  1.4004,  0.5487]])
in-place:  tensor([[-1.0062,  0.2153,  1.1441],
        [ 2.2596,  1.7752, -0.3913],
        [ 0.2584,  1.0012, -1.2084],
        [-0.8504, -0.5192,  0.2126],
        [ 2.5377,  1.4004,  0.5487]])
x[:, 1] tensor([-0.5950,  1.0200,  0.2270, -0.6226,  0.4823])
change size here: 
 torch.Size([4, 4]) torch.Size([16]) torch.Size([2, 8])

Process finished with exit code 0

tensor([0.2193])
0.2193068265914917

Process finished with exit code 0

    """
