{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q1.Create a numpy array starting from 2 till 50 with a stepsize of 3."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 2  5  8 11 14 17 20 23 26 29 32 35 38 41 44 47]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "arr = np.arange(2,50,3)\n",
    "print(arr)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q2.Accept two lists of 5 elements each from the user.\n",
    "Convert them to numpy arrays. Concatenate these arrays and print it. Also sort these arrays and print it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "total number wants to add in list2\n",
      "\n",
      "enter number which you want add in list a11\n",
      "enter number which you want add in list b9\n",
      "\n",
      "enter number which you want add in list a8\n",
      "enter number which you want add in list b100\n",
      "[11, 8]\n",
      "[9, 100]\n",
      "[ 11   8   9 100]\n",
      "[  8   9  11 100]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "a=[]\n",
    "\n",
    "b=[]\n",
    "total=int(input(\"\\ntotal number wants to add in list\"))\n",
    "for i in range(total):\n",
    "    x=int(input(\"\\nenter number which you want add in list a\"))\n",
    "    y=int(input(\"enter number which you want add in list b\"))\n",
    "    a.append(x)\n",
    "    b.append(y)\n",
    "print(a)\n",
    "print(b)\n",
    "arr1=np.array(a)\n",
    "arr2=np.array(b)\n",
    "arr=np.concatenate((arr1,arr2))\n",
    "print(arr)\n",
    "print(np.sort(arr))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q3.Write a code snippet to find the dimensions of a ndarray and its size."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "arr=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])\n",
    "print(np.ndim(arr))\n",
    "print(np.size(arr))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q4.How to convert a 1D array into a 2D array?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " 1.using expand_dims"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1]\n",
      " [ 2]\n",
      " [ 3]\n",
      " [ 4]\n",
      " [ 5]\n",
      " [ 6]\n",
      " [ 7]\n",
      " [ 8]\n",
      " [ 9]\n",
      " [10]]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "arr1=np.array([1,2,3,4,5,6,7,8,9,10])\n",
    "arr2=np.expand_dims(arr1, axis=1)\n",
    "print(arr2)\n",
    "arr2.ndim\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "2.using np.newaxis,"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1]\n",
      " [2]\n",
      " [3]\n",
      " [4]\n",
      " [5]\n",
      " [6]]\n",
      "1\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5, 6])\n",
    "a2 = a[:,np.newaxis]\n",
    "print(a2)\n",
    "print(a.ndim)\n",
    "print(a2.ndim)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3 4 5 6]]\n",
      "1\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "a = np.array([1, 2, 3, 4, 5, 6])\n",
    "a2 = a[np.newaxis,:]\n",
    "print(a2)\n",
    "print(a.ndim)\n",
    "print(a2.ndim)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q5.Consider two square numpy arrays. Stack them vertically and horizontally."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Horizontal Append: \n",
      " [[ 1  2  3  7 89  9]\n",
      " [ 4  5  6 12 13 14]]\n"
     ]
    }
   ],
   "source": [
    "x=np.array([[1,2,3],[4,5,6]])\n",
    "y=np.array([[7,89,9],[12,13,14]])\n",
    "print('Horizontal Append:', '\\n',np.hstack((x,y)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "vertical Append: \n",
      " [[ 1  2  3]\n",
      " [ 4  5  6]\n",
      " [ 7 89  9]\n",
      " [12 13 14]]\n"
     ]
    }
   ],
   "source": [
    "x=np.array([[1,2,3],[4,5,6]])\n",
    "y=np.array([[7,89,9],[12,13,14]])\n",
    "print('vertical Append:', '\\n',np.vstack((x,y)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Q6.How to get unique items and counts of unique items?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "original array [ 10  80  20  90  30  70  40  50  60  10  70  80  90  20 100  40 100]\n",
      "count of unique value \n",
      " [[ 10  20  30  40  50  60  70  80  90 100]\n",
      " [  2   2   1   2   1   1   2   2   2   2]]\n"
     ]
    }
   ],
   "source": [
    "arr = np.array( [10,80,20,90,30,70,40,50,60,10,70,80,90,20,100,40,100] )\n",
    "print(\"original array\",arr)\n",
    "arr1=np.unique(arr,return_counts=True)\n",
    "print(\"count of unique value\",'\\n',np.asarray(arr1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
